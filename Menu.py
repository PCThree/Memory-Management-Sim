import Memory
takenSymbol = "|"
freeSymbol = "-"
upperBoundMemory = 50
lowerBoundMemory = 1

def MainMenu():
    while True:
        print("\nWelcome to the Memory Management SIM:")
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
            print("How much memory do you want the machine to have: [1-50] [C/c to cancel]")
            maxMem = input("> ")
            if maxMem.lower() == "c":
                return
            maxMem = int(maxMem)
            if maxMem < lowerBoundMemory or maxMem > upperBoundMemory:
                raise ValueError
            Machine = Memory.SUC(maxMem)
            jobCounter = 0
            break
        except ValueError:
            print("ERROR: Please input a valid choice")
    
    while True:
        print()
        Machine.printMemory(freeSymbol,takenSymbol)
        Machine.printJobs()
        print("\n[1] Add job")
        print("[2] Deallocate job")
        print("[3] EXIT")

        option = "0"
        optionChoices = ["1","2","3"]
        while option not in optionChoices:
            print("Choose an option")
            option = input("> ")
            if option not in optionChoices:
                print("ERROR: Please pick a valid option")
        
        if option == "1":
            addJob(Machine, "SUC")
        elif option == "2":
            if len(Machine.objects) == 0:
                print("ERROR: No jobs to deallocate")
            else:
                deleteJob(Machine, "SUC")
        elif option == "3":
            return

def FPmem():
    while True:
        try: 
            print("How many partition does the machine have: [1-5] [C/c to cancel]")
            partitionCount = input("> ")
            partSizes = []
            if partitionCount.lower() == "c":
                return
            partitionCount = int(partitionCount)
            if partitionCount < 1 or partitionCount > 5:
                raise ValueError
            partSizesChoices = ["1","2","3","4","5","6","7","8","9","10"]
            for i in range(partitionCount):
                partSize = "0"
                while partSize not in partSizesChoices:
                    partSize = input(f"Enter partition {i} size: [1-10] ")
                    if partSize in partSizesChoices:
                        partSizes.append(int(partSize))
                        break
                    else:
                        print("ERROR: Please input a valid size")
                        input("press ENTER to continue")
            Machine = Memory.FP(partSizes)
            break
        except ValueError:
            print("ERROR: Please input a valid choice")

    while True:
        print()
        Machine.printMemory(freeSymbol,takenSymbol)
        Machine.printJobs()
        print("\n[1] Add job")
        print("[2] Deallocate job")
        print("[3] EXIT")

        option = "0"
        optionChoices = ["1","2","3"]
        while option not in optionChoices:
            print("Choose an option")
            option = input("> ")
            if option not in optionChoices:
                print("ERROR: Please pick a valid option")
        
        if option == "1": ##########################################
            addJob(Machine, "FP")
        elif option == "2": ###############################################
            if len(Machine.objects) == 0:
                print("ERROR: No jobs to deallocate")
            else:
                deleteJob(Machine, "FP")
        elif option == "3":
            return

def DPmem():
    while True:
        try: 
            print("How much memory do you want the machine to have: [1-50] [C/c to cancel]")
            maxMem = input("> ")
            if maxMem.lower() == "c":
                return
            maxMem = int(maxMem)
            if maxMem < lowerBoundMemory or maxMem > upperBoundMemory:
                raise ValueError
            Machine = Memory.DP(maxMem)
            jobCounter = 0
            break
        except ValueError:
            print("ERROR: Please input a valid choice")
    
    while True:
        print()
        Machine.printMemory(freeSymbol,takenSymbol)
        Machine.printJobs()
        print("\n[1] Add job")
        print("[2] Deallocate job")
        print("[3] EXIT")

        option = "0"
        optionChoices = ["1","2","3"]
        while option not in optionChoices:
            print("Choose an option")
            option = input("> ")
            if option not in optionChoices:
                print("ERROR: Please pick a valid option")
        
        if option == "1":
            addJob(Machine, "DP")
        elif option == "2":
            if len(Machine.objects) == 0:
                print("ERROR: No jobs to deallocate")
            else:
                deleteJob(Machine, "DP")
        elif option == "3":
            return

def RDPmem():
    while True:
        try: 
            print("How much memory do you want the machine to have: [1-50] [C/c to cancel]")
            maxMem = input("> ")
            if maxMem.lower() == "c":
                return
            maxMem = int(maxMem)
            if maxMem < lowerBoundMemory or maxMem > upperBoundMemory:
                raise ValueError
            Machine = Memory.RDP(maxMem)
            jobCounter = 0
            break
        except ValueError:
            print("ERROR: Please input a valid choice")
    
    while True:
        print()
        Machine.printMemory(freeSymbol,takenSymbol)
        Machine.printJobs()
        print("\n[1] Add job")
        print("[2] Deallocate job")
        print("[3] Reallocate jobs")
        print("[4] EXIT")

        option = "0"
        optionChoices = ["1","2","3","4"]
        while option not in optionChoices:
            print("Choose an option")
            option = input("> ")
            if option not in optionChoices:
                print("ERROR: Please pick a valid option")
        
        if option == "1":
            addJob(Machine, "RDP")
        elif option == "2":
            if len(Machine.objects) == 0:
                print("ERROR: No jobs to deallocate")
            else:
                deleteJob(Machine, "RDP")
        elif option == "3":
            Machine.reallocate()
        elif option == "4":
            return

def addJob(mach, partType):
    jobSize = 0
    while jobSize <= 0:
        print("How big is the job: [C/c to cancel]")
        jobSize = input("> ")
        if jobSize.lower() == "c":
            return
        jobSize = int(jobSize)
        if jobSize >= 0:
            if partType == "SUC" or partType == "FP":
                mach.newJob(mach.jobCounter,jobSize)
                return
            elif partType == "DP" or partType == "RDP":
                mach.newPartition(mach.jobCounter,jobSize)
                return
        else:
            print("ERROR: Please input a valid size")
            input("press ENTER to continue")

def deleteJob(mach, partType):
    objOption = "-1"
    objOptions = []
    objectAmount = 0
    for i in range(len(mach.objects)):
        objectAmount += len(mach.objects[i].objects)
    for i in range(objectAmount):
        objOptions.append(str(i))
    #print(objOptions)
    while objOption not in objOptions:
        print(f"Which object to delete: [0-{objectAmount-1}] [C/c to cancel]")
        objOption = input("> ")
        if objOption not in objOptions:
            print("ERROR: Please input a valid option")
        elif objOption.lower() == "c":
            return
    objOption = int(objOption)
    if partType == "SUC" or partType == "FP":
        mach.delJob(objOption)
    elif partType == "DP" or partType == "RDP":
        mach.delPartition(objOption)
        
MainMenu()