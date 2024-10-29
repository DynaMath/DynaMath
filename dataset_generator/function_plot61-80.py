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


class Q61:
    # find the local min or max in parabola
    def __init__(self):
        self.a = rd.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        self.b = rd.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        self.c = rd.choice([-3, -2, -1, 1, 2, 3])
        self.query = "Where is the local min or max of the parabola shown in image at?"
        self.answer = -self.b / (2 * self.a)
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = self.a * x ** 2 + self.b * x + self.c
        plt.plot(x, cubic, color='blue', linewidth=1.5)

        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q62:
    # find area of trapezoid
    def __init__(self):
        self.ad = rd.randint(1, 5)
        self.ab = rd.randint(1, 5) + rd.randint(0, 2)
        self.dc = self.ab + rd.randint(2, 4)
        self.query = f"If AD = {self.ad}, AB = {self.ab}, DC = {self.dc}, what is the area of trapezoid ABCD?"
        self.answer = 1 / 2 * self.ad * (self.ab + self.dc)
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "elementary school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q62temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q62temp.png"), dest_image_path)


class Q63:
    # find value of function through table
    def __init__(self):
        self.a = rd.randint(-10, 10)
        self.b = rd.randint(-10, 10)
        self.c = rd.randint(-10, 10)
        self.eq1 = self.c
        self.eq2 = self.a + self.b + self.c
        self.eq3 = 4 * self.a + 2 * self.b + self.c
        self.query = "The function f(x) is quadratic function. What is the value of f(x) when x = 3?"
        self.answer = 9 * self.a + 3 * self.b + self.c
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        data = {
            'x': [0, 1, 2, 3],
            'f(x)': [self.eq1, self.eq2, self.eq3, '?']
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


class Q64:
    # area enclosed by parabola and x-axis
    def __init__(self):
        self.constant_a = rd.randint(1, 5)
        self.constant_b = rd.randint(1, 5)
        self.query = "What is the area enclosed by parabola and x-axis?"
        self.answer = -1 / 3 * self.constant_b * self.constant_b * self.constant_b + (
                self.constant_b - self.constant_a) / 2 \
                      * self.constant_b * self.constant_b + self.constant_a * self.constant_b * self.constant_b - 1 / 3 \
                      * self.constant_a * self.constant_a * self.constant_a - (
                              self.constant_b - self.constant_a) / 2 * self.constant_a * self.constant_a + \
                      self.constant_a * self.constant_b * self.constant_a
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = -(x + self.constant_a) * (x - self.constant_b)
        rx = np.linspace(-self.constant_a, self.constant_b, 200, endpoint=True)
        ry = -(rx + self.constant_a) * (rx - self.constant_b)
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
        ax.plot(x, cubic, color='blue', linewidth=1.5)
        plt.fill(rx, ry, color='lightgray')
        plt.title(f'y = -(x + {self.constant_a})*(x - {self.constant_b})', fontsize=16)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q65:
    # rectangle area 2
    def __init__(self):
        self.factor = rd.randint(1, 9)
        self.x = self.factor + rd.randint(2, 4)
        self.area = (self.x + self.factor) * (self.x - self.factor)
        self.query = f"If the area of the rectangle above is {self.area}, what is the value of x?"
        self.answer = self.x
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        square = plt.Polygon([(1, 1), (1, 3), (4, 3), (4, 1)], closed=True, fill=True, edgecolor='black',
                             facecolor='lightgreen')
        fig, ax = plt.subplots()
        fig.set_size_inches(6, 4)
        ax.add_patch(square)
        ax.set_xlim(0, 5)
        ax.set_ylim(0, 4)
        plt.text(0.3, 2, f'x - {self.factor}', fontsize=18)
        plt.text(2.2, 0.5, f'x + {self.factor}', fontsize=18)
        plt.xticks([])
        plt.yticks([])
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q66:
    # rectangle perimeter 2
    def __init__(self):
        self.factor = rd.randint(1, 9)
        self.x = self.factor + rd.randint(2, 4)
        self.peri = 2 * (self.x + self.factor) + 2 * (self.x - self.factor)
        self.query = f"If the perimeter of the rectangle above is {self.peri}, what is the value of x?"
        self.answer = self.x
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        square = plt.Polygon([(1, 1), (1, 3), (4, 3), (4, 1)], closed=True, fill=True, edgecolor='black',
                             facecolor='purple')
        fig, ax = plt.subplots()
        fig.set_size_inches(6, 4)
        ax.add_patch(square)
        ax.set_xlim(0, 5)
        ax.set_ylim(0, 4)
        plt.text(0.3, 2, f'x - {self.factor}', fontsize=18)
        plt.text(2.2, 0.5, f'x + {self.factor}', fontsize=18)
        plt.xticks([])
        plt.yticks([])
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q67:
    # area of square in circle
    def __init__(self):
        self.area = rd.randint(10, 30)
        self.query = f"If the area of the circle is {self.area}pi, what is the area of the square in circle?"
        self.answer = self.area * 2
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q67temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q67temp.png"), dest_image_path)


class Q68:
    # color of curve 1
    def __init__(self):
        self.query = "What is the green curve? choice: (A) a parabola (B) a line (C) a logarithmic function (D) a " \
                     "trigonometric function "
        self.choice = ["green", "purple", "orange", "blue"]
        self.a = rd.randint(-4, 4)
        self.sin_color = rd.choice(self.choice)
        self.choice.remove(self.sin_color)
        self.ln_color = rd.choice(self.choice)
        self.choice.remove(self.ln_color)
        self.line_color = rd.choice(self.choice)
        self.choice.remove(self.line_color)
        self.square_color = rd.choice(self.choice)
        if self.square_color == "green":
            self.answer = "A"
        elif self.line_color == "green":
            self.answer = "B"
        elif self.ln_color == "green":
            self.answer = "C"
        else:
            self.answer = "D"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        x = np.linspace(-10, 10, 1000, endpoint=True)
        line = x + a
        square = x ** 2 + a
        sin = np.sin(x)
        ln = np.log(x)
        plt.plot(x, line, color=self.line_color, linewidth=1.5)
        plt.plot(x, ln, color=self.ln_color, linewidth=1.5)
        plt.plot(x, sin, color=self.sin_color, linewidth=1.5)
        plt.plot(x, square, color=self.square_color, linewidth=1.5)

        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q69:
    # convex concave 1
    def __init__(self):
        self.a = rd.randint(-3, 3)
        self.b = rd.randint(-3, 3)
        self.c = rd.randint(-3, 3)
        self.query = "Is the function convex or concave? choice: (A) convex (B) concave (C) both"
        if self.a > 0:
            self.answer = "A"
        elif self.a < 0:
            self.answer = "B"
        else:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200, endpoint=True)
        square = self.a * x ** 2 + self.b * x + self.c
        plt.plot(x, square, color='brown', linewidth=1.5)
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

        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q70:
    # Heron's formula
    def __init__(self):
        self.a = rd.randint(1, 10)
        self.b = self.a + rd.randint(2, 5)
        self.c = self.b + rd.randint(0, self.a-1)
        self.p = 1/2 * (self.a + self.b + self.c)
        self.query = "What is the area of this triangle? Please using Heron's formula to solve this problem"
        self.answer = np.sqrt(self.p*(self.p - self.a)*(self.p - self.b)*(self.p - self.c))
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        triangle = plt.Polygon([(1, 1), (4, 1), (2, 2)], closed=True, fill=True, edgecolor='black', facecolor='azure')
        fig, ax = plt.subplots()
        fig.set_size_inches(4, 4)
        ax.add_patch(triangle)
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        plt.text(1, 1.7, f'{self.a}ft', fontsize=12)
        plt.text(2.75, 1.8, f'{self.b}ft', fontsize=12)
        plt.text(2, 0.5, f'{self.c}ft', fontsize=12)
        plt.xticks([])
        plt.yticks([])
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q71:
    # length in ruler 1
    def __init__(self):
        self.f = rd.randint(1, 8)
        self.end = 60 + self.f * 38
        self.query = "Move the ruler to measure the length of the line to the nearest centimeter. The line is about (" \
                     "_) centimeters long. "
        self.answer = self.f
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def draw(self, num):
        img = Image.open('temp_image/Q71temp.png')
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.hlines(50, 60, self.end, colors="black", linewidth=3)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q72:
    # easy markov chain 1
    def __init__(self):
        self.a = rd.choice([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
        self.self_a = round(1.0 - self.a, 1)
        self.b = rd.choice([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
        self.self_b = round(1.0 - self.b, 1)
        self.query = "According to the markov chain shown in the image, what is the probability of the event 'A to B'?"
        self.answer = self.a
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.xlim(-7 * 1.1, 7 * 1.1)
        plt.ylim(-7 * 1.1, 7 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(7, 7)
        circle = Circle((0, 0), 2, color="black", fill=False, linewidth=2)
        circle2 = Circle((-3, 1), 1.5, fill=True, linewidth=2, edgecolor="lightblue", facecolor="azure")
        circle3 = Circle((3, -1), 1.5, fill=True, linewidth=2, edgecolor="red", facecolor="pink")
        circle4 = Circle((-4.5, 1.7), 1, color="black", fill=False, linewidth=2)
        circle5 = Circle((4.5, -1.7), 1, color="black", fill=False, linewidth=2)
        ax.add_patch(circle)
        ax.add_patch(circle4)
        ax.add_patch(circle5)
        ax.add_patch(circle2)
        ax.add_patch(circle3)
        plt.text(0, 1.9, r'$\blacktriangleright$')
        plt.text(-5.65, 1.7, r'$\blacktriangleright$', rotation=90)
        plt.text(5.3, -1.7, r'$\blacktriangleleft$', rotation=90)
        plt.text(0, -2.1, r'$\blacktriangleleft$')
        plt.text(-3.2, 1, "A", fontsize=14)
        plt.text(2.8, -1.1, "B", fontsize=14)
        plt.text(0, 2.3, str(self.a), fontsize=12)
        plt.text(-0.1, -2.7, str(self.b), fontsize=12)
        plt.text(-6.5, 1.7, str(self.self_a), fontsize=12)
        plt.text(5.8, -1.7, str(self.self_b), fontsize=12)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q73:
    # find asymptote 2
    def __init__(self):
        self.a = rd.randint(-4, 4)
        self.query = "What is the vertical asymptote of the function shown in image?"
        self.answer = f"x = {self.a}"
        self.answer_type = "text"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = (x - self.a) ** (-2)
        plt.plot(x, cubic, color='green', linewidth=1.5)

        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q74:
    # find the perimeter of the rectangular prism
    def __init__(self):
        self.a = rd.randint(3, 8)
        self.b = self.a + rd.randint(1, 3)
        self.c = self.b + rd.randint(1, 2)
        self.query = "Find the perimeter of the rectangular prism."
        self.answer = self.a * 4 + self.b * 4 + self.c * 4
        self.answer_type = "float"
        self.subject = "solid geometry"
        self.level = "high school"

    def draw(self, num):
        fig = plt.figure()
        fig.set_size_inches(4, 4, 4)
        x, y, z = np.indices((2, 2, 2))
        filled = np.ones((1, 1, 1))
        ax = fig.add_subplot(projection='3d')
        ax.voxels(x, y, z, filled=filled, color='pink', edgecolor='black')
        ax.text(0.3, 0, -0.3, f"{self.c}ft", fontsize=12)
        ax.text(0, -0.3, 0.7, f"{self.a}ft", fontsize=12)
        ax.text(-0.4, 0.8, 0.8, f"{self.b}ft", fontsize=12)
        ax.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q75:
    # parallel of lines 1
    def __init__(self):
        self.a = rd.randint(-4, 4)
        self.b = rd.randint(-4, 4)
        self.c = rd.randint(-2, 2)
        self.d = rd.choice([-4, -3, 3, 4])
        self.query = "Are the red line and the blue line parallel? choice: (A) Yes (B) No"
        if self.a == self.b:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        func1 = self.a * x + self.c
        func2 = self.b * x + self.d
        plt.plot(x, func1, color='red', linewidth=1.5)
        plt.plot(x, func2, color='Blue', linewidth=1.5)
        plt.xlim(-10 * 1.1, 10 * 1.1)
        plt.ylim(-10 * 1.1, 10 * 1.1)

        plt.xticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        plt.yticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q76:
    # circumcircle of triangle 1
    def __init__(self):
        self.AB = rd.choice([2, 4, 6, 8, 10, 12, 14, 16])
        self.BC = self.AB / 2
        self.query = f"O is the circumcircle of △ABC, with AB=BC={self.AB}. The arc AB is folded down along the chord AB to " \
                     "intersect BC at point D. If point D is the midpoint of BC, What is the length of AC?"
        self.answer = np.sqrt(self.AB * self.BC)
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q76temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q76temp.png"), dest_image_path)


class Q77:
    # integral of sin
    def __init__(self):
        self.b = rd.choice([-3, -2, -1, 1, 2, 3])
        self.query = "Find the area of shaded sectors."
        self.answer = 2 * abs(self.b * 2)
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200, endpoint=True)
        rx = np.linspace(-np.pi, np.pi, 200, endpoint=True)
        sin = self.b * np.sin(x)
        rsin = self.b * np.sin(rx)
        plt.plot(x, sin, color='blue', lw=2.5)
        plt.xlim(-2 * np.pi * 1.1, 2 * np.pi * 1.1)
        plt.ylim(sin.min() * 1.1, sin.max() * 1.1)
        plt.xticks(
            [-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
            [r'-$2\pi$', r'-$3\pi/2$', r'-$\pi$', r'-$\pi/2$', r'$\pi/2$', r'$\pi$', r'-$3\pi/2$', r'$2\pi$']
        )
        plt.yticks([-3, -2, -1, 1, 2, 3])
        plt.tick_params(axis='both', which='major', labelsize=12)
        plt.fill(rx, rsin, color='lightgray')
        plt.title(f'f(x) = {self.b}sin(x)')
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))

        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q78:
    # differentiable 1
    def __init__(self):
        self.a = rd.randint(-3, 3)
        self.query = "Is the function differentiable at x = 0? choice: (A) Yes (B) No"
        if self.a == 0:
            self.answer = "B"
        else:
            self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        absolute = abs(x - self.a)
        plt.plot(x, absolute, color='blue', linewidth=2.5)

        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q79:
    # continuous 2
    def __init__(self):
        self.a = rd.randint(-3, 3)
        self.query = "Is the function continuous at x = 0? choice: (A) Yes (B) No"
        self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        absolute = abs(x - self.a)
        plt.plot(x, absolute, color='orange', linewidth=1.5)

        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q80:
    # Pythagoras theorem 1
    def __init__(self):
        self.side = rd.randint(1, 10)
        self.query = f"The side of the square is {self.side} ft. Find the length of diagonal AB"
        self.answer = self.side * np.sqrt(2)
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        square = plt.Polygon([(1, 1), (1, 3), (3, 3), (3, 1)], closed=True, fill=True, edgecolor='black',
                             facecolor='white')
        fig, ax = plt.subplots()
        fig.set_size_inches(4, 4)
        ax.add_patch(square)
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        plt.text(0.5, 2, f'{self.side}ft', fontsize=12)
        plt.text(2, 0.5, f'{self.side}ft', fontsize=12)
        plt.plot([1, 3], [3, 1], color='black', linewidth=1.5)
        plt.scatter(1, 3, color='black')
        plt.scatter(3, 1, color='black')
        plt.text(0.8, 3.2, "A", fontsize=14)
        plt.text(3.2, 0.8, "B", fontsize=14)
        plt.xticks([])
        plt.yticks([])
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()

