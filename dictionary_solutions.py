# === Easy Questions ===

# 1. Invert Dictionary
def invert_dictionary(d):
    return {v: k for k, v in d.items()}

# 2. Merge Dictionaries
def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


# === Medium Questions === 

# 1. Dictionary Comprehensions
def word_frequencies(text):
    words = text.split()
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies

# 2. Nested Dictionaries
def add_contact(contacts, name, **details):
    if name not in contacts:
        contacts[name] = {}
    contacts[name].update(details)


# === Hard Questions ===

# 1. Dictionary Transformations
def transform_grades(grades_dict):
    result = {}
    for student, grades in grades_dict.items():
        average = round(sum(grades) / len(grades), 2)
        highest = max(grades)
        lowest = min(grades)
        result[student] = {
            "average": average,
            "highest": highest,
            "lowest": lowest
        }
    return result

# 2. Advanced Dictionary Operations
def generate_tree(paths):
    tree = {}
    for path in paths:
        parts = path.split("/")
        current = tree
        for part in parts:
            if part not in current:
                current[part] = {}
            current = current[part]
    return tree


# === Test Cases ===
if __name__ == "__main__":
    print(invert_dictionary({"a": 1, "b": 2, "c": 3}))

    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    print(merge_dictionaries(dict1, dict2))

    text = "the quick brown fox jumps over the lazy dog the"
    print(word_frequencies(text))

    contacts = {}
    add_contact(contacts, "Alice", phone="123-456-7890", email="alice@example.com")
    add_contact(contacts, "Bob", phone="987-654-3210")
    add_contact(contacts, "Alice", address="123 Main St")
    print(contacts)

    grades = {
        "Alice": [85, 90, 95],
        "Bob": [70, 80, 90],
        "Charlie": [90, 92, 93]
    }
    print(transform_grades(grades))

    paths = [
        "folder1/file1.txt",
        "folder1/folder2/file2.txt",
        "folder3/file3.txt"
    ]
    print(generate_tree(paths))
