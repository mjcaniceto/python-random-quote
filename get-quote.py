import random

def primary():
  #print("I am the hunter!")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[13])
  last = len(quotes) - 1
  rnd = random.randint(0, last)

  print(quotes[rnd])

if __name__== "__main__":
  primary()
