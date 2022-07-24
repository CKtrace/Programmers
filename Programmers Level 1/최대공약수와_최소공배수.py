import math
def solution(n, m):
    answer = []
    gcd_val = math.gcd(n, m)
    lcm_val = n*m/gcd_val
    answer.append(gcd_val)
    answer.append(lcm_val)
    return answer
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges