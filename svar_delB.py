
def main():
  sum = sum99()
  print("Summan av jämna tal 0-99: " + str(sum))

  nums = [1,3,9,1,3,2]
  maxNum = findMax(nums)
  print("Största talet: " + str(maxNum))



# Del 1.
def sum99():
  """ 1. Summera alla jämna tal från 0-99 """
  sum = 0
  
  for i in range(0,99):
    if i%2 == 0:
      sum += i
  
  return sum


# Del 2.
def findMax(numbersList):
  """ 2. Hitta maxtalet i en lista av siffror """
  max = 0

  for num in numbersList:
    if (num > max):
      max = num
  
  return max


# Del 3.
def writeToFile(filename):
  """ 3. Skriv ett program som skapar och skriver text till en fil """
  
  # File stängs automatiskt när 'with' används
  with open(filename, 'w') as f:
    f.write("This is some text\n")


# Del 4.
def fac(num):
  """ 4. Skriv en rekursiv funktion som räknar ut fakulteten av ett tal """
  if (num == 1 or num == 0):
    return 1*num
  
  return num*fac(num-1)

# Del 5.
def fib(n):
  prev = 0
  nextNum = 1
  series = [prev, nextNum]

  while (prev+nextNum < n):
    oldNext = nextNum # Temporary nextNum
    nextNum = prev + nextNum
    prev = oldNext
    
    series.append(nextNum)
    

  return series


if __name__ == "__main__":
  main()