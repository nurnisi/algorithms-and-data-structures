# tasksTypes
def tasksTypes(deadlines, day):
    ans = [0, 0, 0]
    for d in deadlines:
        if d <= day:
            ans[0] += 1
        elif day+1 <= d <= day+7:
            ans[1] += 1
        else:
            ans[2] += 1
    return ans
