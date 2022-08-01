def solution(num):
    cnt = 0
    while num != 1:
        if cnt != 500: 
            if num % 2 == 0:
                num = num / 2
            else:
                num = num*3 + 1
            cnt += 1
        elif cnt == 500:
            return -1
    return cnt
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges