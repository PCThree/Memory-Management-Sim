import Memory
takenSymbol = "X"
freeSymbol = "O"
upperBoundMemory = 50
lowerBoundMemory = 1

def MainMenu():
    while True:
        print("Welcome to the Memory Management SIM")
        print("[1] Single User Contiguous Memory")
        print("[2] Fixed Partition")
        print("[3] Dynamic Partition")
        print("[4] Relocatable Dynamic Partition")

        memChoice = "0"
        memChoiceOptions = ["1","2","3","4"]
        while memChoice not in memChoiceOptions:
            memChoice = input("Choose an option: ")
            if memChoice not in memChoiceOptions:
                print("ERROR: Please pick a valid option")

        for i in range(2):
            print()
        
        if memChoice == "1":
            SUCmem()
        elif memChoice == "2":
            FPmem()
        elif memChoice == "3":
            DPmem()
        elif memChoice == "4":
            RDPmem()

def SUCmem():
    while True:
        try: 
            maxMem = int(input("How much memory do you want the machine to have: [1-50] "))
            if maxMem < lowerBoundMemory or maxMem > upperBoundMemory:
                raise TypeError
            Machine = Memory.SUC(maxMem)
            break
        except TypeError:
            print("ERROR: Please input a valid integer")
    
    while True:
        print()
        displayMemory(Machine)
        print("[1] Add job")
        print("[2] Delete job")

        option = "0"
        optionChoices = ["1","2"]
        while option not in optionChoices:
            option = input("Choose an option: ")
            if option not in optionChoices:
                print("ERROR: Please pick a valid option")
                continue
        


def FPmem():
    pass

def DPmem():
    pass

def RDPmem():
    pass

def displayMemory(mach):
    print("[ ", end="")
    for val in mach.memory:
        if val is False:
            print(freeSymbol, end="")
        elif val is True:
            print(takenSymbol, end="")
        else:
            for val2 in val:
                if val is False:
                    print(freeSymbol, end="")
                elif val is True:
                    print(takenSymbol, end="")
    print(" ]")

def deleteJob():
    pass

MainMenu()