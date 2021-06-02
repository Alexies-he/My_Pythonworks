age = eval(input())
if age < 4 :
    money = 0.
elif age < 18 :#elif是在if的逻辑下的，如果if为真，则elif后的语句都不执行
    money = 5
elif age < 65 :
    money = 10
else:money = 5
print("The prise is " + str(money)+" $")