class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def signed_in_decorator(func):
    # Can handle both positional and keyword args
    # def wrapper(*args, **kwargs):
    def wrapper(*args):
        if args[0].is_logged_in:
            return func(args[0])

    return wrapper


@signed_in_decorator
def create_log_post(user: User) -> str:
    return f"This is {user.name}'s new blog post"


big_g = User("Big G")
print(f"Not signed in... {create_log_post(big_g)}")
big_g.is_logged_in = True
print(f"Signed in... {create_log_post(big_g)}")

