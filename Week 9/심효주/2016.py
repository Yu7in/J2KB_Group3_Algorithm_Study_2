import datetime

def solution(a, b):
    answer = ''
    days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    #print(datetime.date(2016, a, b).weekday())
    answer = days[datetime.date(2016, a, b).weekday()]
    return answer

a = 5
b = 24
print(solution(a,b))
