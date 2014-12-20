"""
You are given an integer N. 
Find the digits in this number that exactly divide N and display their count. 
For N = 24, there are 2 digits - 2 & 4. Both these digits exactly divide 24. So our answer is 2.
"""

import sys

lines = sys.stdin.readlines()

for line in lines:
    n_str = line.strip()
    n = int(line)
    digits = list(n_str)
    num_divisible = 0
    if len(digits) < 2:
        continue
    for digit in digits:
        if int(digit) != 0 and n % int(digit) == 0:
            num_divisible += 1
    output = str(num_divisible) + "\n"
    sys.stdout.write(output)






