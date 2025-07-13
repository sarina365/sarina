number = input("Enter numbers separated by spaces: ").split()
number = [int(num) for num in number]

num = list(set(number))
print("without duplicate", num)