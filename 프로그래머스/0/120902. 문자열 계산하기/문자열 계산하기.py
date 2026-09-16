def solution(my_string):
    cut = my_string.replace("-", "+-").replace(" ","")
    return sum([int(i) for i in cut.split("+")])