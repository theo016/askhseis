
import random
n=int(input('Εισαγάγετε τον όρο της ακολουθίας Fibonacci που θέλετε να ελέγξετε αν είναι πρώτος ή όχι: '))
p=0
k=0
j=1
count=int(n)-1
right=0

if n!=1 and n!=2:

  for i in range(int(count)):
     p=j+k
     k=j
     j=p

   

     for m in range(20):
        a=random.randint(0,100000)
        exp=(a**p) % p
        mod=(a%p)

        if (exp==mod):
           right += 1



  if (right==20):
     print("Ο αριθμός", p, "είναι πρώτος")
  else:
     print("Ο αριθμός", p, "δεν είναι πρώτος")
else:
    print("Ο αριθμός 1 είναι πρώτος")