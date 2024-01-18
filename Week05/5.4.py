#希尔排序
def select_sort(arr):
    for i in range(len(arr)):
         # min index
         x = i
         for j in range(i, len(arr)):
             if arr[j] < arr[x]:
                 x = j
             arr[i], arr[x] = arr[x], arr[i]
    return arr

if __name__ == '__main__':
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(select_sort(arr))