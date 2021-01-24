# Tower of Hanoi

## Natprawee Pattayawij

## 24 January 2021

## 1 Introduction

<img src="https://github.com/tonklable/Tower-of-Hanoi/blob/main/Picture/Tower_of_Hanoi.png" width="500" />

```
Figure 1: The purpose of Tower of Hanoi
```
Tower of Hanoiis a puzzle consisting of three pegs and many different-sized disks. The purpose of this puzzle is to move all disks to another peg
obeying three rules:

1. Only one disk can be moved at one time.
2. Only the top disk of each peg can be moved.
3. No larger disk is placed above a smaller disk.

It is proved that the puzzle can be played with any number of disks, and the
minimum times to solve is 2n−1 [1].
Therefore, this project aims to solve the Tower of Hanoi Puzzle by receiving
the number of disks and showing the solution to move all disks from the first peg
to the second peg step-by-step. Moreover, this project illustrates the solution as
a model of the puzzle in order that the solution would be easier to understand.

## 2 Template

The template of this project is a list with three lists inside, and inside each list
there are numbers. The three inside lists represent the three pegs of Tower of Hanoi, and the numbers inside each list represents the disks on each peg. The
bigger number, the larger disk. Hence, the bigger numbers must be on the left
side of the smaller numbers according to the rule. As in the Figure 2, this step
is represented by the list [[3],[2,1],[]]. The variable used to keep the template is
”pegs”.

<img src="https://github.com/tonklable/Tower-of-Hanoi/blob/main/Picture/Towers-Of-Hanoi%20(1)%20(1).png" width="500" />

```
Figure 2: Tower of Hanoi in the template [[3],[2,1],[]]
```
## 3 Used Function

To solve Tower of Hanoi, this project uses 4 functions: printpegs, movedisks,
movetowers and hanoi.

### 3.1 Function printpegs(pegs)

printpegs is a function used to illustrate the model of each step from the template. The input of this function is the template pegs. For example, with the
input [[3],[2,1],[]], this function prints out the model as in Figure 3. Then, this
function can be applied to the movedisk function. (See Section 3.2)

<img src="https://github.com/tonklable/Tower-of-Hanoi/blob/main/Picture/Tower%20of%20Hanoi2.png" width="500" />

```
Figure 3: Tower of Hanoi model from the function printpegs
```
### 3.2 Function movedisk(pegs, source, dest)

movedisk function receive the input pegs, source and dest representing the
template, the beginning peg and the destination peg respectively. This function moves the top disk of the beginning peg to the destination peg obeying to the
rules. (If it violates the rules, a warning will appear.)
To simply describe this function, in the template, this function will pop out
the last member of the source list and add it to the dest list using two list
functions, pop and append.

### 3.3 Function movetower(pegs, nbdisk, source, dest)

movetower is a recursive function. The main point of this function is to move
all disks except the base (nbdisk-1 disks) to spare peg (another peg that is not
source or dest), move the base disk to dest peg and then move all disks at the
spare peg (that are just moved) to the dest peg.
However, there is a rule that only one disk can be moved at one time, so the
recursive function is applied. Before, the function moves nbdisk-1 disks, the
functions moved nbdisk-2 disks to the dest peg, and, to do that, more functions
were doing the same thing with nbdisk-3, nbdisk-4,... disks before. Therefore,
this function checks if nbdisk equals 0 or not. If so, the function will pass to
let the the base disk move to the dest peg. If not, the function will recursively
do until the nbdisk is 0. Then, the recursive function can move nbdisk disks
to another peg.
This function uses the function movedisk to move the base disk to the desk
peg.

### 3.4 Function hanoi(n)

hanoi includes printpegs function and movetower function. This function receives the number of starting disks and prints each step of the solution. This
function is used in the main program to get the solution.

## References

[1] Miodrag Petkovic.Famous puzzles of great mathematicians. American Math-
ematical Society, 2013.


