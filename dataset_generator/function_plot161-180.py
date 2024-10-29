import math
import shutil
import networkx as nx
import os.path
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from matplotlib.patches import *


class Q161:
    # spinner likely to land
    def __init__(self):
        self.a = rd.randint(0, 9)
        self.b = rd.randint(0, 4)
        self.c = rd.randint(5, 9)
        self.query = "On which number is the spinner more likely to land?"
        self.answer = self.a
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        r = 5
        a = self.a
        b = self.b
        c = self.c
        plt.xlim(-7 * 1.1, 7 * 1.1)
        plt.ylim(-7 * 1.1, 7 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        circle = Circle((0, 0), r, edgecolor="black", facecolor="white", fill=True)
        ax.add_patch(circle)
        plt.hlines(0, -5, r, colors="black")
        plt.vlines(0, -5, 5, colors="black")
        plt.scatter(0, 0, color="black")
        plt.text(-2.5, 2.3, f"{a}", fontsize=20)
        plt.text(1.6, 2.3, f"{a}", fontsize=20)
        plt.text(-2.5, -2.3, f"{b}", fontsize=20)
        plt.text(1.6, -2.3, f"{c}", fontsize=20)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.annotate('', xy=(0, -5), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color='black', linewidth=3))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q162:
    # spinner 2
    def __init__(self):
        self.color = rd.choice(["gray", "pink", "blue", "red", "orange", "yellow", "green"])
        self.query = "On which color is the spinner more likely to land?"
        self.answer = "White"
        self.answer_type = "text"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        r = 5
        color = self.color
        plt.xlim(-7 * 1.1, 7 * 1.1)
        plt.ylim(-7 * 1.1, 7 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        circle = Circle((0, 0), r, edgecolor="black", facecolor="white", fill=True)
        wedge1 = Wedge((0, 0), r, -90, 0, edgecolor="black", facecolor=color, fill=True)
        ax.add_patch(circle)
        ax.add_patch(wedge1)
        plt.hlines(0, -5, r, colors="black")
        plt.vlines(0, -5, 5, colors="black")
        plt.scatter(0, 0, color="black")
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.annotate('', xy=(0, -5), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color='black', linewidth=3))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q163:
    # relationship of monotony 1
    def __init__(self):
        self.a = rd.randint(-4, 4)
        self.b = rd.randint(-4, 4)
        self.c = rd.randint(-4, 4)
        self.d = rd.randint(-4, 4)
        self.query = "The blue and green curves are f(x) and g(x). What is the monotonicity of f(x) + g(x)?  choice: " \
                     "(A) monotone increasing (B) monotone decreasing (C) undefined "
        if self.d > 0 and self.b > 0:
            self.answer = "A"
        elif self.d < 0 and self.b < 0:
            self.answer = "B"
        elif self.d == 0 and self.b > 0:
            self.answer = "A"
        elif self.d == 0 and self.b < 0:
            self.answer = "B"
        elif self.d > 0 and self.b == 0:
            self.answer = "A"
        elif self.d < 0 and self.b == 0:
            self.answer = "B"
        else:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = d * 2 ** x + a
        line = b * x + c
        plt.plot(x, cubic, color='green', linewidth=1.5)
        plt.plot(x, line, color='blue', linewidth=1.5)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q164:
    # relationship of monotony 2
    def __init__(self):
        self.a = rd.randint(-4, 4)
        self.b = rd.randint(-4, 4)
        self.c = rd.randint(-4, 4)
        self.d = rd.randint(-4, 4)
        self.query = "The red and green curves are f(x) and g(x). What is the monotonicity of -f(x)?  choice: " \
                     "(A) monotone increasing (B) monotone decreasing (C) undefined "
        if self.d > 0:
            self.answer = "B"
        elif self.d < 0:
            self.answer = "A"
        else:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = d * 2 ** x + a
        line = b * x + c
        plt.plot(x, cubic, color='red', linewidth=1.5)
        plt.plot(x, line, color='green', linewidth=1.5)
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


class Q165:
    # relationship of monotony 3
    def __init__(self):
        self.a = rd.randint(-4, 4)
        self.b = rd.randint(-4, 4)
        self.c = rd.randint(-4, 4)
        self.d = rd.randint(-4, 4)
        self.query = "The purple and orange curves are f(x) and g(x). What is the monotonicity of 1/f(x)?  choice: " \
                     "(A) monotone increasing (B) monotone decreasing (C) undefined "
        if self.d > 0:
            self.answer = "B"
        elif self.d < 0:
            self.answer = "A"
        else:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = d * 2 ** x + a
        line = b * x + c
        plt.plot(x, cubic, color='purple', linewidth=1.5)
        plt.plot(x, line, color='orange', linewidth=1.5)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q166:
    # relationship of monotony 4
    def __init__(self):
        self.a = rd.randint(-4, 4)
        self.b = rd.randint(-4, 4)
        self.c = rd.randint(-4, 4)
        self.d = rd.randint(-4, 4)
        self.query = "The brown and black curves are f(x) and g(x). What is the monotonicity of f[g(x)]?  choice: " \
                     "(A) monotone increasing (B) monotone decreasing (C) undefined "
        if self.d * self.b > 0:
            self.answer = "A"
        elif self.d * self.b < 0:
            self.answer = "B"
        else:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = d * 2 ** x + a
        line = b * x + c
        plt.plot(x, cubic, color='brown', linewidth=1.5)
        plt.plot(x, line, color='black', linewidth=1.5)
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


class Q167:
    # easy geometry proof in square
    def __init__(self):
        self.side = rd.randint(3, 20)
        self.CE = self.side - rd.randint(1, 2)
        self.query = f"quadrilateral ABCD is a square, with DE parallel to AC, AE=AC, and AE intersects CD at point " \
                     f"F. The length of the side of ABCD is {self.side} amd CE = {self.CE}. Find the length of CF. "
        self.answer = self.CE
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q167temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q167temp.png"), dest_image_path)


class Q168:
    # odd even of f(x) + g(x)
    def __init__(self):
        self.a = rd.choice([-3, -1/3, -2, -1/2, -1, 1, 2, 1/2, 3, 1/3])
        self.b = rd.choice([-3, -1/3, -2, -1/2, -1, 1, 2, 1/2, 3, 1/3])
        self.c = rd.randint(-1, 4)
        self.d = rd.randint(-1, 4)
        self.query = "The blue and green curves are f(x) and g(x). Is f(x) + g(x) even or odd?  choice: " \
                     "(A) odd (B) even (C) neither "
        if self.d % 2 == 0 and self.c % 2 == 0 and (self.d != 0 and self.c != 0):
            self.answer = "B"
        elif self.d % 2 != 0 and self.c % 2 != 0:
            self.answer = "A"
        elif self.d == 0 and self.c == 0:
            self.answer = "B"
        else:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = a * x ** c
        line = b * x ** d
        plt.plot(x, cubic, color='green', linewidth=1.5)
        plt.plot(x, line, color='blue', linewidth=1.5)
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


class Q169:
    # odd even of f(x)g(x)
    def __init__(self):
        self.a = rd.choice([-3, -1/3, -2, -1/2, -1, 1, 2, 1/2, 3, 1/3])
        self.b = rd.choice([-3, -1/3, -2, -1/2, -1, 1, 2, 1/2, 3, 1/3])
        self.c = rd.randint(-1, 4)
        self.d = rd.randint(-1, 4)
        self.query = "The purple and orange curves are f(x) and g(x). Is f(x)g(x) even or odd?  choice: " \
                     "(A) odd (B) even (C) neither "
        if self.d % 2 == 0 and self.c % 2 == 0:
            self.answer = "B"
        elif self.d % 2 != 0 and self.c % 2 != 0:
            self.answer = "B"
        else:
            self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = a * x ** c
        line = b * x ** d
        plt.plot(x, cubic, color='purple', linewidth=1.5)
        plt.plot(x, line, color='orange', linewidth=1.5)
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


class Q170:
    # odd even of f[g(x)]
    def __init__(self):
        self.a = rd.choice([-3, -1 / 3, -2, -1 / 2, -1, 1, 2, 1 / 2, 3, 1 / 3])
        self.b = rd.choice([-3, -1 / 3, -2, -1 / 2, -1, 1, 2, 1 / 2, 3, 1 / 3])
        self.c = rd.choice([-1, 1, 2, 3, 4])
        self.d = rd.choice([-1, 1, 2, 3, 4])
        self.query = "The red and green curves are f(x) and g(x). Is f[g(x)] even or odd?  choice: " \
                     "(A) odd (B) even (C) neither "
        if self.d % 2 == 0 and self.c % 2 == 0:
            self.answer = "B"
        elif self.d % 2 != 0 and self.c % 2 != 0:
            self.answer = "A"
        else:
            self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = a * x ** c
        line = b * x ** d
        plt.plot(x, cubic, color='red', linewidth=2.5)
        plt.plot(x, line, color='green', linewidth=2.5)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
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


class Q171:
    # angle in polygon
    def __init__(self):
        self.side = rd.randint(3, 10)
        self.query = "What is the sum of interior angles in this polygon?"
        self.answer = (self.side - 2) * 180
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
        polygon = CirclePolygon(xy=(0, 0), radius=2, resolution=self.side, facecolor="azure", edgecolor="black")
        ax.add_patch(polygon)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q172:
    # angle out polygon
    def __init__(self):
        self.side = rd.randint(3, 10)
        self.query = "What is the sum of external angles in this polygon?"
        self.answer = 360
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
        polygon = CirclePolygon(xy=(0, 0), radius=2, resolution=self.side, facecolor="lightgreen", edgecolor="black")
        ax.add_patch(polygon)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q173:
    # find the angle A
    def __init__(self):
        self.side = rd.randint(3, 10)
        self.query = "Find the ∠A in this regular polygon."
        self.answer = (self.side - 2) * 180 / self.side
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        m = self.side
        n = (m - 2) * 180 / m
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        polygon = CirclePolygon(xy=(0, 0), radius=2, resolution=m, facecolor="white", edgecolor="black")
        angle = Wedge((0, 2), 0.3, 270 - n / 2, 270 + n / 2, fill=False, edgecolor='black')
        ax.add_patch(polygon)
        ax.add_patch(angle)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(-0.1, 2.2, "A", fontsize=14)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q174:
    # shaded area of two square
    def __init__(self):
        self.side = rd.randint(1, 9)
        self.query = "In the diagram below, both squares have a equal side length. What is the area of the azure " \
                     "region? "
        self.answer = self.side * self.side
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        square = plt.Polygon([(2, 2), (-2, 2), (-2, -2), (2, -2)], closed=True, fill=True, edgecolor='black',
                             facecolor='white')
        square2 = plt.Polygon([(2, -2), (2, 2), (6, 2), (6, -2)], closed=True, fill=True, edgecolor='black',
                              facecolor='azure')
        wedge = Wedge((-2, -2), 4, 0, 90, facecolor="azure", edgecolor="black")
        circle = Wedge((2, -2), 4, 0, 90, edgecolor="black", facecolor="white", fill=True)
        ax.add_patch(square)
        ax.add_patch(square2)
        ax.add_patch(wedge)
        ax.add_patch(circle)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(3.8, -3, f"{self.side}", fontsize=14)
        plt.text(-2.8, 0, f"{self.side}", fontsize=14)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q175:
    # ellipse 1
    def __init__(self):
        self.a2 = rd.randint(4, 10)
        self.b2 = rd.randint(2, 10)
        self.query = f"The equation of this ellipse is x^2/{(self.a2/2) * (self.a2/2)} + " \
                     f"y^2/{(self.b2/2) * (self.b2/2)} = 1. Find the length of A1A2. "
        self.answer = self.a2
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a2 = self.a2
        b2 = self.b2
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        ellipse = Ellipse((0, 0), a2, b2, color="black", fill=False, linewidth=2)
        ax.add_patch(ellipse)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(a2 / 2 + 0.4, 0, "A1", fontsize=12)
        plt.scatter(a2 / 2, 0, color='blue', s=12)
        plt.text(-a2 / 2 - 1.2, 0, "A2", fontsize=12)
        plt.scatter(-a2 / 2, 0, color='blue', s=12)
        plt.text(0, b2 / 2 + 0.4, "B1", fontsize=12)
        plt.scatter(0, b2 / 2, color='blue', s=12)
        plt.text(0, -b2 / 2 - 1.2, "B2", fontsize=12)
        plt.scatter(0, -b2 / 2, color='blue', s=12)
        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.tick_params(axis='both', which='major', labelsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q176:
    # ellipse 2
    def __init__(self):
        self.a2 = rd.randint(4, 10)
        self.b2 = rd.randint(2, 10)
        self.query = f"The equation of this ellipse is x^2/{(self.a2 / 2) * (self.a2 / 2)} + " \
                     f"y^2/{(self.b2 / 2) * (self.b2 / 2)} = 1. Find the length of B1B2. "
        self.answer = self.b2
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a2 = self.a2
        b2 = self.b2
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        ellipse = Ellipse((0, 0), a2, b2, color="black", fill=False, linewidth=2)
        ax.add_patch(ellipse)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(a2 / 2 + 0.4, 0, "A1", fontsize=12)
        plt.scatter(a2 / 2, 0, color='blue', s=12)
        plt.text(-a2 / 2 - 1.2, 0, "A2", fontsize=12)
        plt.scatter(-a2 / 2, 0, color='blue', s=12)
        plt.text(0, b2 / 2 + 0.4, "B1", fontsize=12)
        plt.scatter(0, b2 / 2, color='blue', s=12)
        plt.text(0, -b2 / 2 - 1.2, "B2", fontsize=12)
        plt.scatter(0, -b2 / 2, color='blue', s=12)
        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.tick_params(axis='both', which='major', labelsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q177:
    # ellipse 3
    def __init__(self):
        self.a2 = rd.randint(4, 10)
        self.b2 = rd.randint(2, 10)
        self.c = np.sqrt(abs((self.a2 / 2) * (self.a2 / 2) - (self.b2 / 2) * (self.b2 / 2)))
        self.query = f"The equation of this ellipse is x^2/{(self.a2 / 2) * (self.a2 / 2)} + " \
                     f"y^2/{(self.b2 / 2) * (self.b2 / 2)} = 1. Find the eccentricity of this ellipse. "
        self.answer = self.c / max(self.a2/2, self.b2/2)
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a2 = self.a2
        b2 = self.b2
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        ellipse = Ellipse((0, 0), a2, b2, color="black", fill=False, linewidth=2)
        ax.add_patch(ellipse)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(a2 / 2 + 0.4, 0, "A1", fontsize=12)
        plt.scatter(a2 / 2, 0, color='blue', s=12)
        plt.text(-a2 / 2 - 1.2, 0, "A2", fontsize=12)
        plt.scatter(-a2 / 2, 0, color='blue', s=12)
        plt.text(0, b2 / 2 + 0.4, "B1", fontsize=12)
        plt.scatter(0, b2 / 2, color='blue', s=12)
        plt.text(0, -b2 / 2 - 1.2, "B2", fontsize=12)
        plt.scatter(0, -b2 / 2, color='blue', s=12)
        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.tick_params(axis='both', which='major', labelsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q178:
    # area of similar triangle
    def __init__(self):
        self.anp = rd.randint(1, 10)
        self.query = f"In the diagram, triangle ABC is right-angled at C. Also, points M, N and P are the midpoints " \
                     f"of sides BC, AC and AB, respectively. If the area of triangle APN is {self.anp}, then what is the area " \
                     f"of triangle ABC? "
        self.answer = 4 * self.anp
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q178temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q178temp.png"), dest_image_path)


class Q179:
    # find the missing number
    def __init__(self):
        self.fbnc = list(range(1, 9))
        self.fbnc[0] = rd.randint(1, 10)
        for i in range(1, 8):
            self.fbnc[i] = self.fbnc[i - 1] + i
        self.fbnc.append("?")
        self.query = "Find the missing number in the last node."
        self.answer = self.fbnc[7] + 8
        self.answer_type = "float"
        self.subject = "puzzle test"
        self.level = "high school"

    def draw(self, num):
        fbnc = self.fbnc
        G = nx.Graph()
        plt.figure(figsize=(6, 6))

        G.add_nodes_from(fbnc)
        pos = {
            fbnc[0]: (0.5, 1.5),
            fbnc[1]: (1, 1.5),
            fbnc[2]: (1.5, 1.5),
            fbnc[3]: (0.5, 1),
            fbnc[4]: (1, 1),
            fbnc[5]: (1.5, 1),
            fbnc[6]: (0.5, 0.5),
            fbnc[7]: (1, 0.5),
            '?': (1.5, 0.5)

        }
        nx.draw(G, with_labels=True, pos=pos, node_color="white", edgecolors="black", node_size=1500)

        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q180:
    # find the missing number
    def __init__(self):
        self.fbnc = list(range(1, 9))
        self.fbnc[0] = rd.randint(1, 10)
        for i in range(1, 8):
            self.fbnc[i] = self.fbnc[i - 1] + i
        self.fbnc.append("?")
        self.query = "Find the missing number in the last node."
        self.answer = self.fbnc[7] + 8
        self.answer_type = "float"
        self.subject = "puzzle test"
        self.level = "high school"

    def draw(self, num):
        fbnc = self.fbnc
        G = nx.Graph()
        plt.figure(figsize=(6, 6))

        G.add_nodes_from(fbnc)
        pos = {
            fbnc[0]: (0.5, 1.5),
            fbnc[1]: (1, 1.5),
            fbnc[2]: (1.5, 1.5),
            fbnc[3]: (0.5, 1),
            fbnc[4]: (1, 1),
            fbnc[5]: (1.5, 1),
            fbnc[6]: (0.5, 0.5),
            fbnc[7]: (1, 0.5),
            '?': (1.5, 0.5)

        }
        G.add_edges_from(
            [[fbnc[0], fbnc[1]], [fbnc[1], fbnc[2]], [fbnc[2], fbnc[3]], [fbnc[3], fbnc[4]], [fbnc[4], fbnc[5]],
             [fbnc[5], fbnc[6]], [fbnc[6], fbnc[7]], [fbnc[7], fbnc[8]]])
        nx.draw(G, with_labels=True, pos=pos, node_color="white", edgecolors="black", node_size=1500, arrows=True,
                arrowstyle="->")

        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


