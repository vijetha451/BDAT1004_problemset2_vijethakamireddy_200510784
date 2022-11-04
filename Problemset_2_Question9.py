words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

# Printing all words upper case
print([x.upper() for x in words])

# Printing all words lower case
print([x.lower() for x in words])

# Printing length of each word
print([len(x) for x in words])

# Printing the list containing a list for every word of list words,
# where each list contains the word in uppercase and lowercase and the length of the word
print([[x.upper(), x.lower(), len(x)] for x in words])

# Printing the list of words in list words containing 4 or more characters
print([x for x in words if len(x)>=4])
