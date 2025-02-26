#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("gettysberg.txt", 'r')

  lineCount = 0
  wordCount = 0
  letterCount = 0
  
  for line in textFile:
    lineCount += 1
    #print(line)
    words = line.split()
  

    for word in words:
      wordCount += 1
      #print(word)

      for letter in word:
        letterCount += 1
        #print(letter)

  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Letters:", letterCount)
  

if __name__ == '__main__':
  main()
