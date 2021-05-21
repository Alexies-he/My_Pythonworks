#TempConvert.py（此行为注释） 
TempStr = input("请输入带有符号的温度值：")#python是区分大小写的
if TempStr[-1] in ['F','f']:#[-1]为字符串的索引
    C = (eval(TempStr[0:-1])-32)/1.8#[0:-1]为字符串的切片，第1个开始不到最后一个
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:#['C','c']为列表类型
    F = 1.8*eval(TempStr[0:-1])+32#去除字符串最外层的“”双引号,将输入的字符串变为python可以理解处理的数据
    print("转换后的温度是{:.2f}F".format(F))#{}表示一个槽，后续变量填充到槽中；{:.2f}仅输出小数后两位
else:#python有严格的缩进要求，要表示语句的从属关系
    print("输入错误")
if
     