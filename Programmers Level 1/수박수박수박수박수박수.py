def solution(n):
    answer = "수박"*10000
    answer = "".join(map(str, answer[:n]))
    return answer
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges