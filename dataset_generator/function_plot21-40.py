import math
import shutil

import pyglet
from math import sin, cos, pi
import os.path
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from PIL import Image, ImageDraw, ImageFont
from matplotlib.patches import *


class Q21:
    # watch problem 1
    def __init__(self):
        self.lst = [0, 15, 30, 45]
        self.mPointer = rd.choice(self.lst)
        self.hPointer = rd.randint(1, 12)
        self.query = f"What time is shown? Please answer in the form like __:__."
        self.answer = f"{self.hPointer}:{self.mPointer}"
        self.answer_type = "text"
        self.subject = "arithmetic"
        self.level = "elementary school"

    class Watch(pyglet.window.Window):
        def __init__(self, x, y, R=200, width=800, height=500, caption='pointer'):
            super().__init__(width, height, caption=caption)
            pyglet.gl.glClearColor(1, 1, 1, 1)
            self.batch = pyglet.graphics.Batch()
            self.circle_b = pyglet.shapes.Circle(x, y, R * 1.1, color=(255, 0, 255, 255), batch=self.batch)
            self.circle = pyglet.shapes.Circle(x, y, R * 1.05, color=(248, 250, 252, 255), batch=self.batch)
            self.scales = [pyglet.shapes.Line(x + R * cos(i * pi / 30), y + R * sin(i * pi / 30),
                                              x + R * 0.95 * cos(i * pi / 30), y + 0.95 * R * sin(i * pi / 30),
                                              width=3, color=(215, 220, 230, 255), batch=self.batch) for i in range(60)]
            for i, scale in enumerate(self.scales):
                if i % 5 == 0:
                    scale.width, scale.x2, scale.y2 = 5, x + R * 0.92 * cos(i * pi / 30), y + 0.92 * R * sin(
                        i * pi / 30)
            self.labels = [pyglet.text.Label(str((2 - i) % 12 + 1), font_size=R * 0.12, color=(0, 0, 0, 255),
                                             x=x + R * 0.82 * cos(i * pi / 6),
                                             y=y + 0.82 * R * sin(i * pi / 6) - R * 0.06,
                                             anchor_x='center',
                                             batch=self.batch) for i in range(12)]
            self.circle1 = pyglet.shapes.Circle(x, y, R * 0.08, color=(42, 43, 48, 255), batch=self.batch)
            self.hour = pyglet.shapes.Line(x, y, x + R * 0.5, y, width=9, color=(42, 43, 48, 255), batch=self.batch)
            self.minute = pyglet.shapes.Line(x, y, x + R * 0.7, y, width=7, color=(70, 71, 75, 255), batch=self.batch)
            self.circle2 = pyglet.shapes.Circle(x, y, R * 0.05, color=(240, 70, 20, 255), batch=self.batch)
            self.circle3 = pyglet.shapes.Circle(x, y, R * 0.02, color=(255, 255, 255, 255), batch=self.batch)
            self.minute.anchor_position = (R * 0.1, 0)

        def update(self, m, h):
            self.minute.rotation = -90 + m * 6
            self.hour.rotation = -90 + h % 12 * 30 + m / 2

        def on_draw(self):
            self.clear()
            self.batch.draw()
            destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
            pyglet.image.get_buffer_manager().get_color_buffer().get_image_data().save(os.path.join(destination_folder,
                                                                                                    f"image/Q21temp.png"))

        def close_window(self, dt):
            self.close()

        def run(self):
            pyglet.clock.schedule_once(self.close_window, 1)
            pyglet.app.run()

    def draw(self, num):
        watch = self.Watch(400, 250)
        watch.update(self.mPointer, self.hPointer)
        watch.run()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q21temp.png"), dest_image_path)


class Q22:
    # easy matrix problem 1
    def __init__(self):
        self.col1 = np.random.randint(0, 2, 3)
        self.col2 = np.random.randint(0, 2, 3)
        self.col3 = np.random.randint(0, 2, 3)
        self.query = "What is the difference between the number of black squares and the number of white squares?"
        self.answer = abs(9 - 2 * sum(self.col1) - 2 * sum(self.col2) - 2 * sum(self.col3))
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def draw(self, num):
        mat = np.array([self.col1, self.col2, self.col3])
        plt.imshow(mat, cmap="gray")
        constant_a = 0.5
        constant_b = 1.5
        plt.vlines(constant_a, -0.5, 2.5, colors="gray")
        plt.vlines(constant_b, -0.5, 2.5, colors="gray")
        plt.hlines(constant_a, -0.5, 2.5, colors="gray")
        plt.hlines(constant_b, -0.5, 2.5, colors="gray")
        plt.xticks([])
        plt.yticks([])
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q23:
    # find the largest zero of cubic function
    def __init__(self):
        self.a = rd.randint(-5, 5)
        self.b = rd.randint(-5, 5)
        self.c = rd.randint(-5, 5)
        self.query = "Find the largest zero of this cubic function."
        self.answer = max(self.a, self.b, self.c)
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = x ** 3 - (self.a + self.b + self.c) * x ** 2 + (
                self.a * self.b + self.c * self.b + self.a * self.c) * x - self.a * self.b * self.c
        plt.plot(x, cubic, color='blue', linewidth=1.2)

        plt.xlim(-5 * 1.1, 5 * 1.1)
        plt.ylim(-5 * 1.1, 5 * 1.1)

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


class Q24:
    # from small triangle calculating the whole triangle
    def __init__(self):
        self.small = rd.randint(1, 10)
        self.whole = self.small * 4
        self.query = f"As shown in the figure, in triangle △ABC, points D, E, and F are the midpoints of each side. " \
                     f"If the area of △ABC is {self.whole} cm², what is the area of △DEF?"
        self.answer = self.small
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q24temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q24temp.png"), dest_image_path)


class Q25:
    # draw an equation system
    def __init__(self):
        self.x = rd.randint(1, 10)
        self.y = rd.randint(1, 10)
        self.z = rd.randint(1, 10)
        self.u = rd.randint(2, 10)
        self.x = rd.randint(1, 10)
        self.symbol = rd.choice(["+", "-", "*", "/"])
        self.eq1 = round(eval(f"self.x + self.y - self.z {self.symbol} self.u"), 3)
        self.query = "What is the missing computed symbol? Choices: (A) + (B) - (C) * (D) /"
        if self.symbol == '+':
            self.answer = "A"
        elif self.symbol == '-':
            self.answer = "B"
        elif self.symbol == '*':
            self.answer = "C"
        else:
            self.answer = "D"
        self.answer_type = "multiple choice"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def draw(self, num):
        text = f"{self.x} + {self.y} - {self.z} __ {self.u} = {self.eq1}"
        width = 400
        height = 200
        image = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        x1, y1, x2, y2 = draw.textbbox((400, 400), text, font=ImageFont.truetype("arial.ttf", 40))
        text_width, text_height = x2 - x1, y2 - y1
        x = (width - text_width) / 2
        y = (height - text_height) / 2
        draw.text((x, y), text, fill=(0, 0, 0), font=ImageFont.truetype("arial.ttf", 40))
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        image.save(dest_image_path)
        plt.close()


class Q26:
    # find the area of wedge sector
    def __init__(self):
        self.angle = rd.choice([30, 60, 90, 120])
        self.r = rd.randint(1, 5)
        self.query = f"The radius of the circle above is {self.r} and the angle of sector = {self.angle}°. " \
                     f"What is the area of the shaded section of the circle?"
        self.answer = self.r * self.r * self.angle / 360 * np.pi
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
        wedge = Wedge((0, 0), 2, 0, self.angle, color="gray")
        circle = Circle((0, 0), 2, color="black", fill=False)
        ax.add_patch(circle)
        ax.add_patch(wedge)
        plt.text(-0.5, -0.5, f'{self.angle}°', fontsize=12)
        plt.text(1, -0.5, f'r = {self.r}', fontsize=12)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q27:
    # calculate the cone volume through 2D image

    def __init__(self):
        self.r = rd.choice([2, 4, 8, 12])
        self.query = f"A three-quarter sector of a circle of radius {self.r} inches together with its interior can be " \
                     f"rolled up to form the lateral surface area of a right circular cone by taping together along " \
                     f"the two radii shown. What is the volume of the cone in cubic inches? "
        self.R = 3 / 4 * self.r
        self.h = np.sqrt(self.r * self.r - self.R * self.R)
        self.answer = 1 / 3 * np.pi * self.R * self.R * self.h
        self.answer_type = "float"
        self.subject = "solid geometry"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        square = plt.Polygon([(0, -0.2), (0.2, -0.2), (0.2, 0), (0, 0)], closed=True, fill=False, edgecolor='black')
        ax.add_patch(square)
        wedge = Wedge((0, 0), 2, 0, 270, color="black", fill=False)
        ax.add_patch(wedge)
        plt.text(0.7, -0.7, f'r = {self.r}', fontsize=18)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q28:
    # find the ration of x and y
    def __init__(self):
        self.x = rd.randint(1, 5)
        self.h = rd.randint(4, 10)
        self.d = rd.randint(self.x + 1, 10)
        self.y = self.h / ((self.d - self.x) / self.x + 1)
        self.query = "The two rectangles shown in the picture have the same area. what is the ratio x: y."
        self.answer = self.d / self.h
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(0, 10 * 1.1)
        plt.ylim(0, 10 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        s1 = plt.Polygon([(self.x, 0), (self.d, 0), (self.d, self.y), (self.x, self.y)], closed=True, fill=True,
                         edgecolor='black', facecolor='azure')
        s2 = plt.Polygon([(0, self.y), (self.x, self.y), (self.x, self.h), (0, self.h)], closed=True, fill=True,
                         edgecolor='black', facecolor='azure')
        ax.add_patch(s1)
        ax.add_patch(s2)
        plt.xticks([self.d])
        plt.yticks([self.h])
        plt.text(self.x - 0.1, -0.5, "x", fontsize=12)
        plt.text(-0.5, self.y, "y", fontsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q29:
    # the number of square is odd or even
    def __init__(self):
        self.number = rd.randint(1, 4)
        self.show = rd.sample(range(1, 5), self.number)
        self.query = "Is the number of square even or odd? choice: (A) even (B) odd"
        if self.number % 2 == 0:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        square1 = plt.Polygon([(1, 1), (1, 2), (2, 2), (2, 1)], closed=True, fill=True, edgecolor='black',
                              facecolor='azure')
        square2 = plt.Polygon([(-1, -1), (-1, -2), (-2, -2), (-2, -1)], closed=True, fill=True, edgecolor='black',
                              facecolor='azure')
        square3 = plt.Polygon([(-1, 1), (-1, 2), (-2, 2), (-2, 1)], closed=True, fill=True, edgecolor='black',
                              facecolor='azure')
        square4 = plt.Polygon([(1, -1), (1, -2), (2, -2), (2, -1)], closed=True, fill=True, edgecolor='black',
                              facecolor='azure')
        if 1 in self.show:
            ax.add_patch(square1)
        if 2 in self.show:
            ax.add_patch(square2)
        if 3 in self.show:
            ax.add_patch(square3)
        if 4 in self.show:
            ax.add_patch(square4)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q30:
    # pie 2
    def __init__(self):
        self.sizes = np.random.randint(1, 10, 4)
        self.query = "Is purple greater orange? Choices: (A) yes (B) no"
        if self.sizes[3] > self.sizes[2]:
            self.answer = 'A'
        else:
            self.answer = 'B'
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "elementary school"

    def draw(self, num):
        labels = ['red', 'blue', 'orange', 'purple']
        plt.figure(figsize=(5, 5))
        plt.pie(self.sizes, labels=None, autopct=None, startangle=90, colors=['red', 'blue', 'orange', 'purple'])
        plt.legend(labels)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q31:
    # define a new formula symbol
    def __init__(self):
        self.a = rd.randint(1, 10)
        self.b = rd.randint(1, 10)
        self.query = "a, b are two arbitrary number. According to the calculation of first row, find the value of " \
                     "second row of calculations. "
        self.answer = 2 * self.a + self.b
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        concept = "a " + r'$\bigstar$' + " b = 2a + b"
        ques = f"{self.a} " + r'$\bigstar$' + f" {self.b} = ?"
        plt.text(-1.5, 1, concept, fontsize=24)
        plt.text(-1.5, -1, ques, fontsize=24)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q32:
    # Ptolemy's theorem
    def __init__(self):
        self.AD = rd.randint(1, 5)
        self.DC = rd.randint(self.AD + 1, 7)
        self.BC = rd.randint(self.DC + 1, 9)
        self.AB = rd.randint(self.BC, 10)
        self.query = f"Let ABCD be a cyclic convex quadrilateral, AD = {self.AD}, DC = {self.DC}, BC = {self.BC}, " \
                     f"AB = {self.AB}. Determine the value of AC * BD "
        self.answer = self.AB * self.DC + self.AD * self.BC
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q32temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q32temp.png"), dest_image_path)


class Q33:
    # monotony of cubic function
    def __init__(self):
        self.a = rd.randint(-5, 5)
        self.b = rd.randint(-5, 5)
        self.c = rd.randint(-5, 5)
        self.delta = 4 * self.b * self.b - 12 * self.a * self.c
        self.query = "Is this a monotonic function? choice: (A) Yes (B) No"
        if self.delta < 0 or (self.b == 0 and self.a == 0):
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):

        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = self.a * x ** 3 + self.b * x ** 2 + self.c * x
        plt.plot(x, cubic, color='blue', linewidth=1.5)

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


class Q34:
    # parallelogram area
    def __init__(self):
        self.short = rd.randint(5, 13)
        self.long = self.short * 2 + rd.randint(1, 3)
        self.part = rd.randint(3, 4)
        self.query = "What is the area of this parallelogram?"
        self.answer = self.long * np.sqrt(self.short * self.short - self.part * self.part)
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
        ax.add_patch(square2)
        plt.text(-3, 0.2, f"{self.short}ft", fontsize=10)
        plt.text(-2.8, -1.4, f"{self.part}ft", fontsize=10)
        plt.text(0, 1.2, f"{self.long}ft", fontsize=10)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q35:
    # find unknown number
    def __init__(self):
        self.a = rd.randint(1, 100)
        self.b = rd.randint(1, 100)
        self.c = rd.randint(1, 100)
        self.query = "Find the value of the black square."
        self.answer = self.a + self.b - self.c
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.text(-2, 0, r"$\blacksquare$" + f" + {self.c} = {self.a} + {self.b} ", fontsize=30)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q36:
    # find the volume of the rectangular prism
    def __init__(self):
        self.a = rd.randint(3, 8)
        self.b = self.a + rd.randint(1, 3)
        self.c = self.b + rd.randint(1, 2)
        self.query = "Find the volume of the rectangular prism."
        self.answer = self.a * self.b * self.c
        self.answer_type = "float"
        self.subject = "solid geometry"
        self.level = "high school"

    def draw(self, num):
        fig = plt.figure()
        fig.set_size_inches(4, 4, 4)
        x, y, z = np.indices((2, 2, 2))
        filled = np.ones((1, 1, 1))
        ax = fig.add_subplot(projection='3d')
        ax.voxels(x, y, z, filled=filled, color='azure', edgecolor='black')
        ax.text(0.3, 0, -0.3, f"{self.c}ft", fontsize=12)
        ax.text(0, -0.3, 0.7, f"{self.a}ft", fontsize=12)
        ax.text(-0.4, 0.8, 0.8, f"{self.b}ft", fontsize=12)
        ax.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q37:
    # Bar chart 3
    def __init__(self):
        self.value = np.random.randint(1, 11, 6)
        self.query = "What is the value of the largest bar?"
        self.answer = max(self.value)
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "elementary school"

    def draw(self, num):
        total_width = 0.6
        x = np.arange(6)
        plt.bar(x, self.value, total_width, color='blue')
        plt.xticks(np.arange(6), ['ration', 'posse', 'permit', 'acre', 'ego', 'nerve'], fontsize=16)
        plt.ylabel("Value", fontsize=18)
        plt.yticks([0, 2, 4, 6, 8, 10], fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q38:
    # find length of line in right triangle
    def __init__(self):
        self.AB = rd.randint(2, 10)
        self.query = f"As shown in the figure, in the right triangle ABC,  ∠ACB=90°, D is the midpoint of AB, " \
                     f"and  AB={self.AB}. What is the length of CD? "
        self.answer = self.AB / 2
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q38temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q38temp.png"), dest_image_path)


class Q39:
    # scatter 1
    def __init__(self):
        self.y = [rd.randint(50, 100)]
        self.y2 = [rd.randint(5, 20)]
        i = 0
        while i < 19:
            self.y.append(self.y[i] - rd.randint(1, 2))
            self.y2.append(self.y2[i] + rd.randint(-5, 5))
            i += 1
        self.query = "Is Coral the roughest? choice: (A) Yes (B) No"
        self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        x = np.linspace(5, 100, 20).tolist()
        y = self.y
        y2 = self.y2
        plt.scatter(x, y, color='blue')
        plt.scatter(x, y2, color='coral')
        plt.yticks(np.arange(0, 101, 10), fontsize=16)
        plt.xticks([0, 20, 40, 60, 80 ,100], fontsize=16)
        plt.legend(['blue', 'coral'], fontsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q40:
    # equation system2
    def __init__(self):
        self.star = rd.randint(1, 10)
        self.club = rd.randint(1, 10)
        self.spade = rd.randint(1, 10)
        self.query = "What is the value of the star?"
        self.eq1 = self.star + self.club + self.spade
        self.eq3 = self.star + self.club + self.star
        self.eq2 = self.club + self.club + self.spade
        self.answer = self.star
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"


    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        eq1 = r'$\bigstar$' + " + " + r'$\clubsuit$' + " + " r'$\spadesuit$' + f" = {self.eq1}"
        eq2 = r'$\clubsuit$' + " + " + r'$\clubsuit$' + " + " r'$\spadesuit$' + f" = {self.eq2}"
        eq3 = r'$\bigstar$' + " + " + r'$\clubsuit$' + " + " r'$\bigstar$' + f" = {self.eq3}"
        eq4 = r'$\bigstar$' + " = ?"
        plt.text(-1.5, 1, eq1, fontsize=20)
        plt.text(-1.5, 0, eq3, fontsize=20)
        plt.text(-1.5, -1, eq2, fontsize=20)
        plt.text(-1.5, -2, eq4, fontsize=20)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        ax.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


