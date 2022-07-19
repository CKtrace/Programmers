def solution(n):
    num = list(str(n))
    num.sort(reverse=True)
    return int("".join(num))
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges