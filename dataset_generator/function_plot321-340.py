import math
import shutil
import os.path
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from PIL import Image, ImageDraw, ImageFont
from matplotlib.patches import *


class Q321:
    # algorithm flowchart 1
    def __init__(self):
        self.s = rd.randint(10, 99)
        self.x = rd.randint(1, self.s)
        self.query = f"According to the algorithm chart, if we input {self.x}, what is the output?"
        self.answer = self.algorithm(self.x)
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "undergraduate"

    def draw(self, num):
        Img = Image.open('temp_image/Q321temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        plt.text(330, 75, f"{self.s}", fontsize=5)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, dpi=300, bbox_inches='tight')
        plt.close()

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(np.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def algorithm(self, x):
        t = x
        s = self.s
        while s != 0:
            if t % 2 == 0:
                t = t + 1
            else:
                if self.is_prime(t):
                    if t < s:
                        s = s - t
                        t = t + 2
                    else:
                        s = s - 1
                        if s == 0:
                            return t
                else:
                    t = t + 2


class Q322:
    # algorithm flowchart 2
    def __init__(self):
        self.a = rd.randint(1, 99)
        self.b = rd.randint(1, 99)
        self.query = f"According to the following algorithm flowchart, if we input a={self.a}, b={self.b}, what is " \
                     f"the output? "
        self.answer = self.a + self.b
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "undergraduate"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q322temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q322temp.png"), dest_image_path)


class Q323:
    # thermal box 1
    def __init__(self):
        self.m1 = rd.randint(10, 100)
        self.m2 = rd.randint(10, 100)
        self.c1 = rd.randint(0, 100)
        self.c2 = rd.randint(0, 100)
        self.query = "Two containers of the same gas (ideal) have these masses and temperatures Which box has atoms " \
                     "with the largest average thermal energy?  choice:(A) A (B) B (C) Their average thermal energy " \
                     "is the same "
        if self.c1 > self.c2:
            self.answer = "A"
        elif self.c1 < self.c2:
            self.answer = "B"
        elif self.c1 == self.c2:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        Img = Image.open('temp_image/Q323temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        plt.text(225, 300, "Box A", fontsize=13, ha='center', va='center', rotation=-10)
        plt.text(825, 300, "Box B", fontsize=13, ha='center', va='center', rotation=-10)
        plt.text(225, 400, f"{self.m1} g", fontsize=10, ha='center', va='center', rotation=-10)
        plt.text(825, 400, f"{self.m2} g", fontsize=10, ha='center', va='center', rotation=-10)
        plt.text(225, 450, f"{self.c1} °C", fontsize=10, ha='center', va='center', rotation=-10)
        plt.text(825, 450, f"{self.c2} °C", fontsize=10, ha='center', va='center', rotation=-10)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q324:
    # thermal box 2
    def __init__(self):
        self.m1 = rd.randint(10, 100)
        self.m2 = rd.randint(10, 100)
        self.c1 = rd.randint(0, 100) + 273
        self.c2 = rd.randint(0, 100) + 273
        self.query = "Two containers of the same gas (ideal) have these masses and temperatures Which container of " \
                     "gas has the largest thermal energy?  choice:(A) A (B) B (C) Their average thermal energy " \
                     "is the same "
        if self.c1 * self.m1 > self.c2 * self.m2:
            self.answer = "A"
        elif self.c1 * self.m1 < self.c2 * self.m2:
            self.answer = "B"
        elif self.c1 * self.m1 == self.c2 * self.m2:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        Img = Image.open('temp_image/Q323temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        plt.text(225, 300, "Box A", fontsize=13, ha='center', va='center', rotation=-10)
        plt.text(825, 300, "Box B", fontsize=13, ha='center', va='center', rotation=-10)
        plt.text(225, 400, f"{self.m1} g", fontsize=10, ha='center', va='center', rotation=-10)
        plt.text(825, 400, f"{self.m2} g", fontsize=10, ha='center', va='center', rotation=-10)
        plt.text(225, 450, f"{self.c1} °C", fontsize=10, ha='center', va='center', rotation=-10)
        plt.text(825, 450, f"{self.c2} °C", fontsize=10, ha='center', va='center', rotation=-10)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q325:
    # current attraction
    def __init__(self):
        lst = list(range(1, 99)) + list(range(-99, -1))
        self.left = rd.choice(lst)
        self.middle = rd.choice(lst)
        self.right = rd.choice(lst)
        self.query = "Three equally spaced identical long straight wires carry different currents. In which direction " \
                     "will the middle wire try to move when the currents are switched on?  choice: (A) to the left (" \
                     "B) to the right (C) stay the same "
        if self.left + self.right > 0:
            self.answer = "B"
        elif self.left + self.right < 0:
            self.answer = "A"
        elif self.left + self.right == 0:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        plt.gcf().set_size_inches(4, 4)
        plt.xlim(0, 10)
        plt.ylim(0, 10)
        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        ax = plt.gca()
        plt.vlines(2, 1, 9, color="black", linewidth=2)
        plt.vlines(8, 1, 9, color="black", linewidth=2)
        plt.vlines(5, 1, 9, color="black", linewidth=2)
        if self.left > 0:
            plt.text(2, 5, ">", fontsize=15, ha='center', va='center', rotation=90)
        else:
            plt.text(2, 5, "<", fontsize=15, ha='center', va='center', rotation=90)
        plt.text(3, 5, f"{abs(self.left)}A", fontsize=12, ha='center', va='center')
        plt.text(5, 5, "<", fontsize=15, ha='center', va='center', rotation=90)
        plt.text(6, 5, f"{abs(self.middle)}A", fontsize=12, ha='center', va='center')
        if self.right > 0:
            plt.text(8, 5, "<", fontsize=15, ha='center', va='center', rotation=90)
        else:
            plt.text(8, 5, ">", fontsize=15, ha='center', va='center', rotation=90)
        plt.text(9, 5, f"{abs(self.right)}A", fontsize=12, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q326:
    # cut tree
    def __init__(self):
        self.h = rd.randint(50, 100)
        self.s = rd.randint(10, self.h//2)
        self.query = f"To avoid emergency situation, the university decides to cut down the highest eucalyptus, " \
                     f"which is {self.h}m high. They cut the tree at {self.s} metres of the trunk. How far from the " \
                     f"tree will be safe when the eucalyptus falls? "
        self.answer = np.sqrt((self.h - self.s) ** 2 - self.s ** 2)
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        Img = Image.open('temp_image/Q326temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        plt.hlines(330, -100, 100, color="black", linewidth=2)
        plt.hlines(330 - self.s / self.h * 300, 150, 250, color="black", linewidth=2, linestyles='dashed')
        plt.text(260, 330 - self.s / self.h * 300, f"{self.s} m", fontsize=12)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q327:
    # find the biggest result
    def __init__(self):
        self.lst = rd.sample(range(0, 10), 4)
        self.query = f"Steven wants to write each of the digits {self.lst[0]}, {self.lst[1]}, {self.lst[2]} " \
                     f"and {self.lst[3]} into the boxes of this addition: He wants to obtain the biggest result " \
                     f"possible. Which digit does he have to use for the tenth digit number?"
        lst = sorted(self.lst)
        self.answer = lst[2]
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def draw(self, num):
        plt.gcf().set_size_inches(4, 4)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        sq1 = plt.Polygon([[-5, 0], [-4, 0], [-4, 1], [-5, 1]], fill=False)
        sq2 = plt.Polygon([[-3, 0], [-2, 0], [-2, 1], [-3, 1]], fill=False)
        sq3 = plt.Polygon([[-1, 0], [0, 0], [0, 1], [-1, 1]], fill=False)
        sq4 = plt.Polygon([[3, 0], [2, 0], [2, 1], [3, 1]], fill=False)
        plt.text(-2.5, 0.4, f"{self.lst[0]}", fontsize=16, ha='center', va='center')
        plt.text(-4.5, 0.4, f"{self.lst[1]}", fontsize=16, ha='center', va='center')
        plt.text(-0.5, 0.4, f"{self.lst[2]}", fontsize=16, ha='center', va='center')
        plt.text(2.5, 0.4, f"{self.lst[3]}", fontsize=16, ha='center', va='center')
        plt.text(1, 0.4, "+", fontsize=16, ha='center', va='center')
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.add_patch(sq1)
        ax.add_patch(sq2)
        ax.add_patch(sq3)
        ax.add_patch(sq4)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q328:
    # shooting competition
    def __init__(self):
        self.p1 = rd.randint(6, 10)
        self.p2 = rd.randint(6, 10)
        self.p3 = rd.randint(6, 10)
        self.theta1 = rd.randint(-260, 80) * np.pi / 180
        self.theta2 = rd.randint(-260, 80) * np.pi / 180
        self.theta3 = rd.randint(-260, 80) * np.pi / 180
        self.query = "The result of shooters in shooting tournament is shown in the image. What is the score?"
        self.answer = self.p1 + self.p2 + self.p3
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def draw(self, num):
        plt.gcf().set_size_inches(4, 4)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        sq1 = Circle((0, 0), 1, fill=False)
        sq2 = Circle((0, 0), 2, fill=False)
        sq3 = Circle((0, 0), 3, fill=False)
        sq4 = Circle((0, 0), 4, fill=False)
        sq5 = Circle((0, 0), 5, fill=False)
        plt.text(0, 0, "10", fontsize=10, ha='center', va='center')
        plt.text(0, 1.5, "9", fontsize=10, ha='center', va='center')
        plt.text(0, 2.5, "8", fontsize=10, ha='center', va='center')
        plt.text(0, 3.5, "7", fontsize=10, ha='center', va='center')
        plt.text(0, 4.5, "6", fontsize=10, ha='center', va='center')
        plt.scatter((10 - self.p1 + 0.5) * np.cos(self.theta1), (10 - self.p1 + 0.5) * np.sin(self.theta1), color="black", s=20)
        plt.scatter((10 - self.p2 + 0.5) * np.cos(self.theta2), (10 - self.p2 + 0.5) * np.sin(self.theta2), color="black",
                    s=20)
        plt.scatter((10 - self.p3 + 0.5) * np.cos(self.theta3), (10 - self.p3 + 0.5) * np.sin(self.theta3), color="black",
                    s=20)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.add_patch(sq1)
        ax.add_patch(sq2)
        ax.add_patch(sq3)
        ax.add_patch(sq4)
        ax.add_patch(sq5)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q329:
    # balance 1
    def __init__(self):
        self.f1 = rd.randint(10, 50)
        self.f2 = rd.randint(10, 50)
        self.l1 = self.f2
        self.l2 = self.f1
        self.query = "A uniform meterstick is balanced at its midpoint with several forces applied as shown below. If " \
                     "the stick is in equilibrium, what is the magnitude of the force X in N? "
        self.answer = self.f2
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        plt.gcf().set_size_inches(4, 4)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        sq1 = plt.Polygon([[-5, 0], [5, 0], [5, 0.5], [-5, 0.5]], edgecolor="black", facecolor="white")
        plt.text(0, -0.4, r"$\blacktriangle$", fontsize=20, ha='center', va='center')
        plt.text(self.l1/10, 0.9, r"$\uparrow$", fontsize=20, ha='center', va='center')
        plt.text(self.l1/10, 2, f"{self.f1}N", fontsize=14, ha='center', va='center')
        plt.text(-self.l2/10, 0.9, r"$\uparrow$", fontsize=20, ha='center', va='center')
        plt.text(-self.l2/10, 2, "X", fontsize=14, ha='center', va='center')
        plt.text(self.l1/10, -0.5, f"{self.l1}m", fontsize=12, ha='center', va='center')
        plt.text(-self.l2/10, -0.5, f"{self.l2}m", fontsize=12, ha='center', va='center')
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.add_patch(sq1)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q330:
    # balance 2
    def __init__(self):
        self.f1 = rd.randint(10, 50)
        self.f3 = rd.randint(10, 50)
        self.l1 = rd.randint(10, 50)
        self.l2 = rd.randint(10, 50)
        self.l3 = rd.randint(10, 50)
        self.f2 = (self.f1 * self.l1 + self.f3 * self.l3) / self.l2
        self.query = "A uniform meterstick is balanced at its midpoint with several forces applied as shown below. If " \
                     "the stick is in equilibrium, what is the magnitude of the force X in N? "
        self.answer = self.f2
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        plt.gcf().set_size_inches(4, 4)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        sq1 = plt.Polygon([[-5, 0], [5, 0], [5, 0.5], [-5, 0.5]], edgecolor="black", facecolor="white")
        plt.text(0, -0.4, r"$\blacktriangle$", fontsize=20, ha='center', va='center')
        plt.text(self.l1/10, 0.9, r"$\uparrow$", fontsize=20, ha='center', va='center')
        plt.text(self.l1/10, 2, f"{self.f1}N", fontsize=14, ha='center', va='center')
        plt.text(-self.l2/10, 0.9, r"$\uparrow$", fontsize=20, ha='center', va='center')
        plt.text(-self.l2/10, 2, "X", fontsize=14, ha='center', va='center')
        plt.text(self.l1/10, -0.5, f"{self.l1}m", fontsize=12, ha='center', va='center')
        plt.text(-self.l2/10, -0.5, f"{self.l2}m", fontsize=12, ha='center', va='center')
        plt.text(-self.l3 / 10, -1, r"$\downarrow$", fontsize=20, ha='center', va='center')
        plt.text(-self.l3 / 10, -2.1, f"{self.l3}m", fontsize=12, ha='center', va='center')
        plt.text(-self.l3 / 10, -3, f"{self.f3}N", fontsize=12, ha='center', va='center')
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.add_patch(sq1)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q331:
    # momentum 1
    def __init__(self):
        self.s = rd.randint(1, 5) * 2
        self.d = rd.randint(-5, -1) * 2
        self.m = rd.randint(2, 8)
        self.query = "The graph shows the force on an object of mass M as a function of time. For the time interval 0 " \
                     "to 10 s, what is the total change in the momentum of the object?"
        self.answer = self.s * self.m + self.d * (10 - self.m)
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(0, 6 * 1.1)
        plt.ylim(-5 * 1.1, 5 * 1.1)

        plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['bottom'].set_position(('data', 0))
        sq1 = plt.Polygon([[0, self.s], [self.m, self.s], [self.m, 0], [0, 0]], facecolor="white", edgecolor="black", linewidth=2)
        sq2 = plt.Polygon([[self.m, 0], [self.m, self.d], [10, self.d], [10, 0]], facecolor="white", edgecolor="black", linewidth=2)
        plt.text(-1, -1, "Force (N)", fontsize=12, rotation=90)
        plt.text(4, -12, "Time (s)", fontsize=14)
        ax.add_patch(sq1)
        ax.add_patch(sq2)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q332:
    # thermal energy 3
    def __init__(self):
        self.m1 = rd.randint(10, 90)
        self.m2 = rd.randint(10, 90)
        self.s1 = rd.randint(1000, 1500)
        self.s2 = rd.randint(1000, 1500)
        self.query = "The diagrams below show two pure samples of gas in identical closed, rigid containers. Each " \
                     "colored ball represents one gas particle. Both samples have the same number of particles. " \
                     "Compare the average kinetic energies of the particles in each sample. Which sample has the " \
                     "higher temperature?  choice: (A) sample A (B) sample B (C) Their temperature is the same"
        if self.s1 * self.m1 > self.s2 * self.m2:
            self.answer = "A"
        elif self.s1 * self.m1 < self.s2 * self.m2:
            self.answer = "B"
        else:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        Img = Image.open('temp_image/Q332temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        x1 = np.random.uniform(150, 550, size=20)
        y1 = np.random.uniform(400, 800, size=20)
        x2 = np.random.uniform(850, 1250, size=20)
        y2 = np.random.uniform(400, 800, size=20)
        plt.scatter(x1, y1, edgecolors='black', s=20, color="lightblue")
        plt.scatter(x2, y2, edgecolors='black', s=20, color="lightgreen")
        plt.text(350, 1000, "Sample A", fontsize=14, ha='center', va='center')
        plt.text(1050, 1000, "Sample B", fontsize=14, ha='center', va='center')
        plt.text(350, 1050, f"Mass of each particle: {self.m1}u", fontsize=12, ha='center', va='center')
        plt.text(1050, 1050, f"Mass of each particle: {self.m2}u", fontsize=12, ha='center', va='center')
        plt.text(350, 1100, f"Average particle speed: {self.s1}m/s", fontsize=10.5, ha='center', va='center')
        plt.text(1050, 1100, f"Average particle speed: {self.s2}m/s", fontsize=10.5, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q333:
    # electrical circuits 4
    def __init__(self):
        self.v = rd.randint(10, 50)
        self.vl1 = rd.randint(1, self.v)
        self.query = f"The cell in the following circuit has an emf of {self.v / 10} V. The digital voltmeter reads " \
                     f"{self.vl1 / 10} V. What is the voltage at L2? "
        self.answer = (self.v - self.vl1) / 10
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q333temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q333temp.png"), dest_image_path)


class Q334:
    # electrical circuits 5
    def __init__(self):
        self.v = rd.randint(10, 50)
        self.vl1 = rd.randint(1, self.v)
        self.query = f"The cell in the following circuit has an emf of {self.v / 10} V. The digital voltmeter reads " \
                     f"{self.vl1 / 10} V. The resistance of L1 is 1 omega. What is the resistance of L2? "
        self.answer = (self.v - self.vl1) / self.vl1
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q333temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q333temp.png"), dest_image_path)


class Q335:
    # conjugate of complex number 1
    def __init__(self):
        lst = list(range(1, 6)) + list(range(-6, -1))
        self.x = rd.choice(lst)
        self.y = rd.choice(lst)
        self.query = "Which point represents the conjugate of the complex number z?  choice: (A) red point (B) green " \
                     "point (C) blue point "
        self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x = self.x
        y = self.y
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6],
                   ["-6i", "-5i", "-4i", "-3i", "-2i", "-i", "i", "2i", "3i", "4i", "5i", "6i"])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(x, y, color='black')
        plt.scatter(-x, -y, color='blue')
        plt.scatter(-x, y, color='red')
        plt.scatter(x, -y, color='green')
        plt.plot([0, x], [0, y], color='deeppink')
        plt.text(x, y + 0.5, "z", fontsize=10, ha='center', va='center')
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q336:
    # conjugate of complex number 2
    def __init__(self):
        lst = list(range(1, 6)) + list(range(-6, -1))
        self.x = rd.choice(lst)
        self.y = rd.choice(lst)
        self.query = "Find the value of z * (z∗)."
        self.answer = self.x ** 2 + self.y ** 2
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x = self.x
        y = self.y
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6],
                   ["-6i", "-5i", "-4i", "-3i", "-2i", "-i", "i", "2i", "3i", "4i", "5i", "6i"])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(x, y, color='black')
        plt.scatter(x, -y, color='black')
        plt.plot([0, x], [0, y], color='deeppink')
        plt.plot([0, x], [0, -y], color='deeppink')
        plt.text(x, y + 0.5, f"({x}, {y}i)", fontsize=10, ha='center', va='center')
        plt.text(x, -y - 0.5, f"({x}, {-y}i)", fontsize=10, ha='center', va='center')
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q337:
    # 1/z
    def __init__(self):
        lst = list(range(1, 6)) + list(range(-6, -1))
        self.x = rd.choice(lst)
        self.y = rd.choice(lst)
        self.z2 = self.x ** 2 + self.y ** 2
        self.query = "Find the value of z1 * z2."
        self.answer = 1
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x = self.x
        y = self.y
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6],
                   ["-6i", "-5i", "-4i", "-3i", "-2i", "-i", "i", "2i", "3i", "4i", "5i", "6i"])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(x, y, color='black')
        plt.scatter(x/self.z2, -y/self.z2, color='black')
        plt.plot([0, x], [0, y], color='deeppink')
        plt.plot([0, x/self.z2], [0, -y/self.z2], color='deeppink')
        plt.text(x, y + 0.5, f"z1 ({x}, {y}i)", fontsize=10, ha='center', va='center')
        plt.text(x/self.z2, -y/self.z2 - 0.5, f"z2 ({x}/{self.z2}, ({-y}/{self.z2})i)", fontsize=10, ha='center',
                 va='center')
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q338:
    # rotation
    def __init__(self):
        lst = list(range(1, 6)) + list(range(-6, -1))
        self.x = rd.choice(lst)
        self.y = rd.choice(lst)
        self.query = "Find the value of ∠z1oz2. Give the answer in degrees."
        self.answer = 90
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x = self.x
        y = self.y
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6],
                   ["-6i", "-5i", "-4i", "-3i", "-2i", "-i", "i", "2i", "3i", "4i", "5i", "6i"])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(x, y, color='black')
        plt.scatter(y, -x, color='black')
        plt.plot([0, x], [0, y], color='black')
        plt.plot([0, y], [0, -x], color='black')
        plt.text(x, y + 0.5, "z1", fontsize=10, ha='center', va='center')
        plt.text(y, -x + 0.5, "z2", fontsize=10, ha='center', va='center')
        plt.text(0.2, -0.4, "O", fontsize=10, ha='center', va='center')
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q339:
    # angle preserving
    def __init__(self):
        self.x = rd.randint(1, 4)
        self.y = rd.randint(-6, 6)
        self.query = "Is ∠z1oz2 equal to ∠z3oz4?  choice: (A) Yes (B) No"
        self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        plt.gcf().set_size_inches(6, 6)
        x = self.x
        y = self.y
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6],
                   ["-6i", "-5i", "-4i", "-3i", "-2i", "-i", "i", "2i", "3i", "4i", "5i", "6i"])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(x, y, color='black')
        plt.scatter(x + 2, y, color='black')
        plt.plot([x, x + 2], [y, y], color='black')
        plt.scatter(y, -x, color='black')
        plt.scatter(y, -x - 2, color='black')
        plt.plot([y, y], [-x, -x - 2], color='black')

        plt.plot([0, x], [0, y], color='lightgreen', linestyle="dashed")
        plt.plot([0, y], [0, -x], color='lightgreen', linestyle="dashed")
        plt.plot([0, y], [0, -x - 2], color='lightgreen', linestyle="dashed")
        plt.plot([0, x + 2], [0, y], color='lightgreen', linestyle="dashed")
        plt.text(x, y + 0.5, "z1", fontsize=10, ha='center', va='center')
        plt.text(x + 2, y + 0.5, "z2", fontsize=10, ha='center', va='center')
        plt.text(y, -x + 0.5, "z3", fontsize=10, ha='center', va='center')
        plt.text(y, -x - 2 - 0.5, "z4", fontsize=10, ha='center', va='center')
        plt.text(0.2, -0.4, "O", fontsize=10, ha='center', va='center')
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q340:
    # rule of arrow
    def __init__(self):
        self.lst = rd.sample([r"$\nearrow$", r"$\nwarrow$", r"$\searrow$", r"$\swarrow$"], 4)
        self.query = r"Determine the missing part.  Choice: (A) ↗  (B) ↖  (C) ↘  (D) ↙ "
        if r"$\nearrow$" == self.lst[3]:
            self.answer = "A"
        elif r"$\nwarrow$" == self.lst[3]:
            self.answer = "B"
        elif r"$\searrow$" == self.lst[3]:
            self.answer = "C"
        else:
            self.answer = "D"
        self.answer_type = "multiple choice"
        self.subject = "puzzle test"
        self.level = "elementary school"

    def draw(self, num):
        col1 = [1, 1, 1]
        col2 = [1, 0, 1]
        col3 = [1, 1, 1]
        mat = np.array([col1, col2, col3])
        plt.imshow(mat, cmap="gray")
        constant_a = 0.5
        constant_b = 1.5
        plt.vlines(constant_a, -0.5, 2.5, colors="gray")
        plt.vlines(constant_b, -0.5, 2.5, colors="gray")
        plt.hlines(constant_a, -0.5, 2.5, colors="gray")
        plt.hlines(constant_b, -0.5, 2.5, colors="gray")
        plt.text(0, 2, self.lst[0], fontsize=60, ha='center', va='center')
        plt.text(2, 0, self.lst[0], fontsize=60, ha='center', va='center')
        plt.text(0, 1, self.lst[1], fontsize=60, ha='center', va='center')
        plt.text(2, 1, self.lst[1], fontsize=60, ha='center', va='center')
        plt.text(1, 2, self.lst[2], fontsize=60, ha='center', va='center')
        plt.text(1, 0, self.lst[2], fontsize=60, ha='center', va='center')
        plt.text(0, 0, self.lst[3], fontsize=60, ha='center', va='center')
        plt.text(2, 2, "?", fontsize=60, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

