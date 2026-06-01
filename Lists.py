nums=[12,2,3,4,5,6,7,8,9,10]
print(nums[2:5])
nums.append(1)
nums.sort()
nums.remove(12)
nums.insert(11,11)
nums.extend([12,13])
nums.pop(4)
#nums.clear()
#nums.reverse()
copyList=nums.copy()
a=nums.count(1)

print(a)
print(f"length of nums:{len(nums)}")
print(nums)
for i in range(len(nums)):
    print(nums[i])