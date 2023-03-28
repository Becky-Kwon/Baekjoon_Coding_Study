def BruteForceSearch(search, maintext):
    i = 0  # search index
    j = 0  # main index
    while i < len(search) and j < len(maintext):
        print("i, j", i, search[i], j, maintext[j])
        if search[i] != maintext[j]:
            i = 0
            j += 1
        else :
            if i == len(search) - 1:
                point = j
            i +=1
            j +=1

    return point - len(search) + 1



searchtext = 'Python'
maintext = "Hello Pycharm Python"
print(BruteForceSearch(searchtext, maintext))

searchtext = 'Pycharm'
maintext = "Hello Pycharm Python"
print(BruteForceSearch(searchtext, maintext))



#print(maintext[14:])
