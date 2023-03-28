def BruteForceSearch(search, maintext):
    i = 0  # search index
    j = 0  # main index
    count = 0
    index_list = []

    while i < len(search) and j < len(maintext):
        #print("i, j", i, search[i], j, maintext[j])
        if search[i] != maintext[j]:
            j = j - i + 1
            i = 0
            #print("eee", i ,j)
        else :
            if i == len(search) - 1:
                point = j - len(search) + 1
                count += 1
                index_list.append(point)
                i = 0
            else :
                i +=1
                j +=1

    return count, index_list

##total = input()
##search = input()



total = 'ABB ABB ACC ABB'
search = 'ABB'
#total = 'ABC ABCDAB ABCDABCDABDE'
#search = 'ABCDABD'

result_count, result_index = BruteForceSearch(search, total)
print(result_count)
# print(' '.join(str(s) for s in result_index))
print(*result_index)  # unpacking operator(*)
