import tweepy

auth = tweepy.OAuthHandler("JZVUp0w2vwWlKRG3R7zNg7RDU",
                           "nsiPwZfdGeXF8xa52Cgv4VVhjZaAm08YxYVKAg7W9bXNrU1zGC")
auth.set_access_token("1353823326838382592-TxPEbk1FpMq5Eu8GcRwpVVDTaytRw6",
                      "BxhetVdAaTK2qU2fBr7AI11hDvMrGAZfodGgsdjYzPUwR")

api = tweepy.API(auth)

userID=input('Εισαγάγετε το username του χρήστη που επιθυμείτε: ')

tweets = api.user_timeline(screen_name=userID,
                           include_rts=False,
                           tweet_mode='extended',
                           exclude_replies=True )
i=0
savedtweets=[]
while i<9:
  for info in tweets:
   savedtweets.insert(i,info.full_text)
   i+=1


alltweets=""
k=0
while k<9:
    alltweets=alltweets+savedtweets[k]
    k+=1



maxlength = 0
alltweets2=alltweets.split()
max_word1=""
max_word2=""
max_word3=""
max_word4=""
max_word5=""


for word in alltweets2:
    if word.isalpha():
        if len(word) > maxlength:
          maxlength=len(word)
          max_word1=word


maxlength=0
for word in alltweets2:
    if  word.isalpha():
      if len(word) > maxlength and word!=max_word1:
        maxlength=len(word)
        max_word2=word
maxlength=0
for word in alltweets2:
    if word.isalpha():
      if len(word) > maxlength and word!=max_word1 and word!=max_word2:
        maxlength=len(word)
        max_word3=word
maxlength=0
for word in alltweets2:
    if  word.isalpha():
       if len(word) > maxlength and word != max_word1  and word!=max_word2  and word!=max_word3:
         maxlength = len(word)
         max_word4= word


maxlength=0
for word in alltweets2:
    if word.isalpha():
      if len(word) > maxlength and word != max_word1  and word!=max_word2  and word!=max_word3 and word!=max_word4:
        maxlength = len(word)
        max_word5 = word


print('Οι 5 μεγαλύτερες λέξεις είναι:',max_word1, ',', max_word2, ',',max_word3,','  ,max_word4, ','  , max_word5 )


minlength=99999
min_word1=""
min_word2=""
min_word3=""
min_word4=""
min_word5=""


for word in alltweets2:
    if word.isalpha():
          if len(word) < minlength:
             minlength=len(word)
             min_word1=word


minlength=99999
for word in alltweets2:
       if word.isalpha():
           if len(word) < minlength and word!=min_word1:
             minlength=len(word)
             min_word2=word

minlength=99999
for word in alltweets2:
    if word.isalpha():
       if len(word) < minlength and word!=min_word1 and word!=min_word2:
        minlength=len(word)
        min_word3=word

minlength=99999
for word in alltweets2:
    if word.isalpha():
       if len(word) < minlength and word != min_word1  and word!=min_word2  and word!=min_word3:
          minlength = len(word)
          min_word4= word


minlength=99999
for word in alltweets2:
    if word.isalpha():
     if len(word) < minlength and word != min_word1  and word!=min_word2  and word!=min_word3 and word!=min_word4:
        minlength = len(word)
        min_word5 = word



print('Οι 5 μικρότερες λέξεις είναι:',min_word1,   ',' , min_word2,  ',',min_word3 , ','  ,min_word4, ',' ,min_word5 )
