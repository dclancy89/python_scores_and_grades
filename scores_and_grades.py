import random

def grade():
	print "Scores and Grades"
	for x in range(11):
		grade = random.randint(60, 100)
		if grade < 70 :
			print "Score: " + str(grade) + "; Your grade is D"
		elif grade < 80 :
			print "Score: " + str(grade) + "; Your grade is C"
		elif grade < 90 :
			print "Score: " + str(grade) + "; Your grade is B"
		else:
			print "Score: " + str(grade) + "; Your grade is A"
	print "End of the program. Bye!"


grade()
