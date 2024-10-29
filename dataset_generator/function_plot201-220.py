import os

import matplotlib.pyplot as plt
import numpy as np
import random as rd
import pandas as pd
from plottable import Table
from matplotlib.patches import *


class Q201:
    # trapezoidal rule
    def __init__(self):
        self.xa = 1
        self.xb = rd.randint(2, 10)
        self.fxa = rd.randint(1, 100)
        self.fxb = rd.randint(1, 100)
        self.data = {
            'x': [' f(x)'],
            f'{self.xa}': self.fxa,
            f'{self.xb}': self.fxb,
        }
        self.df = pd.DataFrame(self.data)
        self.query = f"what is the trapezoidal approximation of the integral of f(x) from {self.xa} to {self.xb}?"
        self.answer = (self.xb - self.xa) / 2 * (self.fxa + self.fxb)
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(10, 4))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        self.df.set_index('x', inplace=True)
        Table(self.df,
              textprops={
                  'fontsize': 40,
                  'ha': 'center'
              },
              )
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q202:
    # Simpson's rule
    def __init__(self):
        self.xa = 1
        self.xb = rd.randint(2, 10)
        self.x1 = (self.xa + self.xb) / 2
        self.fxa = rd.randint(1, 100)
        self.fxb = rd.randint(1, 100)
        self.fx1 = rd.randint(1, 100)
        self.data = {
            'x': [' f(x)'],
            f'{self.xa}': self.fxa,
            f'{self.x1}': self.fx1,
            f'{self.xb}': self.fxb,
        }
        self.df = pd.DataFrame(self.data)
        self.query = f"what is the Simpson's approximation of the integral of f(x) from {self.xa} to {self.xb}?"
        self.answer = (self.xb - self.xa) / 3 * (self.fxa + 4 * self.fx1 + self.fxb)
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(10, 4))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        self.df.set_index('x', inplace=True)
        Table(self.df,
              textprops={
                  'fontsize': 40,
                  'ha': 'center'
              },
              )
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q203:
    # trapezoidal rule and Riemann sum 1
    def __init__(self):
        self.a = rd.randint(50, 150) / 100
        self.query = "Which of the following descriptions is correct for approximating the " \
                     "integral of f(x) from a to b?  choices: " \
                     "(A) trapezoidal sum underapproximation (B) left Riemann sum underapproximation " \
                     "(C) left Riemann sum overapproximation (D) Neither"
        if self.a > 1:
            self.answer = "B"
        elif self.a < 1:
            self.answer = "C"
        else:
            self.answer = "D"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        a = self.a
        x = np.linspace(-2, 2, 200, endpoint=True)
        line = a ** x
        plt.plot(x, line, color='black', linewidth=1.5)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.vlines(-2, 0, a ** -2, linestyles='dashed', colors='black')
        plt.vlines(2, 0, a ** 2, linestyles='dashed', colors='black')
        plt.text(-2, -0.5, "a", fontsize=12)
        plt.text(2, -0.5, "b", fontsize=12)
        plt.xticks([])
        plt.yticks([])
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


class Q204:
    # trapezoidal rule and Riemann sum 2
    def __init__(self):
        self.a = rd.randint(8, 15)
        self.b = rd.choice([2, -2])
        self.query = "Which of the following descriptions is correct for approximating the " \
                     "integral of f(x) from a to b?  choices: " \
                     "(A) trapezoidal sum underapproximation and left Riemann sum underapproximation (B) trapezoidal sum underapproximation  and left Riemann sum overapproximation " \
                     "(C) trapezoidal sum overapproximation and left Riemann sum underapproximation (D) trapezoidal sum overapproximation  and left Riemann sum overapproximation"
        if self.b == 2:
            self.answer = "B"
        else:
            self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        b = self.b
        x = np.linspace(-2, 2, 200, endpoint=True)
        line = -1 / a * (x + b) ** 2 + 2
        plt.plot(x, line, color='black', linewidth=1.5)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.vlines(-2, 0, -1 / a * (-2 + b) ** 2 + 2, linestyles='dashed', colors='black')
        plt.vlines(2, 0, -1 / a * (2 + b) ** 2 + 2, linestyles='dashed', colors='black')
        plt.text(-2, -0.5, "a", fontsize=12)
        plt.text(2, -0.5, "b", fontsize=12)
        plt.xticks([])
        plt.yticks([])
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


class Q205:
    # length of semicircle
    def __init__(self):
        self.random_a = rd.randint(2, 12)
        self.query = "The two semicircles are in the figure above. What is the total length of the darkened curve?"
        self.answer = 14 + 7 * np.pi
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        random_a = self.random_a
        b = 14 - random_a
        c1 = 7 - random_a / 2
        c2 = (7 - random_a + (-7)) / 2
        plt.xlim(-7 * 1.1, 7 * 1.1)
        plt.ylim(-7 * 1.1, 7 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        wedge2 = Wedge((c1, 0), random_a / 2, 0, 180, edgecolor="black", facecolor="white", fill=True, linewidth=2)
        wedge3 = Wedge((c2, 0), (14 - random_a) / 2, 180, 360, edgecolor="black", facecolor="white", fill=True,
                       linewidth=2)
        ax.add_patch(wedge2)
        ax.add_patch(wedge3)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.xticks([0, 7])
        plt.tick_params(axis='both', which='major', labelsize=18)
        plt.text(-7, 0.5, "-7", fontsize=18)
        plt.scatter(-7, 0)
        plt.scatter(7, 0)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q206:
    # Law of cosine
    def __init__(self):
        self.a = rd.randint(1, 10)
        self.b = self.a + rd.randint(2, 5)
        self.c = self.b + rd.randint(0, self.a - 1)
        self.cosC = (self.a * self.a + self.c * self.c - self.b * self.b) / (2 * self.a * self.c)
        self.query = "What is the measure of ∠C? Answer the question in degrees."
        self.answer = np.arccos(self.cosC) * 360 / (2 * np.pi)
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        triangle = plt.Polygon([(1, 1), (4, 1), (2, 2)], closed=True, fill=True, edgecolor='black', facecolor='white')
        fig, ax = plt.subplots()
        fig.set_size_inches(4, 4)
        ax.add_patch(triangle)
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        plt.text(1, 1.7, f'{self.a}', fontsize=12)
        plt.text(2.75, 1.8, f'{self.b}', fontsize=12)
        plt.text(2, 0.5, f'{self.c}', fontsize=12)
        plt.text(2, 2.2, "A", fontsize=12)
        plt.text(4.2, 1, "B", fontsize=12)
        plt.text(0.7, 1, "C", fontsize=12)
        plt.xticks([])
        plt.yticks([])
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q207:
    # law of sine
    def __init__(self):
        self.a = rd.randint(1, 10)
        self.b = self.a + rd.randint(2, 5)
        self.c = rd.randint(40, 60)
        self.sinB = self.a / self.b * np.sin(self.c / 180 * np.pi)
        self.query = "What is the measure of ∠B? Answer the question in degrees."
        self.answer = np.arcsin(self.sinB) / np.pi * 180
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        triangle = plt.Polygon([(1, 1), (4, 1), (2, 2)], closed=True, fill=True, edgecolor='black', facecolor='white')
        fig, ax = plt.subplots()
        fig.set_size_inches(4, 4)
        ax.add_patch(triangle)
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        plt.text(1, 1.7, f'{self.a}', fontsize=12)
        plt.text(2.75, 1.8, f'{self.b}', fontsize=12)
        plt.text(1.3, 1.1, f'{self.c}°', fontsize=12)
        plt.text(2, 2.2, "A", fontsize=12)
        plt.text(4.2, 1, "B", fontsize=12)
        plt.text(0.7, 1, "C", fontsize=12)
        plt.xticks([])
        plt.yticks([])
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q208:
    # geometric optical illusion 1
    def __init__(self):
        self.a = rd.randint(3, 10)
        angle = list(range(10, 351))
        angle.remove(90)
        angle.remove(180)
        angle.remove(270)
        self.b = rd.choice(angle) / 180 * np.pi
        self.query = "Are three lines in figure the same length? choices: (A) Yes (B) No"
        self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        b = self.b
        plt.hlines(0, -a / 2, a / 2, colors='lightblue', linewidth=2)
        plt.vlines(0, -a / 2, a / 2, colors='lightgreen', linewidth=2)
        plt.plot([0, a * np.cos(b)], [0, a * np.sin(b)], color='purple', linewidth=2)
        plt.xlim(-10 * 1.1, 10 * 1.1)
        plt.ylim(-10 * 1.1, 10 * 1.1)

        plt.xticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        plt.yticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        ax = plt.gca()
        plt.gcf().set_size_inches(6, 6)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q209:
    # geometric optical illusion 2
    def __init__(self):
        self.a = rd.randint(5, 18)
        self.query = "Is the distance between the two orange lines as long as the distance between the two purple " \
                     "lines?  choices: (A) Yes (B) No "
        self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        plt.plot([-8, -6], [a / 2, a / 2], color='purple', linewidth=2)
        plt.plot([-8, -6], [-a / 2, -a / 2], color='purple', linewidth=2)
        i = -a / 2 + 1
        while i < a / 2:
            plt.plot([-8, -6], [i, i], color='black', linewidth=2)
            i += 1
        plt.plot([2, 4], [a / 2 + 1, a / 2 + 1], color='orange', linewidth=2)
        plt.plot([2, 4], [-a / 2 + 1, -a / 2 + 1], color='orange', linewidth=2)
        plt.xlim(-10 * 1.1, 10 * 1.1)
        plt.ylim(-10 * 1.1, 10 * 1.1)

        plt.xticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        plt.yticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        ax = plt.gca()
        plt.gcf().set_size_inches(6, 6)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q210:
    # geometric optical illusion 3
    def __init__(self):
        self.a = rd.randint(5, 18)
        self.query = "Are the red line and the blue line the same length? choices: (A) Yes (B) No"
        self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        plt.plot([-a / 2, a / 2], [8, 8], color='red', linewidth=2)
        plt.plot([-a / 2 - 2, a / 2 + 2], [4, 4], color='black', linewidth=2)
        plt.plot([-a / 2 - 2, -a / 2], [4, 8], color='black', linewidth=2)
        plt.plot([a / 2 + 2, a / 2], [4, 8], color='black', linewidth=2)
        plt.plot([-a / 2, a / 2], [-4, -4], color='blue', linewidth=2)
        plt.plot([-a / 2 + 2, a / 2 - 2], [-8, -8], color='black', linewidth=2)
        plt.plot([-a / 2 + 2, -a / 2], [-8, -4], color='black', linewidth=2)
        plt.plot([a / 2 - 2, a / 2], [-8, -4], color='black', linewidth=2)
        plt.xlim(-12 * 1.1, 12 * 1.1)
        plt.ylim(-12 * 1.1, 12 * 1.1)

        plt.xticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        plt.yticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        ax = plt.gca()
        plt.gcf().set_size_inches(6, 6)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q211:
    # geometric optical illusion 4
    def __init__(self):
        self.a = rd.randint(1, 30) / 10
        self.query = "The curve BD is parallel to the curve AC, and AB=CD=EF=GH. Are the areas of enclosed graph ABCD " \
                     "and EFGH the same?  choice: (A) Yes (B) No "
        self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        x = np.linspace(-10, 10, 200, endpoint=True)
        sine = a * np.sin(x)
        sine2 = a * np.sin(x) + 2
        plt.plot([-10, -10], [a * np.sin(-10), a * np.sin(-10) + 2], color='black')
        plt.plot([10, 10], [a * np.sin(10), a * np.sin(10) + 2], color='black')
        rectangle = plt.Polygon([(-10, -8), (-10, -6), (10, -6), (10, -8)], closed=True, fill=True, edgecolor='black',
                                facecolor='orange', linewidth=1.5)
        plt.text(-10.5, a * np.sin(-10) + 2.5, "A", fontsize=12)
        plt.text(-10.5, a * np.sin(-10) - 1.5, "B", fontsize=12)
        plt.text(10.5, a * np.sin(10) + 2.5, "C", fontsize=12)
        plt.text(10.5, a * np.sin(10) - 1, "D", fontsize=12)
        plt.text(-10.5, -5.5, "E", fontsize=12)
        plt.text(-10.5, -9, "F", fontsize=12)
        plt.text(10.5, -5.5, "G", fontsize=12)
        plt.text(10.5, -9, "H", fontsize=12)
        plt.fill_between(x, sine, sine2, color='lightblue')
        plt.plot(x, sine, color='black')
        plt.plot(x, sine2, color='black')
        plt.xlim(-12 * 1.1, 12 * 1.1)
        plt.ylim(-12 * 1.1, 12 * 1.1)

        plt.xticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        plt.yticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        ax = plt.gca()
        ax.add_patch(rectangle)
        plt.gcf().set_size_inches(6, 6)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q212:
    # geometric optical illusion 5
    def __init__(self):
        self.AB = rd.randint(2, 100)
        self.EF = 5 * self.AB
        self.a = rd.randint(1, 30) / 10
        self.query = f"The curve BD is parallel to the curve AC, AB=CD=EF=GH={self.AB}, and EG = FH = {self.EF}. " \
                     f"What is the area of enclosed graph ABCD?"
        self.answer = self.AB * self.EF
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        x = np.linspace(-10, 10, 200, endpoint=True)
        sine = a * np.sin(x)
        sine2 = a * np.sin(x) + 2
        plt.plot([-10, -10], [a * np.sin(-10), a * np.sin(-10) + 2], color='black')
        plt.plot([10, 10], [a * np.sin(10), a * np.sin(10) + 2], color='black')
        rectangle = plt.Polygon([(-10, -8), (-10, -6), (10, -6), (10, -8)], closed=True, fill=True, edgecolor='black',
                                facecolor='pink', linewidth=1.5)
        plt.text(-10.5, a * np.sin(-10) + 2.5, "A", fontsize=12)
        plt.text(-10.5, a * np.sin(-10) - 1.5, "B", fontsize=12)
        plt.text(10.5, a * np.sin(10) + 2.5, "C", fontsize=12)
        plt.text(10.5, a * np.sin(10) - 1, "D", fontsize=12)
        plt.text(-10.5, -5.5, "E", fontsize=12)
        plt.text(-10.5, -9, "F", fontsize=12)
        plt.text(10.5, -5.5, "G", fontsize=12)
        plt.text(10.5, -9, "H", fontsize=12)
        plt.fill_between(x, sine, sine2, color='lightgreen')
        plt.plot(x, sine, color='black')
        plt.plot(x, sine2, color='black')
        plt.xlim(-12 * 1.1, 12 * 1.1)
        plt.ylim(-12 * 1.1, 12 * 1.1)

        plt.xticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        plt.yticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        ax = plt.gca()
        ax.add_patch(rectangle)
        plt.gcf().set_size_inches(6, 6)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q213:
    # find the lattice point in the circle
    def __init__(self):
        self.r = rd.randint(1, 10)
        self.query = f"Find the number of integer solutions of x^2 + y^2 <= {self.r * self.r}"
        lst = [5, 13, 29, 49, 81, 113, 149, 197, 253, 317]
        self.answer = lst[self.r - 1]
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        plt.xlim(-10 * 1.1, 10 * 1.1)
        plt.ylim(-10 * 1.1, 10 * 1.1)
        plt.xticks([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        ax = plt.gca()
        plt.gcf().set_size_inches(6, 6)
        circle = Circle((0, 0), self.r, color="black", fill=False)
        ax.add_patch(circle)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q214:
    # right triangle and square 1
    def __init__(self):
        self.a = rd.randint(2, 14)
        self.factor = rd.randint(1, 10)
        self.side = self.a * self.factor
        self.other = (16 - self.a) * self.factor
        self.query = "Four identical azure right triangles form a square. Given that " \
                     f"two sides of the azure triangle are {self.side},{self.other}, find the area of the white square."
        self.answer = self.side * self.side + self.other * self.other
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        square = plt.Polygon([(-8, 8), (-8, -8), (8, -8), (8, 8)], closed=True, fill=True, edgecolor='black',
                             facecolor='white')
        tri1 = plt.Polygon([(-8, -8), (-8 + a, -8), (-8, -8 + (16 - a))], closed=True, fill=True, edgecolor='black',
                           facecolor='azure')
        tri2 = plt.Polygon([(8, -8), (-8 + a, -8), (8, -8 + a)], closed=True, fill=True, edgecolor='black',
                           facecolor='azure')
        tri3 = plt.Polygon([(-8, 8), (8 - a, 8), (-8, -8 + (16 - a))], closed=True, fill=True, edgecolor='black',
                           facecolor='azure')
        tri4 = plt.Polygon([(8, 8), (8 - a, 8), (8, -8 + a)], closed=True, fill=True, edgecolor='black',
                           facecolor='azure')
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.xticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        plt.yticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        plt.grid()
        ax.add_patch(square)
        ax.add_patch(tri1)
        ax.add_patch(tri2)
        ax.add_patch(tri3)
        ax.add_patch(tri4)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q215:
    # right triangle and square 2
    def __init__(self):
        self.a = rd.randint(2, 14)
        self.area = self.a * (16 - self.a) / 2
        self.c = self.a * self.a + (16 - self.a) ** 2
        self.query = "Four identical pink right triangles form a big square. Given that " \
                     f"the area of a pink triangle is {self.area}, and the area of white square is {self.c}, " \
                     f"find the area of the big square."
        self.answer = self.area * 4 + self.c
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        square = plt.Polygon([(-8, 8), (-8, -8), (8, -8), (8, 8)], closed=True, fill=True, edgecolor='black',
                             facecolor='white')
        tri1 = plt.Polygon([(-8, -8), (-8 + a, -8), (-8, -8 + (16 - a))], closed=True, fill=True, edgecolor='black',
                           facecolor='pink')
        tri2 = plt.Polygon([(8, -8), (-8 + a, -8), (8, -8 + a)], closed=True, fill=True, edgecolor='black',
                           facecolor='pink')
        tri3 = plt.Polygon([(-8, 8), (8 - a, 8), (-8, -8 + (16 - a))], closed=True, fill=True, edgecolor='black',
                           facecolor='pink')
        tri4 = plt.Polygon([(8, 8), (8 - a, 8), (8, -8 + a)], closed=True, fill=True, edgecolor='black',
                           facecolor='pink')
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.xticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        plt.yticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        plt.grid()
        ax.add_patch(square)
        ax.add_patch(tri1)
        ax.add_patch(tri2)
        ax.add_patch(tri3)
        ax.add_patch(tri4)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q216:
    # Domain problem 1
    def __init__(self):
        self.a = rd.randint(-40, 40) / 10
        self.b = rd.randint(-50, 50)
        self.b2 = self.b / 10
        self.query = "Does the domain of this function cover R? choice: (A) Yes (B) No"
        if self.b == 0 or (self.b > 0 and self.b % 10 == 0):
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        b = self.b2
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = a * x ** b
        plt.plot(x, cubic, color='green', linewidth=1.5)
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


class Q217:
    # joint distribution 1
    def __init__(self):
        self.lst = np.random.random(9)
        self.lst /= self.lst.sum()
        for i in range(0, 9):
            self.lst[i] = round(self.lst[i], 2)
        self.data = {
            '': ["P=1", "P=2", "P=3"],
            "S=1": self.lst[0:3],
            "S=2": self.lst[3:6],
            "S=3": self.lst[6:],
        }
        self.s1 = self.lst[0] + self.lst[3] + self.lst[6]
        self.s2 = self.lst[1] + self.lst[4] + self.lst[7]
        self.s3 = self.lst[2] + self.lst[5] + self.lst[8]

        self.df = pd.DataFrame(self.data)
        self.query = "The joint distribution of S and P is given by the following table. Compute E[P], " \
                     "the expectation of P. "
        self.answer = round(self.s1 + 2 * self.s2 + 3 * self.s3, 3)
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(10, 4))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        self.df.set_index('', inplace=True)
        Table(self.df,
              textprops={
                  'fontsize': 30,
                  'ha': 'center'
              },
              )
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q218:
    # joint distribution 2
    def __init__(self):
        self.lst = np.random.random(9)
        self.lst /= self.lst.sum()
        for i in range(0, 9):
            self.lst[i] = round(self.lst[i], 2)
        self.data = {
            '': ["P=1", "P=2", "P=3"],
            "S=1": self.lst[0:3],
            "S=2": self.lst[3:6],
            "S=3": self.lst[6:],
        }

        self.df = pd.DataFrame(self.data)
        self.query = "The joint distribution of S and P is given by the following table. Compute P[S=P]"
        self.answer = round(self.lst[0] + self.lst[4] + self.lst[8], 3)
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(10, 4))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        self.df.set_index('', inplace=True)
        Table(self.df,
              textprops={
                  'fontsize': 30,
                  'ha': 'center'
              },
              )
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q219:
    # joint distribution 3
    def __init__(self):
        self.lst = np.random.random(9)
        self.lst /= self.lst.sum()
        for i in range(0, 9):
            self.lst[i] = round(self.lst[i], 2)
        self.data = {
            '': ["P=1", "P=2", "P=3"],
            "S=1": self.lst[0:3],
            "S=2": self.lst[3:6],
            "S=3": self.lst[6:],
        }
        self.symbol = rd.choice(['>', '<'])
        self.df = pd.DataFrame(self.data)
        self.query = f"The joint distribution of S and P is given by the following table. Compute P[S{self.symbol}=P]"
        if self.symbol == '>':
            self.answer = round(self.lst[0] + self.lst[1] + self.lst[2] + self.lst[4] + self.lst[5] + self.lst[8], 3)
        else:
            self.answer = round(self.lst[0] + self.lst[3] + self.lst[6] + self.lst[4] + self.lst[7] + self.lst[8], 3)
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(10, 4))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        self.df.set_index('', inplace=True)
        Table(self.df,
              textprops={
                  'fontsize': 30,
                  'ha': 'center'
              },
              )
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q220:
    # complete graph 1
    def __init__(self):
        self.lst = [rd.randint(0, 1), rd.randint(0, 1), rd.randint(0, 1), rd.randint(0, 1), rd.randint(0, 1),
                    rd.randint(0, 1)]
        self.query = "Is the following graph a complete graph?  choice: (A) Yes (B) No"
        if sum(self.lst) == 6:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.scatter(8, 8, color='black', s=40)
        plt.scatter(-8, 8, color='black', s=40)
        plt.scatter(-8, -8, color='black', s=40)
        plt.scatter(8, -8, color='black', s=40)
        plt.xlim(-12 * 1.1, 12 * 1.1)
        plt.ylim(-12 * 1.1, 12 * 1.1)

        plt.xticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        plt.yticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        ax = plt.gca()
        plt.gcf().set_size_inches(6, 6)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        if self.lst[0] == 1:
            plt.plot([8, 8], [-8, 8], color='black')
        if self.lst[1] == 1:
            plt.plot([-8, 8], [-8, 8], color='black')
        if self.lst[2] == 1:
            plt.plot([-8, -8], [-8, 8], color='black')
        if self.lst[3] == 1:
            plt.plot([-8, 8], [8, 8], color='black')
        if self.lst[4] == 1:
            plt.plot([-8, 8], [-8, -8], color='black')
        if self.lst[5] == 1:
            plt.plot([-8, 8], [8, -8], color='black')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

