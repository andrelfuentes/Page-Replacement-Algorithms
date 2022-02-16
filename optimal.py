'''
---------------------------------------------------
Andrel Fuentes Torres
801-19-9857
andrel.fuentes@upr.edu
Prof. Ortiz
CCOM4017-002
---------------------------------------------------
This file is the implementation of the Optimal page
replacement algorith. Given a assigned number of
spaces for the physical memory, when that number of
spaces is reached, it removes the page in memory
that will be referenced further into the set of the
virtual memory accesses.
---------------------------------------------------
'''
#Import sys library to receive parameters from shell
import sys
#Assign the amount of space the physical memory will have
PhysicalMemorySpace = int(sys.argv[1])
#Assign the name of the file that has the virtual memory accesses
InputFileName = sys.argv[2]
#Open file, read its contents and close it
InputFile = open(InputFileName, "r")
FileContents = InputFile.read()
InputFile.close()

#Split the contents of the file twice (Once for the spaces " ", and another for the ":")
FileContentsSplit = FileContents.split(" ")
VirtualMemoryAccesses = []
for i in range(len(FileContentsSplit)):
    VirtualMemoryAccesses.append(FileContentsSplit[i].split(":")[1])

#Function to find the optimal page to replace
def SearchOptimalToRemove(MemoryContent, VirtualContent, CurrentIndex):
    #Copy the contents of VirtualMemoryAccesses (VirtualContent) to a new
    #list so that it's not altered
    VirtualContentToAlter = VirtualContent[:]
    #Remove elements until the CurrentIndex
    for page in range(CurrentIndex):
        VirtualContentToAlter.pop(0)
    #List to hold the upcoming pages
    ListOfNextPages = []
    #Variable to hold the furthest index of the possible page of replacement
    FurthestPageIndex = 0
    #Final index of replacement
    IndexToRemove = 0
    #Loop to go around the lenght of PhysicalMemory (MemoryContent)
    for i in range(len(MemoryContent)):
        #If the page is in the upcoming virtual accesses and not in the list holding them,
        #append the page and change the CurrentPageIndex
        if MemoryContent[i] in VirtualContentToAlter and MemoryContent[i] not in ListOfNextPages:
            ListOfNextPages.append(MemoryContent[i])
            CurrentPageIndex = VirtualContentToAlter.index(MemoryContent[i])
            #If the CurrentPageIndex is larger than the current largest,
            #change FurthestPageIndex and the IndexToRemove becomes the
            #index of that page
            if FurthestPageIndex < CurrentPageIndex:
                FurthestPageIndex = CurrentPageIndex
                IndexToRemove = MemoryContent.index(VirtualContentToAlter[CurrentPageIndex])
        #If the page is not in the upcoming virtual memory accesses,
        #just return that page index
        elif (MemoryContent[i] not in VirtualContentToAlter):
            return i
    #If conditions met, return IndexToRemove
    return IndexToRemove

#Initialize the physical memory, the page fault counter, and a counter for the current index
PhysicalMemory = []
PageFaults = 0
CurrentIndex = 0
#Loop to go through every page in VirtualMemoryAccesses
for page in VirtualMemoryAccesses:
    #If the page is in the physical memory do nothing
    if page in PhysicalMemory:
        pass
    #If it's not in memory...
    else:
        #If the physical memory reached the given size, search what element to remove,
        #make the change to physical memory, and increment the page fault counter
        if len(PhysicalMemory) >= PhysicalMemorySpace:
            IndexOfRemoval = SearchOptimalToRemove(PhysicalMemory, VirtualMemoryAccesses, CurrentIndex)
            PhysicalMemory[IndexOfRemoval] = page
            PageFaults = PageFaults + 1
        #Else, just append the page and increment the page fault counter
        else:
            PageFaults = PageFaults + 1
            PhysicalMemory.append(page)
    #Increment current index
    CurrentIndex = CurrentIndex + 1

#Print the last status of the physical memory and the amount of page faults that occurred
print("Physical memory status: " + str(PhysicalMemory))
print("Amount of page faults occurred: " + str(PageFaults))
