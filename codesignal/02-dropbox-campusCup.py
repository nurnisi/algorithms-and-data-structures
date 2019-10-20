import collections
def campusCup(emails):
    d = collections.defaultdict(int)
    for em in emails:
        d[em.split('@')[1]] += 20
    
    
    for em, pts in d.items():
        pts //= 100
        if pts == 4: pts = 3
        if pts > 5: pts = 5
        d[em] = -pts
        
    att_sorted = sorted([[pts, em] for em, pts in d.items()])
    return [em for pts, em in att_sorted]