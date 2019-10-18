def getEventsOrder(team1, team2, events1, events2):
    return [e for t, e in sorted(getEventsArr(team1, events1) + getEventsArr(team2, events2))]

def getEventsArr(team, events):
    arr = []
    for e in events:
        e_sp = e.split()

        # get time
        time = None
        if e_sp[1].isnumeric(): time = int(e_sp[1])
        elif e_sp[2].isnumeric(): time = int(e_sp[2])
        elif '+' in e_sp[1]: time = int(''.join(e_sp[1].split('+')))
        elif '+' in e_sp[2]: time = int(''.join(e_sp[2].split('+')))

        if time // 100 == 0: time *= 10
        arr.append((time, team + ' ' + e))
    return arr

team1 = 'EDC'
team2 = 'CDE'
events1 = ['asd 12 G', 'bsd csd 43 Y']
events2 = ['vsd 45+1 S nsd', 'nsd 46 G']
print(getEventsOrder(team1, team2, events1, events2))

