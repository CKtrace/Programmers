def solution(price, money, count):
    answer = -1
    sum_price = 0
    
    for i in range(count):
        sum_price += price * (i+1)
    
    if sum_price > money:
        answer = sum_price - money
    else:
        answer = 0
    
    return answer

#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges