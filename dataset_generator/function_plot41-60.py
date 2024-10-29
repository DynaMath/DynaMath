import math
import shutil
import networkx as nx
import os.path
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import pandas as pd
from plottable import Table
from matplotlib.patches import *


class Q41:
    # parallelogram perimeter
    def __init__(self):
        self.short = rd.randint(4, 10)
        self.long = self.short * 2 + rd.randint(-1, 3)
        self.query = "What is the perimeter of this parallelogram?"
        self.answer = self.long * 2 + self.short * 2
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
                             facecolor="coral")
        ax.add_patch(square)
        plt.text(-3, 0.2, f"{self.short}ft", fontsize=10)
        plt.text(-0.2, 1.2, f"{self.long}ft", fontsize=10)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q42:
    # Connected Graph
    def __init__(self):
        self.G = nx.Graph()
        self.G.add_nodes_from("ABCDEFG")
        self.pos = {
            "A": (0.5, 1),
            "B": (1, 0),
            "C": (0, 1),
            "D": (1, 1),
            "E": (0, 2),
            "F": (1, 2),
            "G": (0, 0)
        }
        self.edge = 0
        for node in list(self.G.nodes)[1:]:
            tester = rd.randint(1, 6)
            if tester % 2 == 0:
                self.G.add_edge(node, "A")
                self.edge += 1
        self.query = "Is the graph shown connected? choice: (A) Yes (B) No"
        if self.edge == 6:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color='black')
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q43:
    # fraction of blue
    def __init__(self):
        self.query = "What fraction of the shape is azure?"
        self.r = rd.randint(1, 12) * 30
        self.answer = self.r / 360
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
        wedgeA = Wedge((0, 0), 2, 0, self.r, color="azure")
        ax.add_patch(wedgeA)
        wedge1 = Wedge((0, 0), 2, 0, 30, fill=False, edgecolor="black")
        wedge2 = Wedge((0, 0), 2, 30, 60, fill=False, edgecolor="black")
        wedge3 = Wedge((0, 0), 2, 60, 90, fill=False, edgecolor="black")
        wedge4 = Wedge((0, 0), 2, 90, 120, fill=False, edgecolor="black")
        wedge5 = Wedge((0, 0), 2, 120, 150, fill=False, edgecolor="black")
        wedge6 = Wedge((0, 0), 2, 150, 180, fill=False, edgecolor="black")
        wedge7 = Wedge((0, 0), 2, 180, 210, fill=False, edgecolor="black")
        wedge8 = Wedge((0, 0), 2, 210, 240, fill=False, edgecolor="black")
        wedge9 = Wedge((0, 0), 2, 240, 270, fill=False, edgecolor="black")
        wedge10 = Wedge((0, 0), 2, 270, 300, fill=False, edgecolor="black")
        wedge11 = Wedge((0, 0), 2, 300, 330, fill=False, edgecolor="black")
        wedge12 = Wedge((0, 0), 2, 330, 360, fill=False, edgecolor="black")
        circle = Circle((0, 0), 2, color="black", fill=False)
        ax.add_patch(circle)
        ax.add_patch(wedge1)
        ax.add_patch(wedge2)
        ax.add_patch(wedge3)
        ax.add_patch(wedge4)
        ax.add_patch(wedge5)
        ax.add_patch(wedge6)
        ax.add_patch(wedge7)
        ax.add_patch(wedge8)
        ax.add_patch(wedge9)
        ax.add_patch(wedge10)
        ax.add_patch(wedge11)
        ax.add_patch(wedge12)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q44:
    # find the area of green rectangle
    def __init__(self):
        self.v = rd.randint(2, 5)
        self.h = rd.randint(2, 5)
        self.peri = 2 * self.v + 2 * self.h
        self.area = 2 * self.v * self.v + 2 * self.h * self.h
        self.query = f"The perimeter of green rectangle is {self.peri} cm.There is a azure square on each side of " \
                     f"green rectangle, with each side of the rectangle being the side length of one of the squares. " \
                     f"Given that the sum of the areas of the four squares is {self.area} cm², find the area of the " \
                     f"green rectangle. "
        self.answer = self.v * self.h
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(-7.5, 10 * 1.05)
        plt.ylim(-7.5, 10 * 1.05)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        x = self.h
        y = self.v
        s1 = plt.Polygon([(0, 0), (x, 0), (x, y), (0, y)], closed=True, fill=True, edgecolor='black', facecolor='green')
        s2 = plt.Polygon([(x, 0), (x, y), (x + y, y), (x + y, 0)], closed=True, fill=True, edgecolor='black',
                         facecolor='azure')
        s3 = plt.Polygon([(-y, 0), (-y, y), (0, y), (0, 0)], closed=True, fill=True, edgecolor='black',
                         facecolor='azure')
        s4 = plt.Polygon([(0, y), (x, y), (x, y + x), (0, y + x)], closed=True, fill=True, edgecolor='black',
                         facecolor='azure')
        s5 = plt.Polygon([(0, -x), (x, -x), (x, 0), (0, 0)], closed=True, fill=True, edgecolor='black',
                         facecolor='azure')
        ax.add_patch(s1)
        ax.add_patch(s2)
        ax.add_patch(s3)
        ax.add_patch(s4)
        ax.add_patch(s5)
        ax.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q45:
    # find triangle area 2
    def __init__(self):
        self.BD = rd.randint(2, 3)
        self.DC = 1
        self.ACD = rd.randint(10, 15)
        self.query = f"In △ABC, D is a point on BC, and BD={self.BD}, DC={self.DC}, and the area of △ACD " \
                     f"is {self.ACD}. What is the area of △ABC?"
        self.answer = (self.DC + self.BD) * self.ACD
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q45temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q45temp.png"), dest_image_path)


class Q46:
    # limit1
    def __init__(self):
        self.a = rd.randint(-3, 3)
        self.b = rd.randint(-3, 3)
        self.c = rd.randint(-3, 3)
        self.r = rd.randint(-1, 1)
        self.query = f"what is the limit of this function as x approches {self.r}?"
        self.answer = self.a * self.r ** 3 + self.b * self.r ** 2 + self.c * self.r
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = self.a * x ** 3 + self.b * x ** 2 + self.c * x
        plt.plot(x, cubic, color='blue', linewidth=1.5)
        circle = Circle((self.r, self.answer), 0.2, color="gray", fill=True)
        ax = plt.gca()
        ax.add_patch(circle)
        plt.xlim(-11 * 1.1, 11 * 1.1)
        plt.ylim(-11 * 1.1, 11 * 1.1)

        plt.xticks([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], fontsize=12)
        plt.yticks([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], fontsize=12)
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


class Q47:
    # find the radius of circle
    def __init__(self):
        self.r = rd.randint(1, 6)
        self.query = "What is the radius of this circle?"
        self.answer = self.r
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)
        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        circle = Circle((0, 0), self.r, color="blue", fill=False)
        ax.add_patch(circle)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q48:
    # Table3
    def __init__(self):
        self.score = np.random.randint(1, 11, 4)
        self.num = rd.randint(1, 4)
        self.query = f"How much money does Hunter need to buy {self.num} calendars?"
        self.answer = self.score[2] * self.num
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "elementary school"

    def draw(self, num):
        data = {
            'products': ['notebook', 'map', 'calendar', 'pen'],
            'price': self.score
        }
        df = pd.DataFrame(data, columns=['products', 'price'])
        df.set_index('products', inplace=True)
        Table(df, textprops={
                  'fontsize': 22,
              })
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q49:
    # find triangle area 2
    def __init__(self):
        self.a = rd.randint(120, 150)
        self.query = f"In the parallelogram ABCD, ∠A={self.a}. What is the measure of ∠C?"
        self.answer = self.a
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q49temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q49temp.png"), dest_image_path)


class Q50:
    # grow faster
    def __init__(self):
        self.a = rd.choice([1 / 2, 3 / 2, 5 / 2, 7 / 2])
        self.b = rd.randint(1, 4)
        while abs(self.a - self.b) < 1:
            self.a = rd.choice([1 / 2, 3 / 2, 5 / 2, 7 / 2])
        self.query = "Which function grows faster? choice: (A) Orange (B) Blue"
        if self.a > self.b:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        func1 = self.a * x
        func2 = self.b * x
        plt.plot(x, func1, color='Orange', linewidth=1.5)
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


class Q51:
    # easy matrix 2
    def __init__(self):
        self.col1 = np.random.randint(0, 2, 5)
        self.col2 = np.random.randint(0, 2, 5)
        self.col3 = np.random.randint(0, 2, 5)
        self.col4 = np.random.randint(0, 2, 5)
        self.col5 = np.random.randint(0, 2, 5)
        self.sum = sum(self.col1) + sum(self.col2) + sum(self.col3) + sum(self.col4) + sum(self.col5)
        if self.sum < 20:
            self.query = "How many black squares need to be coloured in white, so that there are exactly fourth as " \
                         "many black squares as there are white squares? "
            self.answer = 20 - self.sum
        else:
            self.query = "How many white squares need to be coloured in black, so that there are exactly fourth as " \
                         "many black squares as there are white squares?"
            self.answer = self.sum - 20
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def draw(self, num):
        mat = np.array([self.col1, self.col2, self.col3, self.col4, self.col5])
        plt.imshow(mat, cmap="gray")
        constant_a = 0.5
        constant_b = 1.5
        plt.vlines(constant_a, -0.5, 4.5, colors="gray")
        plt.vlines(constant_b, -0.5, 4.5, colors="gray")
        plt.vlines(2.5, -0.5, 4.5, colors="gray")
        plt.vlines(3.5, -0.5, 4.5, colors="gray")
        plt.hlines(constant_a, -0.5, 4.5, colors="gray")
        plt.hlines(constant_b, -0.5, 4.5, colors="gray")
        plt.hlines(2.5, -0.5, 4.5, colors="gray")
        plt.hlines(3.5, -0.5, 4.5, colors="gray")
        plt.xticks([])
        plt.yticks([])
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q52:
    # uniform continuity
    def __init__(self):
        self.constant = rd.randint(-3, 3)
        self.query = "Is this function uniform continuous on the interval [-3, 3]? choice: (A) Yes (B) No"
        self.answer_type = "multiple choice"
        if self.constant < 0:
            self.answer = "B"
        else:
            self.answer = "A"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200, endpoint=True)
        function = x ** self.constant
        plt.plot(x, function, color='purple', linewidth=1.5)

        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-3, -2, -1, 1, 2, 3])
        plt.yticks([-3, -2, -1, 1, 2, 3])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q53:
    # area of ring
    def __init__(self):
        self.a = rd.randint(3, 5)
        self.b = self.a + rd.randint(1, 2)
        self.query = "What is the area of blue ring?"
        self.answer = self.b * self.b * np.pi - self.a * self.a * np.pi
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        random_a = self.a
        random_b = self.b
        plt.xlim(-7 * 1.1, 7 * 1.1)
        plt.ylim(-7 * 1.1, 7 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        circle = Circle((0, 0), random_a, edgecolor="black", facecolor="white", fill=True)
        circle2 = Circle((0, 0), random_b, edgecolor="black", facecolor="azure", fill=True)
        ax.add_patch(circle2)
        ax.add_patch(circle)
        plt.text(1, -1, f'r = {random_a}', fontsize=11)
        plt.text(-2, -1, f'R = {random_b}', fontsize=11)
        plt.hlines(0, 0, random_a, colors="black")
        plt.hlines(0, -random_b, 0, colors="black")
        plt.scatter(0, 0, color="black")
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q54:
    # symmetric/even function
    def __init__(self):
        self.constant = rd.randint(-4, 4)
        self.query = "Is this function symmetric about the y-axis? choice: (A) Yes (B) No"
        self.answer_type = "multiple choice"
        if self.constant % 2 != 0 and self.constant != 0:
            self.answer = "B"
        else:
            self.answer = "A"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200, endpoint=True)
        function = x ** self.constant
        plt.plot(x, function, color='orange', linewidth=1.5)

        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-3, -2, -1, 1, 2, 3])
        plt.yticks([-3, -2, -1, 1, 2, 3])
        plt.tick_params(axis='both', which='major', labelsize=14)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q55:
    # find angle in circle 1
    def __init__(self):
        self.dcb = rd.choice([15, 20, 25, 30, 35, 40])
        self.ocd = 45 + self.dcb
        self.query = "Given the diagram, a circle with its center at the origin O intersects the x-axis at points A " \
                     "and B and intersects the positive half of the y-axis at point C. D is a point on the circle O " \
                     f"located in the first quadrant. If ∠DAB={self.dcb}, then what is the measure of ∠OCD?"
        self.answer = self.ocd
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q55temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q55temp.png"), dest_image_path)


class Q56:
    # parabola intersects
    def __init__(self):
        self.a = rd.randint(-3, 3)
        self.b = rd.randint(-3, 3)
        self.c = rd.randint(-3, 3)
        self.a2 = rd.randint(-3, 3)
        self.b2 = rd.randint(-3, 3)
        self.c2 = rd.randint(-3, 3)
        self.delta = (self.b - self.b2) * (self.b - self.b2) - 4 * (self.a - self.a2) * (self.c - self.c2)
        self.query = "Do the two functions intersect? choice: (A) Yes (B) No"
        if self.delta < 0:
            self.answer = "B"
        else:
            self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200, endpoint=True)
        square = self.a * x ** 2 + self.b * x + self.c
        square2 = self.a2 * x ** 2 + self.b2 * x + self.c2
        plt.plot(x, square, color='red', linewidth=2.5)
        plt.plot(x, square2, color='blue', linewidth=2.5)
        plt.xlim(-10 * 1.1, 10 * 1.1)
        plt.ylim(-10 * 1.1, 10 * 1.1)

        plt.xticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])

        plt.yticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
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


class Q57:
    # find area enclosed by rectangles
    def __init__(self):
        self.m = rd.randint(1, 10)
        self.n = 3 * self.m + rd.randint(1, 3)
        self.query = "What is the area of the part enclosed by four rectangles?"
        self.answer = (self.n - self.m) * (self.n - self.m)
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
        square1 = plt.Polygon([(-1, 1), (-1, 2), (2, 2), (2, 1)], closed=True, fill=True, edgecolor='black',
                              facecolor='azure')
        square2 = plt.Polygon([(1, -1), (1, -2), (-2, -2), (-2, -1)], closed=True, fill=True, edgecolor='black',
                              facecolor='azure')
        square3 = plt.Polygon([(-1, -1), (-1, 2), (-2, 2), (-2, -1)], closed=True, fill=True, edgecolor='black',
                              facecolor='azure')
        square4 = plt.Polygon([(1, 1), (1, -2), (2, -2), (2, 1)], closed=True, fill=True, edgecolor='black',
                              facecolor='azure')
        ax.add_patch(square1)
        ax.add_patch(square2)
        ax.add_patch(square3)
        ax.add_patch(square4)
        plt.text(2.4, -1.5, f'{self.n}', fontsize=11)
        plt.text(-1.5, 2.4, f'{self.m}', fontsize=11)
        plt.text(0.3, 2.4, f'{self.n}', fontsize=11)
        plt.text(-0.5, -2.8, f'{self.n}', fontsize=11)
        plt.text(1.5, -2.8, f'{self.m}', fontsize=11)
        plt.text(2.4, 1.5, f'{self.m}', fontsize=11)
        plt.text(-2.8, -1.5, f'{self.m}', fontsize=11)
        plt.text(-2.8, 0, f'{self.n}', fontsize=11)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q58:
    # find asymptote 1:
    def __init__(self):
        self.a = rd.randint(-4, 4)
        self.query = "What is the asymptote of the function shown in image?"
        self.answer = f"y = {self.a}"
        self.answer_type = "text"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = 2 ** x + self.a
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


class Q59:
    # select poker 1
    def __init__(self):
        self.m = rd.choice(["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])
        self.s = rd.choice([r'$\clubsuit$', r'$\spadesuit$'])
        self.query = "According to image, a card is randomly selected from a standard 52-card deck. Find the " \
                     "probability that the next card selected after selecting this card from the deck is a heart."
        self.answer = 13/51
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        square1 = plt.Polygon([(-1.5, 2), (-1.5, -2), (1.5, -2), (1.5, 2)], closed=True, fill=True, edgecolor='black',
                              facecolor='white')
        ax.add_patch(square1)
        plt.text(-1.3, 1.5, f'{self.m}', fontsize=14, weight="bold")
        plt.text(-1.35, 1.05, f'{self.s}', fontsize=14, weight="bold")
        plt.text(0.9, -1.6, f'{self.m}', fontsize=14, weight="bold", rotation=180)
        plt.text(0.95, -1.15, f'{self.s}', fontsize=14, weight="bold", rotation=180)
        plt.text(-0.55, -0.5, f'{self.s}', fontsize=40, weight="bold")
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q60:
    # find the surface area of the rectangular prism
    def __init__(self):
        self.a = rd.randint(3, 8)
        self.b = self.a + rd.randint(1, 3)
        self.c = self.b + rd.randint(1, 2)
        self.query = "Find the surface area of the rectangular prism."
        self.answer = 2 * self.a * self.b + 2 * self.a * self.c + 2 * self.b * self.c
        self.answer_type = "float"
        self.subject = "solid geometry"
        self.level = "high school"

    def draw(self, num):
        fig = plt.figure()
        fig.set_size_inches(4, 4, 4)
        x, y, z = np.indices((2, 2, 2))
        filled = np.ones((1, 1, 1))
        ax = fig.add_subplot(projection='3d')
        ax.voxels(x, y, z, filled=filled, color='orange', edgecolor='black')
        ax.text(0.3, 0, -0.3, f"{self.c}ft", fontsize=12)
        ax.text(0, -0.3, 0.7, f"{self.a}ft", fontsize=12)
        ax.text(-0.4, 0.8, 0.8, f"{self.b}ft", fontsize=12)
        ax.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()
