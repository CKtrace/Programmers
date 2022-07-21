def solution(s):
    answer = ""
    if len(s)%2 == 0:
        a1 = s[len(s)//2 - 1]
        a2 = s[len(s)//2]
        answer = f'{a1}{a2}'
    else:
        b1 = s[len(s)//2]
        answer = f'{b1}'
    return answer
# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges