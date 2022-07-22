def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        new_arr = []
        for z in range(len(arr1[i])):
            new_arr.append(arr1[i][z] + arr2[i][z])
        answer.append(new_arr)
    return answer
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges