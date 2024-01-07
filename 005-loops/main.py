fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(f"{fruit} Pie")

student_heights = "151 145 179"
heights = [int(i) for i in student_heights.split(" ")]
print("Average height of students = {:.2f}".format(sum(heights)/len(heights)))

default_end = "100"
end = int(input("Enter the upper bound of range: ").strip() or default_end)

total = 0
for n in range(2, end + 1, 2):
    total += n

print(f"Sum of all even numbers from 1 to {end} is {total}")
