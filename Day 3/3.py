def linear_search(data, target):
  for i, value in enumerate(data):
    if value == target:
      return i
  return -1


my_list = [10, 20, 30, 40, 50]
target_value = 30
index = linear_search(my_list, target_value)

if index != -1:
  print(f"Target found at index: {index}")
else:
  print("Target not found")
