def weird_faculty(grades):
    score = [0]
    for g in grades:
        score.append(score[-1] + (1 if g else -1))
    
    fsc = score[-1]
    for i in range(len(grades)):
        if score[i] > fsc:
            return i
        fsc += 1 if not grades[i] else -1
    
    return score[-1] > 0

print(weird_faculty([1,0,0,1,0]))
print(weird_faculty([1, 0, 0, 1, 1]))
print(weird_faculty([1, 1, 1, 0, 1]))
