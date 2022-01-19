from pickle import FALSE,TRUE
import random

max_rows = 6
max_letters = 5
allwords = ['Water','Seize','Serve','Sharp','Shelf','Shine','Slice','Solid','Space','Stand','Stone','Eager','Earth','Edict','Eight','Elect','Elite','Entry','Every','Extra']
inputs = []
checks = []
wordCount = 0

def getRandomWord():
    return random.choice(allwords)

def split(word):
    return [char for char in word]

def validateAll(wordlist):
    flag=1
    for word in wordlist:
        if word != 'GREEN':
            flag=0
            break

    if flag == 1:
        return TRUE
    else:
        return FALSE

todayword = getRandomWord()

def checkWord(word):

    outputCheck = []
    today_wordlist = split(todayword.upper())

    for i in range(max_letters):
        if(today_wordlist[i] == word[i]):
            outputCheck.insert(i,"GREEN")
        elif word[i] in today_wordlist :
            outputCheck.insert(i,"YELLOW")
        else:
            outputCheck.insert(i,"WHITE")

    checks.insert(wordCount,outputCheck)
    return outputCheck

for x in range(max_rows):
    word=input("\nEnter the word")
    listword = split(word.upper())
    if len(listword)!=5:
        print ("word must contain 5 letters only...please try again !")
    else:
        output=checkWord(listword)
        print(output)
        checkvalidate = validateAll(output)
        if checkvalidate == TRUE:
            print("\n\nWordle Solved !!!")
            break
        else:
            wordCount=wordCount+1

print("Original result for word[%s]:" %todayword)

for output in checks:
    print(output)