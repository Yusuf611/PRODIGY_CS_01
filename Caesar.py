from colorama import Fore, Style, init

init(autoreset=True)

def encrypt(message, shift):
    encrypted_message = ""
    
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char
    
    return encrypted_message

def decrypt(message, shift):
    decrypted_message = ""
    
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_message += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_message += char
    
    return decrypted_message

def display_shifted_alphabet(shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shifted = alphabet[shift:] + alphabet[:shift]
    print(Fore.YELLOW + "\nShifted Alphabet:")
    print(Fore.CYAN + f"Original: {alphabet}")
    print(Fore.CYAN + f"Shifted : {shifted}\n")

def main():
    print(Fore.GREEN + "Welcome to the Caesar Cipher Program")
    
    while True:
        print(Fore.BLUE + "Menu:")
        print(Fore.MAGENTA + "1. Encrypt a message")
        print(Fore.MAGENTA + "2. Decrypt a message")
        print(Fore.MAGENTA + "3. Exit")
        
        choice = input(Fore.WHITE + "Choose an option (1-3): ")
        
        if choice in ['1', '2']:
            message = input(Fore.WHITE + "Enter the message: ")
            if not message:
                print(Fore.RED + "Message cannot be empty. Please try again.")
                continue
            
            shift = input(Fore.WHITE + "Enter the shift value (1-25): ")
            try:
                shift = int(shift)
                if shift < 1 or shift > 25:
                    print(Fore.RED + "Shift value must be between 1 and 25. Please try again.")
                    continue
            except ValueError:
                print(Fore.RED + "Invalid input for shift value. Please enter a number between 1 and 25.")
                continue
            
            display_shifted_alphabet(shift)

            if choice == '1':
                print(Fore.GREEN + "Encrypted message: " + Fore.YELLOW + encrypt(message, shift))
            elif choice == '2':
                print(Fore.GREEN + "Decrypted message: " + Fore.YELLOW + decrypt(message, shift))
        
        elif choice == '3':
            print(Fore.GREEN + "Exiting the program. Goodbye!")
            break
        
        else:
            print(Fore.RED + "Invalid option. Please choose a number between 1 and 3.")
        
        again = input(Fore.WHITE + "Do you want to perform another operation? (y/n): ").lower()
        if again != 'y':
            print(Fore.GREEN + "Thank you for using the Caesar Cipher Program!")
            break

if __name__ == "__main__":
    main()
