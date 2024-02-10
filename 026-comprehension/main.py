import random

import pandas

# List comprehension:
#   - [new_item for item in list]

# Create a new list of all even numbers from input list multiplied by 2 -> [4,8]
input_list = [1,2,3,4,5]
print([x*2 for x in input_list if x % 2 == 0])

# Works for anything that's a sequence, including a range
input_range = range(1,6)
print([x*2 for x in input_range if x % 2 == 0])

# Works on string
# - creates a list of single characters
# - which can be concatenated back into a single string
print(''.join([x.upper() for x in "superfly"]))

names = ['Bob', 'Frank', 'Enid', 'Charlie', 'Penelope', 'Amy']
print([name.upper() for name in names if len(name) > 4])

numbers_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print([pow(x, 2) for x in numbers_list])

# Create a list of all even numbers
numbers = "1, 1, 2, 3, 5, 8, 13, 21, 34, 55"
# As strings
print([x for x in list(map(lambda num: num.strip(), numbers.split(','))) if int(x) % 2 == 0])
# As integers
print([x for x in list(map(lambda num: int(num), numbers.split(','))) if x % 2 == 0])

# Create list of numbers that appear in both files
with open("./data/file1.txt") as f:
    file1_nums = list(map(lambda n: int(n), f.readlines()))

with open("./data/file2.txt") as f:
    file2_nums = list(map(lambda n: int(n), f.readlines()))

print([x for x in file1_nums if x in file2_nums])

# Dictionary comprehension:
#   - {new_key:new_value for item in list}
#   - {new_key:new_value for (key,value) in dict.items()}

# Assign random score to each 'student'
student_scores = {name:random.randint(1,100) for name in names}
print(student_scores)
student_passes = {name:score for (name,score) in student_scores.items() if score >= 60}
print(student_passes)

# Create dictionary of words and their length
word_str = "What is the Airspeed Velocity of an Unladen Swallow?"
word_dict = {word:len(word) for word in word_str.split()}
print(word_dict)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Iterate using for loop
for (key, value) in student_dict.items():
    print(key)
    print(value)

# Iterating over pandas Dataframe
student_df = pandas.DataFrame(student_dict)
print(f"DF:\n {student_df}")

for (key,value) in student_df.items():
    print(key)
    print(value)

# Use pandas specific iterrows()
for (index,row) in student_df.iterrows():
    print(f"{row.student} - {row.score}")