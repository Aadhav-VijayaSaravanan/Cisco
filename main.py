from collections import Counter
import string
import curses

def numerix():
    def analyze_text(input_str):
        input_str_no_space = input_str.replace(" ", "")
        words = input_str.split()

        num_words = len(words)
        num_chars_with_space = len(input_str)
        num_chars_without_space = len(input_str_no_space)
        average_word_length = sum(len(word) for word in words) / num_words

        print("Number of words:", num_words)
        print("Number of characters (excluding spaces):", num_chars_without_space)
        print("Number of characters (including spaces):", num_chars_with_space)
        print("Average word length:", average_word_length)

    if __name__ == "__main__":
        input_str = input("Input: ")
        analyze_text(input_str)

def crimson():
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

    x = input("Enter a word: ")

    def count(x):
        num = len(x)
        return num

    def search(word):
        array = list(word)
        print("Binary representation:")
        for i in range(len(word)):
            if array[i] in ASCII:
                print(ASCII[array[i]], end=" ")
            else:
                print("Failure at", array[i])
                return False
        return True

    if not search(x):
        print()

def swap():
    strUpper = list(string.ascii_uppercase)
    strLower = list(string.ascii_lowercase)
    inp = input("Input the string: ")
    result = ""

    for char in inp:
        if char.isupper():
            index = strUpper.index(char)
            result += strUpper[25 - index]
        elif char.islower():
            index = strLower.index(char)
            result += strLower[25 - index]
        else:
            result += char

    print("Swapped string:", result)

def menu(stdscr):
  # Initialize variables
  curses.curs_set(0)
  curses.start_color()
  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
  stdscr.keypad(1)

  current_row = 0
  menu_options = ["Analyze Text (Numerix)", "Convert Word to Binary (Crimson)", "Swap Letter Case (Swap)"]

  while True:
      stdscr.clear()
      h, w = stdscr.getmaxyx()

      # Display the menu options
      for idx, option in enumerate(menu_options):
          x = w // 2 - len(option) // 2
          y = h // 2 - len(menu_options) // 2 + idx
          if current_row == idx:
              stdscr.attron(curses.color_pair(1))
              stdscr.addstr(y, x, option)
              stdscr.attroff(curses.color_pair(1))
          else:
              stdscr.addstr(y, x, option)

      stdscr.refresh()

      key = stdscr.getch()

      if key == curses.KEY_UP and current_row > 0:
          current_row -= 1
      elif key == curses.KEY_DOWN and current_row < len(menu_options) - 1:
          current_row += 1
      elif key == 10:  # Enter key
          stdscr.clear()
          stdscr.refresh()
          if current_row == 0:
              numerix()
          elif current_row == 1:
              crimson()
          elif current_row == 2:
              swap()
      elif key == 27:  # Escape key to exit
          break


if __name__ == "__main__":
  curses.wrapper(menu)
