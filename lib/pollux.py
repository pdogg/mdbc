#@pdogg77
# When looking for interesting simple ciphers to use in a 
# CTF I stumbled on http://www.cs.ucf.edu/~gworley/files/pollux_and_frac_morse.txt
# implementation of "Pollux"

from random import choice
import common, morse

polluxexamplekey = {"dots": ["1","4","5","0"], "dashes": ["2","6","8"], "breaks": ["3","7","9"]}



def encode(plain, key):
  morsestring = morse.encodewithbreaks(plain)
  output = ""
  for i in range(len(morsestring)):
      if morsestring[i] == ".":
         output += choice(key['dots'])
      if morsestring[i] == "-":
         output += choice(key['dashes'])                                                                                         
      if morsestring[i] == " ":
         output += choice(key['breaks'])
  return output

def decode(ciphertext, key):
  morsestring = ""
  for i in range(len(ciphertext)):
      if ciphertext[i] in key['dots']:
        morsestring += "."
      if ciphertext[i] in key['dashes']:
        morsestring += "-"
      if ciphertext[i] in key['breaks']:
        morsestring += " "
  return morse.decode(morsestring)

