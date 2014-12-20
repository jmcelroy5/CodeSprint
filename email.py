"""
Task: 

You will be provided with a block of text, spanning not more than hundred lines. 
Your task is to find the unique e-mail addresses present in the text. 

Output:

All the unique e-mail addresses detected by you, in one line, in lexicographical order, with a semi-colon as the delimiter.

"""

import sys
import re 

input = sys.stdin.read()

emails = re.findall(r"\w{1,}\b@\w{1,}.\w{2,3}\b", input)

emails = list(set(emails)).sort()

output = ';'.join(emails)

sys.stdout.write(output)
