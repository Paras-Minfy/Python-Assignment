# === Easy Questions ===

# 1. Tuple Basics
def swap_pairs(t):
    result = []
    for i in range(0, len(t) - 1, 2):
        result.extend([t[i + 1], t[i]])
    if len(t) % 2 != 0:
        result.append(t[-1])
    return tuple(result)

# 2. Tuple Unpacking
def get_stats(numbers):
    if not numbers:
        return (0, 0, 0, 0.0)
    total = sum(numbers)
    return (min(numbers), max(numbers), total, total / len(numbers))


# === Medium Questions ===

# 1. Named Tuples Alternative (simple class instead of namedtuple)
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

def top_student(students):
    best = students[0]
    best_avg = sum(best.grades) / len(best.grades)
    for student in students[1:]:
        avg = sum(student.grades) / len(student.grades)
        if avg > best_avg:
            best = student
            best_avg = avg
    return best

# 2. Tuple as Keys
def count_coordinate_occurrences(coords):
    count = {}
    for coord in coords:
        if coord in count:
            count[coord] += 1
        else:
            count[coord] = 1
    return count


# === Hard Questions ===

# 1. Complex Data Structure
def group_by_department(employees):
    departments = {}
    for name, department, salary in employees:
        if department not in departments:
            departments[department] = {"salaries": [], "names": []}
        departments[department]["salaries"].append(salary)
        departments[department]["names"].append(name)
    
    result = {}
    for dept, data in departments.items():
        avg_salary = sum(data["salaries"]) / len(data["salaries"])
        result[dept] = (avg_salary, data["names"])
    return result

# 2. Recursive Tuple Processing
def flatten_tuple(t):
    flat = []
    for item in t:
        if isinstance(item, tuple):
            flat.extend(flatten_tuple(item))
        else:
            flat.append(item)
    return tuple(flat)


# === Test Cases ===
if __name__ == "__main__":
    print(swap_pairs((1, 2, 3, 4)))
    print(swap_pairs((1, 2, 3)))

    print(get_stats([1, 2, 3, 4, 5]))

    alice = Student("Alice", 20, (85, 90, 95))
    bob = Student("Bob", 19, (70, 80, 90))
    charlie = Student("Charlie", 21, (90, 92, 93))
    print(top_student([alice, bob, charlie]).name)

    coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
    print(count_coordinate_occurrences(coords))

    employees = [
        ("Alice", "Engineering", 80000),
        ("Bob", "Marketing", 70000),
        ("Charlie", "Engineering", 90000),
        ("Diana", "HR", 65000),
        ("Eve", "Marketing", 75000)
    ]
    print(group_by_department(employees))

    nested = (1, (2, 3), (4, (5, 6)), 7)
    print(flatten_tuple(nested))
 