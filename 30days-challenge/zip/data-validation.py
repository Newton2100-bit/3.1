def validate_data(names, emails, ages):
    for name, email, age in zip(names, emails, ages):
        if not name or '@' not in email or age < 0:
            return False, f"Invalid data: {name}, {email}, {age}"
    return True, "All data valid"

names = ['Alice', 'Bob', 'Charlie']
emails = ['alice@email.com', 'bob@email.com', 'charlie@email.com']
ages = [25, 30, 35]

valid, message = validate_data(names, emails, ages)
print(f"{valid}: {message}")
