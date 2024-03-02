# Q.7 Write a Python program to remove duplicates from a list. 
def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))

original_list = [1, 2, 3, 4, 2, 3, 5]
result_list = remove_duplicates(original_list)
print("List after removing duplicates:", result_list)