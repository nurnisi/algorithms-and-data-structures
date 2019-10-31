import math
def perfectCity(departure, destination):
    def getSides(p):
        return [[math.ceil(p), round(math.ceil(p) - p, 2)], [math.floor(p), round(p - math.floor(p), 2)]]
    
    def distances(sidesDepa, sidesDest):
        return [abs(s1[0] - s2[0]) + s1[1] + s2[1] for s1 in sidesDepa for s2 in sidesDest]
    
    x1, y1 = departure
    x2, y2 = destination
    
    return min(distances(getSides(x1), getSides(x2))) + min(distances(getSides(y1), getSides(y2)))
