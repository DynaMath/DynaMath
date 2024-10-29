import math
import shutil
import os.path
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from PIL import Image, ImageDraw, ImageFont
from matplotlib.patches import *


class Q181:
    # parallel 1
    def __init__(self):
        self.c = rd.randint(1, 100) / 10
        self.query = "The line L1 and L2 are parallel to each other. Is ∠A the same as ∠B?  choice: (A) Yes (B) No"
        self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        a = 2
        b = -2
        c = self.c
        x = np.linspace(-10, 10, 200, endpoint=True)
        upper = a + 0 * x
        lower = b + 0 * x
        line = c * x
        angle = np.arctan(c)
        Wedge1 = Wedge((2 / c, 2), 0.4, 180, 180 + angle / (2 * np.pi) * 360, fill=False, edgecolor="black")
        Wedge2 = Wedge((-2 / c, -2), 0.4, 0, angle / (2 * np.pi) * 360, fill=False, edgecolor="black")
        plt.plot(x, upper, color='black', linewidth=1.5)
        plt.plot(x, lower, color='black', linewidth=1.5)
        plt.plot(x, line, color='black', linewidth=1.5)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.add_patch(Wedge1)
        ax.add_patch(Wedge2)
        plt.text(2 / c - 0.7, 1.5, "A", fontsize=12)
        plt.text(-2 / c + 0.5, -1.8, "B", fontsize=12)
        plt.text(6, 2.2, "L1", fontsize=12)
        plt.text(6, -1.8, "L2", fontsize=12)
        plt.grid()
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q182:
    # parallel 2
    def __init__(self):
        self.c = rd.randint(-100, 1) / 10
        self.query = "The line L1 and L2 are parallel to each other. Is ∠A the same as ∠B?  choice: (A) Yes (B) No"
        self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        a = 2
        b = -2
        c = self.c
        x = np.linspace(-10, 10, 200, endpoint=True)
        upper = a + 0 * x
        lower = b + 0 * x
        line = c * x
        angle = np.arctan(c)
        Wedge1 = Wedge((2 / c, 2), 0.4, 180, 360 + angle / (2 * np.pi) * 360, fill=False, edgecolor="black")
        Wedge2 = Wedge((-2 / c, -2), 0.4, 0, 180 + angle / (2 * np.pi) * 360, fill=False, edgecolor="black")
        plt.plot(x, upper, color='black', linewidth=1.5)
        plt.plot(x, lower, color='black', linewidth=1.5)
        plt.plot(x, line, color='black', linewidth=1.5)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.add_patch(Wedge1)
        ax.add_patch(Wedge2)
        plt.text(2 / c - 0.7, 1.5, "A", fontsize=12)
        plt.text(-2 / c + 0.5, -1.8, "B", fontsize=12)
        plt.text(6, 2.2, "L1", fontsize=12)
        plt.text(6, -1.8, "L2", fontsize=12)
        plt.grid()
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q183:
    # parallel 3
    def __init__(self):
        self.c = rd.randint(-100, 1) / 10
        while self.c == 0:
            self.c = rd.randint(-100, 1) / 10
        self.query = "The line L1 and L2 are parallel to each other. Is ∠A the same as ∠B?  choice: (A) Yes (B) No"
        self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        a = 2
        b = -2
        c = self.c
        x = np.linspace(-10, 10, 200, endpoint=True)
        upper = a + 0 * x
        lower = b + 0 * x
        line = c * x
        angle = np.arctan(c)
        Wedge1 = Wedge((2 / c, 2), 0.4, 0, 180 + angle / (2 * np.pi) * 360, fill=False, edgecolor="black")
        Wedge2 = Wedge((-2 / c, -2), 0.4, 0, 180 + angle / (2 * np.pi) * 360, fill=False, edgecolor="black")
        plt.plot(x, upper, color='black', linewidth=1.5)
        plt.plot(x, lower, color='black', linewidth=1.5)
        plt.plot(x, line, color='black', linewidth=1.5)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.add_patch(Wedge1)
        ax.add_patch(Wedge2)
        plt.text(2 / c + 0.4, 2.2, "A", fontsize=12)
        plt.text(-2 / c + 0.5, -1.8, "B", fontsize=12)
        plt.text(6, 2.2, "L1", fontsize=12)
        plt.text(6, -1.8, "L2", fontsize=12)
        plt.grid()
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q184:
    # parallel 4
    def __init__(self):
        self.c = rd.randint(1, 100) / 10
        self.query = "The line L1 and L2 are parallel to each other. Is ∠A the same as ∠B?  choice: (A) Yes (B) No"
        self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        a = 2
        b = -2
        c = self.c
        x = np.linspace(-10, 10, 200, endpoint=True)
        upper = a + 0 * x
        lower = b + 0 * x
        line = c * x
        angle = np.arctan(c)
        Wedge1 = Wedge((2 / c, 2), 0.4, 0, angle / (2 * np.pi) * 360, fill=False, edgecolor="black")
        Wedge2 = Wedge((-2 / c, -2), 0.4, 0, angle / (2 * np.pi) * 360, fill=False, edgecolor="black")
        plt.plot(x, upper, color='black', linewidth=1.5)
        plt.plot(x, lower, color='black', linewidth=1.5)
        plt.plot(x, line, color='black', linewidth=1.5)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.add_patch(Wedge1)
        ax.add_patch(Wedge2)
        plt.text(2 / c + 0.7, 2.2, "A", fontsize=12)
        plt.text(-2 / c + 0.7, -1.8, "B", fontsize=12)
        plt.text(6, 2.2, "L1", fontsize=12)
        plt.text(6, -1.8, "L2", fontsize=12)
        plt.grid()
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q185:
    # protractor 1
    def __init__(self):
        self.angle = rd.randint(1, 18) * 10
        self.query = "Based on the measurement results shown in the diagram, this blue angle is ( )°."
        self.answer = self.angle
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "elementary school"

    def draw(self, num):
        Img = Image.open('temp_image/Q185temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        plt.plot([510, 840], [505, 505], color='blue', linewidth=2)
        plt.plot([510, 330 * np.cos(self.angle / 360 * 2 * np.pi) + 510],
                 [505, 505 - 330 * np.sin(self.angle / 360 * 2 * np.pi)], color='blue', linewidth=2)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q186:
    # protractor 2
    def __init__(self):
        self.angle = rd.randint(1, 17) * 10
        self.query = "Based on the measurement results shown in the diagram, this blue angle is ( )°."
        self.answer = 180 - self.angle
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "elementary school"

    def draw(self, num):
        Img = Image.open('temp_image/Q185temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        plt.plot([180, 510], [505, 505], color='blue', linewidth=2)
        plt.plot([510, 330 * np.cos(self.angle / 360 * 2 * np.pi) + 510],
                 [505, 505 - 330 * np.sin(self.angle / 360 * 2 * np.pi)],
                 color='blue', linewidth=2)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q187:
    # sphere in the cone
    def __init__(self):
        self.radius = rd.randint(1, 10)
        self.h = self.radius + rd.randint(1, 3)
        self.l = np.sqrt(self.radius * self.radius + self.h * self.h)
        self.R = self.radius * self.h / (self.l + self.radius)
        self.query = f"A sphere is inscribed in a cone with height {self.h} and base radius {self.radius}. What is " \
                     f"the volume of the sphere ? "
        self.answer = 4 / 3 * np.pi * self.R * self.R * self.R
        self.answer_type = "float"
        self.subject = "solid geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q187temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q187temp.png"), dest_image_path)


class Q188:
    # plane parallel
    def __init__(self):
        self.exp = rd.randint(0, 2)
        self.query = "Are two planes parallel? choice: (A) Yes (B) No"
        if self.exp == 0:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "solid geometry"
        self.level = "high school"

    def draw(self, num):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x = np.linspace(0, 9, 9)
        y = np.linspace(0, 9, 9)
        X, Y = np.meshgrid(x, y)
        ax.plot_surface(X, Y, Z=X * 0 + 4.5, color='g', alpha=0.6)
        ax.plot_surface(X, Y, Z=(X / 2) ** self.exp + 2, color='b', alpha=0.6)
        ax.set(xlabel='X',
               ylabel='Y',
               zlabel='Z',
               xlim=(0, 9),
               ylim=(0, 9),
               zlim=(0, 9),
               )
        ax.view_init(20)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q189:
    # part of parallelogram area
    def __init__(self):
        self.short = rd.randint(5, 13)
        self.long = self.short * 2 + rd.randint(1, 3)
        self.part = rd.randint(3, 4)
        self.diff = self.long - self.part
        self.query = "What is the area of the azure part?"
        self.answer = (self.long + self.part) * np.sqrt(self.short * self.short - self.part * self.part) / 2
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
        square = plt.Polygon([(-3, -1), (-2, 1), (2, 1), (1, -1)], closed=True, fill=True, edgecolor='black',
                             facecolor="azure")
        ax.add_patch(square)
        plt.vlines(-2, -1, 1, colors="black")
        square2 = plt.Polygon([(-2, -1), (-2.2, -1), (-2.2, -0.8), (-2, -0.8)], closed=True, fill=False,
                              edgecolor='black')
        tri = plt.Polygon([(-3, -1), (-2, 1), (-2, -1)], closed=True, fill=True, facecolor='white', edgecolor='black')
        ax.add_patch(tri)
        ax.add_patch(square2)
        plt.text(-3.5, 0.2, f"{self.short}ft", fontsize=12)
        plt.text(-2.8, -1.4, f"{self.part}ft", fontsize=12)
        plt.text(0, 1.2, f"{self.long}ft", fontsize=12)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q190:
    # find the shaded part area of circle
    def __init__(self):
        self.a = rd.randint(2, 12)
        self.query = "In the diagram, there are two semi-circles. D is the diameter of left azure semi-circle, " \
                     "and d is the diameter of the right white semi-circle. Find the area of azure part. "
        self.answer = 49 * np.pi / 2 - 1 / 2 * (self.a / 2) * (self.a / 2) * np.pi + 1 / 2 * ((14 - self.a) / 2) * (
                    (14 - self.a) / 2) * np.pi
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        random_a = self.a
        b = 14 - random_a
        c1 = 7 - random_a / 2
        c2 = (7 - random_a + (-7)) / 2
        plt.xlim(-7 * 1.1, 7 * 1.1)
        plt.ylim(-7 * 1.1, 7 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        wedge0 = Wedge((0, 0), 7, 180, 360, edgecolor="black", facecolor="white", fill=True)
        wedge1 = Wedge((0, 0), 7, 0, 180, edgecolor="black", facecolor="azure", fill=True)
        wedge2 = Wedge((c1, 0), random_a / 2, 0, 180, edgecolor="black", facecolor="white", fill=True)
        wedge3 = Wedge((c2, 0), (14 - random_a) / 2, 180, 360, edgecolor="black", facecolor="azure", fill=True)
        ax.add_patch(wedge0)
        ax.add_patch(wedge1)
        ax.add_patch(wedge2)
        ax.add_patch(wedge3)
        plt.text(5, -1, f'd = {random_a}', fontsize=11)
        plt.text(-7, -1, f'D = {b}', fontsize=11)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q191:
    # find the coefficient 1
    def __init__(self):
        self.a = rd.randint(-5, 5)
        self.b = rd.randint(-5, 5)
        self.c = rd.randint(-5, 5)
        self.query = "Part of the graph of f(x) = x^3 + bx^2 + cx + d is shown. What is b?"
        self.answer = - (self.a + self.b + self.c)
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = x ** 3 - (self.a + self.b + self.c) * x ** 2 + (
                self.a * self.b + self.c * self.b + self.a * self.c) * x - self.a * self.b * self.c
        plt.plot(x, cubic, color='blue', linewidth=2.5)

        plt.xlim(-5 * 1.1, 5 * 1.1)
        plt.ylim(-5 * 1.1, 5 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(self.a, 0)
        plt.scatter(self.b, 0)
        plt.scatter(self.c, 0)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q192:
    # find the coefficient 2
    def __init__(self):
        self.a = rd.randint(-5, 5)
        self.b = rd.randint(-5, 5)
        self.c = rd.randint(-5, 5)
        self.query = "Part of the graph of f(x) = x^3 + bx^2 + cx + d is shown. What is c?"
        self.answer = self.a * self.b + self.c * self.b + self.a * self.c
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = x ** 3 - (self.a + self.b + self.c) * x ** 2 + (
                self.a * self.b + self.c * self.b + self.a * self.c) * x - self.a * self.b * self.c
        plt.plot(x, cubic, color='purple', linewidth=2.5)

        plt.xlim(-5 * 1.1, 5 * 1.1)
        plt.ylim(-5 * 1.1, 5 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(self.a, 0)
        plt.scatter(self.b, 0)
        plt.scatter(self.c, 0)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q193:
    # find the coefficient 3
    def __init__(self):
        self.a = rd.randint(-5, 5)
        self.b = rd.randint(-5, 5)
        self.c = rd.randint(-5, 5)
        self.query = "Part of the graph of f(x) = x^3 + bx^2 + cx + d is shown. What is d?"
        self.answer = - self.a * self.b * self.c
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = x ** 3 - (self.a + self.b + self.c) * x ** 2 + (
                self.a * self.b + self.c * self.b + self.a * self.c) * x - self.a * self.b * self.c
        plt.plot(x, cubic, color='orange', linewidth=2.5)

        plt.xlim(-5 * 1.1, 5 * 1.1)
        plt.ylim(-5 * 1.1, 5 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(self.a, 0)
        plt.scatter(self.b, 0)
        plt.scatter(self.c, 0)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q194:
    # find azure area in two square
    def __init__(self):
        self.short = rd.randint(1, 9)
        self.long = self.short + rd.randint(1, 3)
        self.query = "Find the area of the azure part in two square."
        self.answer = self.short * self.short / 2 + self.long * self.long - (self.short + self.long) * self.long / 2 - (
                    self.long - self.short) * self.long / 2
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
        square = plt.Polygon([(2, 2), (-2, 2), (-2, -2), (2, -2)], closed=True, fill=True, edgecolor='black',
                             facecolor='white')
        square2 = plt.Polygon([(2, -2), (2, 3), (7, 3), (7, -2)], closed=True, fill=True, edgecolor='black',
                              facecolor='white')
        tri = plt.Polygon([(-2, -2), (2, 2), (7, 3)], closed=True, fill=True, edgecolor='black', facecolor='azure')
        ax.add_patch(square)
        ax.add_patch(square2)
        ax.add_patch(tri)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(7.2, 0, f"{self.long}", fontsize=14)
        plt.text(-2.8, 0, f"{self.short}", fontsize=14)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q195:
    # bisect and square
    def __init__(self):
        self.PA = rd.randint(1, 20)
        self.query = f"Let P be a point on side BC of the square ABCD, PF⊥AP, and CF bisects ∠DCE. PA = {self.PA}," \
                     f"find the length of PF"
        self.answer = self.PA
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q195temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q195temp.png"), dest_image_path)


class Q196:
    # sum of line
    def __init__(self):
        self.a = rd.randint(1, 20)
        self.b = rd.randint(1, 20)
        self.c = rd.randint(1, self.a + self.b - 1)
        self.d = self.a + self.b - self.c
        self.query = "The sum of the numbers at the two vertices at the ends of each edge is equal to the number " \
                     "written on that edge. What number should he write on the edge marked with the question mark? "
        self.answer = self.c
        self.answer_type = "float"
        self.subject = "puzzle test"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
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
        ax.plot([4, 0], [0, -4], color='black', linewidth=1.5)
        ax.plot([4, 0], [0, 4], color='black', linewidth=1.5)
        ax.plot([-4, 0], [0, 4], color='black', linewidth=1.5)
        ax.plot([-4, 0], [0, -4], color='black', linewidth=1.5)
        plt.text(-3, 2.3, f"{self.a}", fontsize=12)
        plt.text(2, 2.3, f"{self.d}", fontsize=12)
        plt.text(-3, -2.8, "?", fontsize=12)
        plt.text(2, -2.8, f"{self.b}", fontsize=12)
        ax.add_patch(circle1)
        ax.add_patch(circle2)
        ax.add_patch(circle3)
        ax.add_patch(circle4)

        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q197:
    # complementary angle 3
    def __init__(self):
        self.angle = rd.randint(10, 80)
        self.query = f"As shown in the figure, points A, O, and B are collinear, and DE is perpendicular to CO. If " \
                     f"∠BOC = {self.angle}°, what is the measure of ∠BOE? "
        self.answer = 90 - self.angle
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        length = 4
        length_s = 0.2
        angle_radians = np.radians(self.angle)
        angle_radians2 = np.radians(self.angle + 90)
        x_end = length * np.cos(angle_radians)
        y_end = length * np.sin(angle_radians)
        x_start = length * np.cos(angle_radians2 + np.radians(180))
        y_start = length * np.sin(angle_radians2 + np.radians(180))
        x_end2 = length * np.cos(angle_radians2)
        y_end2 = length * np.sin(angle_radians2)
        x_pos = length_s * np.cos(angle_radians)
        y_pos = length_s * np.sin(angle_radians)
        x_pos2 = length_s * np.cos(angle_radians2)
        y_pos2 = length_s * np.sin(angle_radians2)
        fig = plt.figure()
        fig.set_size_inches(4, 4)
        plt.plot([x_start, 0], [y_start, 0], color="black")
        plt.plot([0, x_end], [0, y_end], color="black")
        plt.plot([0, x_end2], [0, y_end2], color="black")
        plt.plot([x_pos, x_pos + x_pos2], [y_pos, y_pos + y_pos2], color="black")
        plt.plot([x_pos2, x_pos2 + x_pos], [y_pos2, y_pos2 + y_pos], color="black")
        plt.plot([-4, 4], [0, 0], color="black")
        plt.xlim(-length, length)
        plt.ylim(-length, length)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.text(-4, -0.7, "A", fontsize=14)
        plt.text(3.8, -0.7, "B", fontsize=14)
        plt.text(-0.2, -0.7, "O", fontsize=14)
        plt.text(x_end, y_end + 0.3, "C", fontsize=14)
        plt.text(x_end2, y_end2 + 0.3, "D", fontsize=14)
        plt.text(x_start + 0.2, y_start, "E", fontsize=14)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q198:
    # root differentiable 1
    def __init__(self):
        self.a = rd.randint(-5, 5)
        self.query = "Is the function differentiable at x = 0? choice: (A) Yes (B) No"
        if self.a <= 0:
            self.answer = "B"
        else:
            self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        absolute = (x + self.a) ** (1/2)
        plt.plot(x, absolute, color='red', linewidth=1.5)

        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
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


class Q199:
    # root continuous 1
    def __init__(self):
        self.a = rd.randint(-5, 5)
        self.query = "Is the function continuous on x = 0? choice: (A) Yes (B) No"
        if self.a <= 0:
            self.answer = "B"
        else:
            self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        absolute = (-1) ** self.a * (x + self.a) ** (1 / 2)
        plt.plot(x, absolute, color='purple', linewidth=1.5)

        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
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


class Q200:
    # similar triangle 3
    def __init__(self):
        self.BC = rd.randint(1, 10)
        self.DE = self.BC + rd.randint(1, 4)
        self.AB = self.BC + rd.randint(1, 2)
        self.AD = self.DE / self.BC * self.AB
        self.BD = self.AD - self.AB
        self.query = f"As shown in the figure, BC is parallel to DE, with BC = {self.BC} and DE = {self.DE}. Given AB = {self.AB}, " \
                     "find the length of BD."
        self.answer = self.BD
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q200temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q200temp.png"), dest_image_path)


