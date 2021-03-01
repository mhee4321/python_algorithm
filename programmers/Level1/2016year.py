# def solution(a, b):
#     day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]  # 1월1일이 금요일이므로 7로 나눴을 때 인덱스 1이 금요일로 나오게 배열을 설정
#     mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 각 달의 날짜만큼 배열로 저장
#
#     return day[(sum(mon[:a - 1]) + b) % 7]  # mon배열의 (a-1)월까지 더한수에 <- 3월이면 2월까지의 날짜 다 더한수
import datetime

def solution(a,b):
    day_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return day_list[datetime.datetime(2016, a, b).weekday()]