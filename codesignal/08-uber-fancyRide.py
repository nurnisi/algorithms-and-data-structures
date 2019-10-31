def fancyRide(l, fares):
    ubers = ['UberX', 'UberXL', 'UberPlus', 'UberBlack', 'UberSUV']
    for i in range(len(fares)-1, -1, -1):
        if fares[i] * l <= 20:
            return ubers[i]
