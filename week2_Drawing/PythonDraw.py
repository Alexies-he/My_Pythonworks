import turtle as t
t.setup(650, 350, 200, 200)#t.setup(width, height, startx, starty)设置窗体的大小以及位置
t.penup()#画笔控制函数，成对出现
t.fd(-250)#以海龟为中心的海龟坐标：t.fd()表示向前；t.bk()表示向后；绝对坐标：t.goto()
t.pendown()
t.pensize(25)#画笔宽度
t.pencolor("purple")
t.seth(-40)#t.seth(angle)表示改变海龟行进方向(绝对坐标);t.left(angle)/t.right(angle)
for i in range(4):#for <变量> in range(<参数>)：<被循环执行的语句>;i从0到n-1；"range 函数"：range（M, N）
    t.circle(40, 80)#circle(r, extent)根据半径r绘制extent角度的弧形，在海龟左侧距离为r的位置为圆心
    t.circle(-40, 80)
t.done()
t.circle(40, 80/2)
t.fd(40)
t.circle(16, 180)
t.fd(40 * 2/3)
t.done()#import <库名> <库名>.<函数名>（<函数参数>）或者from <库名>import* <函数名>（<函数参数>）
