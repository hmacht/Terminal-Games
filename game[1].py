import random
import sys

print(' _____             _      _   _       ') 
print('|  __ \           | |    | | | |      ') 
print('| |__) |___  _   _| | ___| |_| |_ ___ ') 
print('|  _  // _ \| | | | |/ _ \ __| __/ _ \\') 
print('| | \ \ (_) | |_| | |  __/ |_| ||  __/') 
print('|_|  \_\___/ \__,_|_|\___|\__|\__\___|') 

print("Conrols: [1] To stop playing press 'q'")


balence = 500


while True:
    print('You have ${0}'.format(balence))
    bet = raw_input("How much would you like to bet ")
    bet = int(bet)
    if balence == 0:
    	end = raw_input('You have no more money would you like to quit or restart (q/anyKey) ')
    	if end == 'q':
    		print("Exiting Game......")
    		sys.exit()
    	else:
    		print("NEW GAME")
    		balence = 500
    		print('You have ${0}'.format(balence))


    while bet > balence:
    	print('Insufficient Funds')
    	bet = raw_input("How much would you like to bet ")
    	bet = int(bet)

    color = raw_input("Place money on red or black (r/b) ")




    spin = random.randint(1,2)
    guess = 0

    if color == 'r':
    	guess = 1
    else:
    	guess = 2

    if spin == guess:
    	balence += bet*2
    	print('You won')
    else:
    	balence -= bet
    	print('You Lose')


    