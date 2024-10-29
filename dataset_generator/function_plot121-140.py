import math
import shutil
import networkx as nx
import os.path
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.patches import *


class Q121:
    # set description
    def __init__(self):
        self.a = rd.randint(10, 90) / 10
        self.b = rd.randint(10, 90) / 10
        self.query = "Which of the following fact is true about set A and set B in image?  " \
                     "choice: (A) A ⊂ B (B) A ⊃ B (C) A ∪ B (D) A ∩ B = ∅"
        if self.a > 4 + self.b:
            self.answer = "B"
        elif self.b > 4 + self.a:
            self.answer = "A"
        elif self.a + self.b <= 4:
            self.answer = "D"
        else:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        b = self.b
        ax = plt.gca()
        plt.xlim(-10 * 1.1, 10 * 1.1)
        plt.ylim(-10 * 1.1, 10 * 1.1)
        plt.gcf().set_size_inches(6, 6)
        plt.xticks([-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        plt.yticks([-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        circleA = Circle((-2, 0), a, edgecolor="green", facecolor="white", fill=False)
        circleB = Circle((2, 0), b, edgecolor="green", facecolor="white", fill=False)
        ax.add_patch(circleA)
        ax.add_patch(circleB)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(-2.5, 0, "A", fontsize=20)
        plt.text(1.5, 0, "B", fontsize=20)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q122:
    # find the shaded part area of semicircle
    def __init__(self):
        self.a = rd.randint(2, 12)
        self.query = "In the diagram, there are three semi-circles. D is the diameter of left white semi-circle, " \
                     "and d is the diameter of the right white semi-circle. Find the area of azure part. "
        self.answer = 49 * np.pi / 2 - 1/2 * (self.a / 2) * (self.a / 2) * np.pi - 1/2 * ((14 - self.a) / 2) * ((14 - self.a) / 2) * np.pi
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
        wedge1 = Wedge((0, 0), 7, 0, 180, edgecolor="black", facecolor="azure", fill=True)
        wedge2 = Wedge((c1, 0), random_a / 2, 0, 180, edgecolor="black", facecolor="white", fill=True)
        wedge3 = Wedge((c2, 0), (14 - random_a) / 2, 0, 180, edgecolor="black", facecolor="white", fill=True)
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


class Q123:
    # perimeter of wedge
    def __init__(self):
        self.a = rd.randint(3, 15) * 10
        self.b = rd.randint(1, 10)
        self.query = "Find the perimeter of the sector of the circle with radius r."
        self.answer = self.b * 2 * np.pi * (self.a / 360) + self.b * 2
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        random_a = self.a
        b = self.b
        plt.xlim(-7 * 1.1, 7 * 1.1)
        plt.ylim(-7 * 1.1, 7 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        wedge1 = Wedge((0, 0), 7, 0, random_a, edgecolor="black", facecolor="white", fill=True)
        wedge2 = Wedge((0, 0), 0.5, 0, random_a, edgecolor="black", facecolor="white", fill=True)
        ax.add_patch(wedge1)
        ax.add_patch(wedge2)
        plt.text(0, -1, f'{random_a}°', fontsize=11)
        plt.text(5, -1, f'r = {b}', fontsize=11)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q124:
    # color of curve 2
    def __init__(self):
        self.query = "What is the purple curve? choice: (A) sigmoid function (B) tanh function (C) LeakyRelu function"
        self.choice = ["purple", "orange", "blue"]
        self.sig_color = rd.choice(self.choice)
        self.choice.remove(self.sig_color)
        self.tan_color = rd.choice(self.choice)
        self.choice.remove(self.tan_color)
        self.relu_color = rd.choice(self.choice)
        if self.sig_color == "purple":
            self.answer = "A"
        elif self.tan_color == "purple":
            self.answer = "B"
        elif self.relu_color == "purple":
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x = np.linspace(-10, 10, 1000, endpoint=True)
        sigmoid = 1 / (1 + np.exp(-x))
        tanh = np.tanh(x)
        LeakyRelu = np.maximum(0.1 * x, x)
        plt.plot(x, sigmoid, color=self.sig_color, linewidth=2.5)
        plt.plot(x, tanh, color=self.tan_color, linewidth=2.5)
        plt.plot(x, LeakyRelu, color=self.relu_color, linewidth=2.5)

        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-1 * 1.1, 1 * 1.1)

        plt.xticks([-5, 0, 5])
        plt.yticks([-1, -0.8, -0.6, -0.4, -0.2, 0.2, 0.4, 0.6, 0.8, 1])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q125:
    # quadrant 1
    def __init__(self):
        self.a = rd.choice([1, 2, 3])
        self.query = "Which quadrant this function lies?  " \
                     "choice: (A) first quadrant (B) second quadrant (C) third quadrant (D) fourth quadrant"
        self.answer = rd.choice(["A", "B", "C", "D"])
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        x = np.linspace(-10, 0, 200, endpoint=True)
        rx = np.linspace(0, 10, 200, endpoint=True)
        f1 = a * rx ** 2
        f2 = a * x ** 2
        f3 = - a * x ** 2
        f4 = - a * rx ** 2

        if self.answer == "A":
            plt.plot(rx, f1, color='lightseagreen', linewidth=2.5)
        elif self.answer == "B":
            plt.plot(x, f2, color='lightseagreen', linewidth=2.5)
        elif self.answer == "C":
            plt.plot(x, f3, color='lightseagreen', linewidth=2.5)
        elif self.answer == "D":
            plt.plot(rx, f4, color='lightseagreen', linewidth=2.5)

        plt.xlim(-5 * 1.1, 5 * 1.1)
        plt.ylim(-5 * 1.1, 5 * 1.1)
        plt.xticks([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        plt.yticks([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        plt.tick_params(axis='both', which='major', labelsize=12)
        plt.scatter(0, 0, color='black')
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q126:
    # truncated right circular cone's volume
    def __init__(self):
        self.R = rd.randint(5, 10)
        self.r = rd.randint(1, 4)
        self.h = rd.randint(4, 8)
        self.query = f"The truncated right circular cone below has a large base radius {self.R} cm and a small base radius of " \
                     f"{self.r} cm. The height of the truncated cone is {self.h} cm. What is the volume of this solid?"
        self.answer = 1/3 * np.pi * self.h * (self.R * self.R + self.r * self.r + self.R * self.r)
        self.answer_type = "float"
        self.subject = "solid geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q126temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q126temp.png"), dest_image_path)


class Q127:
    # rotation 2
    def __init__(self):
        self.choice = [0, 90, 180, 270]
        self.a1 = rd.choice(self.choice)
        self.choice.remove(self.a1)
        self.a2 = rd.choice(self.choice)
        self.choice.remove(self.a2)
        self.a3 = rd.choice(self.choice)
        self.choice.remove(self.a3)
        self.a4 = rd.choice(self.choice)
        self.query = "The \u2660 is drawn on the sheet. We turn the sheet clockwise through 90° and then turn " \
                     "counter-clockwise 180°. Which figure can we now see? choice: (A) (B) (C) (D)"
        if self.a1 == 90:
            self.answer = "A"
        elif self.a2 == 90:
            self.answer = "B"
        elif self.a3 == 90:
            self.answer = "C"
        else:
            self.answer = "D"
        self.answer_type = "multiple choice"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):

        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-5 * 1.1, 5 * 1.1)
        plt.xticks([-4, -3, -2, -1, 1, 2, 3, 4])
        plt.yticks([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(-4, 0, "(A)", fontsize=24)
        plt.text(-3.15, 0, r'$\spadesuit$', fontsize=24, rotation=self.a1)
        plt.text(-2.5, 0, r'(B)', fontsize=24)
        plt.text(-1.5, 0, r'$\spadesuit$', fontsize=24, rotation=self.a2)
        plt.text(-0.75, 0, r'(C)', fontsize=24)
        plt.text(0.25, 0, r'$\spadesuit$', fontsize=24, rotation=self.a3)
        plt.text(1.1, 0, r'(D)', fontsize=24)
        plt.text(2, 0, r'$\spadesuit$', fontsize=24, rotation=self.a4)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q128:
    # derivative 4
    def __init__(self):
        self.x = rd.randint(-4, 4)
        self.d = rd.choice([-4, -1/4, -3, -1/3, -2, -1/2, -1, 1, 1/2, 2, 1/3, 3, 1/4, 4])
        self.e = rd.choice([-3, -2, -1, 1, 2, 3])
        self.query = f"The image shows the second derivative of cubic function f(x). Is f(x) concave or convex " \
                     f"at x = {self.x}?  choice: (A) convex (B) concave (C) inflection point"
        self.v = self.d * self.x + self.e
        if self.v > 0:
            self.answer = "B"
        elif self.v < 0:
            self.answer = "A"
        elif self.v == 0:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x1 = np.linspace(-10, 10, 200, endpoint=True)
        f1 = self.d * x1 + self.e
        plt.plot(x1, f1, color='darkviolet', linewidth=1.5)
        plt.xlim(-8 * 1.1, 8 * 1.1)
        plt.ylim(-8 * 1.1, 8 * 1.1)

        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        ax = plt.gca()
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(self.x, self.d * self.x + self.e, color='green')
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q129:
    # right square pyramid volume
    def __init__(self):
        self.side = rd.randint(5, 20)
        self.h = self.side + rd.randint(-2, 2)
        self.query = "What is the volume of this azure right square pyramid?"
        self.answer = 1/3 * self.side * self.side * self.h
        self.answer_type = "float"
        self.subject = "solid geometry"
        self.level = "high school"

    def draw(self, num):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        v = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1], [0, 0, 1]])
        ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])
        verts = [[v[0], v[1], v[4]], [v[0], v[3], v[4]],
                 [v[2], v[1], v[4]], [v[2], v[3], v[4]], [v[0], v[1], v[2], v[3]]]
        ax.add_collection3d(Poly3DCollection(verts, facecolors='azure', linewidths=1, edgecolors='black', alpha=.25))
        ax.plot3D([0, 0], [0, 0], [1, -1], color='black', linestyle='dashed')
        ax.text(0, -1.5, -1, f"{self.side}", fontsize=16)
        ax.text(1.3, -0.5, -1, f"{self.side}", fontsize=16)
        ax.text(-0.6, -0.3, -1, f"h={self.h}", color='red', fontsize=16)
        ax.view_init(20)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q130:
    # right square pyramid surface area
    def __init__(self):
        self.side = rd.randint(5, 20)
        self.h = self.side + rd.randint(-2, 2)
        self.query = "What is the surface area of this pink right square pyramid?"
        self.answer = self.side * self.side + self.side * np.sqrt(4 * self.h * self.h + self.side * self.side)
        self.answer_type = "float"
        self.subject = "solid geometry"
        self.level = "high school"

    def draw(self, num):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        v = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1], [0, 0, 1]])
        ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])
        verts = [[v[0], v[1], v[4]], [v[0], v[3], v[4]],
                 [v[2], v[1], v[4]], [v[2], v[3], v[4]], [v[0], v[1], v[2], v[3]]]
        ax.add_collection3d(Poly3DCollection(verts, facecolors='lightpink', linewidths=1, edgecolors='black', alpha=.25))
        ax.plot3D([0, 0], [0, 0], [1, -1], color='black', linestyle='dashed')
        ax.text(0, -1.5, -1, f"{self.side}", fontsize=16)
        ax.text(1.3, -0.5, -1, f"{self.side}", fontsize=16)
        ax.text(-0.6, -0.3, -1, f"h={self.h}", color='blue', fontsize=16)
        ax.view_init(20)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q131:
    # cauchy theorem
    def __init__(self):
        self.r = rd.randint(1, 4)
        self.c = rd.randint(2, 100)
        self.query = f"f(z) = {self.c}, C is the purple circle shown in the image. Find ∫cf(z)dz."
        self.answer = 0
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([-4, -3, -2, -1, 1, 2, 3, 4])
        plt.yticks([-4, -3, -2, -1, 1, 2, 3, 4], ["-4i", "-3i", "-2i", "-i", "i", "2i", "3i", "4i"])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        circle = Circle((0, 0), self.r, color="violet", fill=False)
        ax.add_patch(circle)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(self.r - 0.15, 0, r'$\blacktriangledown$', fontsize=12, color='darkviolet')
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q132:
    # symmetry of point 1
    def __init__(self):
        self.x = rd.randint(-6, 6)
        self.y = rd.randint(-6, 6)
        self.ry = -self.y
        self.query = "If the black point is reflected in x-axis, what are the coordinates of its image? Please answer " \
                     "in the form (_, _) "
        self.answer = f"({self.x}, {self.ry})"
        self.answer_type = "text"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
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
        plt.scatter(self.x, self.y, color='black')
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q133:
    # symmetry of point 2
    def __init__(self):
        self.x = rd.randint(-6, 6)
        self.y = rd.randint(-6, 6)
        self.rx = -self.x
        self.query = "If the red point is reflected in y-axis, what are the coordinates of its image? Please answer " \
                     "in the form (_, _) "
        self.answer = f"({self.rx}, {self.y})"
        self.answer_type = "text"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.tick_params(axis='both', which='major', labelsize=12)
        plt.scatter(self.x, self.y, color='red')
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q134:
    # symmetry of point 3
    def __init__(self):
        self.x = rd.randint(-6, 6)
        self.y = rd.randint(-6, 6)
        self.rx = -self.x
        self.ry = -self.y
        self.query = "If the blue point is reflected about the origin, what are the coordinates of its image? Please " \
                     "answer in the form (_, _) "
        self.answer = f"({self.rx}, {self.ry})"
        self.answer_type = "text"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(self.x, self.y, color='blue')
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q135:
    # distance between two point
    def __init__(self):
        self.x = rd.randint(1, 6)
        self.y = rd.randint(-6, 6)
        self.rx = rd.randint(-6, 0)
        self.ry = rd.randint(-6, 6)
        self.query = "Find the distance between point A and point B."
        self.answer = np.sqrt((self.x - self.rx) * (self.x - self.rx) + (self.y - self.ry) * (self.y - self.ry))
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(self.x, self.y, color='blue')
        plt.scatter(self.rx, self.ry, color='blue')
        plt.plot([self.rx, self.x], [self.ry, self.y], color='blue')
        plt.text(self.rx, self.ry + 0.5, "A", fontsize=14)
        plt.text(self.x, self.y + 0.5, "B", fontsize=14)
        plt.tick_params(axis='both', which='major', labelsize=12)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q136:
    # shortest path 1
    def __init__(self):
        self.SA = rd.randint(1, 20)
        self.SB = rd.randint(1, 20)
        self.AE = rd.randint(1, 20)
        self.EF = rd.randint(1, 20)
        self.FG = rd.randint(1, 20)
        self.DG = rd.randint(1, 20)
        self.BC = rd.randint(1, 20)
        self.CD = rd.randint(1, 20)
        self.BE = rd.randint(1, 20)
        self.ED = rd.randint(1, 20)
        self.path1 = self.SA + self.AE + self.EF + self.FG
        self.path2 = self.SB + self.BC + self.CD + self.DG
        self.path3 = self.SB + self.BC + self.CD + self.ED + self.EF + self.FG
        self.path4 = self.SB + self.BE + self.EF + self.FG
        self.query = "What is the shortest distance from node S to node G in this directed graph?"
        self.answer = min(self.path1, self.path2, self.path3, self.path4)
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.Graph()
        G.add_nodes_from("SABCDEFG")
        plt.figure(figsize=(6, 4))
        pos = {
            "S": (0, 1),
            "A": (0.5, 1.5),
            "B": (0.5, 0.5),
            "C": (1, 0.5),
            "D": (1.5, 0.5),
            "E": (1, 1.5),
            "F": (1.5, 1.5),
            "G": (2, 1)
        }
        G.add_edges_from(
            [("S", "A"), ("S", "B"), ("A", "E"), ("E", "F"), ("F", "G"), ("B", "C"), ("C", "D"), ("D", "G"), ("B", "E"),
             ("E", "D")])
        nx.draw(G, with_labels=True, pos=pos, node_color="white", edgecolors="black", node_size=1500, arrows=True,
                arrowstyle="->")
        plt.text(0.1, 1.25, f"{self.SA}", fontsize=16)
        plt.text(0.1, 0.7, f"{self.SB}", fontsize=16)
        plt.text(0.68, 1.55, f"{self.AE}", fontsize=16)
        plt.text(1.2, 1.55, f"{self.EF}", fontsize=16)
        plt.text(0.68, 0.4, f"{self.BC}", fontsize=16)
        plt.text(1.2, 0.4, f"{self.CD}", fontsize=16)
        plt.text(0.6, 1, f"{self.BE}", fontsize=16)
        plt.text(1.3, 1, f"{self.ED}", fontsize=16)
        plt.text(1.8, 1.25, f"{self.FG}", fontsize=16)
        plt.text(1.8, 0.7, f"{self.DG}", fontsize=16)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q137:
    # MST Kruskal's Algorithm
    def __init__(self):
        self.SA = [rd.randint(1, 20), "AS"]
        self.SB = [rd.randint(1, 20), "BS"]
        self.AE = [rd.randint(1, 20), "AE"]
        self.EF = [rd.randint(1, 20), "EF"]
        self.FG = [rd.randint(1, 20), "FG"]
        self.DG = [rd.randint(1, 20), "DG"]
        self.BC = [rd.randint(1, 20), "BC"]
        self.CD = [rd.randint(1, 20), "CD"]
        self.BE = [rd.randint(1, 20), "BE"]
        self.ED = [rd.randint(1, 20), "DE"]
        self.min = min(self.SA, self.SB, self.AE, self.EF, self.FG, self.DG, self.BC, self.CD, self.BE, self.ED)
        self.query = "what is the first edge added to the MST when running Kruskal's Algorithm? In the case of a tie, " \
                     "choose the edge which comes first in alphabetical order i.e. if you had to choose between AS " \
                     "and AE, then you would choose AE first. "
        self.answer = self.min[1]
        self.answer_type = "text"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.Graph()
        G.add_nodes_from("SABCDEFG")
        plt.figure(figsize=(6, 4))
        pos = {
            "S": (0, 1),
            "A": (0.5, 1.5),
            "B": (0.5, 0.5),
            "C": (1, 0.5),
            "D": (1.5, 0.5),
            "E": (1, 1.5),
            "F": (1.5, 1.5),
            "G": (2, 1)
        }
        G.add_edges_from(
            [("S", "A"), ("S", "B"), ("A", "E"), ("E", "F"), ("F", "G"), ("B", "C"), ("C", "D"), ("D", "G"), ("B", "E"),
             ("E", "D")])
        nx.draw(G, with_labels=True, pos=pos, node_color="white", edgecolors="black", node_size=1500)
        plt.text(0.1, 1.25, f"{self.SA[0]}", fontsize=16)
        plt.text(0.1, 0.7, f"{self.SB[0]}", fontsize=16)
        plt.text(0.68, 1.55, f"{self.AE[0]}", fontsize=16)
        plt.text(1.2, 1.55, f"{self.EF[0]}", fontsize=16)
        plt.text(0.68, 0.4, f"{self.BC[0]}", fontsize=16)
        plt.text(1.2, 0.4, f"{self.CD[0]}", fontsize=16)
        plt.text(0.6, 1, f"{self.BE[0]}", fontsize=16)
        plt.text(1.3, 1, f"{self.ED[0]}", fontsize=16)
        plt.text(1.8, 1.25, f"{self.FG[0]}", fontsize=16)
        plt.text(1.8, 0.7, f"{self.DG[0]}", fontsize=16)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q138:
    # relation between absolute functions
    def __init__(self):
        self.a = rd.randint(0, 4)
        self.b = rd.randint(-4, 0)
        self.d = self.a - self.b
        lst = [f"f(x)=g(x)-{self.d}", f"f(x)=g(x - {self.d})", f"f(x)=-g(x)-{self.d}", f"f(x)=-g(x - {self.d})"]
        self.lst = [f"f(x)=g(x)-{self.d}", f"f(x)=g(x - {self.d})", f"f(x)=-g(x)-{self.d}", f"f(x)=-g(x - {self.d})"]
        self.A = rd.choice(lst)
        lst.remove(self.A)
        self.B = rd.choice(lst)
        lst.remove(self.B)
        self.C = rd.choice(lst)
        lst.remove(self.C)
        self.D = rd.choice(lst)
        self.query = "The figure shows graphs of functions $f$ and $g$ defined on real numbers. Each graph consists " \
                     f"of two perpendicular halflines. Which equality is satisfied for every real number $x$?  " \
                     f"choice: (A) {self.A} (B) {self.B} (C) {self.C} (D) {self.D}"
        if self.A == self.lst[3]:
            self.answer = "A"
        elif self.B == self.lst[3]:
            self.answer = "B"
        elif self.C == self.lst[3]:
            self.answer = "C"
        else:
            self.answer = "D"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        absolute1 = abs(x - self.a)
        absolute2 = -abs(x - self.b)
        plt.plot(x, absolute1, color='blue', linewidth=1.5)
        plt.plot(x, absolute2, color='orange', linewidth=1.5)
        plt.text(self.a - 2, 1, "f(x)", fontsize=12)
        plt.text(self.b + 2, -1.5, "g(x)", fontsize=12)
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


class Q139:
    # calculate quotient of points of the rectangle 1
    def __init__(self):
        self.a = rd.randint(1, 4)
        self.b = rd.randint(1, 4)
        lst = [-4, -3, -2, -1, 1, 2, 3, 4]
        lst.remove(-self.a)
        self.start = rd.choice(lst)
        self.A = [self.start / self.start, "A"]
        self.B = [self.start / (self.start + self.a), "B"]
        self.C = [(self.start + self.b)/(self.start + self.a), "C"]
        self.D = [(self.start + self.b)/self.start, "D"]
        self.query = "For each of the points A, B, C, D of the rectangle ABCD, the quotient (y-coordinate):(" \
                     "x-coordinate) is calculated. For which point will you obtain the smallest quotient?  " \
                     "choice: (A) A (B) B (C) C (D)"
        self.answer = min(self.A, self.B, self.C, self.D)[1]
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        b = self.b
        start = self.start

        rectangle = plt.Polygon([(start + a, start), (start + a, start + b), (start, start + b), (start, start)],
                                closed=True, fill=True, edgecolor='black', facecolor='azure')
        plt.scatter(start, start, color='black', s=12)
        plt.scatter(start + a, start + b, color='black', s=12)
        plt.scatter(start + a, start, color='black', s=12)
        plt.scatter(start, start + b, color='black', s=12)
        ax = plt.gca()
        ax.add_patch(rectangle)
        plt.xlim(-8 * 1.1, 8 * 1.1)
        plt.ylim(-8 * 1.1, 8 * 1.1)

        plt.xticks([-8, -6, -4, -2, 2, 4, 6, 8])
        plt.yticks([-8, -6, -4, -2, 2, 4, 6, 8])
        plt.text(start + a, start + b + 0.5, "C", fontsize=14)
        plt.text(start + a, start - 1, "B", fontsize=14)
        plt.text(start - 0.5, start + b + 0.5, "D", fontsize=14)
        plt.text(start - 0.5, start - 1, "A", fontsize=14)
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


class Q140:
    # calculate quotient of points of the rectangle2
    def __init__(self):
        self.a = rd.randint(1, 4)
        self.b = rd.randint(1, 4)
        lst = [-4, -3, -2, -1, 1, 2, 3, 4]
        lst.remove(-self.b)
        self.start = rd.choice(lst)
        self.A = [self.start / self.start, "A"]
        self.B = [(self.start + self.a) / self.start, "B"]
        self.C = [(self.start + self.a)/(self.start + self.b), "C"]
        self.D = [self.start/(self.start + self.b), "D"]
        self.query = "For each of the points A, B, C, D of the rectangle ABCD, the quotient (x-coordinate):(" \
                     "y-coordinate) is calculated. For which point will you obtain the smallest quotient?  " \
                     "choice: (A) A (B) B (C) C (D)"
        self.answer = min(self.A, self.B, self.C, self.D)[1]
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        b = self.b
        start = self.start

        rectangle = plt.Polygon([(start + a, start), (start + a, start + b), (start, start + b), (start, start)],
                                closed=True, fill=True, edgecolor='black', facecolor='lightpink')
        plt.scatter(start, start, color='black', s=12)
        plt.scatter(start + a, start + b, color='black', s=12)
        plt.scatter(start + a, start, color='black', s=12)
        plt.scatter(start, start + b, color='black', s=12)
        ax = plt.gca()
        ax.add_patch(rectangle)
        plt.xlim(-8 * 1.1, 8 * 1.1)
        plt.ylim(-8 * 1.1, 8 * 1.1)

        plt.xticks([-8, -6, -4, -2, 2, 4, 6, 8])
        plt.yticks([-8, -6, -4, -2, 2, 4, 6, 8])
        plt.text(start + a, start + b + 0.5, "C", fontsize=14)
        plt.text(start + a, start - 1, "B", fontsize=14)
        plt.text(start - 0.5, start + b + 0.5, "D", fontsize=14)
        plt.text(start - 0.5, start - 1, "A", fontsize=14)
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


