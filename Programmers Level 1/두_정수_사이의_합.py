def solution(a, b):
    p1 = a-b+1
    p2 = b-a+1
    if a == b:
        return a
    elif a > b:
        return p1*(2*b+(p1-1))/2
    elif a < b:
        return p2*(2*a+(p2-1))/2
    
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges