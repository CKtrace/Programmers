from collections import Counter

def solution(nums):
    cnt = Counter(nums)
    val = len(cnt.keys())
    
    if val > len(nums)/2 :
        answer = len(nums)/2
    else :
        answer = val
    return answer

# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges