order = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

ipt = input()
while ipt != '0':
    shift, string = ipt.split()
    new_string = ''
    for ch in string[::-1]:
        new_string += order[(order.index(ch) + int(shift)) % 28]
    ipt = input()
    print(new_string)
