import random

from colorama import Fore, Back, Style 

#Sessiom

#mix three beat [0-9]

balence = 15000
fans = 10
artists = ["YG", "Post Malone","Justin Beiber", "Kanye", "Wiz Kalifa", "Snoop Dogg", "Kentric Lamar","Drake","Travis Scott"]
items = ["L.A house", "New york appartment", "Ferrarri", "Porche", "Rolex", "Bugattie", "Dog", "Restaurnet"]
haveArtist = False
currentArtist = ""

print(chr(27) + "[2J")

print("Welcome to Studio C time to begin your session")
print("Every hour cost $500 so spend your time wisley")

while True:
	print("\n=============NEW HOUR===================\n")
	print('Balence: ${0}'.format(balence))
	print('Fans: {0}'.format(fans))
	
	action = raw_input("What would you like to do in this hour [enter number] ")

	if action == 'a':
		print("[1] Make Beat")
		print("[2] Take walk")
		print("[3] Enhance Skills")
		print("[4] Buy something")
		action = raw_input("What would you like to do in this hour [enter number] ")

	try:
		val = int(action)
	except ValueError:
		print("-******************************-")
		print("Sorry, I didn't understand that.")
		print("-******************************-")
    	#better try again... Return to the start of the loop
    	
	else:
		action = int(action)
		if action == 1:
			print("\n::Alright lets Begin::")
			
			main = [random.randint(0,9), random.randint(0,9), random.randint(0,9)]

			print("::You have to mix three tracks to make a beat::\n")

			#print('match: {0}'.format(main))

			trackA = raw_input("Track 1 [pick a number [0-9]] ")
			trackB = raw_input("Track 2 [pick a number [0-9]] ")
			trackC = raw_input("Track 3 [pick a number [0-9]] ")

			userMain = [int(trackA), int(trackB), int(trackC)]

			match = 0

			for i in range(0, 3):
				for j in range(0, 3):
					if userMain[i] == main[j]:
						match += 1


			print('match: {0}'.format(match))
			if match >= 2:
				print("\nYo that beats dope man, lets run with this")
				songTitle = raw_input("What do you want to name the song ")
				print("Track just droped:::")
				if haveArtist:
					songTitle = songTitle + " (feat. " + currentArtist + ")"
					sales = random.randint(50000,500000)
					labelCut = sales * 0.4
					artistCut = sales * 0.2
					fans += random.randint(10000,100000)
				else:
					sales = random.randint(5000,50000)
					labelCut = sales * 0.4
					artistCut = 0
					fans += random.randint(100,1000)
				
				print("\n*---------Finances----------*")
				print('Here is how "{0}" did'.format(songTitle))
				print('sales: {0}'.format(sales))
				print('labelCut: {0}'.format(labelCut))
				print('artistCut: {0}'.format(artistCut))
				sales = sales - labelCut - artistCut
				print('into your pocket: {0}'.format(sales))
				print('Fans: {0}'.format(fans))
				print("*---------------------------*\n")
				balence += sales 
				haveArtist = False
			else:
				print("Thats not it, lets work some more")
				if haveArtist:
					print("Aww shit {0} has to go, you just didnt put on a show".format(currentArtist))
					haveArtist = False
				else:
					lostFans = random.randint(100,1000)
					if fans > lostFans:
						print("Aww shit you lost {0} fans".format(lostFans))
						fans -= lostFans

		elif action == 2:
			print("Walking...")
			bump = random.randint(0,1)
			if bump == 1:
				pick = random.randint(0,len(artists) - 1)
				print('You Bumped into {0} and you guys are doing a song together'.format(artists[pick]))
				currentArtist = artists[pick]
				haveArtist = True
			else:
				print("You had a nice walk")
		elif action == 4:
			print("\n::Cheapest thing is $100,000::\n")
			
			cost = random.randint(100000,800000)
			if cost < balence:
				print('You were feeling nice today and bought yourself a {0} and you love it'.format(items[random.randint(0,len(items) - 1)]))
				print("It set you back ${0}".format(cost))
			else:
				print("Not Enough Cash")
				








		print("Paying studios hour fee...")
		balence -= 1000









		


	

    
	
    
    


    	
 

