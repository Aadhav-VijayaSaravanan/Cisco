# Crimson
Crimson is a Python script that processes input words, printing binary character representations using a predefined ASCII dictionary.
## About

Crimson is a Python script that takes a word as input, then prints the binary representation of each character using a predefined ASCII dictionary.

## Table of Contents

- [Usage](#usage)
- [ASCII Dictionary](#ascii-dictionary)
- [Example](#example)

## Usage

1. Clone or download this repository to your local machine.

2. Run the script by executing the following command in your terminal:

   ```bash
   python crimson.py

1.  Enter a word when prompted.

2.  The script will display the binary representation of each character in the input word.

## ASCII Dictionary
```python
   ASCII = {
     "A": '01000001', "B": '01000010', "C": '01000011', "D": '01000100', "E": '01000101',
     "F": '01000110', "G": '01000111', "H": '01001000', "I": '01001001', "J": '01001010',
     "K": '01001011', "L": '01001100', "M": '01001101', "N": '01001110', "O": '01001111',
     "P": '01010000', "Q": '01010001', "R": '01010010', "S": '01010011', "T": '01010100',
     "U": '01010101', "V": '01010110', "W": '01010111', "X": '01011000', "Y": '01011001',
     "Z": '01011010', "a": '01100001', "b": '01100010', "c": '01100011', "d": '01100100',
     "e": '01100101', "f": '01100110', "g": '01100111', "h": '01101000', "i": '01101001',
     "j": '01101010', "k": '01101011', "l": '01101100', "m": '01101101', "n": '01101110',
     "o": '01101111', "p": '01110000', "q": '01110001', "r": '01110010', "s": '01110011',
     "t": '01110100', "u": '01110101', "v": '01110110', "w": '01110111', "x": '01111000',
     "y": '01111001', "z": '01111010', "0": '00110000', "1": '00110001', "2": '00110010',
     "3": '00110011', "4": '00110100', "5": '00110101', "6": '00110110', "7": '00110111',
     "8": '00111000', "9": '00111001', " ": '00100000', "!": '00100001', "\"": '00100010',
     "#": '00100011', "$": '00100100', "%": '00100101', "&": '00100110', "'": '00100111',
     "(": '00101000', ")": '00101001', "*": '00101010', "+": '00101011', ",": '00101100',
     "-": '00101101', ".": '00101110', "/": '00101111', ":": '00111010', ";": '00111011',
     "<": '00111100', "=": '00111101', ">": '00111110', "?": '00111111', "@": '01000000',
     "[": '01011011', "\\": '01011100', "]": '01011101', "^": '01011110', "_": '01011111',
     "`": '01100000', "{": '01111011', "|": '01111100', "}": '01111101', "~": '01111110'
   }
```
## Example
```
Enter a word: Hello, World!

Binary representation:

01001000 01100101 01101100 01101100 01101111 00101100 00100000 01010111 01101111 01110010 01101100 01100100 00100001
