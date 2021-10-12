#To print sum of 2 no's whose sum is b/w 1 and 1000
for t in range(int(input())):
 a, b = map(int,input().split())
 if a in range(-1001,1001) and b in range(-1001,1001):
  print(a+b)
