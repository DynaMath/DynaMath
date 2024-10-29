import os.path
import shutil

import matplotlib.pyplot as plt
import numpy as np
import random as rd
import pandas as pd
from plottable import Table
from PIL import Image, ImageDraw, ImageFont


class Q01:
    # draw sin image
    def __init__(self):
        self.query = "What is the period of this function y = a*sin(b*x), where both a and b are integers? Answer the " \
                     "question with a floating-point number. "
        self.constant_a = rd.randint(1, 3)
        self.constant_b = rd.randint(1, 3)
        self.answer = 2 * np.pi / self.constant_a
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200, endpoint=True)
        cos = self.constant_b * np.cos(self.constant_a * x)
        sin = self.constant_b * np.sin(self.constant_a * x)
        plt.plot(x, sin, color='blue', lw=2.5)

        plt.xlim(-2 * np.pi * 1.1, 2 * np.pi * 1.1)
        plt.ylim(cos.min() * 1.1, cos.max() * 1.1)

        plt.xticks(
            [-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
            [r'-$2\pi$', r'-$3\pi/2$', r'-$\pi$', r'-$\pi/2$', r'$\pi/2$', r'$\pi$', r'-$3\pi/2$', r'$2\pi$']
        )

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


class Q02:
    # line plot 1
    def __init__(self):
        self.query = "Use the graph to answer the question below. Which month is the hottest on average in Cape Town?"
        self.x = np.arange(12)
        self.distance = rd.randint(2, 4)
        self.y = np.random.choice(np.arange(0, 45, self.distance), size=12, replace=False)
        self.month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        max_temp = max(self.y)
        for i in range(0, len(self.y)):
            if self.y[i] == max_temp:
                self.index = i
        self.answer = self.month[self.index]
        self.answer_type = "text"
        self.subject = "statistics"
        self.level = "elementary school"

    def draw(self, num):
        plt.figure()
        plt.plot(self.x, self.y, color='orange', linewidth=1.5, marker='o')
        plt.xticks(np.arange(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontsize=14)
        plt.yticks(np.arange(0, 45, 5), fontsize=14)
        plt.ylabel("Temperature", fontsize=16)
        plt.title("Average temperature in Cape Town, South Africa", fontsize=16)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q03:
    # table 1
    def __init__(self):
        self.score = np.random.randint(1, 11, 8)
        self.query = "The players on a quiz show received the following scores. What is the mean of the numbers?"
        self.answer = sum(self.score) / 8
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        data = {
            'name': ['Arianna', 'Joel', 'Carson', 'Nate', 'Damon', 'Henry', 'Mackenize', 'lan'],
            'score': self.score
        }
        df = pd.DataFrame(data, columns=['name', 'score'])
        df.set_index('name', inplace=True)
        Table(df, textprops={
                  'fontsize': 22,
              })
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q04:
    # table 2
    def __init__(self):
        self.num = np.random.randint(80, 100, 8)
        self.query = "A real estate agent looked into how many houses were sold in different cities. What is the range of the numbers?"
        self.answer = max(self.num) - min(self.num)
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        data = {
            'city': ['Briggs Corner', 'New Humburg', 'Melville', 'Fremont', 'liberty City', 'Charles Falls',
                     'Pleasent Town', 'Penny Town'],
            'Sales number': self.num
        }
        df = pd.DataFrame(data, columns=['city', 'Sales number'])
        df.set_index('city', inplace=True)
        Table(df, textprops={
                  'fontsize': 18,
              })
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q05:
    # pie 1
    def __init__(self):
        self.sizes = np.random.randint(1, 10, 2)
        self.query = "Is Dark Magenta greater than Rosy Brown? Choices: (A) yes (B) no"
        if self.sizes[0] > self.sizes[1]:
            self.answer = 'A'
        else:
            self.answer = 'B'
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "elementary school"

    def draw(self, num):
        labels = ['Dark Magenta', 'Rosy Brown']
        plt.figure(figsize=(5, 5))
        plt.pie(self.sizes, labels=None, autopct=None, startangle=90, colors=['darkmagenta', 'rosybrown'])
        plt.legend(labels, loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q06:
    # draw tan
    def __init__(self):
        self.constant_a = rd.randint(1, 3)
        self.constant_b = rd.randint(1, 3)
        self.query = "Is this a periodic function? Choices: (A) Yes (B) No"
        self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        constant_a = self.constant_a
        constant_b = self.constant_b
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200, endpoint=True)
        tan = constant_b * np.tan(constant_a * x)

        plt.plot(x, tan, color='blue', lw=2.5)

        plt.xlim(-2 * np.pi * 1.1, 2 * np.pi * 1.1)
        plt.ylim(-3, 3)

        plt.xticks(
            [-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
            [r'-$2\pi$', r'-$3\pi/2$', r'-$\pi$', r'-$\pi/2$', r'$\pi/2$', r'$\pi$', r'-$3\pi/2$', r'$2\pi$'],
            fontsize=14
        )

        plt.yticks([-3, -2, -1, 1, 2, 3], fontsize=14)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))

        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q07:
    # find unknown number
    def __init__(self):
        self.query =  "In the addition sum to the right, three digits have been replaced with star. What is the value of star?"
        self.unknown = rd.randint(0, 9)
        self.y = rd.randint(0, 9)
        self.z = rd.randint(0, 9)
        self.x = rd.randint(0, 9)
        self.answer = self.unknown
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def draw(self, num):
        y = self.y
        z = self.z
        x = self.x
        eq1 = 100 + 10 * self.unknown + x
        eq2 = 100 + 10 * self.unknown + y
        eq3 = 100 + 10 * self.unknown + z
        eq4 = eq1 + eq2 + eq3
        text = f"    1 * {x}\n + 1 * {y}\n + 1 * {z}\n-----------\n    {eq4 // 100} {(eq4 % 100) // 10} {eq4 % 10}"
        width = 200
        height = 200
        image = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        x1, y1, x2, y2 = draw.textbbox((400, 400), text, font=ImageFont.truetype("arial.ttf", 30))
        text_width, text_height = x2 - x1, y2 - y1
        x = (width - text_width) / 2
        y = (height - text_height) / 2
        draw.text((x, y), text, fill=(0, 0, 0), font=ImageFont.truetype("arial.ttf", 30))
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        image.save(dest_image_path, bbox_inches='tight')


class Q08:
    # find AO
    def __init__(self):
        self.AO = rd.randint(3, 25)
        self.OB = rd.randint(4, 25)
        self.AB = round(np.sqrt(self.AO * self.AO + self.OB * self.OB), 3)
        self.query = f"As shown in the figure, AO is the height of the cone, the bottom radius of the cone OB = {self.OB}, the length of AB is {self.AB}, then the length of AO is ()?"
        self.answer = np.sqrt(self.AB ** 2 - self.OB ** 2)
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q16temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q16temp.png"), dest_image_path)


class Q09:
    # square perimeter
    def __init__(self):
        self.factor = rd.randint(1, 10)
        self.query = "Find the perimeter of orange square."
        self.answer = self.factor * 4
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "elementary school"

    def draw(self, num):
        square = plt.Polygon([(1, 1), (1, 3), (3, 3), (3, 1)], closed=True, fill=True, edgecolor='black', facecolor='orange')
        fig, ax = plt.subplots()
        fig.set_size_inches(4, 4)
        ax.add_patch(square)
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        plt.text(0.5, 2, f'{self.factor}ft', fontsize=12)
        plt.text(2, 0.5, f'{self.factor}ft', fontsize=12)
        plt.xticks([])
        plt.yticks([])
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q10:
    # triangle perimeter
    def __init__(self):
        self.factor = rd.randint(1, 10)
        self.query = "Find the perimeter of the orange triangle."
        self.answer = self.factor * 3
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "elementary school"

    def draw(self, num):
        triangle = plt.Polygon([(1, 1), (3, 1), (2, 1 + np.sqrt(3))], closed=True, fill=True, edgecolor='black',
                               facecolor='orange')
        fig, ax = plt.subplots()
        fig.set_size_inches(4, 4)
        ax.add_patch(triangle)
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        plt.text(1, 2, f'{self.factor}ft', fontsize=12)
        plt.text(2.75, 2, f'{self.factor}ft', fontsize=12)
        plt.text(2, 0.5, f'{self.factor}ft', fontsize=12)
        plt.xticks([])
        plt.yticks([])
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q11:
    # find angle
    def __init__(self):
        self.AOF = rd.randint(60, 65)
        self.query = f"As shown in the figure, lines AB and CD intersect at point O. OF bisects ∠AOC. If ∠AOF = {self.AOF}, then what is the degree of ∠AOD?"
        self.answer = 180 - 2 * self.AOF
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q19temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q19temp.png"), dest_image_path)


class Q12:
    # draw cos image
    def __init__(self):
        self.query = "What is the period of this function y = a*cos(b*x), where both a and b are integers? Answer the " \
                     "question with a floating-point number. "
        self.constant_a = rd.randint(1, 2)
        self.constant_b = rd.randint(1, 3)
        self.answer = 2 * np.pi / self.constant_a
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200, endpoint=True)
        cos = self.constant_b * np.cos(self.constant_a * x)
        plt.plot(x, cos, color='red', linewidth=1.5)

        plt.xlim(-2 * np.pi * 1.1, 2 * np.pi * 1.1)
        plt.ylim(cos.min() * 1.1, cos.max() * 1.1)

        plt.xticks(
            [-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
            [r'-$2\pi$', r'-$3\pi/2$', r'-$\pi$', r'-$\pi/2$', r'$\pi/2$', r'$\pi$', r'-$3\pi/2$', r'$2\pi$']
        )

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


class Q13:
    # find triangle area
    def __init__(self):
        self.ID = rd.randint(3, 13)
        self.peri = self.ID * 6
        self.query = f"As shown in the figure, AI, BI, and CI bisect ∠BAC, ∠ABC, and ∠ACB, respectively. ID is perpendicular to BC. The perimeter of △ABC is {self.peri}, and ID = {self.ID}. What is the area of △ABC"
        self.answer = self.ID * self.peri / 2
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q20temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q20temp.png"), dest_image_path)


class Q14:
    # compare cos and sin's period
    def __init__(self):
        self.constant_a = rd.randint(1, 2)
        self.constant_b = rd.randint(1, 3)
        self.constant_c = rd.randint(1, 2)
        self.constant_d = rd.randint(1, 3)
        self.query = "The period of the red curve is ____ that of the blue curve. Choices: (A) larger than (B) equal to (C) smaller than"
        if self.constant_a > self.constant_c:
            self.answer = 'C'
        elif self.constant_c > self.constant_a:
            self.answer = 'A'
        else:
            self.answer = 'B'
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200, endpoint=True)
        cos = self.constant_b * np.cos(self.constant_a * x)
        plt.plot(x, cos, color='red', linewidth=1.5)

        sin = self.constant_d * np.sin(self.constant_c * x)
        plt.plot(x, sin, color='blue', lw=2.5)

        plt.xlim(-2 * np.pi * 1.1, 2 * np.pi * 1.1)
        plt.ylim(cos.min() * 1.1, cos.max() * 1.1)

        plt.xticks(
            [-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
            [r'-$2\pi$', r'-$3\pi/2$', r'-$\pi$', r'-$\pi/2$', r'$\pi/2$', r'$\pi$', r'-$3\pi/2$', r'$2\pi$']
        )

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


class Q15:
    # draw parabola
    def __init__(self):
        self.constant_a = rd.randint(0, 2)
        self.constant_b = rd.randint(0, 3)
        self.constant_c = rd.randint(0, 3)
        self.query = "how many zeros this function has? choice: (A) 2 (B) 1 (C) 0"
        self.delta = self.constant_b * self.constant_b - 4 * self.constant_c * self.constant_a
        if self.delta > 0:
            self.answer = "A"
        elif self.delta < 0:
            self.answer = "C"
        else:
            self.answer = "B"
        if self.constant_a == 0:
            self.answer = "B"
        if self.constant_a == 0 and self.constant_b == 0:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        square = self.constant_a * x ** 2 + self.constant_b * x + self.constant_c
        plt.plot(x, square, color='red', linewidth=1.5)

        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5], fontsize=14)

        plt.yticks([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5], fontsize=14)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q16:
    # draw an equation system
    def __init__(self):
        self.x = rd.randint(1, 10)
        self.y = rd.randint(1, 10)
        self.z = rd.randint(1, 10)
        self.u = rd.randint(1, 10)
        self.eq1 = self.x + self.x + self.x
        self.eq2 = self.y + self.y + self.x
        self.eq3 = self.z + self.u + self.u
        self.eq4 = self.z + self.z * self.z
        self.eq5 = self.u + self.y * self.u
        self.query = "Find the value of the last row of calculations."
        self.answer = self.eq5
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        text = f"x + x + x = {self.eq1}\ny + y + x = {self.eq2}\nz + u + u = {self.eq3}\nz + z * z = {self.eq4}\nu + y * u = ?"
        width = 400
        height = 400
        image = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        x1, y1, x2, y2 = draw.textbbox((400, 400), text, font=ImageFont.truetype("arial.ttf", 30))
        text_width, text_height = x2 - x1, y2 - y1
        x = (width - text_width) / 2
        y = (height - text_height) / 2
        draw.text((x, y), text, fill=(0, 0, 0), font=ImageFont.truetype("arial.ttf", 30))
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        image.save(dest_image_path)
        plt.close()


class Q17:
    # square, area
    def __init__(self):
        self.factor = rd.randint(1, 10)
        self.query = "Find the area of the blue square."
        self.answer = self.factor * self.factor
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "elementary school"

    def draw(self, num):
        square = plt.Polygon([(1, 1), (1, 3), (3, 3), (3, 1)], closed=True, fill=True, edgecolor='black', facecolor='azure')
        fig, ax = plt.subplots()
        fig.set_size_inches(4, 4)
        ax.add_patch(square)
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        plt.text(0.5, 2, f'{self.factor}ft', fontsize=12)
        plt.text(2, 0.5, f'{self.factor}ft', fontsize=12)
        plt.xticks([])
        plt.yticks([])
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q18:
    # triangle, area
    def __init__(self):
        self.factor = rd.randint(1, 10)
        self.query = "Find the area of this triangle. Answer the question with a floating-point number."
        self.answer = self.factor * self.factor * np.sqrt(3) / 4
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "elementary school"

    def draw(self, num):
        triangle = plt.Polygon([(1, 1), (3, 1), (2, 1 + np.sqrt(3))], closed=True, fill=True, edgecolor='black',
                               facecolor='azure')
        fig, ax = plt.subplots()
        fig.set_size_inches(4, 4)
        ax.add_patch(triangle)
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        plt.text(1, 2, f'{self.factor}ft', fontsize=12)
        plt.text(2.75, 2, f'{self.factor}ft', fontsize=12)
        plt.text(2, 0.5, f'{self.factor}ft', fontsize=12)
        plt.xticks([])
        plt.yticks([])
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q19:
    # bar chart1
    def __init__(self):
        self.delay = np.random.randint(1, 11, 4)
        self.haste = np.random.randint(1, 11, 4)
        self.tappet = np.random.randint(1, 11, 4)
        self.query = "What is the sum of accuracies of the bar group poison for all the datasets?"
        self.answer = self.delay[3] + self.haste[3] + self.tappet[3]
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "elementary school"

    def draw(self, num):
        total_width = 0.6
        n = 3
        width = total_width / n
        x = np.arange(4)
        plt.bar(x, self.delay, width, label='Delay', color='blue')
        plt.bar(x + width, self.haste, width, label='Haste', color='orange')
        plt.bar(x + 2 * width, self.tappet, width, label='Tappet', color='g')
        plt.xticks(np.arange(4), ['neat', 'acre', 'squad', 'poison'], fontsize=18)
        plt.ylabel("Accuracy", fontsize=18)
        plt.tick_params(axis='y', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q20:
    # bar chart2
    def __init__(self):
        self.Import = np.random.randint(1, 11, 3)
        self.pork = np.random.randint(1, 11, 3)
        self.drew = np.random.randint(1, 11, 3)
        self.constant = rd.randint(1, 11)
        self.query = f"How many groups of bars contain at least one bar with a value {self.constant}?"
        self.answer = 0
        if self.constant in self.Import:
            self.answer += 1
        if self.constant in self.pork:
            self.answer += 1
        if self.constant in self.drew:
            self.answer += 1
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "elementary school"

    def draw(self, num):
        total_width = 0.6
        n = 3
        width = total_width / n
        x = np.arange(3)
        plt.bar(x, self.Import, width, label='import', color='blue')
        plt.bar(x + width, self.pork, width, label='pork', color='g')
        plt.bar(x + 2 * width, self.drew, width, label='draw', color='r')
        plt.xticks(np.arange(3), ['clergy', 'sketch', 'devil'], fontsize=18)
        plt.ylabel("values", fontsize=18)
        plt.tick_params(axis='y', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()

