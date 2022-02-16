'''
-------------------------------------------------------
Andrel Fuentes Torres
801-19-9857
andrel.fuentes@upr.edu
Prof. Ortiz
CCOM4017-002
-------------------------------------------------------
This file is the implementation of the WSClock
(Working Set Clock) page replacement algorithm.
Given a assigned number of spaces for the circular
physical memory, when that number of spaces is reached,
the algorithm searches the circular memory to see what
page to replace. If the page is referenced it
dereferences it and moves to the next page. If a
page is not referenced it evaluates if it's in the
working set, if it is, it moves to the next page and
if it isn't it replaces the page. If it does a full
cycle and it had to dereference every page, it replaces
the page with the lowest time of last use.
-------------------------------------------------------
'''
#Import sys library to receive parameters from shell
import sys
#Assign the amount of space the physical memory will have
PhysicalMemorySpace = int(sys.argv[1])
#Assign the value of the tau
Tau = int(sys.argv[2])
#Assign the name of the file that has the virtual memory accesses
InputFileName = sys.argv[3]
#Open file, read its contents and close it
InputFile = open(InputFileName, "r")
FileContents = InputFile.read()
InputFile.close()

#Split the contents of the file twice (Once for the spaces " ", and another for the ":")
FileContentsSplit = FileContents.split(" ")
VirtualMemoryAccesses = []
for i in range(len(FileContentsSplit)):
    VirtualMemoryAccesses.append(FileContentsSplit[i].split(":")[1])

#Create class to keep track of the page information
class PageInformation:
    PageNumber = 0
    ReferenceBit = 1
    PageTOLA = 0

#Function to see if the page is in the memory
def SearchInMemory(Memory, PageToFind):
    #For every element in PhysicalMemory
    for page in Memory:
        #If the page number matches the page number we are trying to find,
        #return True (to let know it's found) and it's index
        if PageToFind == page.PageNumber:
            return True, Memory.index(page)
    #If not found return False and 0
    return False, 0

#Function to find what element is to be removed
def SearchToRemove(Memory):
    global ClockHand, VirtualTime
    #Loop to infinitely move the hand until we have the index for removal
    while True:
        #If the reference bit of the page is 1, update it to 0
        if Memory[ClockHand].ReferenceBit == 1:
            Memory[ClockHand].ReferenceBit = 0
        #If the page isn't in the working set, return the clock hand (index of removal)
        elif (VirtualTime - Memory[ClockHand].PageTOLA) > Tau:
            return ClockHand
        #Move the clock hand forward once
        ClockHand = (ClockHand + 1) % PhysicalMemorySpace

#Initialize the physical memory, the virtual time, the page fault counter, and the clock hand
PhysicalMemory = []
VirtualTime = 0
PageFaults = 0
ClockHand = 0
#Loop to go through every page in VirtualMemoryAccesses
for page in range(len(VirtualMemoryAccesses)):
    #Save to a variable the page number
    PageNumber = int(VirtualMemoryAccesses[page])
    #Make the page with the class (PageInformation())
    page = PageInformation()
    #Change/update it's page number
    page.PageNumber = PageNumber
    #Search to see if page is in memory
    InMemory, IndexOfPage = SearchInMemory(PhysicalMemory, page.PageNumber)
    #If the page is in memory, update it's TOLA and it's reference bit
    if InMemory == True:
        PhysicalMemory[IndexOfPage].PageTOLA = VirtualTime
        PhysicalMemory[IndexOfPage].ReferenceBit = 1
        VirtualTime = VirtualTime + 1
    #If it's not in memory...
    else:
        #If the physical memory reached the given size, search the circular list
        #to see where to replace
        if len(PhysicalMemory) >= PhysicalMemorySpace:
            page.PageTOLA = VirtualTime
            i2r = SearchToRemove(PhysicalMemory)
            PhysicalMemory[i2r] = page
        ##Else, just append the page and increment the page fault counter
        else:
            page.PageTOLA = VirtualTime
            PhysicalMemory.append(page)
        #Increment the clock hand, virtual time and page fault counter
        ClockHand = (ClockHand + 1) % PhysicalMemorySpace
        VirtualTime = VirtualTime + 1
        PageFaults = PageFaults + 1

#Print the last status of the physical memory and the amount of page faults that occurred
print("Physical memory status: ")
for i in PhysicalMemory:
    print("  (" + str(i.PageNumber) + ", " + str(i.ReferenceBit) + ", " + str(i.PageTOLA) + ")")
print("Amount of page faults occurred: " + str(PageFaults))
