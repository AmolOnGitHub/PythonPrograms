def permiter(word):
    wordlist = list(word)

    while len(wordlist[0]) < len(word):
        for w in wordlist.copy():
            for letter in word:
                if letter not in w:
                    wordlist.append(w + letter)
            wordlist.remove(w)

    return wordlist

def permrec(word, wordlist = []):
    if wordlist == []:
        return permrec(word, list(word))

    if len(wordlist[0]) < len(word):
        for w in wordlist.copy():
            for letter in word:
                if letter not in w:
                    wordlist.append(w + letter)
            wordlist.remove(w)
        return permrec(word, wordlist)

    return wordlists


word = input()
wordlist = permrec(word)
print(wordlist)
print(len(wordlist))