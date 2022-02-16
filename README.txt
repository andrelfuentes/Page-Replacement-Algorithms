
-----------------------------------------------------------------------------------

Andrel Fuentes Torres
801-19-9857
andrel.fuentes@upr.edu
Prof. Ortiz
CCOM4017-002

-----------------------------------------------------------------------------------

This code is meant to be ran with python3.
This README.txt was completed with the advice of Diego Perez.

-----------------------------------------------------------------------------------

File: lifo.py

The program requires importing library sys (already in the code)

To run the program open the terminal in the directory with this
file and the .txt file with the sequence of memory accesses and
write the following command:
  python3 lifo.py <Number of physical memory pages> <access sequence file>
For example:
  python3 lifo.py 5 input.txt

This program only requires you to write that command and nothing else.
After that the program will execute and finish by itself.

This program will receive two input from the shell command (input file and
the space of the memory) which will be used to initialize variables for use
in the program.

This program will read the sequence file and split its contents twice to
end up with the pages themselves.

This program is the implementation of the LIFO (LAST IN, FIRST OUT) page
replacement algorithm. Given the assigned number of spaces for the physical
memory, when that number of spaces is reached, the last element in the
physical memory is replaced. While there is space in the physical memory, it
just adds the page to the physical memory.

Finally, this program will print to the user the final of the physical
memory and the amount of page faults that occurred.

-----------------------------------------------------------------------------------

File: optimal.py

The program requires importing library sys (already in the code)

To run the program open the terminal in the directory with this
file and the .txt file with the sequence of memory accesses and
write the following command:
  python3 optimal.py <Number of physical memory pages> <access sequence file>
For example:
  python3 optimal.py 5 input.txt

This program only requires you to write that command and nothing else.
After that the program will execute and finish by itself.

This program will receive two input from the shell command (input file and
the space of the memory) which will be used to initialize variables for use
in the program.

This program will read the sequence file and split its contents twice to
end up with the pages themselves.

This program is the implementation of the Optimal page replacement algorithm.
Given the assigned number of spaces for the physical memory, when that number of
spaces is reached, it removes the page in memory that will be referenced further
into the set of the virtual memory accesses. While there is space in the physical
memory, it just adds the page to the physical memory.

Finally, this program will print to the user the final of the physical
memory and the amount of page faults that occurred.

-----------------------------------------------------------------------------------

File: wsclock.py

The program requires importing library sys (already in the code)

To run the program open the terminal in the directory with this
file and the .txt file with the sequence of memory accesses and
write the following command:
  python3 wsclock.py <Number of physical memory pages> <tau> <access sequence file>
For example:
  python3 wsclock.py 5 2 input.txt

This program only requires you to write that command and nothing else.
After that the program will execute and finish by itself.

This program will receive two input from the shell command (input file and
the space of the memory) which will be used to initialize variables for use
in the program.

This program will read the sequence file and split its contents twice to
end up with the pages themselves.

This program is the implementation of the WSClock (Working Set Clock)
page replacement algorithm. Given the assigned number of spaces for the circular
physical memory, when that number of spaces is reached, the algorithm searches the
circular memory to see what page to replace. If the page is referenced it
dereferences it and moves to the next page. If a page is not referenced it
evaluates if it's in the working set, if it is, it moves to the next page and if it
isn't it replaces the page. If it does a full cycle and it had to dereference every
page, it replaces the page with the lowest time of last use. While there is space
in the physical memory, it just adds the page to the physical memory.

Finally, this program will print to the user the final of the physical
memory and the amount of page faults that occurred.

-----------------------------------------------------------------------------------
