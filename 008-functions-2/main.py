def greet(name: str, location: str) -> None:
    print(f"Hi {name}")
    print(f"How's the weather in {location} ?")


greet("Gary", "Pampisford")
greet(location = "Pampisford", name = "Gary")