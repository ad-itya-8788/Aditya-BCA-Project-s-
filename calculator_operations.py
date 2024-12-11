import gtts
import pygame
import time
import os

pygame.mixer.init()

def play_audio(file_path):
    if os.path.exists(file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    else:
        print(f"Error: File {file_path} not found.")

def speak_result(result):
    result_str = str(result)
    sound = gtts.gTTS(f"The result is {result_str}", lang='hi')
    sound.save("result.mp3")
    play_audio("result.mp3")

# Basic Operations
def add(x, y):
    result = x + y
    print(f"Addition result: {result}")
    speak_result(result)
    return result

def subtract(x, y):
    result = x - y
    print(f"Subtraction result: {result}")
    speak_result(result)
    return result

def multiply(x, y):
    result = x * y
    print(f"Multiplication result: {result}")
    speak_result(result)
    return result

def divide(x, y):
    if y == 0:
        print("Cannot divide by zero!")
        speak_result("Division by zero is not allowed.")
        return "Error"
    else:
        result = x / y
        print(f"Division result: {result}")
        speak_result(result)
        return result

# Additional Operations
def modulus(x, y):
    result = x % y
    print(f"Modulus result: {result}")
    speak_result(result)
    return result

def power(x, y):
    result = x ** y
    print(f"Power result: {result}")
    speak_result(result)
    return result

def square(x):
    result = x ** 2
    print(f"Square result: {result}")
    speak_result(result)
    return result

def cube(x):
    result = x ** 3
    print(f"Cube result: {result}")
    speak_result(result)
    return result

def square_root(x):
    if x < 0:
        print("Square root of a negative number is not real.")
        speak_result("Square root of a negative number is not allowed.")
        return "Error"
    result = x ** 0.5
    print(f"Square root result: {result}")
    speak_result(result)
    return result

def factorial(x):
    if x < 0:
        print("Factorial of a negative number is not defined.")
        speak_result("Factorial of a negative number is not allowed.")
        return "Error"
    elif x == 0 or x == 1:
        return 1
    else:
        result = 1
        for i in range(2, x + 1):
            result *= i
    print(f"Factorial result: {result}")
    speak_result(result)
    return result

def absolute(x):
    result = abs(x)
    print(f"Absolute value: {result}")
    speak_result(result)
    return result

def logarithm(x, base):
    if x <= 0 or base <= 0:
        print("Logarithm is not defined for non-positive numbers.")
        speak_result("Logarithm is not allowed for zero or negative values.")
        return "Error"
    import math
    result = math.log(x, base)
    print(f"Logarithm result: {result}")
    speak_result(result)
    return result

def gcd(x, y):
    import math
    result = math.gcd(x, y)
    print(f"GCD result: {result}")
    speak_result(result)
    return result

def lcm(x, y):
    if x == 0 or y == 0:
        print("LCM is not defined for zero.")
        speak_result("LCM is not allowed for zero.")
        return "Error"
    import math
    result = abs(x * y) // math.gcd(x, y)
    print(f"LCM result: {result}")
    speak_result(result)
    return result

def percentage(part, total):
    if total == 0:
        print("Percentage calculation requires a non-zero total.")
        speak_result("Percentage calculation is not allowed with zero total.")
        return "Error"
    result = (part / total) * 100
    print(f"Percentage result: {result}%")
    speak_result(f"{result} percent")
    return result

def exponent(x):
    import math
    result = math.exp(x)
    print(f"Exponent (e^x) result: {result}")
    speak_result(result)
    return result

def floor_divide(x, y):
    if y == 0:
        print("Cannot perform floor division by zero.")
        speak_result("Floor division by zero is not allowed.")
        return "Error"
    result = x // y
    print(f"Floor division result: {result}")
    speak_result(result)
    return result

def remainder(x, y):
    if y == 0:
        print("Cannot find remainder with zero as divisor.")
        speak_result("Remainder with zero divisor is not allowed.")
        return "Error"
    result = x % y
    print(f"Remainder result: {result}")
    speak_result(result)
    return result

def natural_log(x):
    if x <= 0:
        print("Natural logarithm is not defined for non-positive numbers.")
        speak_result("Natural logarithm is not allowed for zero or negative values.")
        return "Error"
    import math
    result = math.log(x)
    print(f"Natural log result: {result}")
    speak_result(result)
    return result

def extract_numbers(data):
    numbers = []
    words = data.lower().split()
    for word in words:
        if word.isdigit():
            numbers.append(int(word))
    return numbers
