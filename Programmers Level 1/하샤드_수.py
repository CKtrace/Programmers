def solution(x):
    value = sum(map(int, str(x)))
    if x%value == 0:
        return True
    else:
        return False
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges