import math
import shutil
import networkx as nx
import os.path
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from matplotlib.patches import *


class Q141:
    # sphere in cube
    def __init__(self):
        self.side = rd.randint(1, 50)
        self.query = f"The length of the diameter of this spherical ball is equal to the height of the box in which it " \
                     f"is placed. The box is a cube and has an edge length of {self.side} cm. " \
                     f"How many cubic centimeters of the box are not occupied by the solid sphere?"
        self.answer = self.side * self.side * self.side - 4/3 * np.pi * (self.side/2) * (self.side/2) * (self.side/2)
        self.answer_type = "float"
        self.subject = "solid geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q141temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q141temp.png"), dest_image_path)


class Q142:
    # bipartite 1
    def __init__(self):
        self.G = nx.Graph()
        self.G.add_nodes_from("ABCDEF")
        self.pos = {
            "A": (0.5, 1.5),
            "B": (0.5, 0.5),
            "C": (1, 0.5),
            "D": (1.5, 0.5),
            "E": (1, 1.5),
            "F": (1.5, 1.5),
        }
        for i in range(0, 9):
            t1 = rd.choice(["A", "E", "F"])
            t2 = rd.choice(["B", "C", "D"])
            self.G.add_edge(t1, t2)
        self.query = "Is this graph a bipartite? Choice: (A) Yes (B) No"
        self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(6, 4))
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="lightgreen", edgecolors="black", nodelist=["A", "E", "F"],
                node_size=200, font_color="green")
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", nodelist=["B", "C", "D"],
                node_size=200, font_color="white")
        nx.draw_networkx_edges(self.G, self.pos, edge_color="black")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q143:
    # continuous and differentiable
    def __init__(self):
        self.constant_a = rd.randint(-3, 3)
        self.constant_b = rd.randint(-3, 3)
        self.constant_c = rd.randint(-3, 3)
        self.constant_d = rd.randint(-1, 1)
        self.r = rd.randint(10, 90) / 11
        self.query = "Determine for which values of x=a the function is continuous but not differentiable at x=a."
        self.answer = 1
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = self.constant_a * x ** 3 + self.constant_b * x ** 2 + self.constant_c * x + self.constant_d
        plt.plot(x, cubic, color='violet', linewidth=2.5)
        ax = plt.gca()
        plt.xlim(-10 * 1.1, 10 * 1.1)
        plt.ylim(-10 * 1.1, 10 * 1.1)
        plt.xticks([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.yticks([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.scatter(1, self.constant_a + self.constant_b + self.constant_c + self.constant_d, color='white', edgecolor='black')
        plt.scatter(1, self.r, color='brown')
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q144:
    # find shaded area between sin and cos
    def __init__(self):
        self.b = rd.choice([-3, -2, -1, 1, 2, 3])
        self.query = "Find the area of shaded part."
        self.answer = abs(self.b * (np.sqrt(2) - 1))
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        b = self.b
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200, endpoint=True)
        rx = np.linspace(0, np.pi / 4, 200, endpoint=True)
        sin = b * np.sin(x)
        rsin = b * np.sin(rx)
        cos = b * np.cos(x)
        rcos = b * np.cos(rx)
        plt.plot(x, sin, color='blue', lw=2.5)
        plt.plot(x, cos, color='orange', lw=2.5)
        plt.fill_between(rx, rsin, rcos, color='lightgray')
        plt.xlim(-2 * np.pi * 1.1, 2 * np.pi * 1.1)
        plt.ylim(sin.min() * 1.1, sin.max() * 1.1)
        plt.xticks(
            [-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
            [r'-$2\pi$', r'-$3\pi/2$', r'-$\pi$', r'-$\pi/2$', r'$\pi/2$', r'$\pi$', r'-$3\pi/2$', r'$2\pi$']
        )
        plt.yticks([-3, -2, -1, 1, 2, 3])
        plt.fill(rx, rsin, color='lightgray')
        if b == -1:
            plt.title(f'f(x) = sin(x)  g(x) = cos(x)', fontsize=14)
        elif b == 1:
            plt.title(f'f(x) = -sin(x)  g(x) = -cos(x)', fontsize=14)
        else:
            plt.title(f'f(x) = {b}sin(x)  g(x) = {b}cos(x)', fontsize=14)
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


class Q145:
    # find the side length of the square
    def __init__(self):
        self.PA = rd.randint(1, 10)
        self.PB = 2 * self.PA
        self.PC = 3 * self.PA
        self.query = f"P is a point inside the square ABCD, and PA = {self.PA}, PB = {self.PB}, PC = {self.PC}. Find " \
                     f"the side length of the square. "
        self.answer = np.sqrt(5 + 2 * np.sqrt(2)) * self.PA
        self.answer_type = "float"
        self.subject = "solid geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q145temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q145temp.png"), dest_image_path)


class Q146:
    # find relationship and missing number
    def __init__(self):
        self.random = rd.randint(2, 5)
        self.a = rd.randint(6, 10)
        self.b = rd.choice([11, 13, 17, 19, 23, 29, 31, 37])
        self.c = rd.choice([51, 53, 57, 59, 61, 67, 71, 73])
        if rd.randint(1, 2) % 2 == 0:
            self.b2 = "?"
            self.c2 = self.c * self.random
            self.answer = self.b * self.random
        else:
            self.b2 = self.b * self.random
            self.c2 = "?"
            self.answer = self.c * self.random
        self.query = "Find the missing number."
        self.answer_type = "float"
        self.subject = "puzzle test"
        self.level = "high school"

    def draw(self, num):
        G = nx.Graph()
        plt.figure(figsize=(6, 6))
        random = self.random
        a = self.a
        b = self.b
        c = self.c
        a2 = a * random
        b2 = self.b2
        c2 = self.c2
        G.add_nodes_from([f"{a}", f"{a2}", f"{b}", f"{c}", f"{random}", f"{c2}", f"{b2}"])
        pos = {
            f"{a}": (1, 1.5),
            f"{a2}": (1, 0.5),
            f"{b}": (0.5, 1.25),
            f"{c}": (1.5, 1.25),
            f"{random}": (1, 1),
            f"{c2}": (0.5, 0.75),
            f"{b2}": (1.5, 0.75)
        }
        G.add_edges_from(([f"{a}", f"{random}"], [f"{a2}", f"{random}"], [f"{b}", f"{random}"], [f"{c}", f"{random}"],
                          [f"{random}", f"{c2}"], [f"{random}", f"{b2}"]))
        nx.draw(G, with_labels=True, pos=pos, node_color="white", edgecolors="black", node_size=1500)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q147:
    # ceil function differentiable
    def __init__(self):
        self.d = rd.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        self.e = rd.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        self.query = "Is this function differentiable? choice: (A) Yes (B) No"
        self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        d = self.d
        e = self.e
        x1 = np.linspace(-10, 10, 200, endpoint=True)
        f1 = np.ceil(d * x1 + e)
        plt.plot(x1, f1, color='blue', linewidth=2.5)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
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


class Q148:
    # floor function continuous
    def __init__(self):
        self.d = rd.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        self.query = "Is this function uniformly continuous on [-8, 8]? choice: (A) Yes (B) No"
        self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        random = self.d
        x1 = np.linspace(-10, 10, 200, endpoint=True)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        for i in range(-8, 8):
            plt.hlines(random * i, i, i + 1, color='red', linewidth=2.5)
            plt.scatter(i, random * i, color='white', edgecolor='black')
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q149:
    # compare f(1) and f(-1)
    def __init__(self):
        self.a = rd.randint(-30, 30) / 10
        self.b = rd.randint(-30, 30) / 10
        self.c = rd.randint(-30, 30) / 10
        self.d = rd.randint(-10, 10) / 10
        self.query = "The function value f(1) is ____ f(-1) choice: (A) smaller than (B) larger than (C) equal to"
        if self.a + self.b + self.c + self.d > -self.a + self.b - self.c + self.d:
            self.answer = "B"
        elif self.a + self.b + self.c + self.d < -self.a + self.b - self.c + self.d:
            self.answer = "A"
        else:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        constant_a = self.a
        constant_b = self.b
        constant_c = self.c
        constant_d = self.d
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = constant_a * x ** 3 + constant_b * x ** 2 + constant_c * x + constant_d
        plt.plot(x, cubic, color='lightseagreen', linewidth=1.5)
        ax = plt.gca()
        plt.xlim(-10 * 1.1, 10 * 1.1)
        plt.ylim(-10 * 1.1, 10 * 1.1)
        plt.xticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        plt.yticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        plt.scatter(1, constant_a + constant_b + constant_c + constant_d, color='black')
        plt.scatter(-1, -constant_a + constant_b - constant_c + constant_d, color='black')
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q150:
    # compare f(1) and 0
    def __init__(self):
        self.a = rd.randint(-30, 30) / 10
        self.b = rd.randint(-30, 30) / 10
        self.c = rd.randint(-30, 30) / 10
        self.d = rd.randint(-10, 10) / 10
        self.query = "The function value f(1) is ____ 0 choice: (A) smaller than (B) larger than (C) equal to"
        if self.a + self.b + self.c + self.d > 0:
            self.answer = "B"
        elif self.a + self.b + self.c + self.d < 0:
            self.answer = "A"
        else:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        constant_a = self.a
        constant_b = self.b
        constant_c = self.c
        constant_d = self.d
        x = np.linspace(-10, 10, 200, endpoint=True)
        cubic = constant_a * x ** 3 + constant_b * x ** 2 + constant_c * x + constant_d
        plt.plot(x, cubic, color='salmon', linewidth=1.5)
        ax = plt.gca()
        plt.xlim(-10 * 1.1, 10 * 1.1)
        plt.ylim(-10 * 1.1, 10 * 1.1)
        plt.xticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        plt.yticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        plt.scatter(1, constant_a + constant_b + constant_c + constant_d, color='black')
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q151:
    # MST kruskal's algorithm 2
    def __init__(self):
        self.AC = [rd.randint(1, 20), "AC"]
        self.AD = [rd.randint(1, 20), "AD"]
        self.AG = [rd.randint(1, 20), "AG"]
        self.EG = [rd.randint(1, 20), "EG"]
        self.FG = [rd.randint(1, 20), "FG"]
        self.DG = [rd.randint(1, 20), "DG"]
        self.CE = [rd.randint(1, 20), "CE"]
        self.DF = [rd.randint(1, 20), "DF"]
        self.BE = [rd.randint(1, 20), "BE"]
        self.BF = [rd.randint(1, 20), "BF"]
        self.BG = [rd.randint(1, 20), "BG"]
        self.CG = [rd.randint(1, 20), "CG"]
        self.min = min(self.AC, self.AD, self.AG, self.EG, self.FG, self.DG, self.CE, self.DF, self.BE, self.BF, self.BG
                       , self.CG)
        self.query = "what is the first edge added to the MST when running Kruskal's Algorithm? In the case of a tie, " \
                     "choose the edge which comes first in alphabetical order i.e. if you had to choose between AG " \
                     "and AD, then you would choose AD first. "
        self.answer = self.min[1]
        self.answer_type = "text"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.Graph()
        plt.figure(figsize=(6, 6))

        G.add_nodes_from("ABCDEFG")
        pos = {
            "A": (1, 1.5),
            "B": (1, 0.5),
            "C": (0.5, 1.25),
            "D": (1.5, 1.25),
            "G": (1, 1),
            "E": (0.5, 0.75),
            "F": (1.5, 0.75)
        }
        G.add_edges_from((["A", "G"], ["B", "G"], ["C", "G"], ["D", "G"], ["G", "E"], ["G", "F"]))
        G.add_edges_from((["D", "F"], ["A", "C"], ["A", "D"], ["E", "C"], ["B", "E"], ["B", "F"]))
        nx.draw(G, with_labels=True, pos=pos, node_color="white", edgecolors="black", node_size=1500)
        plt.text(0.7, 1.4, f"{self.AC[0]}", fontsize=20)
        plt.text(1.25, 1.4, f"{self.AD[0]}", fontsize=20)
        plt.text(1.02, 1.25, f"{self.AG[0]}", fontsize=20)
        plt.text(1.02, 0.75, f"{self.BG[0]}", fontsize=20)
        plt.text(0.4, 1, f"{self.CE[0]}", fontsize=20)
        plt.text(1.55, 1, f"{self.DF[0]}", fontsize=20)
        plt.text(0.7, 0.55, f"{self.BE[0]}", fontsize=20)
        plt.text(1.25, 0.55, f"{self.BF[0]}", fontsize=20)
        plt.text(0.75, 1.15, f"{self.CG[0]}", fontsize=20)
        plt.text(1.2, 1.15, f"{self.DG[0]}", fontsize=20)
        plt.text(0.75, 0.95, f"{self.EG[0]}", fontsize=20)
        plt.text(1.2, 0.95, f"{self.FG[0]}", fontsize=20)

        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q152:
    # MST Prim's algorithm
    def __init__(self):
        self.AC = [rd.randint(1, 20), "AC"]
        self.AD = [rd.randint(1, 20), "AD"]
        self.AG = [rd.randint(1, 20), "AG"]
        self.EG = [rd.randint(1, 20), "EG"]
        self.FG = [rd.randint(1, 20), "FG"]
        self.DG = [rd.randint(1, 20), "DG"]
        self.CE = [rd.randint(1, 20), "CE"]
        self.DF = [rd.randint(1, 20), "DF"]
        self.BE = [rd.randint(1, 20), "BE"]
        self.BF = [rd.randint(1, 20), "BF"]
        self.BG = [rd.randint(1, 20), "BG"]
        self.CG = [rd.randint(1, 20), "CG"]
        self.min = min(self.AC, self.AD, self.AG)
        self.query = "what is the first edge added to the MST when running Prim's Algorithm from node A? " \
                     "In the case of a tie, " \
                     "choose the edge which comes first in alphabetical order i.e. if you had to choose between AG " \
                     "and AD, then you would choose AD first. "
        self.answer = self.min[1]
        self.answer_type = "text"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.Graph()
        plt.figure(figsize=(6, 6))

        G.add_nodes_from("ABCDEFG")
        pos = {
            "A": (1, 1.5),
            "B": (1, 0.5),
            "C": (0.5, 1.25),
            "D": (1.5, 1.25),
            "G": (1, 1),
            "E": (0.5, 0.75),
            "F": (1.5, 0.75)
        }
        G.add_edges_from((["A", "G"], ["B", "G"], ["C", "G"], ["D", "G"], ["G", "E"], ["G", "F"]))
        G.add_edges_from((["D", "F"], ["A", "C"], ["A", "D"], ["E", "C"], ["B", "E"], ["B", "F"]))
        nx.draw(G, with_labels=True, pos=pos, node_color="white", edgecolors="black", node_size=1500)
        plt.text(0.7, 1.4, f"{self.AC[0]}", fontsize=20)
        plt.text(1.25, 1.4, f"{self.AD[0]}", fontsize=20)
        plt.text(1.02, 1.25, f"{self.AG[0]}", fontsize=20)
        plt.text(1.02, 0.75, f"{self.BG[0]}", fontsize=20)
        plt.text(0.4, 1, f"{self.CE[0]}", fontsize=20)
        plt.text(1.55, 1, f"{self.DF[0]}", fontsize=20)
        plt.text(0.7, 0.55, f"{self.BE[0]}", fontsize=20)
        plt.text(1.25, 0.55, f"{self.BF[0]}", fontsize=20)
        plt.text(0.75, 1.15, f"{self.CG[0]}", fontsize=20)
        plt.text(1.2, 1.15, f"{self.DG[0]}", fontsize=20)
        plt.text(0.75, 0.95, f"{self.EG[0]}", fontsize=20)
        plt.text(1.2, 0.95, f"{self.FG[0]}", fontsize=20)

        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q153:
    # find azure area in square
    def __init__(self):
        self.side = rd.randint(2, 20)
        self.query = "The azure area in the figure is composed of 4 identical sectors, which can be combined to form " \
                     "a complete circle. What is the area of the azure part"
        self.answer = self.side * self.side / 4 * np.pi
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
        triangle = plt.Polygon([(2, 2), (-2, 2), (-2, -2), (2, -2)], closed=True, fill=True, edgecolor='black',
                               facecolor='white')
        wedge1 = Wedge((-2, -2), 2, 0, 90, facecolor="azure", edgecolor="black")
        wedge2 = Wedge((-2, 2), 2, -90, 0, facecolor="azure", edgecolor="black")
        wedge3 = Wedge((2, 2), 2, 180, 270, facecolor="azure", edgecolor="black")
        wedge4 = Wedge((2, -2), 2, 90, 180, facecolor="azure", edgecolor="black")
        ax.add_patch(triangle)
        ax.add_patch(wedge1)
        ax.add_patch(wedge2)
        ax.add_patch(wedge3)
        ax.add_patch(wedge4)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(-0.2, 2.2, f"{self.side}", fontsize=14)
        plt.text(2.2, 0,  f"{self.side}", fontsize=14)
        plt.text(-2.6, 0,  f"{self.side}", fontsize=14)
        plt.text(-0.2, -2.6,  f"{self.side}", fontsize=14)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q154:
    # find azure area in square
    def __init__(self):
        self.side = rd.randint(2, 20)
        self.query = "The white area in the figure is composed of 4 identical sectors, which can be combined to form " \
                     "a complete circle. What is the area of the azure part"
        self.answer = self.side * self.side - self.side * self.side / 4 * np.pi
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
        triangle = plt.Polygon([(2, 2), (-2, 2), (-2, -2), (2, -2)], closed=True, fill=True, edgecolor='black',
                               facecolor='azure')
        wedge1 = Wedge((-2, -2), 2, 0, 90, facecolor="white", edgecolor="black")
        wedge2 = Wedge((-2, 2), 2, -90, 0, facecolor="white", edgecolor="black")
        wedge3 = Wedge((2, 2), 2, 180, 270, facecolor="white", edgecolor="black")
        wedge4 = Wedge((2, -2), 2, 90, 180, facecolor="white", edgecolor="black")
        ax.add_patch(triangle)
        ax.add_patch(wedge1)
        ax.add_patch(wedge2)
        ax.add_patch(wedge3)
        ax.add_patch(wedge4)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(-0.2, 2.2, f"{self.side}", fontsize=14)
        plt.text(2.2, 0, f"{self.side}", fontsize=14)
        plt.text(-2.6, 0, f"{self.side}", fontsize=14)
        plt.text(-0.2, -2.6, f"{self.side}", fontsize=14)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q155:
    # fibonacchi/find the missing number
    def __init__(self):
        self.fbnc = list(range(1, 9))
        self.fbnc[0] = rd.randint(1, 5)
        self.fbnc[1] = rd.randint(6, 10)
        for i in range(2, 8):
            self.fbnc[i] = self.fbnc[i - 1] + self.fbnc[i - 2]
        self.fbnc.append("?")
        self.query = "Find the missing number in the last node."
        self.answer = self.fbnc[6] + self.fbnc[7]
        self.answer_type = "float"
        self.subject = "puzzle test"
        self.level = "high school"

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
        nx.draw(G, with_labels=True, pos=pos, node_color="white", edgecolors="black", node_size=1500)

        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q156:
    # fibonacchi/find the missing number (more hints)
    def __init__(self):
        self.fbnc = list(range(1, 9))
        self.fbnc[0] = rd.randint(1, 5)
        self.fbnc[1] = rd.randint(6, 10)
        for i in range(2, 8):
            self.fbnc[i] = self.fbnc[i - 1] + self.fbnc[i - 2]
        self.fbnc.append("?")
        self.query = "Find the missing number in the last node."
        self.answer = self.fbnc[6] + self.fbnc[7]
        self.answer_type = "float"
        self.subject = "puzzle test"
        self.level = "high school"

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


class Q157:
    # geometry proof: AE=AF
    def __init__(self):
        self.AE = rd.randint(1, 20)
        self.query = "As shown in the figure, quadrilateral ABCD is a square, with DE parallel to AC, and CE equal to " \
                     f"CA. Line EC intersects the extended line of DA at point F. AE = {self.AE}, find the length of AF"
        self.answer = self.AE
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q157temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q157temp.png"), dest_image_path)


class Q158:
    # vector
    def __init__(self):
        self.d = rd.choice([-2, -1, 1, 2])
        self.e = rd.choice([-3, -2, -1, 1, 2, 3])
        self.xA = rd.randint(-3, 3)
        self.xB = rd.randint(-3, 3)
        while self.xA == self.xB:
            self.xB = rd.randint(-3, 3)
        self.yA = self.d * self.xA + self.e
        self.yB = self.d * self.xB + self.e
        self.query = "What are the coordinates of the vector between two blue points?"
        self.answer = f"({self.xA - self.xB}, {self.yA - self.yB})"
        self.answer_type = "text"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        d = self.d
        e = self.e
        x1 = np.linspace(-10, 10, 200, endpoint=True)
        f1 = d * x1 + e
        xA = self.xA
        xB = self.xB
        yA = d * xA + e
        yB = d * xB + e
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
        plt.scatter(xA, yA, color='blue')
        plt.scatter(xB, yB, color='blue')
        ax.annotate('', xy=(xA, yA), xytext=(xB, yB), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))

        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q159:
    # shaded area between horizontal line and root function
    def __init__(self):
        self.a = rd.choice([1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 6, 1 / 7])
        self.query = f"Find the area of the region bounded by the curves y = x^1/{int(1/self.a)}, y = 1, and x = 5."
        self.answer = 1/(self.a + 1) * (5 ** (self.a + 1)) - 1/(self.a + 1) - 4
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        a = self.a
        x = np.linspace(0, 10, 200, endpoint=True)
        rx = np.linspace(1, 5, 200, endpoint=True)
        f1 = 0 * x + 1
        f2 = x ** a
        fr1 = 0 * rx + 1
        fr2 = rx ** a
        plt.plot(x, f1, color='blue', linewidth=1.5)
        plt.plot(x, f2, color='orange', linewidth=1.5)
        plt.xlim(-5 * 1.1, 5 * 1.1)
        plt.ylim(-5 * 1.1, 5 * 1.1)
        plt.xticks([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        plt.yticks([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        ax = plt.gca()
        print(self.query)
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.fill_between(rx, fr1, fr2, color='lightgray')
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q160:
    # parabola transformation
    def __init__(self):
        self.a = rd.choice([1, 2, 3, 4, 5])
        self.cond = rd.choice([[1, "C"], [2, "D"], [3, "A"], [4, "B"]])
        self.query = "The blue curve is the function transformed from black curve. What transformation is applied to " \
                     "the original function?  choice: (A) shift up (B) shift down (C) shift left (D) shift right "
        self.answer = self.cond[1]
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        a = self.a
        cond = self.cond[0]
        x = np.linspace(-10, 10, 200, endpoint=True)
        ori = x ** 2
        if cond == 1:
            cubic = (x + a) ** 2
        elif cond == 2:
            cubic = (x - a) ** 2
        elif cond == 3:
            cubic = x ** 2 + a
        elif cond == 4:
            cubic = x ** 2 - a
        plt.plot(x, cubic, color='blue', linewidth=1.5)
        plt.plot(x, ori, color='black', linewidth=1.5)
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)

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
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()

