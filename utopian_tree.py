"""
The Utopian tree goes through 2 cycles of growth every year. 
The first growth cycle occurs during the spring, when it doubles in height. 
The second growth cycle occurs during the summer, when its height increases by 1 meter. 
Now, a new Utopian tree sapling is planted at the onset of the spring. Its height is 1 meter. 
Can you find the height of the tree after N growth cycles?
"""

import sys

n_cases = sys.stdin.readline()
lines = sys.stdin.readlines()

height = 1
cycles_completed = 0
spring = True

for line in lines:
    num_cycles = int(line)
    for cycle in range(1, num_cycles - cycles_completed + 1):
        if spring: 
            height *= 2
            spring = False
        else:
            height += 1
            spring = True
    output = str(height) + "\n"
    sys.stdout.write(output)
    cycles_completed = num_cycles