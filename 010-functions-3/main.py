def format_name(f_name: str, l_name: str) -> str:
    """ Takes a first and last name and returns them formatted
        as a full name in title case """
    return f"{f_name.lower().capitalize()} {l_name.lower().capitalize()}"


print(f"Formatted name: {format_name('boBbY', 'BOBbiNs')}")