#DiceRoll.py
#Name:
#Date:
#Assignment:
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  rollCount = input("How many rolls? ")
  rollCount = int(rollCount)
  for count in range(rollCount):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

  
    #find the sum total of the two dice
    total = die1 + die2
    #print(total)

    rolls[total-2] = rolls[total-2] + 1

  num = 2

  for r in rolls:
    print(num, ":", r, "%2.1f" %((r/rollCount)*100), "%")
    num = num + 1


  
  #print statictics for dice rolls




if __name__ == '__main__':
  main()
