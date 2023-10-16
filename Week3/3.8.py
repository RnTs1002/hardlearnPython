#冒泡排序
def bubbleSort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print("冒牌排序的结果为：",arr)
#选择排序
def selectSort(arr):
     for i in range(len(arr)-1):
         #记录最小数的索引
         minIndex = i
         for j in range(i+1,len(arr)):
             if arr[j] < arr[minIndex]:
                 minIndex = j
         #i不是最小数时，将i和最小数进行交换
         if i != minIndex:
             arr[i],arr[minIndex] = arr[minIndex],arr[i]
     print("选择排序的结果为：",arr)
#插入排序
def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = current
    print("插入排序的结果为：",arr)

import random
arr = list()
num = int(input())
for i in range(1,num+1):
    arr.append(random.randrange(1,100))
print(arr)

arr1 = arr
arr2 = arr
arr3 = arr

bubbleSort(arr1)
selectSort(arr2)
insertionSort(arr3)