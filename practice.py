basket_num, try_num, *remains= map(int,open(0).read().split())
result = list(range(1,6))

while remains:
    left,right,*remains=remains
    result[left-1],result[right-1]=result[right-1],result[left-1]
print(*result)