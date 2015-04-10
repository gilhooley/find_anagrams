from sys import argv

# we're expecting one argument, the path to the on-disk dictionary file
local_dictionary = open(argv[1])

def find_anagrams(dictionary):
    anagrams = {}
    res = []

    for word in dictionary:
        # we're only interested in words of length 4 or greater (5 including newline character)
        if len(word) >= 5:
            # slice off newline character
            word = word[:-1]
            # sort letters in word alphabetically--this is how we'll find and associate anagrams
            listified_word = ''.join(sorted(word.lower()))

            if not listified_word in anagrams:
                anagrams[listified_word] = []
            anagrams[listified_word].append(word)

    for key in anagrams:
        if len(anagrams[key]) >= len(key): 
            res.append(', '.join(anagrams[key]))

    print '\n'.join(res)

if __name__ == '__main__':
    find_anagrams(local_dictionary)
