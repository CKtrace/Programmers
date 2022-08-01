def solution(n):
    answer = 0
    n = n ** 0.5
    if n == int(n):
        return (n+1)**2
    else:
        return -1
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges