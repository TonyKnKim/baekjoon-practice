# import sys
# data = list(map(int,sys.stdin.readline().split()))

# print(data)

import sys
data = map(int,sys.stdin.readlines())
data = [data.strip]
print(max(data))
print(data.index(max(data))+1)

print("깃허브 추가 수정")