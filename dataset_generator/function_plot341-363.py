
import shutil
import networkx as nx
import pyglet
from math import sin, cos, pi
import os.path
import matplotlib.pyplot as plt
import random as rd
from PIL import Image, ImageDraw, ImageFont
from matplotlib.patches import *


class Q341:
    # calendar 1
    def __init__(self):
        self.day = rd.randint(1, 30)
        self.year = rd.randint(2000, 2024)
        self.month = rd.choice(
            [['Jan', "01"], ['Feb', "02"], ['Mar', "03"], ['Apr', "04"], ['May', "05"], ['June', "06"],
             ['July', "07"], ['Aug', "08"], ['Sep', "09"], ['Oct', "10"], ['Nov', "11"],
             ['Dec', "12"]])
        self.query = "What is the date today? Answer in the format like mm/dd/yyyy."
        if self.day < 10:
            self.answer = f"{self.month[1]}/0{self.day}/{self.year}"
        else:
            self.answer = f"{self.month[1]}/{self.day}/{self.year}"
        self.answer_type = "text"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def draw(self, num):
        Img = Image.open('temp_image/Q341temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        plt.text(500, 600, f"{self.day}", fontsize=100, ha='center', va='center')
        plt.text(150, 1000, f"{self.month[0]}", fontsize=20, ha='center', va='center')
        plt.text(800, 1000, f"{self.year}", fontsize=20, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q342:
    # calendar 2
    def __init__(self):
        self.day = rd.randint(1, 30)
        self.year = rd.randint(2001, 2024)
        self.month = rd.choice(
            [['Mar', 3], ['Apr', 4], ['May', 5], ['June', 6],
             ['July', 7], ['Aug', 8], ['Sep', 9], ['Oct', 10], ['Nov', 11],
             ['Dec', 12]])
        self.re = (math.floor(20/4) - 2 * 20 + (self.year % 100) + math.floor((self.year % 100)/4) + math.floor((13 * (self.month[1] + 1)/5)) + self.day - 1) % 7
        self.query = "The calendar is partially covered with ink. What day is it today? Answer in word with the first " \
                     "letter capitalized. "
        if self.re == 1:
            self.answer = "Monday"
        elif self.re == 2:
            self.answer = "Tuesday"
        elif self.re == 3:
            self.answer = "Wednesday"
        elif self.re == 4:
            self.answer = "Thursday"
        elif self.re == 5:
            self.answer = "Friday"
        elif self.re == 6:
            self.answer = "Saturday"
        elif self.re == 0:
            self.answer = "Sunday"
        self.answer_type = "text"
        self.subject = "arithmetic"
        self.level = "undergraduate"

    def draw(self, num):
        Img = Image.open('temp_image/Q342temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        plt.text(500, 600, f"{self.day}", fontsize=100, ha='center', va='center')
        plt.text(150, 1000, f"{self.month[0]}", fontsize=20, ha='center', va='center')
        plt.text(800, 1000, f"{self.year}", fontsize=20, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q343:
    # watch problem 2
    def __init__(self):
        self.lst = [0, 15, 30, 45]
        self.mPointer = rd.choice(self.lst)
        self.hPointer = rd.randint(1, 12)
        self.mPointer2 = rd.choice(self.lst)
        self.hPointer2 = rd.randint(1, 12)
        self.query = f"Mike shot two clock pictures. The left one was shotted before the midday. " \
                     f"The right one was shotted after the midday. How many minutes passed between two shots?"
        self.answer = (self.hPointer2 + 12 - self.hPointer) * 60 + self.mPointer2 - self.mPointer
        self.answer_type = "float"
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
            pyglet.image.get_buffer_manager().get_color_buffer().get_image_data().save(f"temp_image/Q343temp.png")

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
        os.rename("temp_image/Q343temp.png", f"temp_image/Q343temp1.png")
        watch = self.Watch(400, 250)
        watch.update(self.mPointer2, self.hPointer2)
        watch.run()
        os.rename("temp_image/Q343temp.png", f"temp_image/Q343temp2.png")
        image1 = Image.open(f"temp_image/Q343temp1.png")
        image2 = Image.open(f"temp_image/Q343temp2.png")
        width = image1.width + image2.width
        new_image = Image.new('RGB', (width, max(image1.height, image2.height)))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (image1.width, 0))
        new_image.save(dest_image_path, dpi=(600, 600))
        plt.close()
        if os.path.exists(f"temp_image/Q343temp1.png"):
            os.remove(f"temp_image/Q343temp1.png")
        if os.path.exists(f"temp_image/Q343temp2.png"):
            os.remove(f"temp_image/Q343temp2.png")


class Q344:
    # food chain 2
    def __init__(self):
        self.level4 = rd.choice(["tiger", "lion", "bear", "crocodile"])
        self.level3 = rd.choice(["wolf", "leopard", "fox", "cheetah", "hyena", "coyote", "boar"])
        self.level2 = rd.choice(["sheep", "goat", "moose", "deer", "cattle", "camel", "duck"])
        self.level1 = rd.choice(["grass"])
        self.query = f"If the {self.level3} population were to decrease, what would happen to the {self.level2} " \
                     f"population?  choice: (A) increase (B) decrease "
        self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        level4 = self.level4
        level3 = self.level3
        level2 = self.level2
        level1 = self.level1
        plt.xlim(-4 * 1.1, 4 * 1.1)
        plt.ylim(-4 * 1.1, 4 * 1.1)

        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(-1, 8, level4, fontsize=20)
        plt.text(-1, 3, level3, fontsize=20)
        plt.text(-1, -3, level2, fontsize=20)
        plt.text(-1, -8, level1, fontsize=20)
        ax.annotate('', xy=(0, -3), xytext=(0, -7), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        ax.annotate('', xy=(0, 3), xytext=(0, -2), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        ax.annotate('', xy=(0, 7.5), xytext=(0, 4), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q345:
    # global maximum 1
    def __init__(self):
        lst = list(range(-4, -1)) + list(range(1, 4))
        self.a = rd.choice(lst)
        self.b = rd.choice(lst)
        self.c = rd.choice(lst)
        self.d = rd.randint(0, 1)
        self.query = "What is the global maximum of this function?"
        self.answer = abs(self.a) + self.c
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200, endpoint=True)
        sin = a * np.sin(b * x + np.pi / 2 * d) + c
        plt.plot(x, sin, color='lightseagreen', lw=1.5)
        plt.xlim(-2 * np.pi * 1.1, 2 * np.pi * 1.1)
        plt.ylim(-8 * 1.1, 8 * 1.1)
        plt.xticks(
            [-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
            [r'-$2\pi$', r'-$3\pi/2$', r'-$\pi$', r'-$\pi/2$', r'$\pi/2$', r'$\pi$', r'-$3\pi/2$', r'$2\pi$']
        )
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.title("y = a * sin(b * x) + c", fontsize=16)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q346:
    # global maximum 2
    def __init__(self):
        lst = list(range(-4, -1)) + list(range(1, 4))
        self.a = rd.choice(lst)
        self.b = rd.choice(lst)
        self.c = rd.choice(lst)
        self.d = rd.randint(0, 1)
        self.query = "What is the global minimum of this function?"
        self.answer = -abs(self.a) + self.c
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200, endpoint=True)
        sin = a * np.sin(b * x + np.pi / 2 * d) + c
        plt.plot(x, sin, color='lawngreen', lw=1.5)
        plt.xlim(-2 * np.pi * 1.1, 2 * np.pi * 1.1)
        plt.ylim(-8 * 1.1, 8 * 1.1)
        plt.xticks(
            [-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
            [r'-$2\pi$', r'-$3\pi/2$', r'-$\pi$', r'-$\pi/2$', r'$\pi/2$', r'$\pi$', r'-$3\pi/2$', r'$2\pi$']
        )
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.title("y = a * cos(b * x) + c", fontsize=16)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q347:
    # number of odd function
    def __init__(self):
        self.exp = rd.sample(range(1, 6), 4)
        self.cons = rd.sample(range(1, 20), 4)
        self.addition = rd.randint(-5, -1)
        self.query = "how many odd functions are in the graph?"
        self.answer = sum(x % 2 for x in self.exp)
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        plt.gcf().set_size_inches(6, 6)
        x = np.linspace(10, -10, 200, endpoint=True)
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)
        color = ["lightseagreen", "deeppink", "orange", "violet"]
        for i in range(0, 4):
            if self.exp[i] % 2 != 0 and self.exp[i] >= 3:
                x1 = self.cons[i]/10 * x ** self.exp[i] + self.addition * x ** (self.exp[i] - 2)
            else:
                x1 = self.cons[i]/10 * x ** self.exp[i]
            plt.plot(x, x1, color=color[i], lw=1.5)
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


class Q348:
    # number of even function
    def __init__(self):
        self.exp = rd.sample(range(1, 6), 4)
        self.cons = rd.sample(range(1, 20), 4)
        self.addition = rd.randint(-5, -1)
        self.query = "how many even functions are in the graph?"
        self.answer = 4 - sum(x % 2 for x in self.exp)
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        plt.gcf().set_size_inches(6, 6)
        x = np.linspace(10, -10, 200, endpoint=True)
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)
        color = ["lightseagreen", "deeppink", "orange", "violet"]
        for i in range(0, 4):
            if self.exp[i] % 2 == 0 and self.exp[i] >= 4:
                x1 = self.cons[i] / 10 * x ** self.exp[i] + self.addition * x ** (self.exp[i] - 2)
            else:
                x1 = self.cons[i] / 10 * x ** self.exp[i]
            plt.plot(x, x1, color=color[i], lw=1.5)
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


class Q349:
    # Pascal's law
    def __init__(self):
        self.f1 = rd.randint(1, 50)
        self.s2 = rd.randint(10, 50)
        self.query = f"F1 = {self.f1}N, S1 = 1m^2, and S2 = {self.s2}m^2, find the value of force F2."
        self.answer = self.f1 * self.s2
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q349temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q349temp.png"), dest_image_path)


class Q350:
    # find the rule
    def __init__(self):
        self.fbnc = list(range(1, 9))
        self.fbnc[0] = rd.randint(1, 10)
        self.add = rd.randint(1, 20)
        for i in range(1, 8):
            self.fbnc[i] = self.fbnc[i - 1] + self.add
        self.fbnc.append("?")
        self.query = "Find the missing number in the last node."
        self.answer = self.fbnc[7] + self.add
        self.answer_type = "float"
        self.subject = "puzzle test"
        self.level = "elementary school"

    def draw(self, num):
        fbnc = self.fbnc
        G = nx.Graph()
        plt.figure(figsize=(6, 6))

        G.add_nodes_from(fbnc)
        pos = {
            fbnc[0]: (0.5, 1.5),
            fbnc[1]: (1, 1.5),
            fbnc[2]: (1.5, 1.5),
            fbnc[3]: (0.5, 1),
            fbnc[4]: (1, 1),
            fbnc[5]: (1.5, 1),
            fbnc[6]: (0.5, 0.5),
            fbnc[7]: (1, 0.5),
            '?': (1.5, 0.5)

        }
        G.add_edges_from(
            [[fbnc[0], fbnc[1]], [fbnc[1], fbnc[2]], [fbnc[2], fbnc[3]], [fbnc[3], fbnc[4]], [fbnc[4], fbnc[5]],
             [fbnc[5], fbnc[6]], [fbnc[6], fbnc[7]], [fbnc[7], fbnc[8]]])
        nx.draw(G, with_labels=True, pos=pos, node_color="white", edgecolors="black", node_size=1500, arrows=True,
                arrowstyle="->")

        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q351:
    # order of growth
    def __init__(self):
        self.lst = rd.sample([[0, "1"], [0.5, "logN"], [1, "N"], [1.5, "NlogN"], [2, "N^2"], [2.5, "N^2logN"],
                              [3, "N^3"], [4, "2^N"], [5, "N!"]], 4)
        self.max = max(self.lst[0][0], self.lst[1][0], self.lst[2][0], self.lst[3][0])
        self.query = "Which function has the highest order or growth? choice: (A) f1 (B) f2 (C) f3 (D) f4"
        if self.max == self.lst[0][0]:
            self.answer = "A"
        elif self.max == self.lst[1][0]:
            self.answer = "B"
        elif self.max == self.lst[2][0]:
            self.answer = "C"
        else:
            self.answer = "D"
        self.answer_type = "multiple choice"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        plt.gcf().set_size_inches(8, 6)
        x = rd.randint(1, 4)
        y = rd.randint(-6, 6)
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.hlines(0, -6, 6, color="black", linewidth=2)
        plt.hlines(3, -6, 6, color="black", linewidth=2)
        plt.hlines(-3, -6, 6, color="black", linewidth=2)
        plt.vlines(0, -3, 3, color="black", linewidth=2)
        plt.vlines(6, -3, 3, color="black", linewidth=2)
        plt.vlines(-6, -3, 3, color="black", linewidth=2)
        plt.text(-3, 1.5, f"f1 = O({self.lst[0][1]})", fontsize=21, ha='center', va='center')
        plt.text(3, 1.5, f"f2 = O({self.lst[1][1]})", fontsize=21, ha='center', va='center')
        plt.text(-3, -1.5, f"f3 = O({self.lst[2][1]})", fontsize=21, ha='center', va='center')
        plt.text(3, -1.5, f"f4 = O({self.lst[3][1]})", fontsize=21, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q352:
    # order of growth 2
    def __init__(self):
        self.lst = rd.sample([[0, "1"], [0.5, "logN"], [1, "N"], [1.5, "NlogN"], [2, "N^2"], [2.5, "N^2logN"],
                              [3, "N^3"], [4, "2^N"], [5, "N!"]], 4)
        self.min = min(self.lst[0][0], self.lst[1][0], self.lst[2][0], self.lst[3][0])
        self.query = "Which function has the lowest order or growth? choice: (A) f1 (B) f2 (C) f3 (D) f4"
        if self.min == self.lst[0][0]:
            self.answer = "A"
        elif self.min == self.lst[1][0]:
            self.answer = "B"
        elif self.min == self.lst[2][0]:
            self.answer = "C"
        else:
            self.answer = "D"
        self.answer_type = "multiple choice"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        plt.gcf().set_size_inches(8, 6)
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.hlines(0, -6, 6, color="black", linewidth=2)
        plt.hlines(3, -6, 6, color="black", linewidth=2)
        plt.hlines(-3, -6, 6, color="black", linewidth=2)
        plt.vlines(0, -3, 3, color="black", linewidth=2)
        plt.vlines(6, -3, 3, color="black", linewidth=2)
        plt.vlines(-6, -3, 3, color="black", linewidth=2)
        plt.text(-3, 1.5, f"f1 = O({self.lst[0][1]})", fontsize=21, ha='center', va='center')
        plt.text(3, 1.5, f"f2 = O({self.lst[1][1]})", fontsize=21, ha='center', va='center')
        plt.text(-3, -1.5, f"f3 = O({self.lst[2][1]})", fontsize=21, ha='center', va='center')
        plt.text(3, -1.5, f"f4 = O({self.lst[3][1]})", fontsize=21, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q353:
    # work by ideal gas
    def __init__(self):
        self.w1, self.h1 = rd.randint(1, 5), rd.randint(1, 9)
        self.w2 = rd.randint(self.w1 + 1, 9)
        self.query = "A sample of ideal gas is taken from an initial state to a final state following a curve on a pV " \
                     "diagram at right. What is the work that the gas does? "
        self.answer = (self.w2 - self.w1) * self.h1 * 100
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(0, 10)
        plt.ylim(0, 10)
        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   ["0", "100", "200", "300", "400", "500", "600", "700", "800", "900", "1000"])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        ax = plt.gca()
        w1, h1 = self.w1, self.h1
        w2 = self.w2
        plt.scatter(w1, h1, color="black")
        plt.scatter(w2, h1, color="black")
        plt.text(w1, h1 + 0.5, "start", fontsize=10, ha='center', va='center')
        plt.text(w2, h1 + 0.5, "end", fontsize=10, ha='center', va='center')
        plt.text(-1, 5, "Pressure (Pa)", fontsize=12, ha='center', va='center', rotation=90)
        plt.text(5, -1, "Volume (m^3)", fontsize=12, ha='center', va='center')
        ax.annotate('', xy=(w2, h1), xytext=(w1, h1), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q354:
    # work by ideal gas
    def __init__(self):
        self.w1, self.h1 = rd.randint(1, 8), rd.randint(1, 5)
        self.h2 = rd.randint(self.h1 + 1, 9)
        self.query = "A sample of ideal gas is taken from an initial state to a final state following a curve on a pV " \
                     "diagram at right. What is the work that the gas does? "
        self.answer = 0
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(0, 10)
        plt.ylim(0, 10)
        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   ["0", "100", "200", "300", "400", "500", "600", "700", "800", "900", "1000"])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        ax = plt.gca()
        w1, h1 = self.w1, self.h1
        h2 = self.h2
        plt.scatter(w1, h1, color="black")
        plt.scatter(w1, h2, color="black")
        plt.text(w1, h1 - 0.5, "start", fontsize=10, ha='center', va='center')
        plt.text(w1, h2 + 0.5, "end", fontsize=10, ha='center', va='center')
        plt.text(-1, 5, "Pressure (Pa)", fontsize=12, ha='center', va='center', rotation=90)
        plt.text(5, -1, "Volume (m^3)", fontsize=12, ha='center', va='center')
        ax.annotate('', xy=(w1, h2), xytext=(w1, h1), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q355:
    # find biggest number
    def __init__(self):
        self.lst = rd.sample(list(range(0, 10)), 4)
        self.query = f"Each of the digits {self.lst[0]}, {self.lst[1]}, {self.lst[2]} and {self.lst[3]} will be " \
                     f"placed in a square. Then there will be two numbers, which will be added together. What is the " \
                     f"biggest number that they could make? "
        temp = sorted(self.lst)
        self.answer = temp[3] * 10 + temp[0] + temp[2] * 10 + temp[1]
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q355temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q355temp.png"), dest_image_path)


class Q356:
    # algorithm flowchart 3
    def __init__(self):
        self.start = rd.randint(1, 99)
        self.minus = rd.randint(1, 99)
        self.add = rd.randint(1, 99)
        self.mult = rd.randint(2, 10)
        self.query = "Find the missing value."
        self.answer = (self.start - self.minus + self.add) * self.mult
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def draw(self, num):
        Img = Image.open('temp_image/Q356temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        plt.text(120, 80, f"{self.start}", fontsize=12, ha='center', va='center')
        plt.text(260, 70, f"{self.minus}", fontsize=10)
        plt.text(570, 70, f"{self.add}", fontsize=10)
        plt.text(870, 70, f"{self.mult}", fontsize=10)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q357:
    # algorithm flowchart 4
    def __init__(self):
        self.start = rd.randint(1, 99)
        self.minus = rd.randint(1, 99)
        self.add1 = rd.randint(1, 99)
        self.add2 = rd.randint(1, 99)
        self.add3 = rd.randint(1, 99)
        self.mult = rd.randint(2, 10)
        self.query = "Find the missing number."
        self.answer = (self.start + self.add1 + self.add2 + self.add3 - self.minus) * self.mult
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "elementary school"

    def draw(self, num):
        Img = Image.open('temp_image/Q357temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        plt.text(95, 95, f"{self.start}", fontsize=12, ha='center', va='center')
        plt.text(180, 65, f"{self.add1}", fontsize=9)
        plt.text(350, 65, f"{self.add2}", fontsize=9)
        plt.text(500, 65, f"- {self.minus}", fontsize=9)
        plt.text(685, 65, f"{self.add3}", fontsize=9)
        plt.text(830, 65, f"* {self.mult}", fontsize=9)
        plt.text(930, 95, "?", fontsize=14, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q358:
    # binary to decimal
    def __init__(self):
        self.len = rd.randint(4, 8)
        self.lst = [rd.randint(0, 1) for i in range(0, self.len)]
        self.sum = 0
        str1 = ""
        i = self.len - 1
        while i >= 0:
            self.sum = self.sum + self.lst[i] * 2 ** i
            str1 = str1 + f"{self.lst[i]}"
            i -= 1
        self.query = "Input binary number B = " + str1 + ", find the corresponding decimal value by the algorithm " \
                                                         "shown in image. "
        self.answer = self.sum
        self.answer_type = "float"
        self.subject = "scientific figure"
        self.level = "undergraduate"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q358temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q358temp.png"), dest_image_path)


class Q359:
    # volume of cylinder
    def __init__(self):
        self.r = rd.randint(1, 50)
        self.h = rd.randint(1, 50)
        self.query = f"The height h of the cylinder is {self.h}. Find the volume of the cylinder."
        self.answer = self.h * self.r ** 2 * np.pi
        self.answer_type = "float"
        self.subject = "solid geometry"
        self.level = "high school"

    def draw(self, num):
        Img = Image.open('temp_image/Q359temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        plt.text(780, 190, f"{self.r}", fontsize=14, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q360:
    # surface area of cylinder
    def __init__(self):
        self.r = rd.randint(1, 50)
        self.h = rd.randint(1, 50)
        self.query = f"The height h of the cylinder is {self.h}. Find the surface area of the cylinder."
        self.answer = 2 * self.r ** 2 * np.pi + self.h * 2 * self.r * np.pi
        self.answer_type = "float"
        self.subject = "solid geometry"
        self.level = "high school"

    def draw(self, num):
        Img = Image.open('temp_image/Q359temp.png')
        fig, ax = plt.subplots()
        ax.imshow(Img)
        plt.text(780, 190, f"{self.r}", fontsize=14, ha='center', va='center')
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q361:
    # symmetry of point ex1
    def __init__(self):
        self.x = rd.randint(-6, 6)
        self.y = rd.randint(-6, 6)
        self.ry = -self.y
        self.query = "If the black point is reflected in x-axis, what are the coordinates of its image? Please answer " \
                     "in the form (_, _) "
        self.answer = f"({format(self.x, '.3f')}, {format(self.ry, '.3f')})"
        self.answer_type = "text"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        plt.yticks([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(self.x, self.y, color='black')
        plt.hlines(self.y, 0, self.x, colors='black', linestyles="dashed")
        plt.vlines(self.x, 0, self.y, colors='black', linestyles="dashed")
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q362:
    # symmetry of point ex2
    def __init__(self):
        self.x = rd.randint(-6, 6)
        self.y = rd.randint(-6, 6)
        self.rx = -self.x
        self.query = "If the red point is reflected in y-axis, what are the coordinates of its image? Please answer " \
                     "in the form (_, _) "
        self.answer = f"({format(self.rx, '.3f')}, {format(self.y, '.3f')})"
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
        plt.scatter(self.x, self.y, color='red')
        plt.hlines(self.y, 0, self.x, colors='black', linestyles="dashed")
        plt.vlines(self.x, 0, self.y, colors='black', linestyles="dashed")
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q363:
    # symmetry of point ex3
    def __init__(self):
        self.x = rd.randint(-6, 6)
        self.y = rd.randint(-6, 6)
        self.rx = -self.x
        self.ry = -self.y
        self.query = "If the blue point is reflected about the origin, what are the coordinates of its image? Please " \
                     "answer in the form (_, _) "
        self.answer = f"({format(self.rx, '.3f')}, {format(self.ry, '.3f')})"
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
        plt.hlines(self.y, 0, self.x, colors='black', linestyles="dashed")
        plt.vlines(self.x, 0, self.y, colors='black', linestyles="dashed")
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

