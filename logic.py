def process_user(name: str, age: int) -> str:
    if age < 18:
        return f"Hello {name}, you are under 18."
    return f"Welcome {name}, you are {age} years old!"