# String Splitting and Joining

# Task: Given the string s, use string methods to:
# Split into a list: break the string into a list of substrings based on the delimiter ,.
# Join with spaces: combine the list of substrings back into a single string, with each element separated by a space.
# s:str ="apple,banana,cherry,dates"
# Expected Output:
# ["apple", "banana", "cherry", "dates"]
# apple banana cherry dates

# Split into a list
s:str ="apple,banana,cherry,dates"
split_list= s.split(",")

# Join with spaces
join_string = " ".join(split_list)
print(split_list)
print(join_string)

