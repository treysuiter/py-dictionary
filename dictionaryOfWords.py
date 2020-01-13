# Create an empty dictionary
# animal = dict()
# # Add k/v pairs
# animal["name"] = "Kevin"
# animal["breed"] = "Bulldog"
# animal["age"] = 5

# Create the dictionary with k/v pairs and assign to variable
# animal = {
#     "name": "Kevin",
#     "breed": "Bulldog",
#     "age": 5
# }

# for (key, value) in animal.items():
#     print(f"{key}: {value}")

# Output
# name: Kevin
# breed: Bulldog
# age: 5

"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["synthesis"] = "the combination of ideas to form a theory or system"

word_definitions["cartography"] = "the science or practice of drawing maps"

word_definitions["muppet"] = "An incompetent or foolish person"


"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print("muppet def", word_definitions["muppet"])
print("cartography def", word_definitions["cartography"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for (key, value) in word_definitions.items():
    print(f"The definition of {key} is {value}")