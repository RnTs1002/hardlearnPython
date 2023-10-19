nums = [5, 3, 6, 4, 1, 2, 8, 7]
def ShellSort(nums):
    step = len(nums)//2#初始化增量为数组长度的一半
    while step > 0:#增量必须是大于0的整数
        for i in range(step, len(nums)):#遍历需要进行插入排序的数
            ind = i
            while ind >= step and nums[ind] < nums[ind-step]: #对每组进行插入排序
                nums[ind], nums[ind-step] = nums[ind-step], nums[ind]
                ind -= step
        step //= 2#增量缩小一半
    print(nums)
ShellSort(nums)