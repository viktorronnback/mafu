import math

MORSE_LETTER_SPACE = " "
MORSE_WORD_SPACE = " / "

charTree = [
  '-', 'T','E','M','N','A','I','O','G','K','D',
  'W','R','U','S',' ',' ','Q','Z','Y','C','X','B',
  'J','P',' ','L',' ','F','V','H'
]


def left(i):
  """ Returns index of left child"""
  return 2*i + 1


def right(i):
  """ Returns index of right child """
  return 2*i + 2


def parent(i):
  """ Returns index of parent """
  return math.floor((i-1)/2)


def isLeaf(i):
  """ Returns True if i is leaf, otherwise False"""
  if (i >= len(charTree) or charTree[i] == ' '):
    return True
  return False



def main():
  # TODO: Remove 'pass' and implement your own function(s)
  pass


if __name__ == "__main__":
	main()
  