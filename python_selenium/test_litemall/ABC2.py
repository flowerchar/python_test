import turtle
import random

# 设置画布
screen = turtle.Screen()
screen.title("绘制彩色正方形")

# 创建一个Turtle对象
square_turtle = turtle.Turtle()

# 设置画笔的宽度
square_turtle.pensize(5)

# 绘制五个彩色正方形
for _ in range(5):
    # 清除画布上的所有图形
    square_turtle.clear()

    # 将画笔移动到画布的中心并设置方向为向右
    square_turtle.home()
    square_turtle.setheading(0)

    # 随机生成颜色
    color = (random.random(), random.random(), random.random())
    square_turtle.color(color)

    # 绘制正方形
    for _ in range(4):
        square_turtle.forward(100)
        square_turtle.right(90)

    # 提起画笔，向前移动一段距离，准备绘制下一个正方形
    square_turtle.penup()
    square_turtle.forward(150)
    square_turtle.pendown()

# 完成绘制
turtle.done()
