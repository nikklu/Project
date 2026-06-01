def duplicates(nums):
    #a=set(nums)
    nums[:]=sorted(set(nums))
    return len(nums)

b=[1,1,2,2,3,4,5]
print(duplicates(b))