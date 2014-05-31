# author: big-bacon
import random
NumPeople = 6
Pic = 100
for j in range (0,Pic):
	ok = True 
	for i in range(0,NumPeople):
		r = random.randint(0,100)
		
		#print "r %d" % r
		if r > 50: 
			ok = False
			#print "person %d blinked"     %i
	if ok == True:
		print "Nobody blinked after taking %d pictures." %j
		break