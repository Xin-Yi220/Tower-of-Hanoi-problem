# Tower-of-Hanoi-problem
The Hanoi Tower problem is a classic mathematical and computer science problem that was proposed by the French mathematician Édouard Lucas in 1883. The problem is described as follows:

There are three columns and a series of discs of different sizes, which are stacked on one of the pillars in order of size to form a tower. The goal is to move the entire tower to another column, following the following rules:

Only one disc can be moved at a time.
The disc can only be moved from the top to the top of another column.
When moving between three columns, the larger disc cannot be placed on top of the smaller one.
The solution to the Tower of Hanoi problem involves a recursive algorithm, the basic idea of which is:

Moves all but the largest disc from the start pillar to the secondary column, in the order of target column, secondary column, and start column.
Move the largest disc from the start column to the target column.
Move all the disks on the secondary column to the target column, in the order of the starting column, the target column, and the auxiliary column.
