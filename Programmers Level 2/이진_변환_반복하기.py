def solution(s):
    answer = []
    cnt = 0
    zero = 0
    while(s != '1'):
        if '0' in s:
            zero += s.count('0')
            s = s.replace('0', '')
            s = bin(len(s))[2:]
            cnt +=1
        else:
            s = s = bin(len(s))[2:]
            cnt +=1
    
    answer = [cnt, zero]
    return answer

#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges