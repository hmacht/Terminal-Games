import time
import random
import pygame

pygame.init()



tokens = 10
counter = 0
point = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

while True:
	time.sleep(0.2)
	counter += 1
	isSlot = False
	ranNum = random.randint(1,3)
	if ranNum == 2:
		isSlot = True
		print("{0} [                 ]".format(point[counter]))
	else:
		print("XX [-----------------]")
	
	if counter == 9:
		counter = 0


	events = pygame.event.get()
	for event in events:
	    if event.type == pygame.KEYDOWN:
	        print("INSERTTOKEN")
