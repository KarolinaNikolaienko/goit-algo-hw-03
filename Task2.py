# Завдання 2:

# Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха»
# за умови, що користувач повинен мати можливість вказати рівень рекурсії.

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import turtle

def koch_curve_line(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve_line(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.title("Koch Snowflake")
    window.bgcolor("#1C2833")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.pen(pencolor="skyblue", fillcolor="lightblue")
    t.penup()
    t.goto(-size / 2, -size / 4)
    t.pendown()

    t.begin_fill()

    for angle in [60, -120, -120]:
        t.left(angle)
        koch_curve_line(t, order, size)
    
    t.end_fill()
    window.mainloop()


def main():
    order = int(input("Введіть рівень рекурсії: "))
    draw_koch_curve(order)

if __name__ == "__main__":
    main() 