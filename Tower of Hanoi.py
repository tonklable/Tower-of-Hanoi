#!/usr/bin/env python
# coding: utf-8

# In[174]:

def print_pegs(pegs):
    base=max(pegs)[0]
    height=max([len(i) for i in pegs])
    print((" "*(base-1)+"||"+" "*(base))*3)
    for i in range(height):
        for disks in pegs:
            try:
                d=disks[height-i-1]
                print(" "*(base-d)+"OO"*d+" "*(base-d),end=" ")
            except:
                print(" "*(base-1)+"||"+" "*(base-1),end=" ")
        print("")
    print("="*(2+2*3*base))

def move_disk(pegs, source, dest):
    """Moves a single disk from peg source to peg dest.

    Args:
        pegs (array):       Array holding the pegs
        source ({0,1,2}):   Source peg
        dest ({0,1,2}):     Destination peg
    """
    # check if the move is valid
    # If the move is invalid, it will raise an error telling you what is the problem
    if source not in [0,1,2]:    raise AssertionError("source index out of bounds")
    if dest not in [0,1,2]:      raise AssertionError("destination index out of bounds")
    if pegs[source] == []:       raise AssertionError("source peg is empty")
    disk = pegs[source][-1] # disk is the top disk in the source peg
    if pegs[dest] and (pegs[dest][-1] <= disk): raise AssertionError("destination has smaller disk")

    # The move is valid so (i) we print the move on the screen
    print(f"STEP: move disk {disk} from peg {source} to peg {dest}")

    # then (ii) we execute the move
    pegs[source].pop()       # Take the disk on top of the source peg
    pegs[dest].append(disk)  # and move it to the top of the destination peg

    # and (iii) we display the new configuration
    print_pegs(pegs)

def hanoi(n):
    """Solves the "Tower of Hanoi" puzzle for n disks."""
    if n <= 0: raise AssertionError("n must be positive")

    # Initialization: the two lines below create the game with 3 pegs
    # and insert n disks on the leftmost peg (peg at index 0)
    # the largest disk is n, then n-1, then ..., until disk 2, and disk 1
    pegs = [[] for _ in range(3)]     # 3 empty pegs
    pegs[0] = list(range(n, 0, -1))   # fill the leftmost peg (peg 0) with n disks
    
    # Display the initial configuration.
    print("Starting configuration")
    print_pegs(pegs)
    
    # move the tower (=the n disks)
    # from the letftmost peg (peg 0) to the central peg (peg 1)
    move_tower(pegs, n, 0, 1)


##############################################################################
##############################################################################
##############################################################################

def move_tower(pegs, nb_disk, source, dest):
    """Moves a whole tower of nb_disk disks from source peg to dest peg.
    
    Args:
        pegs (array):        Array holding the pegs
        nb_disk ({1,...,n}): Number of disks to move (i.e. height of the tower)
        source ({0,1,2}):    Source peg (i.e., in which the tower is originally)
        dest ({0,1,2}):      Destination peg (i.e., where to put the tower)
    """
    spare = 3 - source - dest
    if nb_disk==0:
        pass
    else:
        move_tower(pegs,nb_disk-1,source,spare)
        move_disk(pegs,source,dest)
        move_tower(pegs,nb_disk-1,spare,dest)


# Main program
n = int(input("n = "))
hanoi(n)


