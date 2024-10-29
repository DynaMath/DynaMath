import os

import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import random as rd
from PIL import Image, ImageDraw, ImageFont
from matplotlib.patches import *


class Q301:
    # ratio of unshaded area
    def __init__(self):
        self.w = rd.choice([4, 6])
        self.h = rd.choice([4, 6])
        self.w1, self.h1 = rd.choice([((0, 0), (2, 0)), ((2, 0), (0, 0)), ((0, 2), (0, 4)), ((2, 0), (4, 0))])
        self.w2, self.h2 = rd.choice([((8, 0), (10, 0)), ((6, 0), (8, 0)), ((10, 2), (10, 4)), ((10, 0), (10, 2))])
        self.w3, self.h3 = rd.choice([((0, 10), (2, 10)), ((2, 10), (4, 10)), ((0, 8), (0, 6)), ((0, 10), (0, 8))])
        self.w4, self.h4 = rd.choice([((8, 10), (10, 10)), ((6, 10), (8, 10)), ((10, 8), (10, 6)), ((10, 10), (10, 8))])
        self.query = "In the diagram drawn on the square grid, find the ratio of the unshaded area to the shaded " \
                     "area. choice: (A) 1/4 (B) 2/5 (C) 1/3 (D) 1/5 "
        self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        plt.gcf().set_size_inches(4, 4)
        plt.xlim(0, 10.2)
        plt.ylim(-0.2, 10.2)
        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.hlines(0, 0, 10, color="black", linewidth=1)
        plt.vlines(0, 0, 10, color="black", linewidth=1)
        plt.hlines(10, 0, 10, color="black", linewidth=1)
        plt.vlines(10, 0, 10, color="black", linewidth=1)
        plt.hlines(2, 0, 10, color="black", linewidth=1)
        plt.vlines(2, 0, 10, color="black", linewidth=1)
        plt.hlines(8, 0, 10, color="black", linewidth=1)
        plt.vlines(8, 0, 10, color="black", linewidth=1)
        plt.hlines(6, 0, 10, color="black", linewidth=1)
        plt.vlines(6, 0, 10, color="black", linewidth=1)
        plt.hlines(4, 0, 10, color="black", linewidth=1)
        plt.vlines(4, 0, 10, color="black", linewidth=1)

        sq1 = plt.Polygon([(0, 10), (10, 10), (10, 0), (0, 0)], color="gray")
        w = self.w
        h = self.h
        ax = plt.gca()
        ax.add_patch(sq1)
        plt.scatter(w, h, color="black")
        w1, h1 = self.w1, self.h1
        w2, h2 = self.w2, self.h2
        w3, h3 = self.w3, self.h3
        w4, h4 = self.w4, self.h4
        tri1 = plt.Polygon([w1, h1, (w, h)], edgecolor="black", facecolor="white")
        tri2 = plt.Polygon([w2, h2, (w, h)], edgecolor="black", facecolor="white")
        tri3 = plt.Polygon([w3, h3, (w, h)], edgecolor="black", facecolor="white")
        tri4 = plt.Polygon([w4, h4, (w, h)], edgecolor="black", facecolor="white")
        ax.add_patch(tri1)
        ax.add_patch(tri2)
        ax.add_patch(tri3)
        ax.add_patch(tri4)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q302:
    # spilt to two triangle by one straight line
    def __init__(self):
        self.m = rd.randint(3, 4)
        self.n = rd.randint(5, 10)
        self.query = "Which of the shapes cannot be split into two triangles using a single straight line?  choice: (" \
                     "A) left shape (B) right shape "
        self.answer = rd.choice(["A", "B"])
        self.answer_type = "multiple choice"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        m = self.m
        n = self.n
        plt.xlim(-5 * 1.1, 5 * 1.1)
        plt.ylim(-5 * 1.1, 5 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        left = (-2, 0)
        right = (3, 0)
        plt.gcf().set_size_inches(4, 4)
        if self.answer == "A":
            polygon1 = CirclePolygon(xy=left, radius=2, resolution=m, facecolor="gray", edgecolor="black")
            polygon2 = CirclePolygon(xy=right, radius=2, resolution=n, facecolor="gray", edgecolor="black")
        else:
            polygon1 = CirclePolygon(xy=right, radius=2, resolution=n, facecolor="gray", edgecolor="black")
            polygon2 = CirclePolygon(xy=left, radius=2, resolution=m, facecolor="gray", edgecolor="black")
        ax.add_patch(polygon1)
        ax.add_patch(polygon2)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q303:
    # point and triangle
    def __init__(self):
        self.w1, self.h1 = rd.randint(1, 9), rd.randint(1, 9)
        self.w2, self.h2 = rd.randint(1, 9), rd.randint(1, 9)
        self.w3, self.h3 = rd.randint(1, 9), rd.randint(1, 9)
        self.a = np.sqrt((self.w1 - self.w2) ** 2 + (self.h1 - self.h2) ** 2)
        self.b = np.sqrt((self.w1 - self.w3) ** 2 + (self.h1 - self.h3) ** 2)
        self.c = np.sqrt((self.w2 - self.w3) ** 2 + (self.h2 - self.h3) ** 2)
        self.p = 1/2 * (self.a + self.b + self.c)
        self.query = "Find the area of the triangle enclosed by three black points."
        self.answer = np.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        plt.gcf().set_size_inches(4, 4)
        plt.xlim(0, 10)
        plt.ylim(0, 10)
        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        ax = plt.gca()
        w1, h1 = self.w1, self.h1
        w2, h2 = self.w2, self.h2
        w3, h3 = self.w3, self.h3
        plt.scatter(w1, h1, color="black")
        plt.scatter(w2, h2, color="black")
        plt.scatter(w3, h3, color="black")
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q304:
    # point in circle
    def __init__(self):
        self.a = rd.randint(5, 90) / 10
        self.b = rd.randint(5, 90) / 10
        self.c = rd.randint(5, 90) / 10
        self.d = rd.randint(5, 90) / 10
        self.e = rd.randint(5, 90) / 10
        self.f = rd.randint(5, 90) / 10
        self.query = "How many circles is the red point inside?"
        self.answer = 0
        if self.a > 2:
            self.answer += 1
        if self.b > 2:
            self.answer += 1
        if self.c > 2:
            self.answer += 1
        if self.d > 2:
            self.answer += 1
        if self.e > np.sqrt(2):
            self.answer += 1
        if self.f > np.sqrt(2):
            self.answer += 1
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        ax = plt.gca()
        plt.xlim(-10 * 1.1, 10 * 1.1)
        plt.ylim(-10 * 1.1, 10 * 1.1)
        plt.gcf().set_size_inches(6, 6)
        plt.xticks([-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        plt.yticks([-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        circleA = Circle((-2, 0), self.a, edgecolor="black", facecolor="white", fill=False)
        circleB = Circle((2, 0), self.b, edgecolor="black", facecolor="white", fill=False)
        circleC = Circle((0, -2), self.c, edgecolor="black", facecolor="white", fill=False)
        circleD = Circle((0, 2), self.d, edgecolor="black", facecolor="white", fill=False)
        circleE = Circle((1, 1), self.e, edgecolor="black", facecolor="white", fill=False)
        circleF = Circle((-1, -1), self.f, edgecolor="black", facecolor="white", fill=False)
        plt.scatter(0, 0, color="red", s=40)
        ax.add_patch(circleA)
        ax.add_patch(circleB)
        ax.add_patch(circleC)
        ax.add_patch(circleD)
        ax.add_patch(circleE)
        ax.add_patch(circleF)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q305:
    # find unknown number
    def __init__(self):
        self.star = rd.randint(1, 20)
        self.sq = rd.randint(1, 20)
        self.tri = rd.randint(1, 20)
        self.c1 = self.star * 5
        self.c2 = self.star * 3 + self.sq * 2
        self.c3 = self.sq * 2 + self.tri * 3
        self.c4 = self.star * 2 + self.sq * 2 + self.tri
        self.query = "The store has 4 combinations of candies. Each candy type has the same price. Find the price of " \
                     "the fourth combination. "
        self.answer = self.c4
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        plt.gcf().set_size_inches(4, 4)
        plt.xlim(0, 10)
        plt.ylim(0, 10)
        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        ax = plt.gca()
        plt.text(4, 8, r'1. $\bigstar$ $\bigstar$ $\bigstar$ $\bigstar$ $\bigstar$', fontsize=20, ha='center',
                 va='center')
        plt.text(9, 8, f"${self.c1}", fontsize=12, ha='center', va='center')
        plt.text(4, 6, r'2. $\bigstar$ $\blacksquare$ $\bigstar$ $\blacksquare$ $\bigstar$', fontsize=20, ha='center',
                 va='center')
        plt.text(9, 6, f"${self.c2}", fontsize=12, ha='center', va='center')
        plt.text(4, 4, r'3. $\blacktriangle$ $\blacksquare$ $\blacktriangle$ $\blacksquare$ $\blacktriangle$',
                 fontsize=20, ha='center', va='center')
        plt.text(9, 4, f"${self.c3}", fontsize=12, ha='center', va='center')
        plt.text(4, 2, r'4. $\bigstar$ $\blacksquare$ $\blacksquare$ $\blacktriangle$ $\bigstar$', fontsize=20,
                 ha='center', va='center')
        plt.text(9, 2, "$?", fontsize=12, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q306:
    # define a new calculation
    def __init__(self):
        self.a = rd.randint(1, 99)
        self.b = rd.randint(1, 99)
        self.c = rd.randint(1, 99)
        self.query = "a, b are two arbitrary number. According to the calculation of first and second rows, find the " \
                     "value of third row of calculations. "
        self.answer = self.a - 0.5 * self.b + 0.5 * self.c
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def draw(self, num):
        plt.gcf().set_size_inches(4, 4)
        plt.xlim(0, 10)
        plt.ylim(0, 10)
        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        ax = plt.gca()
        plt.text(5, 8, r'a $\flat$ b = a - 0.5b', fontsize=16, ha='center', va='center')
        plt.text(5, 6, r'a $\sharp$ b = a + 0.5b', fontsize=16, ha='center', va='center')
        plt.text(5, 4, fr'{self.a} $\flat$ {self.b} $\sharp$ {self.c} = ___', fontsize=16, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q307:
    # solution 1
    def __init__(self):
        self.sa = rd.randint(5, 50)
        self.sb = rd.randint(5, 50)
        self.query = "The diagram below is a model of two solutions. Each ball represents one particle of solute. " \
                     "Which solution has a higher concentration of particles?  choice: (A) Solution A (B) Solution B " \
                     "(C) Their concentrations are the same "
        if self.sa > self.sb:
            self.answer = "A"
        elif self.sa < self.sb:
            self.answer = "B"
        elif self.sa == self.sb:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        Img = Image.open('temp_image/Q307temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        x1 = np.random.uniform(125, 770, size=self.sa)
        y1 = np.random.uniform(600, 900, size=self.sa)
        x2 = np.random.uniform(1000, 1700, size=self.sb)
        y2 = np.random.uniform(600, 900, size=self.sb)
        plt.scatter(x1, y1, edgecolors='black', s=20, color="deeppink")
        plt.scatter(x2, y2, edgecolors='black', s=20, color="deeppink")
        plt.text(450, 1100, "Solvent Volume: 100 mL", fontsize=14, ha='center', va='center')
        plt.text(1400, 1100, "Solvent Volume: 100 mL", fontsize=14, ha='center', va='center')
        plt.text(450, 1200, "Solution A", fontsize=18, ha='center', va='center')
        plt.text(1400, 1200, "Solution B", fontsize=18, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q308:
    # solution 2
    def __init__(self):
        self.sa = rd.randint(5, 30)
        self.sb = rd.randint(5, 30)
        self.query = "The diagram below is a model of two solutions. Each ball represents one mole particle of solute." \
                     "Which solution has a higher mass?  choice: (A) Solution A (B) Solution B " \
                     "(C) Their masses are the same "
        if self.sa * 58.5 > self.sb * 40:
            self.answer = "A"
        elif self.sa * 58.5 < self.sb * 40:
            self.answer = "B"
        elif self.sa * 58.5 == self.sb * 40:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        Img = Image.open('temp_image/Q307temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        x1 = np.random.uniform(125, 770, size=self.sa)
        y1 = np.random.uniform(600, 900, size=self.sa)
        x2 = np.random.uniform(1000, 1700, size=self.sb)
        y2 = np.random.uniform(600, 900, size=self.sb)
        plt.scatter(x1, y1, edgecolors='black', s=20, color="lightgreen")
        plt.scatter(x2, y2, edgecolors='black', s=20, color="deeppink")
        plt.text(450, 1100, "Solvent Volume: 100 mL", fontsize=14, ha='center', va='center')
        plt.text(1400, 1100, "Solvent Volume: 100 mL", fontsize=14, ha='center', va='center')
        plt.text(450, 1200, "Solution A", fontsize=18, ha='center', va='center')
        plt.text(1400, 1200, "Solution B", fontsize=18, ha='center', va='center')
        plt.legend(["NaCl", "NaOH"], loc=1)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q309:
    # solution 3
    def __init__(self):
        self.sa = rd.randint(5, 30)
        self.sb = rd.randint(5, 30)
        self.query = "The diagram below is a model of three solutions. Each ball represents 0.01 mole KMnO4. If " \
                     "researcher pour left two solutions to rightmost beaker. Find the concentration of the solution " \
                     "in the rightmost beaker."
        self.answer = 0.01 * (self.sa + self.sb) * 158 / (0.01 * (self.sa + self.sb) * 158 + 300)
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        Img = Image.open('temp_image/Q309temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        x1 = np.random.uniform(100, 650, size=self.sa)
        y1 = np.random.uniform(550, 800, size=self.sa)
        x2 = np.random.uniform(850, 1400, size=self.sb)
        y2 = np.random.uniform(550, 800, size=self.sb)
        plt.scatter(x1, y1, edgecolors='black', s=15, color="slateblue")
        plt.scatter(x2, y2, edgecolors='black', s=15, color="slateblue")
        plt.text(1000, 1100, "Solvent Volume per beaker: 100 mL", fontsize=20, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q310:
    # exchange
    def __init__(self):
        self.yen = rd.randint(120, 160)
        self.num = rd.randint(100, 900)
        self.query = "Fill in the blank of the second equation."
        self.answer = self.num / self.yen
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "elementary school"

    def draw(self, num):
        plt.gcf().set_size_inches(4, 4)
        plt.xlim(0, 10)
        plt.ylim(0, 10)
        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        ax = plt.gca()
        plt.text(5, 8, fr'$\yen$ {self.yen}  = ', fontsize=24, ha='center', va='center')
        plt.text(9, 8, r'$1', fontsize=24, ha='center', va='center')
        plt.text(5, 4, fr'$\yen$ {self.num}  = ', fontsize=24, ha='center', va='center')
        plt.text(9, 4, r'$___', fontsize=24, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q311:
    # instrument panel
    def __init__(self):
        self.angle = rd.randint(10, 180)
        self.query = "A ticket will be issued when the vehicle speed exceeds 70 mph. According to the instrument " \
                     "panel below, will this vehicle get the ticket?  choice: (A) Yes (B) No "
        if self.angle >= 90:
            self.answer = "B"
        else:
            self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
        self.level = "elementary school"

    def draw(self, num):
        Img = Image.open('temp_image/Q311temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        plt.scatter(360, 300, color="dimgrey", s=200)
        plt.plot([360, 90 * np.cos(self.angle / 360 * 2 * np.pi) + 360], [300, 300 - 90 * np.sin(self.angle / 360 * 2 * np.pi)],
                 color="dimgrey", linewidth=2)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q312:
    # consecutive number to 10
    def __init__(self):
        self.a = rd.randint(0, 9)
        self.query = "The sum of numbers on three consecutive underlines is always 10. Find the number on the red " \
                     "underlines. "
        self.answer = self.a
        self.answer_type = "float"
        self.subject = "puzzle test"
        self.level = "elementary school"

    def draw(self, num):
        a = self.a
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.hlines(0, -5, -4, color="black", linewidth=2)
        plt.hlines(0, -3, -2, color="black", linewidth=2)
        plt.hlines(0, -1, 0, color="black", linewidth=2)
        plt.hlines(0, 1, 2, color="red", linewidth=2)
        plt.hlines(0, 3, 4, color="black", linewidth=2)
        plt.hlines(0, 5, 6, color="black", linewidth=2)
        plt.text(-4.5, 0.4, f"{a}", fontsize=20, ha='center', va='center')
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q313:
    # 3 digit code
    def __init__(self):
        self.lst = rd.sample(range(0, 10), 3)
        temp = list(range(0, 10))
        temp.remove(self.lst[0])
        temp.remove(self.lst[1])
        temp.remove(self.lst[2])
        self.row1 = rd.choice([[rd.choice(temp), rd.choice(temp), self.lst[0]], [rd.choice(temp), self.lst[0], rd.choice(temp)]])
        self.row2 = [rd.choice(temp), self.lst[1], rd.choice(temp)]
        self.row3 = [self.lst[2], rd.choice(temp), self.lst[1]]
        self.query = "The statements on the right give clues to the identity of a three-digit code. What is the code?"
        self.answer = f"{self.lst[0]}{self.lst[1]}{self.lst[2]}"
        self.answer_type = "text"
        self.subject = "puzzle test"
        self.level = "elementary school"

    def draw(self, num):
        plt.xlim(-5 * 1.1, 5 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.hlines(0, -5, -4, color="black", linewidth=2)
        plt.hlines(0, -3, -2, color="black", linewidth=2)
        plt.hlines(0, -1, 0, color="black", linewidth=2)
        plt.hlines(3, -5, -4, color="black", linewidth=2)
        plt.hlines(3, -3, -2, color="black", linewidth=2)
        plt.hlines(3, -1, 0, color="black", linewidth=2)
        plt.hlines(-3, -5, -4, color="black", linewidth=2)
        plt.hlines(-3, -3, -2, color="black", linewidth=2)
        plt.hlines(-3, -1, 0, color="black", linewidth=2)
        plt.text(-2.5, 0.4, f"{self.row2[1]}", fontsize=16, ha='center', va='center')
        plt.text(-4.5, 0.4, f"{self.row2[0]}", fontsize=16, ha='center', va='center')
        plt.text(-0.5, 0.4, f"{self.row2[2]}", fontsize=16, ha='center', va='center')
        plt.text(-2.5, 3.4, f"{self.row1[1]}", fontsize=16, ha='center', va='center')
        plt.text(-4.5, 3.4, f"{self.row1[0]}", fontsize=16, ha='center', va='center')
        plt.text(-0.5, 3.4, f"{self.row1[2]}", fontsize=16, ha='center', va='center')
        plt.text(-2.5, -2.6, f"{self.row3[1]}", fontsize=16, ha='center', va='center')
        plt.text(-4.5, -2.6, f"{self.row3[0]}", fontsize=16, ha='center', va='center')
        plt.text(-0.5, -2.6, f"{self.row3[2]}", fontsize=16, ha='center', va='center')
        plt.text(1, 0, "One digits is correct and in the right place", fontsize=20)
        plt.text(1, 3, "One digits is correct but in the wrong place", fontsize=20)
        plt.text(1, -3, "Two digits is correct but in the wrong place", fontsize=20)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q314:
    # normal distribution 1
    def __init__(self):
        self.lst = rd.sample(range(50, 150), 4)
        for i in range(0, 4):
            self.lst[i] = self.lst[i] / 100
        maximal = max(self.lst)
        self.query = "What is the color of the normal distribution line with largest standard deviation? " \
                     "choice: (A) red (B) blue (C) green (D) orange"
        if self.lst[0] == maximal:
            self.answer = "A"
        elif self.lst[1] == maximal:
            self.answer = "B"
        elif self.lst[2] == maximal:
            self.answer = "C"
        else:
            self.answer = "D"
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.xlim(-5, 5)
        plt.ylim(0, 1)

        x_normal = np.linspace(-5, 5, 500)
        y_normal = norm.pdf(x_normal, 0, self.lst[0])
        x_normal2 = np.linspace(-5, 5, 500)
        y_normal2 = norm.pdf(x_normal2, 0, self.lst[1])
        x_normal3 = np.linspace(-5, 5, 500)
        y_normal3 = norm.pdf(x_normal3, 0, self.lst[2])
        x_normal4 = np.linspace(-5, 5, 500)
        y_normal4 = norm.pdf(x_normal4, 0, self.lst[3])

        plt.plot(x_normal, y_normal, color='red')
        plt.plot(x_normal2, y_normal2, color='blue')
        plt.plot(x_normal3, y_normal3, color='green')
        plt.plot(x_normal4, y_normal4, color='orange')
        plt.xlabel('x', fontsize=14)
        plt.ylabel('Probability Density', fontsize=14)
        plt.title('Normal Distribution', fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q315:
    # sudo 2
    def __init__(self):
        self.lst = rd.sample(range(1, 6), 4)
        temp = list(range(1, 6))
        self.up = rd.choice(self.lst)
        temp.remove(self.lst[0])
        if self.up != self.lst[0]:
            temp.remove(self.up)
        self.down = rd.choice(temp)
        self.query = "Write the numbers 1, 2, 3, 4, 5 in the square 5x5 in such a way that every row and every column " \
                     "has each number. How many kinds of number can be put to replace 'x'? "
        self.answer = 3
        self.answer_type = "float"
        self.subject = "puzzle test"
        self.level = "elementary school"

    def draw(self, num):
        plt.gcf().set_size_inches(4, 4)
        plt.xlim(0, 10.2)
        plt.ylim(-0.2, 10.2)
        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.hlines(0, 0, 10, color="black", linewidth=1)
        plt.vlines(0, 0, 10, color="black", linewidth=1)
        plt.hlines(10, 0, 10, color="black", linewidth=1)
        plt.vlines(10, 0, 10, color="black", linewidth=1)
        plt.hlines(2, 0, 10, color="black", linewidth=1)
        plt.vlines(2, 0, 10, color="black", linewidth=1)
        plt.hlines(8, 0, 10, color="black", linewidth=1)
        plt.vlines(8, 0, 10, color="black", linewidth=1)
        plt.hlines(6, 0, 10, color="black", linewidth=1)
        plt.vlines(6, 0, 10, color="black", linewidth=1)
        plt.hlines(4, 0, 10, color="black", linewidth=1)
        plt.vlines(4, 0, 10, color="black", linewidth=1)
        plt.text(1, 1, f"{self.lst[3]}", fontsize=16, ha='center', va='center')
        plt.text(1, 3, f"{self.lst[2]}", fontsize=16, ha='center', va='center')
        plt.text(1, 5, f"{self.lst[1]}", fontsize=16, ha='center', va='center')
        plt.text(1, 7, f"{self.lst[0]}", fontsize=16, ha='center', va='center')
        plt.text(3, 9, f"{self.up}", fontsize=16, ha='center', va='center')
        plt.text(3, 7, f"{self.down}", fontsize=16, ha='center', va='center')
        plt.text(7, 9, "x", fontsize=16, ha='center', va='center')
        ax = plt.gca()
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q316:
    # boarding pass
    def __init__(self):
        self.h1 = rd.randint(1, 11)
        self.m1 = rd.randint(10, 59)
        self.h2 = rd.randint(1, 11)
        self.m2 = rd.randint(10, 59)
        self.query = "According to the boarding pass, how long is the flight time of this airplane? Answer the " \
                     "question using the total number of minutes. "
        self.answer = (self.h2 + 12 - self.h1) * 60 + self.m2 - self.m1 - 300
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def draw(self, num):
        Img = Image.open('temp_image/Q316temp.png')
        fig, ax = plt.subplots()
        if self.h1 < 10:
            plt.text(100, 500, f"0{self.h1}:{self.m1}", fontsize=9)
        else:
            plt.text(100, 500, f"{self.h1}:{self.m1}", fontsize=9)
        if self.h2 < 10:
            plt.text(790, 500, f"0{self.h2}:{self.m2}", fontsize=9)
        else:
            plt.text(790, 500, f"{self.h2}:{self.m2}", fontsize=9)
        ax.imshow(Img)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, dpi=300)
        plt.close()


class Q317:
    # find the value behind the symbol
    def __init__(self):
        self.lst = rd.sample(range(1, 10), 4)
        self.num = [rd.choice(self.lst) for i in range(0, 5)]
        self.num2 = [rd.choice(self.lst) for i in range(0, 5)]
        self.sum1 = 10000 * self.num[0] + 1000 * self.num[1] + 100 * self.num[2] + 10 * self.num[3] + self.num[4]
        self.sum2 = 10000 * self.num2[0] + 1000 * self.num2[1] + 100 * self.num2[2] + 10 * self.num2[3] + self.num2[4]
        self.sum = self.sum1 + self.sum2
        self.query = "Tom writes down two five-digit number. He places different shapes on different digits. He " \
                     "places the same shape on the same digits. Find the value of first five-digit number. "
        self.answer = self.sum1
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def preprocess(self, lst):
        str1 = ""
        for num in lst:
            if num == self.lst[0]:
                str1 = str1 + " \u2764"
            elif num == self.lst[1]:
                str1 = str1 + " \u2660"
            elif num == self.lst[2]:
                str1 = str1 + " \u2666"
            elif num == self.lst[3]:
                str1 = str1 + " \u2663"
        return str1.lstrip()

    def draw(self, num):
        plt.gcf().set_size_inches(4, 4)
        plt.xlim(0, 10)
        plt.ylim(0, 10)
        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        symbol1 = self.preprocess(self.num)
        symbol2 = self.preprocess(self.num2)
        result = str(self.sum)
        ax = plt.gca()
        plt.text(5, 7, symbol1, fontsize=16, ha='center', va='center')
        plt.text(5, 5, symbol2, fontsize=16, ha='center', va='center')
        plt.text(2, 5, "+", fontsize=16, ha='center', va='center')
        plt.hlines(4, 2, 8, color="black", linewidth=2)
        if len(result) > 5:
            plt.text(7, 3, f"{result[0]}  {result[1]}  {result[2]}  {result[3]}  {result[4]}  {result[5]}", fontsize=16
                     , ha='right', va='center')
        else:
            plt.text(7, 3, f"{result[0]}  {result[1]}  {result[2]}  {result[3]}  {result[4]}", fontsize=16
                     , ha='right', va='center')
        plt.grid()
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, dpi=300)
        plt.close()


class Q318:
    # distance in space
    def __init__(self):
        self.ax1 = rd.randint(0, 10)
        self.ax2 = rd.randint(0, 10)
        self.ay1 = rd.randint(0, 10)
        self.ay2 = rd.randint(0, 10)
        self.az1 = rd.randint(0, 9)
        self.az2 = rd.randint(0, 9)
        self.query = "Find the distance between orange and blue point."
        self.answer = np.sqrt((self.ax1 - self.ax2) ** 2 + (self.ay1 - self.ay2) ** 2 + (self.az1 - self.az2) ** 2)
        self.answer_type = "float"
        self.subject = "solid geometry"
        self.level = "high school"

    def draw(self, num):
        ax1 = self.ax1
        ax2 = self.ax2
        ay1 = self.ay1
        ay2 = self.ay2
        az1 = self.az1
        az2 = self.az2
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter3D(ax1, ay1, az1, s=50)
        ax.scatter3D(ax2, ay2, az2, s=50)
        ax.text(ax1, ay1, az1 + 1, f"({ax1}, {ay1}, {az1})", fontsize=12)
        ax.text(ax2, ay2, az2 + 1, f"({ax2}, {ay2}, {az2})", fontsize=12)
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax.plot3D([ax1, ax2], [ay1, ay2], [az1, az2], 'deeppink')
        ax.set_xlim3d(0, 10)
        ax.set_ylim3d(0, 10)
        ax.set_zlim3d(0, 10)
        ax.view_init(10)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, dpi=300)
        plt.close()


class Q319:
    # remove dark blue square
    def __init__(self):
        self.c1 = np.random.randint(0, 2, 5)
        self.c2 = np.random.randint(0, 2, 5)
        self.c3 = np.random.randint(0, 2, 5)
        self.c4 = np.random.randint(0, 2, 5)
        self.c5 = np.random.randint(0, 2, 5)
        self.query = "In the grid, how many dark blue squares have to be coloured white, so that in each row and each " \
                     "column there is exactly one dark blue square? If it is impossible that in each row and each " \
                     "column there is exactly one dark blue square, answer 0."
        if sum(self.c1) == 0 or sum(self.c2) == 0 or sum(self.c3) == 0 or sum(self.c4) == 0 or sum(self.c5) == 0:
            self.answer = 0
        else:
            self.answer = sum(self.c1) + sum(self.c2) + sum(self.c3) + sum(self.c4) + sum(self.c5) - 5
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def draw(self, num):
        col1 = self.c1
        col2 = self.c2
        col3 = self.c3
        col4 = self.c4
        col5 = self.c5
        plt.hlines(0.5, -0.5, 4.5, color="black", linewidth=1)
        plt.vlines(0.5, -0.5, 4.5, color="black", linewidth=1)
        plt.hlines(1.5, -0.5, 4.5, color="black", linewidth=1)
        plt.vlines(1.5, -0.5, 4.5, color="black", linewidth=1)
        plt.hlines(2.5, -0.5, 4.5, color="black", linewidth=1)
        plt.vlines(2.5, -0.5, 4.5, color="black", linewidth=1)
        plt.hlines(3.5, -0.5, 4.5, color="black", linewidth=1)
        plt.vlines(3.5, -0.5, 4.5, color="black", linewidth=1)
        plt.hlines(4.5, -0.5, 4.5, color="black", linewidth=1)
        plt.vlines(4.5, -0.5, 4.5, color="black", linewidth=1)
        plt.hlines(-0.5, -0.5, 4.5, color="black", linewidth=1)
        plt.vlines(-0.5, -0.5, 4.5, color="black", linewidth=1)
        mat = np.array([col1, col2, col3, col4, col5])
        plt.imshow(mat, cmap="Blues")
        ax = plt.gca()
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q320:
    # distance in space 2
    def __init__(self):
        self.ax1 = rd.randint(0, 10)
        self.ax2 = rd.randint(0, 10)
        self.ay1 = rd.randint(0, 10)
        self.ay2 = rd.randint(0, 10)
        self.az1 = rd.randint(0, 9)
        self.az2 = rd.randint(0, 9)
        self.ax3 = rd.randint(0, 10)
        self.ay3 = rd.randint(0, 10)
        self.az3 = rd.randint(0, 9)
        self.query = "Which line is longer, the pink or the red line?  choice: (A) pink (B) red (C) Their lengths are " \
                     "the same "
        pink = np.sqrt((self.ax1 - self.ax2) ** 2 + (self.ay1 - self.ay2) ** 2 + (self.az1 - self.az2) ** 2)
        red = np.sqrt((self.ax1 - self.ax3) ** 2 + (self.ay1 - self.ay3) ** 2 + (self.az1 - self.az3) ** 2)
        if pink > red:
            self.answer = "A"
        elif pink < red:
            self.answer = "B"
        elif pink == red:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "solid geometry"
        self.level = "high school"

    def draw(self, num):
        ax1 = self.ax1
        ax2 = self.ax2
        ay1 = self.ay1
        ay2 = self.ay2
        az1 = self.az1
        az2 = self.az2
        ax3 = self.ax3
        ay3 = self.ay3
        az3 = self.az3
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter3D(ax1, ay1, az1, s=50)
        ax.scatter3D(ax2, ay2, az2, s=50)
        ax.scatter3D(ax3, ay3, az3, s=50)
        ax.text(ax1, ay1, az1 + 1, f"({ax1}, {ay1}, {az1})", fontsize=12)
        ax.text(ax2, ay2, az2 + 1, f"({ax2}, {ay2}, {az2})", fontsize=12)
        ax.text(ax3, ay3, az3 + 1, f"({ax3}, {ay3}, {az3})", fontsize=12)
        ax.plot3D([ax1, ax2], [ay1, ay2], [az1, az2], 'deeppink')
        ax.plot3D([ax1, ax3], [ay1, ay3], [az1, az3], 'red')
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax.set_xlim3d(0, 10)
        ax.set_ylim3d(0, 10)
        ax.set_zlim3d(0, 10)
        ax.view_init(10)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()
