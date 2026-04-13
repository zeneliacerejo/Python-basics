# Take marks as input from users
print ("Enter marks obtained in 4 subjects:")
maths = int(input("maths:"))
english = int (input("english:"))
science = int (input("science:"))
hindi = int(input("hindi:"))

#lets calculate the percentage of marks
sum =(maths+english+science+hindi)
print("Sum of all the mentioned subjects:",sum)

perc = sum/400*100
print (end="Percentage marks=")
print(perc)