import math
import shutil
import networkx as nx
import pyglet
from math import sin, cos, pi
import os.path
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import pandas as pd
import plottable
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from plottable import Table
import mpl_toolkits.axisartist as ax
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image, ImageDraw, ImageFont
from matplotlib.patches import *


class Q261:
    # mirror 1
    def __init__(self):
        lst = ['A', 'B', 'C']
        self.x = rd.randint(1, 6)
        self.y = rd.randint(1, 6)
        self.up = rd.choice(lst)
        lst.remove(self.up)
        self.asy = rd.choice(lst)
        lst.remove(self.asy)
        self.query = "An object is placed near a plane mirror, as shown above. Which of the labeled points is the " \
                     "position of the image? choice: (A) point A (B) point B (C) point C"
        self.answer = rd.choice(lst)
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        x = self.x
        y = self.y
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.vlines(0, -6, 6, linestyles='dashed', colors='black', linewidth=3)
        plt.scatter(x, y, color='black')
        plt.scatter(-x, -y, color='black')
        plt.scatter(-x, y, color='black')
        plt.scatter(x, -y, color='black')
        plt.text(-0.6, 6.2, "Mirror", fontsize=18)
        plt.text(-x - 1, -y - 1, "objection", fontsize=18, rotation=90)
        plt.text(x - 0.1, y + 0.5, f"{self.asy}", fontsize=18)
        plt.text(-x - 0.1, y + 0.5, f"{self.up}", fontsize=18)
        plt.text(x - 0.1, -y - 1, f"{self.answer}", fontsize=18)
        plt.grid()
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q262:
    # mirror 2
    def __init__(self):
        lst = ['A', 'B', 'C']
        self.x = rd.randint(1, 6)
        self.y = rd.randint(1, 6)
        self.right = rd.choice(lst)
        lst.remove(self.right)
        self.asy = rd.choice(lst)
        lst.remove(self.asy)
        self.query = "An object is placed near a plane mirror, as shown above. Which of the labeled points is the " \
                     "position of the image? choice: (A) point A (B) point B (C) point C"
        self.answer = rd.choice(lst)
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        x = self.x
        y = self.y
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.hlines(0, -6, 6, linestyles='dashed', colors='black', linewidth=3)
        plt.scatter(x, y, color='black')
        plt.scatter(-x, -y, color='black')
        plt.scatter(-x, y, color='black')
        plt.scatter(x, -y, color='black')
        plt.text(6.2, -0.6, "Mirror", fontsize=18, rotation=90)
        plt.text(-x - 1, -y - 1, "objection", fontsize=18)
        plt.text(x - 0.1, y + 0.5, f"{self.asy}", fontsize=18)
        plt.text(-x - 0.1, y + 0.5, f"{self.answer}", fontsize=18)
        plt.text(x - 0.1, -y - 1, f"{self.right}", fontsize=18)
        plt.grid()
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q263:
    # mirror 3
    def __init__(self):
        self.x = rd.randint(1, 99)
        self.y = rd.randint(1, 99)
        self.query = "An inverse expression is placed near a mirror. The mirror shows its original appearance, " \
                     "but due to the ink dot on the mirror, part of the formula is obscured. Find the value of '?' in " \
                     "this expression. "
        self.answer = self.x + self.y
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        x = self.x
        y = self.y
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.hlines(0, -6, 6, linestyles='dashed', colors='black', linewidth=3)
        plt.text(6.2, -0.6, "Mirror", fontsize=12)
        plt.text(-3, -1.5, f"{x} + {y} = ?", fontsize=30, rotation=180)
        plt.text(-3, 1.5, fr"{x} + $\blacksquare$ = ?", fontsize=30)
        plt.grid()
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q264:
    # lens 1
    def __init__(self):
        self.x = rd.randint(20, 60) / 10
        self.query = "An object is located a distance from a thin converging lens of focal length f as shown in the " \
                     "diagram below. The distance of the image v from the lens will be ____.  choice: (A) f<v<2f (B) " \
                     "v=2f (C) v>2f (D) 0 (No image) "
        if 2 < self.x < 4:
            self.answer = "C"
        elif self.x == 2:
            self.answer = "D"
        elif self.x == 4:
            self.answer = "A"
        elif self.x > 4:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        x = self.x
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ellipse = Ellipse((0, 0), 0.5, 6, color="black", fill=False, linewidth=1.5)
        ax.add_patch(ellipse)
        plt.scatter(-x, 0, color='black')
        plt.scatter(-2, 0, color='black')
        plt.scatter(-4, 0, color='black')
        plt.text(-2, 0.5, "F", fontsize=16)
        plt.text(-4, 0.5, "P", fontsize=16)
        plt.text(-x - 1, -1, "objection", fontsize=16)
        plt.text(-2, -3.5, "|-----f-----|", fontsize=16, ha='center')
        plt.hlines(0, -6, 6, colors='black', linewidth=1.5)
        ax.annotate('', xy=(-x, 0), xytext=(-x, -0.6), arrowprops=dict(arrowstyle="->", color='black', linewidth=1))
        plt.grid()
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q265:
    # lens 2
    def __init__(self):
        self.x = rd.randint(20, 60) / 10
        self.f = rd.randint(10, 99)
        self.u = round(self.x * (self.f / 2), 0)
        while self.f == self.u:
            self.f = rd.randint(10, 99)
            self.u = round(self.x * (self.f / 2), 0)
        self.query = f"An object is located a distance {self.u} from a thin converging lens of focal length {self.f} " \
                     f"as shown in the diagram below. Find the distance of the image from the lens. "
        self.answer = (self.f * self.u) / (self.u - self.f)
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        x = self.x
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ellipse = Ellipse((0, 0), 0.5, 6, color="black", fill=False, linewidth=1.5)
        ax.add_patch(ellipse)
        plt.scatter(-x, 0, color='black')
        plt.scatter(-2, 0, color='black')
        plt.scatter(-4, 0, color='black')
        plt.text(-2, 0.5, "F", fontsize=16)
        plt.text(-4, 0.5, "P", fontsize=16)
        plt.text(-x - 1, -1, "objection", fontsize=16)
        plt.text(-2, -3.5, f"|----{self.f}----|", fontsize=16, ha='center')
        plt.hlines(0, -6, 6, colors='black', linewidth=1.5)
        ax.annotate('', xy=(-x, 0), xytext=(-x, -0.6), arrowprops=dict(arrowstyle="->", color='black', linewidth=1))
        plt.grid()
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q266:
    # Velocity and Time 1
    def __init__(self):
        self.b = rd.randint(1, 6)
        self.base = rd.randint(3, 7)
        self.answer = self.base
        self.query = "The velocity vs. time graph for the motion of a car on a straight track is shown in the " \
                     "diagram. The thick line represents the velocity. At which " \
                     "time the car change the direction to drive?"
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(2, 8, 200, endpoint=True)
        b = self.b
        base = self.base
        a = -b / base
        line = a * x + b
        plt.plot(x, line, color='black', linewidth=1.5)
        plt.xlim(0, 6 * 1.1)
        plt.ylim(-5 * 1.1, 5 * 1.1)

        plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        plt.hlines(2 * a + b, 0, 2, colors='black')
        plt.hlines(8 * a + b, 8, 10, colors='black')
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(-1, -1, "Velocity", fontsize=12, rotation=90)
        plt.text(5, -6, "Time", fontsize=12)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q267:
    # velocity and time 2
    def __init__(self):
        self.a = rd.randint(-5, 5) / 500
        self.b = rd.randint(-5, 5) / 500
        self.c = rd.randint(-5, 5) / 500
        self.d = rd.randint(-3, 3)
        if 1000 * self.a + 100 * self.b + 10 * self.c > 5:
            self.d = -5
        elif 1000 * self.a + 100 * self.b + 10 * self.c < -5:
            self.d = 6
        self.integral = 1/4 * self.a * (10 ** 4 - 1) + 1/3 * self.b * (10 ** 3 - 1) + 1/2 * self.c * (100 - 1) + self.d * 9
        self.query = "The velocity vs. time graph for the motion of a car on a straight track is shown in the " \
                     "diagram. The thick line represents the velocity. Assume that the car starts at the origin x = 0 " \
                     "and the positive velocity represents moving forward. The position of car at t=10s is ____.  " \
                     "choice: (A) in front of the start  (B) behind the start (C) at the start"
        if self.integral > 0:
            self.answer = "A"
        elif self.integral < 0:
            self.answer = "B"
        else:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        constant_a = self.a
        constant_b = self.b
        constant_c = self.c
        constant_d = self.d
        x = np.linspace(0, 10, 200, endpoint=True)
        cubic = constant_a * x ** 3 + constant_b * x ** 2 + constant_c * x + constant_d
        plt.plot(x, cubic, color='black', linewidth=1.5)
        plt.xlim(0, 6 * 1.1)
        plt.ylim(-5 * 1.1, 5 * 1.1)

        plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(-1, -1, "Velocity", fontsize=12, rotation=90)
        plt.text(-1, -1, "Velocity", fontsize=12, rotation=90)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q268:
    # velocity and time 3
    def __init__(self):
        self.x1 = rd.randint(1, 8)
        self.y1 = rd.randint(1, 9)
        self.x2 = rd.randint(self.x1 + 1, 10)
        self.query = "The motion of a car in a straight line is shown in the graph below. After 10 seconds, " \
                     "how far is the car from the starting point? "
        if self.x2 == 10:
            self.answer = (10 + 10 - self.x1) * self.y1 / 2
        else:
            self.answer = 1/2 * self.x1 * self.y1 + 1/2 * (10 - self.x2) * self.y1 + (self.x2 - self.x1) * self.y1
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        plt.plot([0, x1], [0, y1], color='black')
        plt.plot([x1, x2], [y1, y1], color='black')
        plt.plot([x2, 10], [y1, 0], color='black')
        plt.xlim(0, 10)
        plt.ylim(0, 10)

        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.text(-1, 4, "Velocity (m/s)", fontsize=12, rotation=90)
        plt.text(4.5, -1.2, "Time (s)", fontsize=12)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q269:
    # acceleration and Time
    def __init__(self):
        self.x1 = rd.randint(1, 8)
        self.y1 = rd.randint(1, 9)
        self.x2 = rd.randint(self.x1 + 1, 10)
        self.query = "Starting from rest at time t = 0, a car moves in a straight line with an acceleration given by " \
                     "the accompanying graph. What is the speed of the car at t = 10s ? "
        self.answer = 1/2 * (self.x1 + self.x2) * self.y1
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        plt.plot([0, x1], [y1, y1], color='black')
        plt.plot([x1, x2], [y1, 0], color='black')
        plt.xlim(0, 10)
        plt.ylim(0, 10)

        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.text(-1, 3, "acceleration (m/s^2)", fontsize=12, rotation=90)
        plt.text(4.5, -1, "Time (s)", fontsize=12)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q270:
    # Newton's second law
    def __init__(self):
        self.mass = rd.randint(1, 5)
        self.x1 = rd.randint(1, 8)
        self.y1 = rd.randint(1, 9)
        self.query = f"A block of mass {self.mass} kg, initially at rest, is pulled along a frictionless, horizontal " \
                     f"surface with a force shown as a function of time t by the graph above. What is the " \
                     f"acceleration of the block at t = {self.x1}s ? "
        self.answer = self.y1 / self.mass
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        x1 = self.x1
        y1 = self.y1
        plt.plot([0, x1], [0, y1], color='black')
        plt.plot([x1, 10], [y1, y1], color='black')
        plt.xlim(0, 10)
        plt.ylim(0, 10)

        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.text(-1, 4.5, "Force (N)", fontsize=12, rotation=90)
        plt.text(4.5, -1.2, "Time (s)", fontsize=12)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q271:
    # kinetic friction
    def __init__(self):
        self.x = rd.randint(10, 90) / 10
        self.pull = round(rd.randint(100, 999) / 10, 1)
        self.coe = rd.randint(10, 90) / 100
        self.query = f"The {self.x} kg box shown in the figure to the right is sliding to the right along the floor. " \
                     f"A horizontal force of {self.pull} N is being applied to the right. The coefficient of kinetic " \
                     f"friction between the box and the floor is {self.coe}. The box is moving with:____.  choice: (" \
                     f"A) acceleration to the left (B) acceleration to the right (C) constant velocity "
        if self.x * 9.8 * self.coe > self.pull:
            self.answer = "A"
        elif self.x * 9.8 * self.coe < self.pull:
            self.answer = "B"
        elif self.x * 9.8 * self.coe == self.pull:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
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
        plt.hlines(0, -4, 4, colors='black', linewidth=1.5)
        plt.text(-0.8, 0.8, f"{self.x}0 kg", fontsize=12)
        square = plt.Polygon([(1, 2), (-1, 2), (-1, 0), (1, 0)], closed=True, fill=True, edgecolor='black',
                             facecolor='white')
        ax.add_patch(square)
        ax.annotate('', xy=(4, 1), xytext=(1, 1), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        plt.text(2, 1.3, f"{self.pull} N", fontsize=12)
        ax.annotate('', xy=(2, 3), xytext=(0, 3), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        plt.text(-0.7, 2.8, "V", fontsize=12)
        plt.grid()
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q272:
    # vector, x component
    def __init__(self):
        lst = list(range(-6, 6))
        lst.remove(0)
        self.x = rd.randint(-6, 6)
        self.y = rd.choice(lst)
        self.query = "What is the x-component of this vector?"
        self.answer = self.x
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        x = self.x
        y = self.y
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.annotate('', xy=(x, y), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color='blue', linewidth=2))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q273:
    # vector, y component
    def __init__(self):
        lst = list(range(-6, 6))
        lst.remove(0)
        self.x = rd.randint(-6, 6)
        self.y = rd.choice(lst)
        self.query = "What is the y-component of this vector?"
        self.answer = self.y
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        x = self.x
        y = self.y
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.annotate('', xy=(x, y), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color='orange', linewidth=2))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q274:
    # calculate impulse
    def __init__(self):
        self.x1 = rd.randint(1, 8)
        self.y1 = rd.randint(1, 9) * 10
        self.x2 = rd.randint(self.x1 + 1, 10)
        self.query = "The graph shows smoothed force-versus-time data for a collision. Find the impulse delivered by " \
                     "the force. "
        self.answer = (self.x2 - self.x1) * self.y1
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        plt.plot([0, x1], [0, 0], color='violet', linewidth=2)
        plt.plot([x1, x1], [0, y1], color='violet', linewidth=2)
        plt.plot([x1, x2], [y1, y1], color='violet', linewidth=2)
        plt.plot([x2, x2], [y1, 0], color='violet', linewidth=2)
        plt.plot([x2, 10], [0, 0], color='violet', linewidth=2)
        plt.xlim(0, 10)
        plt.ylim(0, 10)

        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        plt.text(-1, 30, "Force (N)", fontsize=12, rotation=90)
        plt.text(4.5, -10, "Time (s)", fontsize=12)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q275:
    # Time of the ball in the air
    def __init__(self):
        self.a1 = rd.randint(1, 100) / 5
        self.b1 = rd.randint(10, 100)
        self.a2 = rd.randint(1, 100) / 5
        self.b2 = rd.randint(10, 100)
        self.v1 = self.b1 * self.b1 / (4 * self.a1)
        self.v2 = self.b2 * self.b2 / (4 * self.a2)
        self.query = "Ball 1 and ball 2 follow the paths shown, where the darkblue path is Ball 1 and the green path " \
                     "is Ball 2. Which ball is in the air for a longer time? Assume that you can ignore air " \
                     "resistance for this problem.  choice: (A) Ball 1 (B) Ball 2 (C) The amount time of balls in air " \
                     "is same "
        if self.v1 > self.v2:
            self.answer = "A"
        elif self.v1 < self.v2:
            self.answer = "B"
        elif self.v1 == self.v2:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(0, 10, 200, endpoint=True)
        a1 = self.a1
        b1 = self.b1
        a2 = self.a2
        b2 = self.b2
        y1 = -x * (a1 * x - b1)
        y2 = -x * (a2 * x - b2)
        plt.plot(x, y1, color='darkblue', linewidth=2.5)
        plt.plot(x, y2, color='lightgreen', linewidth=2.5)
        plt.autoscale()
        plt.ylim(0, top=None)
        plt.grid()
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.tight_layout()
        plt.savefig(dest_image_path)
        plt.close()


class Q276:
    # electrical circuits 1
    def __init__(self):
        self.r1 = rd.randint(1, 99)
        self.r2 = rd.randint(1, 99)
        self.r3 = rd.randint(1, 99)
        self.r12 = self.r1 + self.r2
        self.query = "refer to the following diagram that shows part of a closed electrical circuit. What is the " \
                     "electrical resistance of the part of the circuit shown between point X and point Y? "
        self.answer = (self.r12 * self.r3) / (self.r12 + self.r3)
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        Img = Image.open('temp_image/Q276temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        plt.text(360, 50, fr"{self.r1}$\Omega$", fontsize=14)
        plt.text(610, 50, fr"{self.r2}$\Omega$", fontsize=14)
        plt.text(500, 460, fr"{self.r3}$\Omega$", fontsize=14)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q277:
    # electrical circuits 2
    def __init__(self):
        self.r1 = rd.randint(1, 99)
        self.r2 = rd.randint(1, 99)
        self.r3 = rd.randint(1, 99)
        self.v = rd.randint(1, 99)
        self.r23 = (self.r2 * self.r3) / (self.r2 + self.r3)
        self.r = self.r1 + self.r23
        self.query = "refer to the following diagram that shows a closed electrical circuit. What is the " \
                     "electric current of the circuit? "
        self.answer = self.v / self.r
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        Img = Image.open('temp_image/Q277temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        plt.text(270, 185, fr"R1 = {self.r1}$\Omega$", fontsize=16)
        plt.text(700, 35, fr"R2 = {self.r2}$\Omega$", fontsize=16)
        plt.text(700, 520, fr"R3 = {self.r3}$\Omega$", fontsize=16)
        plt.text(530, 750, f"U = {self.v}V", fontsize=16)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q278:
    # electrical circuits 3
    def __init__(self):
        self.r1 = rd.randint(1, 10)
        self.r2 = rd.randint(10, 40)
        self.r3 = self.r2 * 2 + rd.randint(0, 5)
        self.v1 = rd.randint(1, 10)
        self.v2 = rd.randint(11, 20)
        self.v3 = self.v2 * 2 + rd.randint(1, 5)
        self.i = (self.v3 - self.v2)/(self.r2 + self.r3)
        self.u = self.i * self.r2
        self.query = "Find the potential difference Uab between points a and b."
        self.answer = self.r1 + self.v1 + self.u
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "undergraduate"

    def draw(self, num):
        Img = Image.open('temp_image/Q278temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        plt.text(160, 90, fr"{self.r1}$\Omega$", fontsize=16)
        plt.text(145, 30, fr"{self.r3}$\Omega$", fontsize=16)
        plt.text(155, 170, fr"{self.r2}$\Omega$", fontsize=16)
        plt.text(350, 110, f"{self.v3}V", fontsize=16)
        plt.text(0, 115, f"{self.v2}V", fontsize=16)
        plt.text(90, 100, f"{self.v1}V", fontsize=16)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q279:
    # planet orbiting speed
    def __init__(self):
        self.theta1 = rd.randint(10, 360) * np.pi / 180
        self.theta2 = rd.randint(10, 360) * np.pi / 180
        self.dist1 = np.sqrt((5 * np.cos(self.theta1) - (-2))**2 + (3 * np.sin(self.theta1))**2)
        self.dist2 = np.sqrt((5 * np.cos(self.theta2) - (-2)) ** 2 + (3 * np.sin(self.theta2)) ** 2)
        self.query = "Two planets travel in an elliptical orbit about the sun as shown. Which planet have greater " \
                     "orbital speed?  choice: (A) Blue planet (B) Orange planet (C) Both two planet have the same " \
                     "speed "
        if self.dist1 > self.dist2:
            self.answer = "B"
        elif self.dist1 < self.dist2:
            self.answer = "A"
        elif self.dist1 == self.dist2:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        theta1 = self.theta1
        theta2 = self.theta2
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        ellipse = Ellipse((0, 0), 10, 6, color="black", fill=False, linewidth=2)
        ax.add_patch(ellipse)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(-2, 0, color="red", s=100)
        plt.text(-1.5, -0.3, "sun", fontsize=12)
        plt.scatter(5 * np.cos(theta1), 3 * np.sin(theta1), color="blue", s=50)
        plt.scatter(5 * np.cos(theta2), 3 * np.sin(theta2), color="orange", s=50)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q280:
    # planet orbiting acceleration
    def __init__(self):
        self.theta1 = rd.randint(10, 360) * np.pi / 180
        self.theta2 = rd.randint(10, 360) * np.pi / 180
        self.dist1 = np.sqrt((5 * np.cos(self.theta1) - (-2)) ** 2 + (3 * np.sin(self.theta1)) ** 2)
        self.dist2 = np.sqrt((5 * np.cos(self.theta2) - (-2)) ** 2 + (3 * np.sin(self.theta2)) ** 2)
        self.query = "Two planets travel in an elliptical orbit about the sun as shown. Which planet have greater " \
                     "acceleration?  choice: (A) Brown planet (B) Pink planet (C) Both two planet have the same " \
                     "acceleration "
        if self.dist1 > self.dist2:
            self.answer = "B"
        elif self.dist1 < self.dist2:
            self.answer = "A"
        elif self.dist1 == self.dist2:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        theta1 = self.theta1
        theta2 = self.theta2
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        ellipse = Ellipse((0, 0), 10, 6, color="black", fill=False, linewidth=2)
        ax.add_patch(ellipse)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(-2, 0, color="red", s=100)
        plt.text(-1.5, -0.3, "sun", fontsize=12)
        plt.scatter(5 * np.cos(theta1), 3 * np.sin(theta1), color="brown", s=50)
        plt.scatter(5 * np.cos(theta2), 3 * np.sin(theta2), color="pink", s=50)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()
