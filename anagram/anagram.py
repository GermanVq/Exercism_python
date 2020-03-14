def find_anagrams(word, candidates):
    word=word.lower()
    anagram =[]
    for x in candidates:
        if sorted(word) == sorted(x.lower()) and word != x.lower():
            anagram.append(x)
    return anagram