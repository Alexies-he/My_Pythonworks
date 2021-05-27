for num in range(1,21):
    print(num)
nums = [range(1,1000000)]#这样写并没有数字，相当于是字符组成的列表
for num in nums:
    print(num)
nums = list(range(1,1000001))
print(max(nums))
print(min(nums))
print(sum(nums))
nums = list(range(1,21,2))
for num in nums:
    print(num)
nums = []
for i in range(1,11):
    nums.append(i*3)
    print(nums[i-1])
nums = []
for i in range(1,11):
    nums.append(i**3)
    print(nums[i-1])
squares = [i**2 for i in range(1,11)]
print(squares)
 