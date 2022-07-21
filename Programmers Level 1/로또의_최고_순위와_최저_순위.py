from collections import Counter

def solution(lottos, win_nums):
    answer = []
    cnt = 0
    
    for i in range(6) :
        if lottos[i] in win_nums :
           cnt += 1
    
    zero_counter = Counter(lottos)
    zero_counter[0]
    
    num1 = cnt + zero_counter[0]
    num2 = cnt
    
    if num1 == 6 or num2 == 6:
        if num1 == 6 and num2 == 6:
            answer.append(1)
            answer.append(1)
        else :
            answer.append(1)
    
    if num1 == 5 or num2 == 5:
        if num1 == 5 and num2 == 5:
            answer.append(2)
            answer.append(2)
        else :
            answer.append(2)
    
    if num1 == 4 or num2 == 4:
        if num1 == 4 and num2 == 4:
            answer.append(3)
            answer.append(3)
        else :
            answer.append(3)
    
    if num1 == 3 or num2 == 3:
        if num1 == 3 and num2 == 3:
            answer.append(4)
            answer.append(4)
        else :
            answer.append(4)
    
    if num1 == 2 or num2 == 2:
        if num1 == 2 and num2 == 2:
            answer.append(5)
            answer.append(5)
        else :
            answer.append(5)
    if num1 == 1 or num2  == 1 :
        if num1 == num2 :
            answer.append(6)
            answer.append(6)
        else :
            answer.append(6)
    if num1 == 0 or num2  == 0 :
        if num1 == num2 :
            answer.append(6)
            answer.append(6)
        else :
            answer.append(6)
            
    return answer


# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

