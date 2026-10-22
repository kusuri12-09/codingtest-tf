def solution(my_string):
    answer = []
    arr = list(my_string)
    for i in range(len(arr)):
        if arr[i].isdigit():
            answer.append(int(arr[i]))
    answer.sort()

    return answer