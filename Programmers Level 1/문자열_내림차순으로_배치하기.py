def solution(s):
    newlist = sorted(s, reverse=True)
    answer = ''
    for i in newlist:
        answer += i
    return answer
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges