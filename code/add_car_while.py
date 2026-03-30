# 4장 과제

num = 0
i = 1
while(True):
    i += 1
    
    if i % 2 == 0:
        num += i

    if i > 5:
        if i % 6 == 0:
            num-= i

    if i == 50: 
        break

print(num) 