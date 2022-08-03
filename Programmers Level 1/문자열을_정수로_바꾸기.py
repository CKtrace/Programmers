def solution(s):
    answer = 0
    # list(map(str, s))
    if s[0] == '-':
        return int(s[1:]) * -1
    else:
        return int(s[:])
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges