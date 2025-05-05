import sys
import pyfiglet

def intro_to_algorithm():
    print("Welcome to the Algorithm Playground!")
    print("An algorithm is a step-by-step logical plan to solve a problem.\n")
    print("Input (most of the time) => logic => Output\n")
    print("Now you understood how to use your debugger ?")

def variable_basics():
    print("Variable Basics")
    age = 45
    name = "Mr Fantastic"
    pi = 3.14
    is_smart = True
    print(f"Name: {name}, Age: {age}, Pi: {pi}, Smart? {is_smart}")
    print()

    # CHALLENGE: Create 3 variables: a price, a product (just its name), and a quantity.
    # First, print the description of the purchase (for ex: You want to purchase 12 chairs at the price of 50 euros each).
    # Then print the price of the bill using the 3 variables. That price will be stored in a new variable first.


def input_output_demo():
    print("Simulated Input/Output")
    name = input()
    print(f"Hello, {name}!")
    print()

def string_tips():
    print("STRING TIPS — Working with strings in Python")

    demo = "Hello World"

    # Accessing characters by index
    print("Character at index 0:", demo[0])     # 'H'
    print("Last character:", demo[-1])          # 'd'
    # Python uses 0-based indexing. Negative indexes count from the end.

    # Slicing a string
    print("First 5 characters:", demo[:5])      # 'Hello'
    print("Last 5 characters:", demo[-5:])      # 'World'
    # demo[start:stop] includes start, excludes stop

    # Reversing a string
    print("Reversed string:", demo[::-1])       # 'dlroW olleH'
    # [::-1] creates a new string stepping backwards

    # Changing case
    print("Uppercase:", demo.upper())           # 'HELLO WORLD'
    print("Lowercase:", demo.lower())           # 'hello world'
    print("Swapcase:", demo.swapcase())         # 'hELLO wORLD'

    # Splitting and joining
    words = demo.split(" ")                     # ['Hello', 'World']
    print("Split by space:", words)
    joined = "_".join(words)
    print("Joined with underscores:", joined)   # 'Hello_World'

    # Finding substrings
    print("Does it contain 'World'?", "World" in demo)  # True
    print("Index of 'World':", demo.find("World"))       # 6
    print("Index of 'x':", demo.find("x"))               # -1 if not found

    # Replacing parts of a string
    print("Replace 'World' with 'Universe':", demo.replace("World", "Universe"))

    # Removing whitespace
    messy = "   clean me    "
    print("Original with spaces:", repr(messy))
    print("Trimmed:", messy.strip())             # 'clean me'

    # Counting occurrences
    text = "banana"
    print("How many 'a's:", text.count("a"))     # 3

    # challenges in the other doc, this has probably taken enough time already



def arithmetic_operations():
    print("Arithmetic Operations")
    a, b = 10, 3
    print(f"{a} + {b} = {a + b}")
    print(f"{a} % {b} = {a % b}")
    print(f"{a} ** {b} = {a ** b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} // {b} = {a // b}")s

    print()


def conditions_and_logic():
    print("Conditions and Logic")
    age = 17
    if age >= 18:
        print("You're an adult.")
    else:
        print("You're a minor.")
    print()


def loops_demo():
    print("Looping")
    for i in range(3):
        print("For loop:", i)
    print()

    i = 0
    while i < 2:
        print("While loop:", i)
        i += 1
    print()

    # CHALLENGE: Print even numbers from 1 to 20 using a loop,
    # CHALLENGE: Reverse a word using a loop

    # advanced CHallenge: OdooSAP !
    # For numbers from 1 to 50:
    # - If divisible by 3 or ends by 3, print "Odoo"
    # - If divisible by 5, print "SAP"
    # - Else, print the number

    # Further thinking:
    # What if we wanted to replace "OdooSAP" with something dynamic, of your choice?
    # Can you create a version that uses inputs to decide what to substitute?
    # Can you count how many times "Odoo", "SAP", and "OdooSAP" are printed?


def collection_basics():
    print("Collections")
    fruits = ["apple", "banana", "cherry"]
    person = {"name": "Lena", "age": 30}
    print("First fruit:", fruits[0])
    print("Name from dict:", person["name"])
    print()

    # CHALLENGE: Add a new fruit to the list and print all fruits
    # CHALLENGE: Create a dict with first_name and city and print both keys and values
    
    # super advanced challenge, using arithmetic operations aswell:
    # The Odoo Stock Builder
    # Goal: Calculate how many complete manufacturing batches can be produced from available stock.

    # You are given:
    # - A dict representing required quantities per unit (BoM)
    # - A dict representing current stock

    # Your task: Return how many full batches can be produced.

    # If an ingredient is missing in the stock, assume it's 0.

    # For testing purposes:
    # if __name__ == "__main__":
        # required = {"resistor": 2, "capacitor": 4, "chip": 1}
        # stock = {"resistor": 10, "capacitor": 20, "chip": 3}
        # print("Batches possible:", compute_batches(required, stock))  # Output: 3

        # stock_missing = {"resistor": 10}  # Missing capacitor and chip
        # print("Batches possible:", compute_batches(required, stock_missing))  # Output: 0

def function_basics():
    print("Functions & External Libraries")

    def greet(name):
        return f"Hi {name}, welcome!"

    print(greet("Amir"))

    print("\nASCII Art Greetings:")
    if sys.argv[1:]:
        for arg in sys.argv[1:]:
            fancy_text = pyfiglet.figlet_format(arg)
            print(fancy_text)

    # Example:
    # $ python script.py Odoo Python
    # will print large ASCII banners for "Odoo" and "Python". How does it work ?

    # can you reuse the code you wrote before, with the purchase of chairs, make it into a function, then use that function ?

def run_all():
    intro_to_algorithm()
    variable_basics()
    # input_output_demo()
    arithmetic_operations()
    conditions_and_logic()
    loops_demo()
    collection_basics()
    function_basics()


if __name__ == "__main__":
    run_all()
