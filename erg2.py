n = int(input("Εισάγετε τον όρο της ακολουθίας Fibonacci:"))
count = 0
n1 = 1
n2 = 1
sum = 0
IsPrime = True

if n < 0 :
    print("Εισάγετε έναν θετικό ακέραιο")
elif n == 0 :
    print("Ο αριθμός που εισάγατε είναι το 0")
elif n == 1 :
    print ("Ο αριθμός", n ,"είναι πρώτος")
elif n == 2 :
    print ("Ο αριθμός 1 είναι πρώτος")
else :
    while count < n - 2  :
        sum = n1 + n2
        n1 = n2
        n2 = sum
        count += 1
    from random import randint
    for i in range (1,21):
        a = randint(2,n)
        if pow(a, sum, sum) != a % sum :
            print ("Ο αριθμός", sum , "δεν είναι πρώτος")
            IsPrime = False
            break
    if IsPrime == True :
        print ("Ο αριθμός", sum ,"είναι πρώτος" )
