import math

MORSE_LETTER_SPACE = " "
MORSE_WORD_SPACE = " / "

charTree = [
  '-', 'T','E','M','N','A','I','O','G','K','D',
  'W','R','U','S',' ',' ','Q','Z','Y','C','X','B',
  'J','P',' ','L',' ','F','V','H'
]

def left(i):
  return 2*i + 1


def right(i):
  return 2*i + 2


def parent(i):
  return math.floor((i-1)/2)


def isLeaf(i):
  if (i >= len(charTree) or charTree[i] == ' '):
    return True
  return False



def decodeMorseWord(morseWord):
  """ Returns a decoded morse letter """
  morseChars = morseWord.split(MORSE_LETTER_SPACE)
  decodedWord = ""

  # Loop through each Morse character in Morse word
  for char in morseChars:
    currCharI = 0

    # Loop through each dot/dash in word
    for unit in char:
      if unit == '-':
        # Go left in tree
        currCharI = left(currCharI)
      elif unit == '.':
        # Go right in tree
        currCharI = right(currCharI)
      
      if isLeaf(currCharI):
        raise Exception("Morse character '" + char + "' not found in alphabet!")
    
    decodedWord += charTree[currCharI]
  
  return decodedWord


def decodeMorseSentence(morseSentence):
  morseWords = morseSentence.split(MORSE_WORD_SPACE)
  decodedSentence = ""

  for word in morseWords:
    decodedSentence += decodeMorseWord(word) + " "

  return decodedSentence


def main():
  morseCode = "-.-. --- -. --. .-. .- - ..- .-.. .- - .. --- -. ... / -.-- --- ..- / ... --- .-.. ...- . -.. / .. -"
  decoded = ""
  
  try:
    decoded = decodeMorseSentence(morseCode)
  except Exception as e:
    print("Error: " + str(e))
    exit(1)

  print("Decoded word: " + decoded)


if __name__ == "__main__":
	main()
