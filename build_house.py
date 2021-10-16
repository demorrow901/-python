import turtle as t


def draw_rectangle(width = 0, height = 0, fill = "#000000"):
    t.fillcolor(fill)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

def build_house(base_x = 500, base_y = 500, base_width = 100, base_height = 10,  base_fill = "#8D917A"):
    """
        base_x - это Х левого нижнего угла
        base_y - это Y левого нижнего угла фундамента

        Параметры фундамента:
        base_width - ширина фундамента
        base_height - высота фундамента
        base_fill - цвет заливки фундамента
    """
    t.speed(1)


    def build_base(base_x = 0, base_y = 0):
        # подготовка
        t.penup()
        t.goto(base_x, base_y)
        t.pencolor(base_fill)
        t.setheading(0)
        t.pendown()

        # рисование
        draw_rectangle(width = base_width, height = base_height, fill = base_fill)



    def build_walls():
        print("стены")


    def build_roof():
        print("крыша")


    build_base()
    build_walls()
    build_roof()



build_house(base_x = 0, base_y = 0, base_width = 200, base_height = 10, base_fill = "#755C48")
