import turtle

class Shape:
    def position(self):
        x = int(input("Zadaj x: "))
        y = int(input("Zadaj y: "))
        turtle.setposition(x, y)

    def farba(self):
        print("Tabuľka farieb: \n"
              "1.Modrá\n"
              "2.Žltá\n"
              "3.Zelená\n"
              "4.Rúžová\n"
              "5.Červená\n")
        farba = int(input("Zadaj číslo farby: "))
        if farba == 1:
            turtle.pencolor("blue")

        elif farba == 2:
            turtle.pencolor("yellow")

        elif farba == 3:
            turtle.pencolor("green")

        elif farba == 4:
            turtle.pencolor("pink")

        elif farba == 5:
            turtle.pencolor("red")


class Triangle(Shape):
    def draw(self):
        turtle.penup()
        self.position()
        turtle.pendown()
        self.farba()
        for i in range(3):
            turtle.forward(100)
            turtle.left(120)

class Rectangle(Shape):
    def draw(self):
        turtle.penup()
        self.position()
        turtle.pendown()
        self.farba()
        for i in range(2):
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)


class Circle(Shape):
    def draw(self):
        turtle.penup()
        self.position()
        turtle.pendown()
        self.farba()
        for i in range(1):
            turtle.circle(100)


triangle = Triangle()
triangle.draw()
rectangle = Rectangle()
rectangle.draw()
circle = Circle()
circle.draw()


turtle.exitonclick()