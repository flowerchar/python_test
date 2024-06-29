import turtle

# 定义彩虹颜色的英文单词列表
rainbow_color = ("red", "orange", "yellow", "green", "cyan", "blue", "purple")

# 设置画笔速度
# turtle.speed(2)
# 设置画笔宽度
turtle.pensize(50)
x, y = 0, 0
color_index = 0

# 循环绘制7个正方形，每个正方形的颜色不同|循环1
for color_index in range(7):
    # 设置画笔颜色
    turtle.pencolor(rainbow_color[color_index])
    # 提起画笔并移动到新的位置
    turtle.penup()
    turtle.goto(x - 100, y - 100)
    # 放下画笔开始绘制
    turtle.pendown()

    # 绘制一个正方形， 四条边|循环2
    for _ in range(4):
        # 向前移动200个像素, 也就是边长为200的正方形
        turtle.forward(200)
        # 向左转90度，向左转四次就回到原点
        turtle.left(90)

# 完成绘制，保持窗口打开
turtle.done()