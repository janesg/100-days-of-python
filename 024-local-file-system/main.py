file = open("my_file.txt")
print(file.read())
file.seek(0)
lines = file.readlines()
print(lines)
print(lines[1])
file.close()

# If file doesn't exist, it gets created
# Note: Absolute Windows path is C:\Temp\capture.txt
#   - Python root on Windows is implicitly C:, so no need to include it
#   - Python absolute path is OS agnostic and uses '/' seperator
file2 = open("/Temp/capture.txt", "w")
for page_no in range(1, 6):
    file2.write(f"This is line number {page_no}\n")
file2.close()

# Automated closure using 'with' syntax
with open("/Temp/capture.txt") as f:
    print(f.readlines()[3])
