print(r" _____                   _ _   _____       _                ")
print(r"/  ___|                 | (_) /  ___|     | |               ")
print(r"\ `--.  __ _ _ __  _   _| |_  \ `--.  ___ | |_   _____ _ __ ")
print(r" `--. \/ _` | '_ \| | | | | |  `--. \/ _ \| \ \ / / _ \ '__|")
print(r"/\__/ / (_| | | | | |_| | | | /\__/ / (_) | |\ V /  __/ |   ")
print(r"\____/ \__,_|_| |_|\__,_|_|_| \____/ \___/|_| \_/ \___|_|   ")
print("Ladataan...",end="")
errorflag=False
import os
import requests
if not os.path.isfile(os.path.join(os.path.abspath(os.path.dirname(__file__)),"kaikkisanat.txt")):
    print("Asennetaan...",end="")
    f=open(os.path.join(os.path.abspath(os.path.dirname(__file__)),"kaikkisanat.txt"),'w',encoding="utf-8")
    f.write(requests.get("https://raw.githubusercontent.com/hugovk/everyfinnishword/refs/heads/master/kaikkisanat.txt").text)
    f.close()
                                                           
rawwordlist=open(os.path.join(os.path.abspath(os.path.dirname(__file__)),"kaikkisanat.txt"),"r",encoding="utf-8").read().split("\n")
wordlist=[]
for word in rawwordlist:
    if word.isalpha():
        wordlist.append(word)
lettercount=5
print("Valmis")
print("Kirjoita /ohje ohjeisiin tai /poistu poistuaksesi")
while True:
    phase=0
    wrongchars=[]
    correctchars="*****"
    possiblechars=[]
    while True:
        errorflag=False
        text=input(": ").lower().rstrip()
        if text == "?" or text == "/help" or text == "/ohje":
            print("Kirjoita sanat jotka näkyvät sanulissa ja paina enter jokaisen sanan jälkeen")
            print("Kirjoita - kirjaimen jälkeen jos se on keltainen ja . kirjaimen jälkeen jos se on vihreä")
            print("Kun olet kirjoittanut kaikki sanat, paina enter uudelleen") 
            print("/kirjainmäärä [luku] (esim. /kirjainmäärä 6) muuttaaksesi kirjainmäärää")
            print("Kirjoita /ohje ohjeisiin tai /poistu poistuaksesi")
            continue
        elif text=="" or phase==5:
            break
        elif text[:13] == "/kirjainmäärä":
            try:
                lettercount=int(text[13:])
                print("Käynnistetään uudelleen...")
                wrongchars=[]
                correctchars="*"*lettercount
                possiblechars=[]
                continue
            except Exception as e:
                print("Error: "+str(e))
        elif text[:12] == "/lettercount":
            try:
                lettercount=int(text[12:])
                print("Käynnistetään uudelleen...")
                wrongchars=[]
                correctchars="*"*lettercount
                possiblechars=[]
                continue
            except Exception as e:
                print("Error: "+str(e))
        elif text == "/exit" or text=="/stop" or text=="/quit" or text=="/close" or text=="/q" or text=="/lopeta" or text=="/poistu":
            exit()
        else:
            for char in text:
                if not char in "abcdefghijklmnopqrstuvwxyzäö-.":
                    print("Error: "+char+" ei ole kirjain")
                    errorflag=True
                    break
            if errorflag:
                errorflag=False
                continue
            text+=" "
            for i in range(len(text)):
                if i>len(text)-1:
                    break
                if text[i].isalpha():
                    if text[i+1].isalpha() or text[i+1]==" ":
                        if wrongchars.count(text[i])==0:
                            wrongchars.append(text[i])
                    else:
                        if text[i+1] == ".":
                            s = list(correctchars)
                            s[i] = text[i]
                            correctchars = "".join(s)
                        elif text[i+1] == "-":
                            possiblechars.append((i,text[i]))
                if text[i]!=" ":
                    if not text[i+1].isalpha() or text[i+1]==" ":
                        text=text[:i+1]+text[i+2:]
            phase+=1
    #print("possiblechars: ",possiblechars)
    #print("wrongchars: ",wrongchars)
    #print("correctchars: ",correctchars)
    print("Mahdolliset sanat:")
    for word in wordlist:
        cancel=False
        for char in word:
            if char not in "abcdefghijklmnopqrstuvwxyzäö":
                cancel=True
        word2=word
        if len(word2)!=lettercount:
           continue
        for pc in possiblechars:
            if (pc[1] not in word2) or ((pc[1] in word2) and (word2[pc[0]] == pc[1])):
                cancel=True
        for i in range(len(correctchars)):
            if correctchars[i] != '*':
                if word2[i] == correctchars[i]:
                    word2=word2[:i]+' '+word2[i+1:]
                else:
                    cancel=True
        word2=word2.replace(" ","")
        for char in word2:
            if char in wrongchars:
                cancel=True
        if not cancel:
            print(word,end="  ")
    print()
        