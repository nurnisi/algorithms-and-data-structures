from collections import Counter
def ScrabbleSolver(strArr): 
    # code goes here 
    d = Counter(strArr[3:])
    word, tile = strArr[1], strArr[2]
    words = [tile + word, word + tile]
    for c in word:
        words.append(tile + c)
        words.append(c + tile)

    count = 0
    for cur in words:
        if cur in d:
            count += 1

    return count

print(ScrabbleSolver(["15", "cat", "s", "as", "after", "apple", "bat", "cat", "cats", "department", "game", "games", "going", "scat", "water"]))