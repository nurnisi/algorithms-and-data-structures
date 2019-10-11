import math
def autoscale_policy(inst, averageUtils):
    for u in averageUtils:
        if u < 25:
            inst = math.ceil(inst / 2)
        elif u > 60:
            inst = inst * 2 % (2*1e08)
    return int(inst)

print(autoscale_policy(1, [5,10,80]))