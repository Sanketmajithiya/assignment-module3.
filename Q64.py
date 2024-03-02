# Q.64 Write a Python program to find the maximum and minimum numbers from the specified decimal numbers. 

# numbers = [float(num) for num in input("Enter decimal numbers separated by space: ").split()]
# print("Maximum number:", max(numbers, default="No numbers were provided."))
# print("Minimum number:", min(numbers, default=None) if numbers else None)


nums = [float(num) for num in input("Enter decimal numbers separated by space: ").split()]
print("Maximum number:", max(nums, default="No numbers were provided."), "\nMinimum number:", min(nums, default=None) if nums else None)
