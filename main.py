# Initialize the list of words
fruits = [
    "banana", "avocado", "apple", "banana", "Strawberry",
    "orange", "BANANA", "grape", "bananaA", "avocado", "apple"
]

# Converting to lowercase and stripping whitespace
fruits = {fruit.strip().lower() for fruit in fruits}

# Define the desired order of fruits
desired_order = ['banana', 'apple', 'strawberry', 'orange', 'grape', 'avocado']

# Filter and order the normalized fruits to match the desired output
result = [fruit for fruit in desired_order if fruit in fruits]

print(result)