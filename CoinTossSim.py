# @author: Ama Freeman
# @purpose: a simple coin toss simulator which asks the user
#    how many times to flip, flips the coin the amount, and returns
#    the amount of heads and tails tossed and the probability of the result
# @date: Jan. 19. 2017

#Import random library
import random

#Global Heads and Tails
heads = 0
tails = 0

def main():
    print("Welcome to coin toss!")
    #print("How fair is the coin?")
    
    coinFlips = input("How many times would you like to flip the coin? Enter a number: ")
    coinFlips = int(coinFlips)
    coinFlipper(coinFlips)

    #choice = input("Would you like to toss again? (Enter yes or no)")
    #if  choice is "no": break
    
    print("Thank you for using Coin Toss!")

#Define Coin Toss here
def coinFlipper(coinFlips):
    heads = 0
    tails = 0
    for x in range(0,coinFlips):
        coinFace = random.randint(1,2)

        if coinFace is 1:
            heads += 1
        else:
            tails += 1
            
    print("Total heads flipped is ", heads)
    print("Total tails flipped is ", tails)

    headsProb = heads / coinFlips
    tailsProb = tails / coinFlips

    print("Probability of heads is: ", headsProb)
    print("Probability of tails is: ", tailsProb)

#Define main function
if __name__ == '__main__':
    main()

    
