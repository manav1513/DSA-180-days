def sol(arr , n , m):
    if(m == 0 or n == 0):
        return 0
    arr.sort()
    if (n < m):
        return -1
    diff = arr[n-1] - arr[0]
    for i in range(len(arr)-m+1):
        diff = min(diff , arr[i+m-1] - arr[i])
        return diff
    
N = 8
M = 5
A = [3, 4, 1, 9, 56, 7, 9, 12]
print(sol(A, N, M))