# Exercise 2

# Tasks:
# Define a dictionary.
# Add your content as values for keys.
# Follow the instruction in the pseudo code bellow:
# 1. Define a dictionary call story1, it should have the following keys: `'start', 'middle' and 'end'`
# 2. Print the entire dictionary.
# 3. Print the type of your dictionary.
# 4. Print only the keys.
# 5. Print only the values.
# 6. Print the individual values using the keys (individually, lots of print commands).
# 7. Now let's add a new key: value pair `'hero': yourSuperHero`

# Set up the dictionary
story1 = {
    "start": "Once upon a time there was a Junior DevOps Consultant.",
    "middle": "He completed the entire course correctly.",
    "end": "And finally he got a job!"
}

# Print the dictionary
print("Let's print the whole dictionary: ")
print(story1)

# Print the type of the dictionary
print("Let's print the type of the dictionary: ")
print(type(story1))

# Print the keys
print("Let's print the keys of the dictionary: ")
print(story1.keys())

# Print the values
print("Let's print the values of the dictionary: ")
print(story1.values())

# Print the individual values using the keys (individually, lots of print commands).
print("Let's print the individual values using the keys: ")
for item in story1:
    print(story1[item])

# Let's add a new key: value pair `'hero': yourSuperHero`
story1["hero"] = "Oliver&Benji"
print("hero: " + story1["hero"])
