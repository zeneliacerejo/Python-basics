print ("Enter a number (Numerator)")
num = int(input())
print ("Enter a number (Denominator)")
numd = int (input())

if num % numd == 0 :
    print("\n" + str (num) + "Is divisible by "+ str(numd))
else:
    print("\n" + str (num) + "Is not divisible by "+ str(numd))
    