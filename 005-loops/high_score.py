default = [78,65,89,86,55,91,64,89]
scores = input("Please enter a comma separated list of scores: ")

if not scores.strip():
    scores = default
else:
    # scores = [int(i) for i in scores.split(",")]
    scores = scores.split(",")
    for n in range(0, len(scores)):
        scores[n] = int(scores[n])

highest = 0
for score in scores:
    if score > highest:
        highest = score

print(f"Highest score is {highest}")