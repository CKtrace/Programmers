def solution(s):
    answer = True
    
    if (len(s) == 4 or len(s) == 6):
        answer = s.isdigit()
    else:
        answer = False
    
    return answer

#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges