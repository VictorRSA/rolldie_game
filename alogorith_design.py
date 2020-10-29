def main(x,**nums):
    for i in range(len(nums)):
        if nums[i] ==x:
            return i
        else:
            return -1
    print("hello linear search")
main([4,9,48,4,854,85,6523,4 ])