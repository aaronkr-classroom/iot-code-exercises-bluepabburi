# 4장 과제

month = int(input("월을 입력하세요: "))
day = int(input("일을 입력하세요: "))

if month == 8 and day == 15:
    print("그날 광복절")

elif month % 2 == 0 and day == 16:
    print("그날")

elif month % 2 != 0 and day == 15:
    print("그날")

else:
    print("평일")