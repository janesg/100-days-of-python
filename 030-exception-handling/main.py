try:
    with open("non_existent_file.txt") as f:
        f.readlines()
except FileNotFoundError as ex:
    print(f"An exception was thrown: {ex}")
else:
    print("Nothing to do here")
finally:
    print("The end is nigh...")

# ----------------------------------------------
f_input = "['Apple', 'Pear', 'Orange']"
fruits = eval(f_input)


def make_pie(idx: int):
    try:
        print(f"{fruits[idx]} pie")
    except IndexError:
        print(f"No fruit available with index of {idx}... no pie")


make_pie(4)

# ----------------------------------------------
fb_input = "[{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2}, {'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]"
facebook_posts = eval(fb_input)

total_likes = 0

for post in facebook_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        pass

print(f"Total Likes: {total_likes}")

# Can use dict.get() to completely avoid KeyError
print(f"Total Likes: {sum([post.get('Likes') for post in facebook_posts if post.get('Likes') is not None])}")
