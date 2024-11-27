nums = []
for i in range(int(input())):
    nums.append(int(input()))
squares = [i**2 for i in range(int(max(nums)**0.5 + 1))]
for num in nums:
    output = ''
    if num % 2 == 1:
        output += 'O'
    if num in squares:
        output += 'S'
    if output == '':
        print("EMPTY")
    else:
        print(output)