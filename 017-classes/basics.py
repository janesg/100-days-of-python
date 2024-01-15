class EmptyImplementation:
    pass


class User:
    def __init__(self, name: str):
        self.name = name
        self.followers = 0
        self.following = 0

    # To avoid 'forward-referencing' we use a string for the type hint
    def follow(self, user: 'User'):
        user.followers += 1
        self.following += 1

    def print(self):
        print(f"{self.name} - Followers: {self.followers}, Following: {self.following}")


bob = User("Bob")
# Can programmatically add attributes directly to the already created object
bob.id = "001"
print(f"{bob.name} = {bob.id}")

enid = User("Enid")
enid.follow(bob)
enid.print()
bob.print()
