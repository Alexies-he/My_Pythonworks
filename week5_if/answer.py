num = input()
real_num = 44
if eval(num) > real_num:
    print("猜大了，再试试")
elif  eval(num) < real_num:
    print("猜小了，再试试")
else:
    print("正确！")