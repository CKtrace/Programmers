def solution(s):
    answer = True
    
    s = s.lower()

    if s.count('p') == s.count('y'):
        return True
    else:
        return False
    
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges