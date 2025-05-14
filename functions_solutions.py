# === Easy Question ===

# 1: Function Basics
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# 2: Default Parameters
def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# === Medium Question ===

# 1: Variable Arguments
def calculate_total(*prices, discount=0):
    total = sum(prices)
    if discount:
        total -= total * (discount / 100)
    return total

# 2: Closures 
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

# === Hard Questions ===

# 1: Recursion with O(log n)
def power(x, n):
    if n == 0:
        return 1
    half = power(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x

# 2: Higher-Order Functions
def compose(*functions):
    def composed(x):
        for func in reversed(functions):
            x = func(x)
        return x
    return composed

# Test Cases
if __name__ == "__main__":
    # Test case calculate_average
    print(calculate_average([5, 10, 15, 20]))
    print(calculate_average([]))         

    # Test case greet_user
    print(greet_user("PARAS"))                
    print(greet_user("Rohan", "Hi"))            

    # Test case calculate_total
    print(calculate_total(10, 20, 30))               
    print(calculate_total(10, 20, 30, discount=10))  

    # Test case create_multiplier
    double = create_multiplier(2)
    triple = create_multiplier(3)
    print(double(5))                      
    print(triple(5))                      

    # Test case power
    print(power(2, 10))                     
    print(power(3, 4))                    

    # Test case compose
    def add_one(x): return x + 1
    def double(x): return x * 2
    def square(x): return x ** 2

    f = compose(square, double, add_one)
    print(f(3))                           
