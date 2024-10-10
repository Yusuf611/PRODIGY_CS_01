# Caesar Cipher Program

This is a simple Python program that demonstrates the Caesar Cipher, a type of substitution cipher in which each letter in the plaintext is shifted by a certain number of positions down or up the alphabet. The program provides options for both encryption and decryption of messages using a user-specified shift value.

## Features
- Encrypts messages using a Caesar Cipher with a shift value between 1 and 25.
- Decrypts messages using the same method.
- Displays the shifted alphabet for visualization.
- Input validation for messages and shift values.
- Interactive and user-friendly interface.

## Prerequisites
This program requires Python to be installed on your system. Additionally, it makes use of the `colorama` library for colored terminal output.

How to Use
Clone the repository:

```bash
git clone https://github.com/Yusuf611/caesar-cipher.git
cd caesar-cipher
```
Install the necessary dependencies:

```bash
pip install -r requirements.txt
```
Run the program:

```bash
python caesar_cipher.py
```

Follow the on-screen instructions to either encrypt or decrypt a message.

Program Options

Encrypt a message: Allows you to input a message and a shift value, and outputs the encrypted message.

Decrypt a message: Allows you to input an encrypted message and the shift value used for encryption, and outputs the original message.

Exit: Ends the program.
