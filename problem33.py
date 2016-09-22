words = ['15', '18', '44', '45', '81']


"""
Minglish lesson
===============
Welcome to the lab, minion. Henceforth you shall do the bidding of Professor
Boolean. Some say he's mad, trying to develop a zombie serum and all... but we
think he's brilliant!
First things first - Minions don't speak English, we speak Minglish. Use the
Minglish dictionary to learn! The first thing you'll learn is how to use the
dictionary.
Open the dictionary. Read the page numbers, figure out which pages come before
others. You recognize the same letters used in English, but the order of letters
is completely different in Minglish than English (a < b < c < ...).
Given a sorted list of dictionary words (you know they are sorted because you
can read the page numbers), can you find the alphabetical order of the Minglish
alphabet?
For example, if the words were ["z", "yx", "yz"] the alphabetical order would be
"xzy," which means x < z < y. The first two words tell you that z < y, and the
last two words tell you that x < z.
Write a function answer(words) which, given a list of words sorted
alphabetically in the Minglish alphabet, outputs a string that contains each
letter present in the list of words exactly once; the order of the letters in
the output must follow the order of letters in the Minglish alphabet.
The list will contain at least 1 and no more than 50 words, and each word will
consist of at least 1 and no more than 50 lowercase letters [a-z].
It is guaranteed that a total ordering can be developed from the input provided,
(i.e. given any two distinct letters, you can tell which is greater),
and so the answer will exist and be unique.
"""


def answer(words):
    from collections import defaultdict

    # Get full alphabet, unordered
    alph_length = len(set([letter for word in words for letter in word]))

    # Helper: append element to array if only if array is empty or the final element of array isn't equal to element
    def repend(l, e):
        l.append(e) if len(l) == 0 or (l[-1] is not e) else False
    # list_dic will be dictionary of ordered lists of all letters following every prefix
    list_dict = defaultdict(list)
    first = []
    # put in first letter array directly, save as '11' to avoid overlap with other letters
    for word in words:
        repend(first, word[0])
    list_dict['11'] = first
    # for each word, add each letter to dictionary, with each prefix as key
    for word in words:
        for i  in range(len(word)-1):
            repend( list_dict[word[:i+1]],  (word[i+1]) )
    # convert dictionary to list of lists that are greater than 1 (lists of 1 are useless)
    all_lists = [letter_list for key, letter_list in list_dict.items() if len(letter_list)>1]
    indexed_letters = defaultdict(list)
    for index, li in enumerate(all_lists):
        # if one of the lists happens to already be the length of the alphabet, we're done!
        if len(li) == alph_length:
            return ('').join(li)
        # map each letter to index of list it appears in
        for letter in li:
            indexed_letters[letter].append(index)

    solution = []
    for _ in range(alph_length):
        # get all current first letters
        firsts = [ li[0] for li in all_lists if len(li)>0]
        for letter in firsts:
            candidate = True
            # look for letter that ONLY appears as a first letter
            for n in indexed_letters[letter]:
               if all_lists[n][0]!= letter:
                    candidate = False
                    break
            # When found, append to solution, remove all occurances, and repeat
            if candidate == True:
                solution.append(letter)
                for n in indexed_letters[letter]:
                    all_lists[n].pop(0)
                break
    return ('').join(solution)

print(
    answer(words)
)
