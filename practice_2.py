# import sys
# data = list(map(int,sys.stdin.readline().split()))

# print(data)

import sys
data = list(map(int,sys.stdin.readline().split("\n")))
print(max(data))
print(data.index(max(data))+1)