# What does this piece of code do?
# Answer:Output the largest of ten randomly generated numbers from 1 to 100

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
stored_random_number=0
while progress<10:
	progress+=1 #When progress is less than 10, increase progress by one, progress is equal to zero at the beginning, that is, ten times
	n = randint(1,100) #Generate a random number between 1 and 100 and temporarily call it n
	if n > stored_random_number:
		stored_random_number = n #If n is greater than the last number, overwrite the last number

print(stored_random_number) #Finally output the answer
