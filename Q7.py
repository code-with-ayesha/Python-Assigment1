# String Stripping and Justifying

# Task: Given the string s, use string methods to:
# Remove leading/trailing spaces: remove all leading and trailing whitespace characters from the string.
# Left justify with '*': left justify the string within a field of width 20, using * as the fill character.
# Right justify with '*': right justify the string within a field of width 20, using * as the fill character.
# s:str ="   Python is fun!   "
# Expected Output:
# Python is fun!
# Python is fun!*****
# *****Python is fun!
s:str ="   Python is fun!   "
# Remove leading/trailing spaces
stripped_s = s.strip()

# Left justify with '*' within a field of width 20
left_justified_s = stripped_s.ljust(20, '*')

# Right justify with '*' within a field of width 20
right_justified_s = stripped_s.rjust(20, '*')

# Output the results
print(stripped_s)
print(left_justified_s)
print(right_justified_s)
