import gtts
import pygame
import time
import os
import speech_recognition as sr
from calculator_operations import *  

try:
    pygame.mixer.init()
except pygame.error as e:
    print(f"Error initializing pygame mixer: {e}")
    exit()

# Function to play audio file
def play_audio(file_path):
    if os.path.exists(file_path):
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():  
                time.sleep(0.1)
        except Exception as e:
            print(f"Error playing audio file {file_path}: {e}")
    else:
        print(f"Error: File {file_path} not found.")

def show(data):
    try:
        audio_filename = "response_" + str(time.time()) + ".mp3"  
        sound = gtts.gTTS(data, lang='hi')
        sound.save(audio_filename)
        play_audio(audio_filename)
    except Exception as e:
        print(f"Error in text-to-speech: {e}")
        play_audio("error1.mp3")

def extract_numbers(data):
    numbers = []
    words = data.split()
    for word in words:
        if word.isdigit():
            numbers.append(int(word))
    return numbers

operations = {
    'add': add,
    'addition': add,
    'sum': add,
    'subtract': subtract,
    'minus': subtract,
    'sub': subtract,
    'difference': subtract,
    'multiply': multiply,
    'product': multiply,
    'multi': multiply,
    'divide': divide,
    'div': divide,
    'modulus': modulus,
    'mod': modulus,
    'power': power,
    'pawar': power,
    'square': square,
    'cube': cube,
    'square root': square_root,
    'squareroot': square_root,
    'factorial': factorial,
    'fact': factorial,
    'absolute': absolute,
    'abs': absolute,
    'logarithm': logarithm,
    'log': logarithm,
    'gcd': gcd,
    'lcm': lcm,
    'percentage': percentage,
    'per': percentage,
    'exponent': exponent
}

def manual_input():
    print("Enter a mathematical operation (e.g., add 5 and 3, factorial of 4):",end="")
    user_input = input().lower()

    show(f"App ne kaha hai: {user_input}")  

    numbers = extract_numbers(user_input)  

    if "factorial" in user_input or "fact" in user_input:
        if len(numbers) == 1:
            result = factorial(numbers[0])
            show(f"Factorial of {numbers[0]} is {result}")
            return
        else:
            show("Please provide a valid number for factorial.")
            return

    elif "absolute" in user_input or "abs" in user_input:
        if len(numbers) == 1:
            result = absolute(numbers[0])
            show(f"Absolute value: {result}")
            return
        else:
            show("Please provide a valid number for absolute value.")
            return

    elif "square" in user_input:  
        if len(numbers) >= 1:  
            result = square(numbers[0])  
            show(f"Square result: {result}")
            return
        else:
            show("Please provide a number for squaring.")
            return

    for operation in operations:
        if operation in user_input:
            if operation in ['factorial', 'abs', 'absolute', 'square']:  
                if len(numbers) >= 1:  
                    result = operations[operation](numbers[0])
                    show(f"Result: {result}")
                else:
                    show(f"Please provide a number for {operation}.")
                return
            elif len(numbers) >= 2:  
                result = operations[operation](numbers[0], numbers[1])
                show(f"Result: {result}")
                return
            else:
                show(f"Please provide two numbers for {operation}.")
                return

    show("Sorry, operation samajh nahi aaya.")

def audio_input():
    rec = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Ask Me Something, I am Listening.....☺️")
            rec.adjust_for_ambient_noise(source)  
            audio = rec.listen(source)  
        try:
            print("Processing.....")
            data = rec.recognize_google(audio).lower()  
            print(f"Recognized Speech: {data}")
            show(f"App ne kaha hai: {data}")  

            numbers = extract_numbers(data)  

            if "factorial" in data or "fact" in data:
                if len(numbers) == 1:
                    result = factorial(numbers[0])
                    show(f"Factorial result: {result}")
                    return
                else:
                    show("Please provide a valid number for factorial.")
                    return

            elif "absolute" in data or "abs" in data:
                if len(numbers) == 1:
                    result = absolute(numbers[0])
                    show(f"Absolute value: {result}")
                    return
                else:
                    show("Please provide a valid number for absolute value.")
                    return

            elif "square" in data:  
                if len(numbers) >= 1:  
                    result = square(numbers[0])  
                    show(f"Square result: {result}")
                    return
                else:
                    show("Please provide a number for squaring.")
                    return

            for operation in operations:
                if operation in data:
                    if operation in ['factorial', 'abs', 'absolute', 'square']:
                        if len(numbers) >= 1:  
                            result = operations[operation](numbers[0])
                            show(f"Result: {result}")
                        else:
                            show(f"Please provide a number for {operation}.")
                        return
                    elif len(numbers) >= 2:  
                        result = operations[operation](numbers[0], numbers[1])
                        show(f"Result: {result}")
                        return
                    else:
                        show(f"Please provide two numbers for {operation}.")
                        return

            show("Sorry, operation samajh nahi aaya.")
        except Exception as e:
            print(f"Sorry, I could not understand the audio input: {e}")
            show("Sorry, maine aapka input nahi samjha.")
    except Exception as e:
        print(f"Error with the microphone: {e}")
        show("Microphone mein kuch error aaya.")

def delete_response_files():
    for filename in os.listdir():
        if filename.startswith("response_") and filename.endswith(".mp3"):
            try:
                os.remove(filename)
            except Exception as e:
                print("")

def main():
    while True:  
        print("\nChoose an input method:")
        print("1. Audio Input")
        print("2. Text Input")
        print("3. Quit and Delete Temp File")
        choice = input("Enter 1 for Audio, 2 for Text, or 3 to Quit: ").strip()

        if choice == "1":
            audio_input()
        elif choice == "2":
            manual_input()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            show("Program band ho raha hai. Bye Bye!")
            delete_response_files() 
            break  
        else:
            show("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    show("Hello I am Calculator Mai app ki Kaise Madat Karu:")
    main()
