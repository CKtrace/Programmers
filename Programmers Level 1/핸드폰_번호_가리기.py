def solution(phone_number):
    answer = ''
    answer = '*' * (len(phone_number) - 4)
    answer = answer + phone_number[-4:]
    return answer
#출처: 프로그래머스 코딩 테스트 연습, 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges