f = open("JARGON.txt", "r")
wordList = f.read().split("\n")
stop = "XXX"
choice = '' #dummy value
while choice != stop:
    print("+++++++++++++++\n1. Exact Match\n2. Start of Term\n3. Within Term\n+++++++++++++++")
    choice = input("Choice? ")
    if choice == "1" or choice == "2" or choice == "3":
        term = input("Term? ")
        if choice == "1":
            count = 0
            for word in wordList:
                if word == term:
                    count += 1
                    print(word)
            print("There were %d matching term(s)" %count)
            print()
        elif choice == "2":
            count = 0
            for word in wordList:
                if word != term and word.startswith(term) == True:
                    count += 1
                    print(word)
            print("There were %d matching term(s)" %count)
            print()
        elif choice == "3":
            count = 0
            for word in wordList:
                if word!= term and word.startswith(term) == False and term in word:
                    count += 1
                    print(word)
            print("There were %d matching term(s)" %count)
            print()
    elif choice != stop:
        print("Invalid, try again.")
        print()
