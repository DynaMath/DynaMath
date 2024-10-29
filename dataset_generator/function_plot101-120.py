import math
import shutil
import os.path
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import pandas as pd
from plottable import Table
from PIL import Image, ImageDraw, ImageFont
from matplotlib.patches import *
import turtle as t


class Q101:
    # differentiable 2
    def __init__(self):
        self.a = rd.randint(-3, 3)
        self.b = rd.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        self.c = rd.choice([-1, 1])
        lst = [self.a - 2, self.a - 1, self.a, self.a + 1, self.a + 2]
        lst.remove(self.a)
        self.x1 = rd.choice(lst)
        lst.remove(self.x1)
        self.x2 = rd.choice(lst)
        self.query = f"The derivative of f(x) at x={self.x1} is ____ that at x={self.x2}  " \
                     f"choice: (A) larger than (B) smaller than (C) equal to"
        if self.b > 0:
            if self.x1 > self.a and self.x2 > self.a:
                self.answer = "C"
            elif self.x1 > self.a > self.x2:
                self.answer = "A"
            elif self.x2 > self.a > self.x1:
                self.answer = "B"
            elif self.x2 < self.a and self.x1 < self.a:
                self.answer = "C"
        elif self.b < 0:
            if self.x1 > self.a and self.x2 > self.a:
                self.answer = "C"
            elif self.x1 > self.a > self.x2:
                self.answer = "B"
            elif self.x2 > self.a > self.x1:
                self.answer = "A"
            elif self.x2 < self.a and self.x1 < self.a:
                self.answer = "C"

        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        absolute = (self.b ** self.c) * abs(x - self.a)
        plt.plot(x, absolute, color='purple', linewidth=1.5)

        plt.xlim(-8 * 1.1, 8 * 1.1)
        plt.ylim(-8 * 1.1, 8 * 1.1)

        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q102:
    # limit 4
    def __init__(self):
        self.constant_a = rd.randint(-3, 3)
        self.constant_b = rd.randint(-3, 3)
        self.constant_c = rd.randint(-3, 3)
        self.r = rd.randint(-9, 9)
        self.query = "What is the function value when x = 1?"
        self.answer = self.r
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = self.constant_a * x ** 3 + self.constant_b * x ** 2 + self.constant_c * x
        plt.plot(x, cubic, color='brown', linewidth=2.5)
        ax = plt.gca()
        plt.xlim(-10 * 1.1, 10 * 1.1)
        plt.ylim(-10 * 1.1, 10 * 1.1)
        plt.xticks([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.tick_params(axis='both', which='major', labelsize=12)
        plt.scatter(1, self.constant_a + self.constant_b + self.constant_c, color='white', edgecolor='black')
        plt.scatter(1, self.r, color='brown')
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q103:
    # polar coordinates 1
    def __init__(self):
        self.theta = rd.randrange(0, round(2 * np.pi) * 100) / 100
        self.r = rd.randint(1, 5)
        self.query = f"The polar coordinates of a point are ({self.r},{self.theta}). Determine the Cartesian " \
                     f"coordinates for the point. "
        self.rcos = round(self.r * np.cos(self.theta), 3)
        self.rsin = round(self.r * np.sin(self.theta), 3)
        self.answer = f"({self.rcos}, {self.rsin})"
        self.answer_type = "text"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        theta = [0, self.theta]
        r = [0, self.r]
        ax = plt.subplot(111, projection='polar')
        plt.polar(theta, r)
        ax.set_rticks([])
        ax.set_thetagrids(np.arange(0.0, 360.0, 90.0))
        plt.scatter(self.theta, self.r)
        plt.text(self.theta, self.r + 0.2, f"({self.r}, {self.theta})")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q104:
    # omnixie
    def __init__(self):
        self.hour = rd.randint(0, 23)
        self.minute = rd.randint(0, 59)
        if self.hour < 10 and self.minute < 10:
            self.clock = f"0{self.hour}:0{self.minute}"
        elif self.hour < 10 and self.minute >= 10:
            self.clock = f"0{self.hour}:{self.minute}"
        elif self.hour >= 10 and self.minute < 10:
            self.clock = f"{self.hour}:0{self.minute}"
        else:
            self.clock = f"{self.hour}:{self.minute}"
        self.query = "The clock shows the time. What time is it? Answer in the form of __:__."
        self.answer = self.clock
        self.answer_type = "text"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def drawgap(self):
        t.penup()
        t.fd(5)

    def drawline(self, draw):
        self.drawgap()
        t.pendown() if draw else t.penup()
        t.fd(40)
        self.drawgap()
        t.right(90)

    def drawdight(self, dight):
        self.drawline(True) if dight in [2, 3, 4, 5, 6, 8, 9] else self.drawline(False)
        self.drawline(True) if dight in [0, 1, 3, 4, 5, 6, 7, 8, 9] else self.drawline(False)
        self.drawline(True) if dight in [0, 2, 3, 5, 6, 8, 9] else self.drawline(False)
        self.drawline(True) if dight in [0, 2, 6, 8] else self.drawline(False)
        t.left(90)
        self.drawline(True) if dight in [0, 4, 5, 6, 8, 9] else self.drawline(False)
        self.drawline(True) if dight in [0, 2, 3, 5, 6, 7, 8, 9] else self.drawline(False)
        self.drawline(True) if dight in [0, 1, 2, 3, 4, 7, 8, 9] else self.drawline(False)
        t.left(180)
        t.penup()
        t.fd(20)

    def draw(self, num):
        t.reset()
        t.tracer(False)
        t.hideturtle()
        t.setup(400, 400)
        t.bgcolor("white")
        t.pencolor('black')
        t.width(10)
        t.speed(0)
        t.penup()
        t.fd(-150)
        for i in self.clock:
            if i == ':':
                t.left(270)
                t.fd(40)
                t.write(':', font=('arial', 60, 'normal'))
                t.left(180)
                t.fd(40)
                t.right(90)
                t.fd(40)
            else:
                self.drawdight(eval(i))
        t.update()
        ts = t.getscreen()
        ts.getcanvas().postscript(file=r"temp_image/image104.eps", colormode='color')
        im = Image.open("temp_image/image104.eps")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        im.save(dest_image_path, "PNG")
        im.close()
        os.remove(f"temp_image/image104.eps")


class Q105:
    # estimation
    def __init__(self):
        self.a = rd.choice([-1/4, -4, -1/3, -3, -1/2, -2, -1, 1, 1/2, 2, 1/3, 3, 1/4, 4, 1/5, 5])
        self.b = rd.choice([-1/4, -4, -1/3, -3, -1/2, -2, -1, 1, 1/2, 2, 1/3, 3, 1/4, 4, 1/5, 5])
        self.c = rd.choice([-3, -2, -1, 1, 2, 3])
        self.x1 = round(self.a + self.b + self.c)
        self.x1w1 = self.x1 + rd.randint(1, 2)
        self.x1w2 = self.x1 - rd.randint(1, 2)
        self.query = f"Which of the following numbers is the closest to the value of f(x) at x=1? " \
                     f"choice: (A) {self.x1w1} (B) {self.x1} (C) {self.x1w2} "
        self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):

        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = self.a * x ** 2 + self.b * x + self.c
        plt.plot(x, cubic, color='blue', linewidth=2.5)

        plt.xlim(-10 * 1.1, 10 * 1.1)
        plt.ylim(-10 * 1.1, 10 * 1.1)

        plt.xticks([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(1, self.a + self.b + self.c, color='violet')
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q106:
    # injective, surjective, bijective 3
    # symmetric/even function
    def __init__(self):
        self.constant = rd.randint(-4, 4)
        self.query = "Is the function f:R\{0}->R injective, surjective, or bijective? choice: (A) Injective (B) " \
                     "Surjective (C) Bijective (D) Neither "
        self.answer_type = "multiple choice"
        if self.constant % 2 == 0:
            self.answer = "D"
        elif self.constant % 2 != 0 and self.constant < 0:
            self.answer = "A"
        elif self.constant % 2 != 0 and self.constant > 0:
            self.answer = "C"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200, endpoint=True)
        function = x ** self.constant
        plt.plot(x, function, color='violet', linewidth=1.5)

        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-3, -2, -1, 1, 2, 3])
        plt.yticks([-3, -2, -1, 1, 2, 3])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.tick_params(axis='both', which='major', labelsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q107:
    # circle in square
    def __init__(self):
        self.r = rd.randint(1, 10)
        self.query = f"Two identical circles are placed into a square in such a way that they are tangent to each " \
                     f"other at a single point, and each circle is tangent to the square at two points, as shown. If " \
                     f"the radius of each circle is {self.r} , what is the area of the square? "
        self.answer = (6 + 4 * np.sqrt(2)) * self.r * self.r
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q107temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q107temp.png"), dest_image_path)


class Q108:
    # find value of function through table 2
    def __init__(self):
        self.a = rd.randint(-10, 10)
        self.b = rd.randint(-10, 10)
        self.c = rd.randint(-10, 10)
        self.d = rd.randint(-10, 10)
        self.eq1 = self.d
        self.eq2 = self.a + self.b + self.c + self.d
        self.eq3 = 8 * self.a + 4 * self.b + 2 * self.c + self.d
        self.eq4 = 27 * self.a + 9 * self.b + 3 * self.c + self.d
        self.eq5 = 64 * self.a + 16 * self.b + 4 * self.c + self.d
        self.query = "The function f(x) is a cubic function. What is the value of f(x) when x = 4?"
        self.answer = self.eq5
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        data = {
            'x': [0, 1, 2, 3, 4],
            'f(x)': [self.eq1, self.eq2, self.eq3, self.eq4, '?']
        }
        df = pd.DataFrame(data, columns=['x', 'f(x)'])
        df.set_index('x', inplace=True)
        Table(df,
              textprops={
                  'fontsize': 30
              })
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q109:
    # derivative 1
    def __init__(self):
        self.d = rd.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        self.e = rd.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        self.query = "The image shows the derivative of f(x). Where is the local min or max of f(x) at?"
        self.answer = -self.e / self.d
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x1 = np.linspace(-10, 10, 200, endpoint=True)
        f1 = self.d * x1 + self.e
        plt.plot(x1, f1, color='green', linewidth=1.5)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(-self.e / self.d, 0, color='orange')
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q110:
    # derivative 2
    def __init__(self):
        self.a = rd.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        self.b = rd.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        self.c = rd.choice([-1/3, -3, -1/2, -2, -1, 1, 1/2, 2, 1/3, 3])
        while self.a == self.b:
            self.b = rd.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        self.x1 = self.a
        self.x2 = self.b
        self.query = "The image shows the derivative of f(x). " \
                     "Where is the local min of f(x) at? "
        if self.c > 0:
            self.answer = max(self.x1, self.x2)
        elif self.c < 0:
            self.answer = min(self.a, self.b)
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = self.c * (x - self.a) * (x - self.b)
        plt.plot(x, cubic, color='slateblue', linewidth=2.5)

        plt.xlim(-8 * 1.1, 8 * 1.1)
        plt.ylim(-8 * 1.1, 8 * 1.1)

        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(self.a, 0, color='violet')
        plt.scatter(self.b, 0, color='violet')
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q111:
    # derivative 3
    def __init__(self):
        self.a = rd.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        self.b = rd.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        self.c = rd.choice([-1/3, -3, -1/2, -2, -1, 1, 1/2, 2, 1/3, 3])
        while self.a == self.b:
            self.b = rd.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        self.x1 = self.a
        self.x2 = self.b
        self.query = "The image shows the derivative of f(x). Where is the local max of f(x) at?"
        if self.c > 0:
            self.answer = min(self.x1, self.x2)
        elif self.c < 0:
            self.answer = max(self.a, self.b)
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = self.c * (x - self.a) * (x - self.b)
        plt.plot(x, cubic, color='slateblue', linewidth=1.5)

        plt.xlim(-5 * 1.1, 5 * 1.1)
        plt.ylim(-5 * 1.1, 5 * 1.1)

        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(self.a, 0, color='violet')
        plt.scatter(self.b, 0, color='violet')
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q112:
    # find the area of azure part
    def __init__(self):
        self.side = rd.randint(1, 10)
        self.query = "Find the area of azure part."
        self.answer = np.pi * 1/8 * self.side * self.side
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        triangle = plt.Polygon([(2, 2), (-2, 2), (-2, -2), (2, -2)], closed=True, fill=True, edgecolor='black',
                               facecolor='white')
        wedge = Wedge((-2, 2), 4, -90, 0, facecolor="azure", edgecolor="black")
        circle = Wedge((-2, 0), 2, -90, 90, edgecolor="black", facecolor="white", fill=True)
        ax.add_patch(triangle)
        ax.add_patch(wedge)
        ax.add_patch(circle)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(-0.2, 2.2, f"{self.side}", fontsize=14)
        plt.text(2.2, 0, f"{self.side}", fontsize=14)
        plt.text(-2.6, 0, f"{self.side}", fontsize=14)
        plt.text(-0.2, -2.6, f"{self.side}", fontsize=14)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q113:
    # area of ring 2
    def __init__(self):
        self.a = rd.randint(3, 5)
        self.b = self.a + 2
        self.theta = rd.randint(1, 15) * 10
        self.query = f"The angle of the sector is {self.theta} degree. What is the area of the blue part?"
        self.answer = np.pi * self.a * self.a * self.theta/360 + (np.pi * (self.b * self.b - self.a * self.a)) * (360 - self.theta) / 360
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(-7 * 1.1, 7 * 1.1)
        plt.ylim(-7 * 1.1, 7 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        circle = Circle((0, 0), self.a, edgecolor="black", facecolor="white", fill=True)
        circle2 = Circle((0, 0), self.b, edgecolor="black", facecolor="azure", fill=True)
        wedge1 = Wedge((0, 0), self.a, 0, self.theta, edgecolor="black", facecolor="azure", fill=True)
        wedge2 = Wedge((0, 0), self.b, 0, self.theta, edgecolor="black", facecolor="white", fill=True)
        ax.add_patch(circle2)
        ax.add_patch(circle)
        ax.add_patch(wedge2)
        ax.add_patch(wedge1)
        plt.text(1, -1, f'r = {self.a}', fontsize=11)
        plt.text(-2, -1, f'R = {self.b}', fontsize=11)
        plt.hlines(0, -self.b, 0, colors="black")
        plt.scatter(0, 0, color="black")
        plt.hlines(0, 0, self.a, colors="black", linewidth=3)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q114:
    # easy map/direction 1:
    def __init__(self):
        lst = ["university", "restaurant", "park", "library"]
        self.N = rd.choice(lst)
        lst.remove(self.N)
        self.S = rd.choice(lst)
        lst.remove(self.S)
        self.E = rd.choice(lst)
        lst.remove(self.E)
        self.W = rd.choice(lst)
        self.query = f"What is on the north side of home? choice: (A) university (B) restaurant (C) park (D) library"
        if self.N == "university":
            self.answer = "A"
        elif self.N == "restaurant":
            self.answer = "B"
        elif self.N == "park":
            self.answer = "C"
        else:
            self.answer = "D"
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
        self.level = "elementary school"

    def draw(self, num):
        plt.xlim(-10 * 1.1, 10 * 1.1)
        plt.ylim(-10 * 1.1, 10 * 1.1)

        plt.xticks([-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        plt.yticks([-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(-1, 0, "home", fontsize=18)
        plt.text(0, 9, self.N, fontsize=18, ha='center')
        plt.text(7, 0, self.E, fontsize=18)
        plt.text(0, -9, self.S, fontsize=18, ha = 'center')
        plt.text(-10.5, 0, self.W, fontsize=18, ha='left')
        ax.annotate('', xy=(0, -8), xytext=(0, -0.2), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        ax.annotate('', xy=(0, 8.8), xytext=(0, 1.3), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        ax.annotate('', xy=(-5, 0.3), xytext=(-1.2, 0.3),
                    arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        ax.annotate('', xy=(7, 0.3), xytext=(2, 0.3), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        plt.text(9, 9, "N", fontsize=20)
        plt.text(8.9, 7.5, r'$\blacktriangleright$', fontsize=20, rotation=90)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q115:
    # fill in the blankets
    def __init__(self):
        self.sum = rd.randint(50, 100)
        self.center = rd.randint(1, 10)
        self.rsum = self.sum + self.center
        self.n1 = rd.randint(1, self.sum - 1)
        self.n2 = self.sum - self.n1
        self.n3 = rd.randint(1, self.sum - 1)
        self.n4 = self.sum - self.n3
        self.query = f"The sum of the three numbers on each of the two lines of the cross is {self.rsum}. " \
                     f"Find the number in the center."
        self.answer = self.center
        self.answer_type = "float"
        self.subject = "puzzle test"
        self.level = "elementary school"

    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        circle0 = Circle((0, 0), 1, edgecolor="black", facecolor="white", fill=True)
        circle1 = Circle((-5, 0), 1, edgecolor="black", facecolor="white", fill=False)
        circle2 = Circle((5, 0), 1, edgecolor="black", facecolor="white", fill=False)
        circle3 = Circle((0, 5), 1, edgecolor="black", facecolor="white", fill=False)
        circle4 = Circle((0, -5), 1, edgecolor="black", facecolor="white", fill=False)
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.plot([0, 0], [-4, -1], color='black', linewidth=1.5)
        ax.plot([-4, -1], [0, 0], color='black', linewidth=1.5)
        ax.plot([0, 0], [1, 4], color='black', linewidth=1.5)
        ax.plot([1, 4], [0, 0], color='black', linewidth=1.5)
        ax.add_patch(circle1)
        ax.add_patch(circle2)
        ax.add_patch(circle3)
        ax.add_patch(circle4)
        ax.add_patch(circle0)
        plt.text(0, 5, f"{self.n1}", fontsize=12, ha='center', va='center')
        plt.text(5, 0, f"{self.n3}", fontsize=12, ha='center', va='center')
        plt.text(0, -5, f"{self.n2}", fontsize=12, ha='center', va='center')
        plt.text(-5, 0, f"{self.n4}", fontsize=12, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q116:
    # relation between squares and triangles
    def __init__(self):
        self.AC = rd.randint(1, 20)
        self.BC = self.AC + rd.randint(-2, -1)
        self.AB = self.AC + rd.randint(-2, 2)
        self.query = "Squares ACDE and CBFG are constructed on the outside of △ABC with AC " \
                     f"and BC as one side, respectively. Point P is the midpoint of EF. AC = {self.AC}, BC = {self.BC}, " \
                     f"AB = {self.AB}, find the length of PQ."
        self.answer = self.AB / 2
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q116temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q116temp.png"), dest_image_path)


class Q117:
    # bounded 1
    def __init__(self):
        self.up = rd.randint(1, 5)
        self.down = rd.randint(1, 10)
        self.c = rd.randint(1, 9)
        self.query = "Is this function bounded in interval [-8, 8]? choice: (A) Yes (B) No"
        if self.up > self.down:
            self.answer = "B"
        elif self.up <= self.down and self.down % 2 != 0:
            self.answer = "B"
        elif self.up <= self.down and self.down % 2 == 0:
            self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x1 = np.linspace(-10, 10, 200, endpoint=True)
        f1 = x1 ** self.up / (self.c + x1 ** self.down)
        plt.plot(x1, f1, color='deeppink', linewidth=2.5)
        plt.xlim(-8 * 1.1, 8 * 1.1)
        plt.ylim(-8 * 1.1, 8 * 1.1)

        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q118:
    # bounded 2
    def __init__(self):
        self.up = rd.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        self.query = "What is the least upper bound of this function?"
        self.answer = abs(self.up) * np.pi / 2
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x1 = np.linspace(-10, 10, 200, endpoint=True)
        f1 = self.up * np.arctan(x1)
        plt.plot(x1, f1, color='deeppink', linewidth=1.5)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        if self.up == 1:
            plt.title(f"arctan(x)", fontsize=14)
        elif self.up == -1:
            plt.title(f"-arctan(x)", fontsize=14)
        else:
            plt.title(f"{self.up}arctan(x)", fontsize=14)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q119:
    # shaded area between cubic and cubic root function
    def __init__(self):
        self.a = rd.choice([-3, -2, -1, 1, 2, 3])
        self.query = "Find the area of the shaded part."
        self.answer = self.a * 1/2
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x = np.linspace(0, 10, 200, endpoint=True)
        rx = np.linspace(0, 1, 200, endpoint=True)
        f1 = self.a * x ** 3
        f2 = self.a * x ** (1 / 3)
        fr1 = self.a * rx ** 3
        fr2 = self.a * rx ** (1 / 3)
        plt.plot(x, f1, color='blue', linewidth=1.5)
        plt.plot(x, f2, color='orange', linewidth=1.5)
        plt.xlim(-5 * 1.1, 5 * 1.1)
        plt.ylim(-5 * 1.1, 5 * 1.1)
        plt.xticks([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        plt.yticks([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.fill_between(rx, fr1, fr2, color='lightgray')
        if self.a == 1:
            plt.title(f"f1 = x^3  f2 = x^1/3", fontsize=14)
        elif self.a == -1:
            plt.title(f"f1 = -x^3  f2 = -x^1/3", fontsize=14)
        else:
            plt.title(f"f1 = {self.a}x^3  f2 = {self.a}x^1/3", fontsize=14)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q120:
    # cycle in the graph
    def __init__(self):
        self.c1 = rd.randint(0, 1)
        self.c2 = rd.randint(0, 1)
        self.c3 = rd.randint(0, 1)
        self.c4 = rd.randint(0, 1)
        self.query = "Is this graph a cyclic graph? choice: (A) Yes (B) No"
        if self.c1 == 0 and self.c2 == 0 and self.c3 == 0 and self.c4 == 0:
            self.answer = "B"
        else:
            self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        circle0 = Circle((0, 0), 1, edgecolor="black", facecolor="white", fill=True)
        circle1 = Circle((-5, 0), 1, edgecolor="black", facecolor="white", fill=False)
        circle2 = Circle((5, 0), 1, edgecolor="black", facecolor="white", fill=False)
        circle3 = Circle((0, 5), 1, edgecolor="black", facecolor="white", fill=False)
        circle4 = Circle((0, -5), 1, edgecolor="black", facecolor="white", fill=False)
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.plot([0, 0], [-4, -1], color='black', linewidth=1.5)
        ax.plot([-4, -1], [0, 0], color='black', linewidth=1.5)
        ax.plot([0, 0], [1, 4], color='black', linewidth=1.5)
        ax.plot([4, 0], [0, -4], color='black', linewidth=1.5)
        if self.c1 == 1:
            ax.plot([4, 0], [0, 4], color='black', linewidth=1.5)
        if self.c2 == 1:
            ax.plot([-4, 0], [0, 4], color='black', linewidth=1.5)
        if self.c3 == 1:
            ax.plot([-4, 0], [0, -4], color='black', linewidth=1.5)
        if self.c4 == 1:
            ax.plot([1, 4], [0, 0], color='black', linewidth=1.5)
        ax.add_patch(circle1)
        ax.add_patch(circle2)
        ax.add_patch(circle3)
        ax.add_patch(circle4)
        ax.add_patch(circle0)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


