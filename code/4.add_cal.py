# 4장 과제

num = 0
for i in range(1, 51):
    
    if i % 2 == 0:
        num += i
        if i % 6  == 0:
            num -= i

print(num) 