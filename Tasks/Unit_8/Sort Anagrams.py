def sort_anagrams(list_of_strings):
    result = []
    for string in list_of_strings:
        found = False
        for sublist in result:
            if sorted(sublist[0]) == sorted(string):
                sublist.append(string)
                found = True
                break
        if not found:
            result.append([string])
    return result


        
list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
# print(sort_anagrams(list_of_words))
t = ('3', 'd', 67)
d = { t :87}
print(d[t])