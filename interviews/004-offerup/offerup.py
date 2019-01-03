# 
# Your previous Swift 4 content is preserved below:
# 
# /*
# 
# Write a method that produces images of a pine tree (with a stand) as output.
# 
# The method should take two parameters: one for the number of segments in the tree and one for the height of each segment. For example, a tree with 3 segments of height 4 would look like this:
# 
#      *
#     ***
#    *****
#   *******
#     ***
#    *****
#   *******
#  *********
#    *****
#   *******
#  *********
# ***********
#      *
#      *
#  *********
# 
# */
# 


def makeTree(segments, height):
    # define length of the last row of the last segment
    lenLast = 1 + (segments - 1) * 2 + (height-1) * 2
    
    # create segments
    for i in range(segments):
        lenSpaces = lenLast // 2 + 1 - i
        lenAst = 2 * i + 1
        # create rows in a segment
        for _ in range(height):
            spcStr, astStr = "", ""
            for _ in range(lenSpaces):
                spcStr += " "
            for _ in range(lenAst):
                astStr += "*"
            print(spcStr + astStr)
            lenSpaces -= 1
            lenAst += 2
    
    # create a base
    lenSpaces = lenLast // 2 + 1
    spcStr = ""
    for _ in range(lenSpaces):
        spcStr += " "
    for _ in range(2):
        print(spcStr + "*")
    
    astStr = ""
    for _ in range(lenLast - 2):
       astStr += "*"
    print("  " + astStr)
            
def makeTreeRefactored(segments, height):
    # define length of the last row of the last segment
    lenLast = 1 + (segments - 1) * 2 + (height-1) * 2
    
    # create segments
    for i in range(segments):
        lenSpaces, lenAst = lenLast // 2 + 1 - i, 2 * i + 1
        # create rows in a segment
        for _ in range(height):
            print(getRow(lenSpaces, lenAst))
            lenSpaces -= 1
            lenAst += 2
            
    # create a base
    lenSpaces = lenLast // 2 + 1
    print(getRow(lenSpaces, 1))
    print(getRow(lenSpaces, 1))
    print(getRow(2, lenLast - 2))
    
# get spaces and astericks string for a row 
def getRow(lenSpaces, lenAst):
    spcStr = " " * lenSpaces
    astStr = "*" * lenAst
    return spcStr + astStr

segments = 2
height = 2

print("Initial solution")
makeTree(segments, height)

print("\nRefactored solution")
makeTreeRefactored(segments, height)

print("Time complexity: O((segments + height) * segments)")
print("Space complexity: O(segments + height)")