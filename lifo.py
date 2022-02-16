'''
--------------------------------------------------
Andrel Fuentes Torres
801-19-9857
andrel.fuentes@upr.edu
Prof. Ortiz
CCOM4017-002
--------------------------------------------------
This file is the implementation of the LIFO (LAST
IN, FIRST OUT) page replacement algorith. Given a
assigned number of spaces for the physical memory,
when that number of spaces is reached, the last
element in the physical memory is replaced.
--------------------------------------------------
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

#Initialize the physical memory and the page fault counter
PhysicalMemory = []
PageFaults = 0
#Loop to go through every page in VirtualMemoryAccesses
for page in VirtualMemoryAccesses:
    #If the page is in the physical memory do nothing
    if page in PhysicalMemory:
        pass
    #If it's not in memory...
    else:
        #If the physical memory reached the given size, remove the last page and increment the page fault counter
        if len(PhysicalMemory) >= PhysicalMemorySpace:
            PageFaults = PageFaults + 1
            PhysicalMemory.pop(-1)
            PhysicalMemory.append(page)
        #Else, just append the page and increment the page fault counter
        else:
            PageFaults = PageFaults + 1
            PhysicalMemory.append(page)

#Print the last status of the physical memory and the amount of page faults that occurred
print("Physical memory status: " + str(PhysicalMemory))
print("Amount of page faults occurred: " + str(PageFaults))
