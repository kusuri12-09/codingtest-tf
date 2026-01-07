n = int(input())
lst = list(map(int, input().split()))
print("Sad" if (len(list(filter(lambda x: x%2==1, lst))))*2 >= len(lst) else "Happy")