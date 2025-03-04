def binary_search(value, start, end):
    if start>end:
        return False
    median = (start+end)//2
    if N_list[median]>value:
        return binary_search(value, start, median-1)
    elif N_list[median]<value:
        return binary_search(value, median+1, end)
    else:
        return True
N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()
M  = int(input())
M_list = list(map(int, input().split()))
for m in M_list:
    if binary_search(m, 0,N-1):
        print(1)
    else:
        print(0)