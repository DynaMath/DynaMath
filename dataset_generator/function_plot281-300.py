import math
import shutil
import os.path
import matplotlib.pyplot as plt
import mpltern
import numpy as np
import random as rd
import pandas as pd
from itertools import groupby
from PIL import Image, ImageDraw, ImageFont
from matplotlib.patches import *


class Q281:
    # area between triangle and square
    def __init__(self):
        self.AB = rd.randint(1, 99)
        self.query = f"In the figure below, the area of square ABCD is equal to the sum of the area of triangles ABE " \
                     f"and DCE. If AB = {self.AB}, then CE = ___ "
        self.answer = self.AB / 2
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q281temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q281temp.png"), dest_image_path)


class Q282:
    # addition puzzle
    def __init__(self):
        self.a1 = rd.randint(1, 49)
        self.a2 = rd.randint(1, 49)
        self.a3 = self.a1 + self.a2
        self.a4 = rd.randint(0, self.a1 - 1)
        self.a5 = rd.randint(0, self.a2 - 1)
        self.a6 = self.a4 + self.a5
        self.a7 = self.a1 - self.a4
        self.a8 = self.a2 - self.a5
        self.a9 = self.a7 + self.a8
        self.query = f"Fill in the white spaces to make the equations work.  choice: (A) {self.a1}, {self.a6}, {self.a4}, and {self.a8}  (B) {self.a6}, {self.a4}, {self.a1 - 1}, and {self.a8} (C) {self.a8 + 1}, {self.a4 - 1}, {self.a6}, {self.a1} "
        self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "puzzle test"
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
        plt.text(1, 3, "=", fontsize=20, ha='center', va='center')
        plt.text(1, 7, "+", fontsize=20, ha='center', va='center')
        plt.text(3, 1, "+", fontsize=20, ha='center', va='center')
        plt.text(3, 5, "+", fontsize=20, ha='center', va='center')
        plt.text(3, 9, "+", fontsize=20, ha='center', va='center')
        plt.text(7, 1, "=", fontsize=20, ha='center', va='center')
        plt.text(7, 5, "=", fontsize=20, ha='center', va='center')
        plt.text(7, 9, "=", fontsize=20, ha='center', va='center')
        plt.text(9, 3, "=", fontsize=20, ha='center', va='center')
        plt.text(9, 7, "+", fontsize=20, ha='center', va='center')
        plt.text(5, 7, "+", fontsize=20, ha='center', va='center')
        plt.text(5, 3, "=", fontsize=20, ha='center', va='center')
        plt.text(5, 1, f"{self.a2}", fontsize=20, ha='center', va='center')
        plt.text(9, 1, f"{self.a3}", fontsize=20, ha='center', va='center')
        plt.text(5, 5, f"{self.a5}", fontsize=20, ha='center', va='center')
        plt.text(1, 9, f"{self.a7}", fontsize=20, ha='center', va='center')
        plt.text(9, 9, f"{self.a9}", fontsize=20, ha='center', va='center')
        sq1 = plt.Polygon([(2, 6), (4, 6), (4, 8), (2, 8)], color="gray")
        sq2 = plt.Polygon([(6, 2), (8, 2), (8, 4), (6, 4)], color="gray")
        sq3 = plt.Polygon([(2, 2), (4, 2), (4, 4), (2, 4)], color="gray")
        sq4 = plt.Polygon([(6, 6), (8, 6), (8, 8), (6, 8)], color="gray")
        ax = plt.gca()
        ax.add_patch(sq1)
        ax.add_patch(sq2)
        ax.add_patch(sq3)
        ax.add_patch(sq4)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q283:
    # 5x5 sudoku
    def __init__(self):
        lst1 = [2, 4, 5, 3, 1, 4, 3, 1, 5, 2, 1, 5, 4, 2, 3, 5, 2, 3, 1, 4, 3, 1, 2, 4, 5]
        lst2 = [3, 4, 1, 2, 5, 1, 2, 5, 3, 4, 5, 3, 4, 1, 2, 4, 1, 2, 5, 3, 2, 5, 3, 4, 1]
        lst3 = [4, 5, 2, 1, 3, 1, 3, 5, 2, 4, 3, 2, 1, 4, 5, 2, 4, 3, 5, 1, 5, 1, 4, 3, 2]
        self.lst = rd.choice([lst1, lst2, lst3])
        self.choice = rd.randint(0, 24)
        self.query = "Fill in the white space to make it like a 5x5 sudoku."
        self.answer = self.lst[self.choice]
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
        h = 1
        v = 1
        count = 0
        for i in range(0, 5):
            for j in range(0, 5):
                if count != self.choice:
                    plt.text(h, v, f"{self.lst[count]}", fontsize=20, ha='center', va='center')
                h += 2
                count += 1
            h = 1
            v += 2
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q284:
    # find missing number 1
    def __init__(self):
        self.a1 = rd.randint(1, 30)
        self.a2 = rd.randint(1, 30)
        self.ac = rd.randint(1, 30)
        self.a3 = self.a1 + self.a2 + self.ac
        self.b1 = rd.randint(1, 30)
        self.b2 = rd.randint(1, 30)
        self.bc = rd.randint(1, 30)
        self.b3 = self.b1 + self.b2 + self.bc
        self.c1 = rd.randint(1, 30)
        self.c2 = rd.randint(1, 30)
        self.cc = rd.randint(1, 30)
        self.c3 = self.c1 + self.c2 + self.cc
        self.query = "Find the missing value."
        self.answer = self.cc * 2
        self.answer_type = "float"
        self.subject = "puzzle test"
        self.level = "elementary school"

    def draw(self, num):
        Img = Image.open('temp_image/Q284temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        plt.text(200, 900, f"{self.a1}", fontsize=20, ha='center', va='center')
        plt.text(450, 900, f"{self.a2}", fontsize=20, ha='center', va='center')
        plt.text(320, 650, f"{self.a3}", fontsize=20, ha='center', va='center')
        plt.text(980, 900, f"{self.c1}", fontsize=20, ha='center', va='center')
        plt.text(1230, 900, f"{self.c2}", fontsize=20, ha='center', va='center')
        plt.text(1120, 650, f"{self.c3}", fontsize=20, ha='center', va='center')
        plt.text(570, 400, f"{self.b1}", fontsize=20, ha='center', va='center')
        plt.text(820, 400, f"{self.b2}", fontsize=20, ha='center', va='center')
        plt.text(690, 150, f"{self.b3}", fontsize=20, ha='center', va='center')
        plt.text(690, 300, f"{2 * self.bc}", fontsize=20, ha='center', va='center')
        plt.text(320, 800, f"{2 * self.ac}", fontsize=20, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q285:
    # find the missing number 2
    def __init__(self):
        self.a = rd.randint(1, 30)
        self.b = rd.randint(1, 30)
        self.c = rd.randint(1, 30)
        self.query = "Find the missing number."
        self.answer = self.c * self.c
        self.answer_type = "float"
        self.subject = "puzzle test"
        self.level = "elementary school"

    def draw(self, num):
        r = 2
        plt.xlim(-7 * 1.1, 7 * 1.1)
        plt.ylim(-7 * 1.1, 7 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        circle = Circle((0, 0), r, edgecolor="black", facecolor="white", fill=True)
        circle2 = Circle((-5, 0), r, edgecolor="black", facecolor="white", fill=True)
        circle3 = Circle((5, 0), r, edgecolor="black", facecolor="white", fill=True)
        ax.add_patch(circle)
        ax.add_patch(circle2)
        ax.add_patch(circle3)
        plt.hlines(0, -2, r, colors="black")
        plt.vlines(0, -2, r, colors="black")
        plt.hlines(0, -7, -3, colors="black")
        plt.vlines(-5, -2, r, colors="black")
        plt.hlines(0, 3, 7, colors="black")
        plt.vlines(5, -2, r, colors="black")
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(-0.8, 0.9, f"{self.a}", fontsize=12, ha='center', va='center')
        plt.text(0.8, 0.9, f"{self.a * 2}", fontsize=12, ha='center', va='center')
        plt.text(-0.8, -0.9, f"{self.a * 3}", fontsize=12, ha='center', va='center')
        plt.text(0.8, -0.9, f"{self.a * self.a}", fontsize=12, ha='center', va='center')
        plt.text(-0.8 - 5, 0.9, f"{self.b}", fontsize=12, ha='center', va='center')
        plt.text(0.8 - 5, 0.9, f"{self.b * 2}", fontsize=12, ha='center', va='center')
        plt.text(-0.8 - 5, -0.9, f"{self.b * 3}", fontsize=12, ha='center', va='center')
        plt.text(0.8 - 5, -0.9, f"{self.b * self.b}", fontsize=12, ha='center', va='center')
        plt.text(-0.8 + 5, 0.9, f"{self.c}", fontsize=12, ha='center', va='center')
        plt.text(0.8 + 5, 0.9, f"{self.c * 2}", fontsize=12, ha='center', va='center')
        plt.text(-0.8 + 5, -0.9, f"{self.c * 3}", fontsize=12, ha='center', va='center')
        plt.text(0.8 + 5, -0.9, "?", fontsize=12, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q286:
    # find the missing numbers
    def __init__(self):
        self.a = rd.randint(10, 99)
        self.b = rd.randint(10, 99)
        self.c = rd.randint(10, 99)
        self.central = max(self.a + self.b, self.a + self.c, self.b + self.c) + rd.randint(1, 99)
        self.ab = self.central - self.a - self.b
        self.ac = self.central - self.a - self.c
        self.bc = self.central - self.b - self.c
        self.query = "Find the missing numbers so that the sum of numbers on the each side equal to the number in the " \
                     "center. The answer should be in the order of the missing number on the left side, the missing " \
                     "number on the bottom side, and the missing number on the right side, following the format like " \
                     "'1, 2, 3' "
        self.answer = f"{self.ab}, {self.bc}, {self.ac}"
        self.answer_type = "text"
        self.subject = "puzzle test"
        self.level = "elementary school"

    def draw(self, num):
        r = 1
        plt.xlim(-7 * 1.1, 7 * 1.1)
        plt.ylim(-7 * 1.1, 7 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        plt.plot([-4, -1], [-5 / 2 * np.sqrt(3), -5 / 2 * np.sqrt(3)], color="black", linewidth=1)
        plt.plot([4, 1], [-5 / 2 * np.sqrt(3), -5 / 2 * np.sqrt(3)], color="black", linewidth=1)
        plt.plot([-5, 0], [-5 / 2 * np.sqrt(3), 5 / 2 * np.sqrt(3)], color="black", linewidth=1, zorder=1)
        plt.plot([5, 0], [-5 / 2 * np.sqrt(3), 5 / 2 * np.sqrt(3)], color="black", linewidth=1, zorder=1)
        circle = Circle((0, -5 / 2 * np.sqrt(3)), r, edgecolor="black", facecolor="white", fill=True)
        circle2 = Circle((-5, -5 / 2 * np.sqrt(3)), r, edgecolor="black", facecolor="white", fill=True)
        circle3 = Circle((5, -5 / 2 * np.sqrt(3)), r, edgecolor="black", facecolor="white", fill=True)
        circle4 = Circle((0, 5 / 2 * np.sqrt(3)), r, edgecolor="black", facecolor="white", fill=True)
        circle5 = Circle((-5 / 2, 0), r, edgecolor="black", facecolor="white", fill=True)
        circle6 = Circle((5 / 2, 0), r, edgecolor="black", facecolor="white", fill=True)
        ax.add_patch(circle)
        ax.add_patch(circle2)
        ax.add_patch(circle3)
        ax.add_patch(circle4)
        ax.add_patch(circle5)
        ax.add_patch(circle6)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(0, -2, f"{self.central}", fontsize=12, ha='center', va='center')
        plt.text(0, 5 / 2 * np.sqrt(3), f"{self.a}", fontsize=12, ha='center', va='center')
        plt.text(0, -5 / 2 * np.sqrt(3), "?", fontsize=12, ha='center', va='center')
        plt.text(-5 / 2, 0, "?", fontsize=12, ha='center', va='center')
        plt.text(5 / 2, 0, "?", fontsize=12, ha='center', va='center')
        plt.text(-5, -5 / 2 * np.sqrt(3), f"{self.b}", fontsize=12, ha='center', va='center')
        plt.text(5, -5 / 2 * np.sqrt(3), f"{self.c}", fontsize=12, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q287:
    # rotation, flip, dilation
    def __init__(self):
        self.a = chr(rd.randint(97, 122))
        self.query = "What type of transformation of the left letter was applied to become the right letter? " \
                     "choice: (A) reduction (B) rotation (C) enlargement"
        self.answer = rd.choice(["A", "B", "C"])
        self.answer_type = "multiple choice"
        self.subject = "plane geometry"
        self.level = "elementary school"

    def draw(self, num):
        a = self.a
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.text(-4, 0, a, fontsize=80, ha='center', va='center', color='purple')
        if self.answer == "B":
            plt.text(3, 0, a, fontsize=80, ha='center', va='center', color='purple', rotation=90)
        elif self.answer == "A":
            plt.text(3, 0, a, fontsize=40, ha='center', va='center', color='purple')
        elif self.answer == "C":
            plt.text(3, 0, a, fontsize=100, ha='center', va='center', color='purple')
        plt.text(-2, -1, r'$\rightarrow$', fontsize=45)
        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
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


class Q288:
    # stem and leaf graph 1
    def __init__(self):
        self.data = [rd.randint(30, 99) for i in range(0, 20)]
        self.query = "The diagram shows weights of students. How many students are at least 40 kilograms weight but " \
                     "less than 70 kilograms weight? "
        self.answer = 0
        for num in self.data:
            if 40 <= num < 70:
                self.answer += 1
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.gcf().set_size_inches(4, 4)
        data = self.data
        i = 1
        j = 0.0
        for k, g in groupby(sorted(data), key=lambda x: math.floor(x / 10)):
            lst = map(str, [d % 10 for d in list(g)])
            plt.text(-0.7, i, str(k), fontsize=12)
            for s in lst:
                plt.text(j, i, s, fontsize=12)
                j += 0.35
            i -= 0.5
            j = 0.0
        plt.vlines(-0.2, -3, 2, color="lightblue", linewidth=1.5)
        plt.hlines(1.5, -2, 2, color="lightblue", linewidth=1.5)
        plt.hlines(2, -2, 2, color="lightblue", linewidth=1.5)
        plt.text(-0.7, 1.7, "Stem", fontsize=12, ha='center', va='center')
        plt.text(0.3, 1.7, "Leaf", fontsize=12, ha='center', va='center')
        plt.text(0, 2.3, "Student Weights (kg)", fontsize=12, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q289:
    # stem and leaf graph 2
    def __init__(self):
        self.data = [rd.randint(10, 99) for i in range(0, 20)]
        self.query = "The diagram shows Exam score of students. What is the average score of this exam?"
        self.answer = sum(self.data) / 20
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.gcf().set_size_inches(4, 4)
        data = self.data
        i = 1
        j = 0.0
        for k, g in groupby(sorted(data), key=lambda x: math.floor(x / 10)):
            lst = map(str, [d % 10 for d in list(g)])
            plt.text(-0.7, i, str(k), fontsize=12)
            for s in lst:
                plt.text(j, i, s, fontsize=12)
                j += 0.35
            i -= 0.5
            j = 0.0
        plt.vlines(-0.2, -3, 2, color="violet", linewidth=1.5)
        plt.hlines(1.5, -2, 2, color="violet", linewidth=1.5)
        plt.hlines(2, -2, 2, color="violet", linewidth=1.5)
        plt.text(-0.7, 1.7, "Stem", fontsize=12, ha='center', va='center')
        plt.text(0.3, 1.7, "Leaf", fontsize=12, ha='center', va='center')
        plt.text(0, 2.3, "Exam Score", fontsize=12, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q290:
    # stem and leaf graph 3
    def __init__(self):
        self.data = [rd.randint(10, 99) for i in range(0, 20)]
        self.rd = rd.randint(10, 99)
        self.query = f"The diagram shows height of buildings in town. How many buildings are exactly {self.rd} meters?"
        self.answer = 0
        for num in self.data:
            if num == self.rd:
                self.answer += 1
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.gcf().set_size_inches(4, 4)
        data = self.data
        i = 1
        j = 0.0
        for k, g in groupby(sorted(data), key=lambda x: math.floor(x / 10)):
            lst = map(str, [d % 10 for d in list(g)])
            plt.text(-0.7, i, str(k), fontsize=12)
            for s in lst:
                plt.text(j, i, s, fontsize=12)
                j += 0.35
            i -= 0.5
            j = 0.0
        plt.vlines(-0.2, -3, 2, color="lightgreen", linewidth=1.5)
        plt.hlines(1.5, -2, 2, color="lightgreen", linewidth=1.5)
        plt.hlines(2, -2, 2, color="lightgreen", linewidth=1.5)
        plt.text(-0.7, 1.7, "Stem", fontsize=12, ha='center', va='center')
        plt.text(0.3, 1.7, "Leaf", fontsize=12, ha='center', va='center')
        plt.text(0, 2.3, "Height of buildings (meters)", fontsize=12, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q291:
    # stem and leaf plot 4
    def __init__(self):
        self.data = rd.sample(list(range(0, 99)), 20)
        index = 0
        for i in range(0, 20):
            if self.data[i] > self.data[index]:
                index = i
        self.query = "The diagram shows Exam score of students. What is the student No. of the student who get the " \
                     "highest score? "
        self.answer = index
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        plt.stem(self.data)
        plt.yticks([0, 20, 40, 60, 80, 100])
        plt.xticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
        plt.title("Exam scores")
        plt.xlabel("Student No")
        plt.ylabel("Score")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q292:
    # stem and leaf plot 5
    def __init__(self):
        self.data = [3 * rd.randint(10, 33) for i in range(0, 20)]
        self.query = "The diagram shows weights of students. How many students are at least 40 kilograms weight but " \
                     "less than 70 kilograms weight? "
        self.answer = 0
        for num in self.data:
            if 40 <= num < 70:
                self.answer += 1
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        plt.stem(self.data)
        plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        plt.xticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
        plt.title("Student Weights (kg)")
        plt.xlabel("Student No", fontsize=12)
        plt.ylabel("Weight", fontsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q293:
    # stem and leaf plot 6
    def __init__(self):
        self.data = [rd.randint(10, 95) for i in range(0, 20)]
        self.rd = rd.choice([20, 40, 60, 80])
        self.query = f"The diagram shows height of buildings in town. How many buildings are exactly {self.rd} meters?"
        self.answer = 0
        for num in self.data:
            if num == self.rd:
                self.answer += 1
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        plt.stem(self.data)
        plt.yticks([0, 20, 40, 60, 80, 100])
        plt.xticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
        for i, j in zip(range(0, 20), self.data):
            plt.text(i, j+1, f'{j}', ha='center', va='bottom', fontsize=12)
        plt.title("Height of buildings (meters)")
        plt.xlabel("buildings", fontsize=12)
        plt.ylabel("Height", fontsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q294:
    # ternary plot 1
    def __init__(self):
        self.a = rd.randint(0, 10)
        self.b = rd.randint(0, 10 - self.a)
        self.c = 10 - self.a - self.b
        self.query = "The ternary plot shows the three-sector model of an unknown country. What is the percentage of " \
                     "primary sector in the economy of this country . "
        self.answer = self.a / 10
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        ax = plt.subplot(projection="ternary", ternary_sum=100.0)

        ax.set_tlabel("Primary Sector (%)")
        ax.set_llabel("Secondary Sector (%)")
        ax.set_rlabel("Tertiary Sector (%)")
        ticks = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        ax.taxis.set_ticks(ticks)
        ax.laxis.set_ticks(ticks)
        ax.raxis.set_ticks(ticks)
        positions = ['corner', 'tick1']
        for i, position in enumerate(positions):
            ax.taxis.set_label_position(position)
            ax.laxis.set_label_position(position)
            ax.raxis.set_label_position(position)
        ax.scatter(self.a / 10, self.b / 10, self.c / 10)
        ax.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q295:
    # ternary plot 2
    def __init__(self):
        self.lst = np.random.random(3)
        self.lst /= self.lst.sum()
        self.query = "The ternary plot shows the three-sector model of an unknown country. Which sector contributes " \
                     "most to the economy of this country?  choice: (A) Primary Sector (B) Secondary Sector (C) " \
                     "Tertiary Sector "
        maximum = max(self.lst)
        if self.lst[0] == maximum:
            self.answer = "A"
        elif self.lst[1] == maximum:
            self.answer = "B"
        else:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        ax = plt.subplot(projection="ternary", ternary_sum=100.0)

        ax.set_tlabel("Primary Sector (%)")
        ax.set_llabel("Secondary Sector (%)")
        ax.set_rlabel("Tertiary Sector (%)")
        ticks = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        ax.taxis.set_ticks(ticks)
        ax.laxis.set_ticks(ticks)
        ax.raxis.set_ticks(ticks)
        positions = ['corner', 'tick1']
        for i, position in enumerate(positions):
            ax.taxis.set_label_position(position)
            ax.laxis.set_label_position(position)
            ax.raxis.set_label_position(position)
        ax.scatter(self.lst[0], self.lst[1], self.lst[2], color="purple")
        ax.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q296:
    # slope field 1
    def __init__(self):
        self.a = rd.choice([-3, -1 / 3, -2, -1 / 2, -1, 1, 1 / 2, 2, 1 / 3, 3])
        self.b = rd.randint(0, 3)
        self.c = rd.randint(-2, 2)
        self.query = f"According to the slope field, dx/dy = a * x^{self.b}, find the value of 'a'."
        self.answer = self.a
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        a = self.a
        b = self.b
        c = self.c
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([-3, -2, -1, 1, 2, 3])
        plt.yticks([-3, -2, -1, 1, 2, 3])
        x, y = np.meshgrid(np.arange(-3, 3, .5), np.arange(-3, 3, .5))
        x2 = np.linspace(-3, 3, 100)
        y2 = a * x2 ** (b + 1) / (b + 1) + c
        plt.plot(x2, y2, color="blue", linewidth=1)
        u = 1
        v = a * x ** b
        plt.quiver(x, y, u, v, headwidth=0, headlength=0, headaxislength=0, scale=60, facecolor='lightblue')
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


class Q297:
    # slope field 2
    def __init__(self):
        self.a = rd.choice([-3, -2, -1, 1, 2, 3])
        self.b = rd.randint(-3, 3)
        self.query = f"According to the slope field, dx/dy = a * sin(x), find the value of 'a'."
        self.answer = self.a
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        a = self.a
        b = self.b
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([-3, -2, -1, 1, 2, 3])
        plt.yticks([-3, -2, -1, 1, 2, 3])
        x, y = np.meshgrid(np.arange(-3, 3, .5), np.arange(-3, 3, .5))
        x2 = np.linspace(-3, 3, 100)
        y2 = -a * np.cos(x2) + b
        plt.plot(x2, y2, color="blue", linewidth=1)
        u = 1
        v = a * np.sin(x)
        plt.quiver(x, y, u, v, headwidth=0, headlength=0, headaxislength=0, scale=60, facecolor='lightblue')
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


class Q298:
    # slope field 3
    def __init__(self):
        self.a = rd.choice([-3, -2, -1, 1, 2, 3])
        self.b = rd.randint(-3, 3)
        self.query = f"Which differential equation generates the slope field? (A) {self.a}x + {self.b}y (B) {self.a}x - {abs(self.b)}y (C) {self.b}y - {abs(self.a)}x (D) {self.a}x (E) -{abs(self.a)}x - {abs(self.b)}y "
        if self.a > 0 and self.b > 0:
            self.answer = "A"
        elif self.a > 0 and self.b < 0:
            self.answer = "B"
        elif self.a < 0 and self.b > 0:
            self.answer = "C"
        elif self.b == 0:
            self.answer = "D"
        elif self.a < 0 and self.b < 0:
            self.answer = "E"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        a = self.a
        c = self.b
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([-3, -2, -1, 1, 2, 3])
        plt.yticks([-3, -2, -1, 1, 2, 3])
        x, y = np.meshgrid(np.arange(-3, 3, .5), np.arange(-3, 3, .5))
        u = 1
        v = a * x + c * y
        plt.quiver(x, y, u, v, headwidth=0, headlength=0, headaxislength=0, scale=60, facecolor='lightblue')
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


class Q299:
    # slope field 4
    def __init__(self):
        self.a = rd.randint(-5, 5)
        self.b = rd.randint(-5, 5)
        if self.a == 0 and self.b != 0:
            self.a = rd.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        if self.b == 0 and self.a != 0:
            self.b = rd.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        self.query = f"Which differential equation generates the slope field? choice: (A) x/y " \
                     f"(B) (x + {self.a})/(y + {self.b}) (C) (x - {abs(self.a)})/(y + {self.b}) " \
                     f"(D) (x - {abs(self.a)})/(y - {abs(self.b)}) (E) (x + {self.a})/(y - {abs(self.b)}) "
        if self.a == 0 and self.b == 0:
            self.answer = "A"
        elif self.a > 0 and self.b > 0:
            self.answer = "B"
        elif self.a < 0 and self.b > 0:
            self.answer = "C"
        elif self.a < 0 and self.b < 0:
            self.answer = "D"
        elif self.a > 0 and self.b < 0:
            self.answer = "E"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        a = self.a
        b = self.b
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        x, y = np.meshgrid(np.arange(-6, 6, .5), np.arange(-6, 6, .5))
        u = 1
        v = (x + a) / (y + b)
        plt.quiver(x, y, u, v, headwidth=0, headlength=0, headaxislength=0, scale=60, facecolor='cyan')
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


class Q300:
    # slope field 5
    def __init__(self):
        self.a = rd.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        self.query = f"What is the general solution to the differential equation that generated the slope field?  " \
                     f"choice: (A) x = {self.a}cos(y) + C (B) y = {abs(self.a)}cos(x) + C (C) y = -{abs(self.a)}cos(" \
                     f"x) + C (D) y = {self.a}sin(x) + C "
        self.answer = "D"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        a = self.a
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        x, y = np.meshgrid(np.arange(-6, 6, .5), np.arange(-6, 6, .5))
        u = 1
        v = a * np.cos(x)
        plt.quiver(x, y, u, v, headwidth=0, headlength=0, headaxislength=0, scale=60, facecolor='cyan')
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


