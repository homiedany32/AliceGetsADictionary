import re
import time

def loadWordsFromFile(fileName):
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    return re.split('\s+', textData)

def binarySearch(anArray, item):
    LI = 0
    UI = len(anArray) - 1
    while LI <= UI:
        MI = (LI + UI) // 2
        if anArray[MI] == item:
            return MI
        elif anArray[MI] < item:
            LI = MI + 1
        elif anArray[MI] > item:
            UI = MI - 1
    return -1

def linearSearch(anArray, item):
    for i in range(len(anArray)):
        if anArray[i] == item:
            return i
    return -1

def main():
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    done = True
    while done:

        print("Main Menu")
        print("1: Spell Check a Word (Linear Search)")
        print("2: Spell Check a Word (Binary Search)")
        print("3: Spell Check Alice In Wonderland (Linear Search)")
        print("4: Spell Check Alice In Wonderland (Binary Search)")
        print("5: Exit")

        Selection = input("Enter menu selection (1-5):")
        if Selection == "1":
            WordInput = input("Enter a word you want to look for:")
            TimeStart = time.perf_counter()
            Output = linearSearch(dictionary, WordInput)
            if Output == -1:
                TimeEnd = time.perf_counter()
                TimeOutput = TimeEnd - TimeStart
                print("The word you typed in wasn't found, make sure you type in all lowercase letters", "(",TimeOutput,"seconds)")
            else:
                TimeEnd = time.perf_counter()
                TimeOutput = TimeEnd - TimeStart
                print("The word was found at possition:", Output, "(",TimeOutput,"seconds)")
        elif Selection == "2":
            WordInput = input("Enter a word you want to look for:")
            TimeStart = time.perf_counter()
            Output = binarySearch(dictionary, WordInput)
            if Output == -1:
                TimeEnd = time.perf_counter()
                TimeOutput = TimeEnd - TimeStart
                print("The word you typed in wasn't found, make sure you type in all lowercase letters", "(",TimeOutput,"seconds)")
            else:
                TimeEnd = time.perf_counter()
                TimeOutput = TimeEnd - TimeStart
                print("The word was found at possition:", Output, "(",TimeOutput,"seconds)")
        elif Selection == "3":
            TimeStart = time.perf_counter()
            result = 0
            print("This will take a bit, so hold your balls")
            for word in aliceWords:
                Output = linearSearch(dictionary, word)
                if Output == -1:
                    result += 1
            TimeEnd = time.perf_counter()
            TimeOutput = TimeEnd - TimeStart
            print("There were ", result, " words not found in the dictionary", "(",TimeOutput,"seconds)")
        elif Selection == "4":
            TimeStart = time.perf_counter()
            result = 0
            for word in aliceWords:
                print(word)
                Output = binarySearch(dictionary, word)
                if Output == -1:
                    result += 1
            TimeEnd = time.perf_counter()
            TimeOutput = TimeEnd - TimeStart
            print("There were ", result, " words not found in the dictionary", "(",TimeOutput,"seconds)")
        elif Selection == "5":
            done = False
        else:
            print("Error 404")

main()