def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x + (x*i))
    return answer
#출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges