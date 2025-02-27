import random

# List of simple AI-generated Python scripts
scripts = [
    """# Random number generator
import random
print("Random number:", random.randint(1, 100))""",

    """# Simple to-do list
tasks = []
def add_task(task):
    tasks.append(task)
    print("Task added:", task)
add_task("Finish GitHub automation")""",

    """# Fetch current date and time
from datetime import datetime
print("Current Date & Time:", datetime.now())""",

    """# Simple calculator
def add(a, b):
    return a + b
print("Sum:", add(5, 10))""",

    """# Motivational quote generator
import random
quotes = ["Keep going!", "You're doing great!", "Success is near."]
print(random.choice(quotes))"""
]

# Pick a random script
selected_script = random.choice(scripts)

# Save it as a new Python file
filename = "auto_generated_script.py"
with open(filename, "w") as file:
    file.write(selected_script)

print(f"Generated script saved as {filename}")
