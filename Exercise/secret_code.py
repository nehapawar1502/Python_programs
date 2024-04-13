

str = input("Enter the message")
words = str.split(" ")
coding = False

if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = "def"                                    
            r2 = "jkm"
            strnew = r1 + word[1:] + word[0] + r2
            nwords.append(strnew)
        else:
            nwords.append(word[::-1])

    print(" ".join(nwords))        
   
else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            strnew = word[3:-3]
            strnew = strnew[-1] + strnew[:-1]
            nwords.append(strnew)
        else:
             nwords.append(word[::-1])

    print(" ".join(nwords))  
            
            