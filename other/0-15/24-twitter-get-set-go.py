def get_set_go(calCounts, requiredCals):
    cum_cals = [0]
    for c in calCounts:
        tmp = []
        for cum_c in cum_cals:
            if cum_c + c == requiredCals:
                return True
            if cum_c + c < requiredCals:
                tmp.append(cum_c + c)
        cum_cals += tmp
    
    return False

print(get_set_go([2,9,5,1,6], 12))
print(get_set_go([2,3,15,1,16], 8))