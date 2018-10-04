def projectionArea(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    z = 0
    for col in grid:
        for row in col:
            if row != 0: z += 1
    
    x = 0
    for col in grid:
        maxx = 0
        for row in col:
            maxx = max(row, maxx)
        x += maxx

    y = 0    
    for i in range(len(grid)):
        maxy = 0
        for j in range(len(grid)):
            maxy = max(grid[j][i], maxy)
        y += maxy

    return z + x + y

def projectionArea2(grid):
    x, z = 0, 0
    for col in grid:
        x += max(col)
        for row in col:
            if row != 0: z += 1

    y = 0    
    for i in range(len(grid)):
        maxy = 0
        for j in range(len(grid)):
            maxy = max(grid[j][i], maxy)
        y += maxy

    return z + x + y