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
    pass

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
    pass

def addJob(mach, partType):
    jobSize = 0
    while jobSize <= 0:
        print("How big is the job: [C/c to cancel]")
        jobSize = input("> ")
        if jobSize.lower() == "c":
            return
        jobSize = int(jobSize)
        if partType == "SUC":
            mach.newJob(mach.jobCounter,jobSize)
        elif partType == "DP":
            mach.newPartition(mach.jobCounter,jobSize)

def deleteJob(mach, partType):
    objOption = "-1"
    objOptions = []
    for i in range(len(mach.objects)):
        objOptions.append(str(i))
    #print(objOptions)
    while objOption not in objOptions:
        print(f"Which object to delete: [0-{len(mach.objects)-1}] [C/c to cancel]")
        objOption = input("> ")
        if objOption not in objOptions:
            print("ERROR: Please input a valid option")
        elif objOption.lower() == "c":
            return
    objOption = int(objOption)
    if partType == "SUC":
        mach.delJob(objOption)
    elif partType == "DP":
        mach.delPartition(objOption)
        
MainMenu()