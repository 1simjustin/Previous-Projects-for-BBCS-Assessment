def readLog():
    f = open("WEBLOG.txt", "r")
    return

def processLog():
    f = open("WEBLOG.txt", "r")
    g = open("SUMMARY.txt", "w")
    sep = ", "
    accessList = f.read().split("\n")
    accessDict = {}
    for access in accessList:
        domain, date = access.split(" - - ")
        date = date.strip("[").strip("]")
        if domain in accessDict:
            dateList = accessDict.get(domain)
            dateList.append(date)
            accessDict[domain] = dateList
        else:
            dateList = [date]
            accessDict[domain] = dateList
    noDomain = len(accessDict)
    highFreq = 0
    highFreqDomain = []
    for key in accessDict:
        g.write(key)
        if len(key)>23:
            g.write("\t")
        elif len(key)>15:
            g.write("\t\t")
        elif len(key)>7:
            g.write("\t\t\t")
        else:
            g.write("\t\t\t\t")
        listOfDates = accessDict.get(key)
        datesAccess = sep.join(listOfDates)
        g.write(datesAccess+"\n")
        freq = len(listOfDates)
        if freq > highFreq:
            highFreq = freq
            highFreqDomain = [key]
        elif freq == highFreq:
            highFreqDomain.append(key)
    print("Highest frequency (days):", highFreq)
    print("Accessed by:")
    for domain in highFreqDomain:
        print(domain)
    g.close()
    return

readLog()
processLog()
