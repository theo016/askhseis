import random

i = 0
j = 3
myList1 = []
myList2 = []
triada = []
protash = []
words = 0
with open('two_cities_ascii.txt','r') as file:     
    for line in file: 
        for word in line.split():
            myList1.append(word)

count = len(myList1)

while(True):
    if count >= 3:
        myList2.append(myList1[i:j])
        i += 1
        j += 1
        count -= 3
    else:
        break

while(len(myList2) > 0 and words < 200):
    randomElement = random.sample(myList2, 1)
    word1 = randomElement[0][1]
    word2 = randomElement[0][2]

    for k in range(len(myList2)):
        if word1 == myList2[k][0] and word2 == myList2[k][1]:
            triada = myList2[k]
            break

    del myList2[k]

    protash.append(word1)
    protash.append(word2)
    protash.append(triada[0])
    protash.append(triada[1])
    protash.append(triada[2])
    words += 5

    random.shuffle(protash)

    separator = " "
    print(separator.join(protash))

    protash.clear()

if words == 200:
    print('')
    print('Word limit has been reached.')
else:
    print('')
    print('No triads left.')