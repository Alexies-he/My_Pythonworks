temp = input()
if temp[0] in ['C', 'c']:
    f = 1.8*eval(temp[1:])+32
    print("F{:.2f}".format(f))
elif temp[0] in ['F', 'f']:
    c = (eval(temp[1:]))-32/1.8
    print("C{:.2f}".format(c))
else:
    print("错误")