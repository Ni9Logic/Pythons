def sortwords(words):
     words  = input('Enter Words but with spaces: ')
     print("\n")
     wordslist = words.split()
     print("Before Sorrting the list is: ", wordslist)
     sorted_wordslist = sorted(wordslist)
     print("List of Sorted Words are: ", sorted_wordslist)
     return sorted_wordslist