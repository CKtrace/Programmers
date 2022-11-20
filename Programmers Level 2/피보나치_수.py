def solution(n):
    a1, a2 = 0, 1
    for i in range(n-1):
        a1, a2 = a2, a2+a1
    return a2 % 1234567

#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges