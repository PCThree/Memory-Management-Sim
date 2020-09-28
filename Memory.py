# Pasta ahead
# TODO:
# implement error handling
# implement dynamic partitions

class Partition:
    def __init__(self, maxSize, index):
        super().__init__()
        self.type = "Partition"
        self.maxSize = maxSize
        self.memory = [False for i in range(maxSize)]
        self.gaps = [[0,self.maxSize]]
        self.size = 0
        self.objects = []
        self.jobCounter = 0
        self.index = index

    # The original gapcheck algorithm, found a more simpler approach
    # Welp, cant make that work, imma stick with this
    def gapCheck(self):
        self.gaps.clear()
        counter = 0
        gapStart = None
        gapEnd = None
        while counter < len(self.memory):
            if gapStart is None and self.memory[counter] is False:
                gapStart = counter
            if gapEnd is None and gapStart is not None:
                if self.memory[counter] is not False:
                    gapEnd = counter - 1
                    self.gaps.append([gapStart,gapEnd])
                    gapStart = None
                    gapEnd = None
                elif counter + 1 >= len(self.memory):
                    gapEnd = counter
                    self.gaps.append([gapStart,gapEnd])
                    gapStart = None
                    gapEnd = None
            counter += 1

    def newPartition(self, size):
        for gap in self.gaps:
            if (gap[1] - gap[0]) + 1 >= size:
                self.objects.append(Partition(size, gap[0]))
                self.objects.sort(key=lambda x: x.index, reverse=False)
                for i in range(size):
                    del self.memory[gap[0]]
                self.memory.insert(gap[0],[False for i in range(size)])
                #print(self.memory)
                self.gapCheck()
                #print(self.gaps)
                return
        print("ERROR: No space available")

    def newJob(self, name, jobSize):
        for gap in self.gaps:
            if (gap[1] - gap[0]) + 1 >= jobSize:
                self.objects.append(Job(name, jobSize, gap[0]))
                self.objects.sort(key=lambda x: x.startLoc, reverse=False)
                for i in range(gap[0],gap[0]+jobSize):
                    self.memory[i] = True
                #print(self.memory)
                self.gapCheck()
                self.jobCounter += 1
                return
        print("ERROR: No space available")

    def delJob(self, index):
        for i in range(self.objects[index].startLoc, self.objects[index].endLoc):
            self.memory[i] = False
        del self.objects[index]
        self.gapCheck()

    def printJobs(self):
        print("\nJOB LIST:")
        print("INDEX\tSIZE\tLOCATION")
        for i in range(len(self.objects)):
            print(f"{i}:\t{self.objects[i].size}\t{self.objects[i].startLoc}-{self.objects[i].endLoc}")
        print()
    
    def printMemory(self, freeSymbol, takenSymbol):
        print("[ ", end="")
        for val in self.memory:
            if val is False:
                print(freeSymbol, end="")
            elif val is True:
                print(takenSymbol, end="")
            else:
                print(" ", end="")
                for val2 in val:
                    if val is False:
                        print(freeSymbol, end="")
                    elif val is True:
                        print(takenSymbol, end="")
        print(" ]")

class SUC(Partition): # Single User Contiguous
    def __init__(self, maxSize):
        super().__init__(maxSize, None)
        self.type = "Single User Contiguous"

class FP(Partition): # Fixed Partition
    def __init__(self, maxSize):
        super().__init__(maxSize, None)
        self.type = "Fixed Partition"
        # I don't exactly know how a computer assigns partition size
        # That's why im just gonna make 5 partitions and assign them arbitrary percentages of memory, namely [40%, 15%, 20%, 20%, 5%]

        self.newPartition(int(self.maxSize*0.40))
        self.newPartition(int(self.maxSize*0.15))
        self.newPartition(int(self.maxSize*0.20))
        self.newPartition(int(self.maxSize*0.20))
        self.newPartition(self.maxSize - (int(self.maxSize*0.40) + int(self.maxSize*0.15) + int(self.maxSize*0.20) + int(self.maxSize*0.20))) # Had to workaround for the decimal values disposed during integer conversion

        self.sum = 0
        for obj in self.objects:
            self.sum += obj.maxSize
        #print(f"Max Memory: {self.sum}")

class DP(Partition): # Dynamic Partition
    def __init__(self, maxSize):
        super().__init__(maxSize, None)
        self.type = "Dynamic Partition"

    def newPartition(self, name, size):
        for gap in self.gaps:
            if (gap[1] - gap[0]) + 1 >= size:
                p = Partition(size, gap[0])
                p.newJob(name, size)
                self.objects.append(p)
                self.objects.sort(key=lambda x: x.index, reverse=False)
                for i in range(size):
                    del self.memory[gap[0]]
                self.memory.insert(gap[0], p.memory)
                #print(self.memory)
                self.gapCheck()
                return
        print("ERROR: No space available")
        input("Press ENTER to continue")
    
    def delPartition(self, index):
        tmp = 0 # Accounting for the extra "False" values added in self.memory
        for i in range(self.objects[index].maxSize):
            self.memory.insert(self.objects[index].index + 1, False)
            tmp += 1
        for i in range(index+1, len(self.objects)):
            self.objects[i].index += (tmp - 1)
        del self.memory[self.objects[index].index]
        del self.objects[index]
        self.gapCheck()

class RDP(DP): # Relocatable Dynamic Partition
    def __init__(self, maxSize):
        super().__init__(maxSize)
        self.type = "Relocatable Dynamic Partition"

    def reallocate(self):
        if len(self.gaps) == 0:
            return
        firstEmpty = self.gaps[0][0]
        for p in self.objects:
            if p.index > firstEmpty:
                self.memory.insert(firstEmpty, self.memory.pop(p.index))
                p.index = firstEmpty
                if firstEmpty + 1 < len(self.memory):
                    firstEmpty += 1
                else:
                    self.gapCheck()
                    return
        self.gapCheck()

class Job:
    def __init__(self, name, size, startLoc):
        super().__init__()
        self.name = name
        self.size = size
        self.startLoc = startLoc
        self.endLoc = (startLoc + size) - 1
