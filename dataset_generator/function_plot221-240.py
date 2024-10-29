import os

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from matplotlib.patches import *


class Q221:
    # planar graph 1
    def __init__(self):
        self.trial = rd.randint(12, 24)
        self.query = "Is the following graph a planar graph?  choice: (A) Yes (B) No"
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
        for i in range(0, self.trial):
            t1 = rd.choice(["A", "B", "C", "D", "E", "F"])
            t2 = rd.choice(["A", "B", "C", "D", "E", "F"])
            if t1 != t2:
                self.G.add_edge(t1, t2)
        if self.G.number_of_edges() > 3 * 6 - 6:
            self.answer = "B"
        else:
            self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(6, 4))
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="lightgreen", edgecolors="black", nodelist=self.pos,
                node_size=200,
                font_color="lightgreen")
        nx.draw_networkx_edges(self.G, self.pos, edge_color="black")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q222:
    # remove edge 1
    def __init__(self):
        self.num = rd.choice([4, 5, 6])
        if self.num == 4:
            self.lst = rd.sample([1, 1, 1, 1, 0, 0], 6)
        elif self.num == 5:
            self.lst = rd.sample([1, 1, 1, 1, 1, 0], 6)
        elif self.num == 6:
            self.lst = rd.sample([1, 1, 1, 1, 1, 1], 6)
        self.query = "What is the maximum number of edges to remove so that the following graph is still connected?"
        self.answer = sum(self.lst) - 3
        self.answer_type = "float"
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


class Q223:
    # complete graph 2
    def __init__(self):
        self.trial = rd.randint(10, 20)
        self.query = "How many edges should be added to this graph so that it is complete?"
        self.G = nx.Graph()
        self.G.add_nodes_from("ABCDE")
        self.pos = {
            "A": (1, 1.2),
            "C": (0.5, 1),
            "D": (1.5, 1),
            "E": (0.7, 0.75),
            "B": (1.3, 0.75)
        }
        for i in range(0, self.trial):
            t1 = rd.choice(["A", "B", "C", "D", "E"])
            t2 = rd.choice(["A", "B", "C", "D", "E"])
            if t1 != t2:
                self.G.add_edge(t1, t2)
        self.answer = 10 - self.G.number_of_edges()
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(6, 6))
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", node_size=1500)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q224:
    # planar graph 2
    def __init__(self):
        self.trial = rd.randint(10, 30)
        self.query = "Is the following graph a planar graph?  choice: (A) Yes (B) No"
        self.G = nx.Graph()
        self.G.add_nodes_from("ABCDE")
        self.pos = {
            "A": (1, 1.2),
            "C": (0.5, 1),
            "D": (1.5, 1),
            "E": (0.7, 0.75),
            "B": (1.3, 0.75)
        }
        for i in range(0, self.trial):
            t1 = rd.choice(["A", "B", "C", "D", "E"])
            t2 = rd.choice(["A", "B", "C", "D", "E"])
            if t1 != t2:
                self.G.add_edge(t1, t2)
        if self.G.number_of_edges() > 9:
            self.answer = "B"
        else:
            self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(6, 6))
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", node_size=1500)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q225:
    # remove edge 2
    def __init__(self):
        self.query = "What is the maximum number of edges to remove so that the following graph is still connected?"
        self.G = nx.Graph()
        self.G.add_nodes_from("ABCDE")
        self.pos = {
            "A": (1, 1.2),
            "C": (0.5, 1),
            "D": (1.5, 1),
            "E": (0.7, 0.75),
            "B": (1.3, 0.75)
        }
        while not nx.is_connected(self.G):
            t1 = rd.choice(["A", "B", "C", "D", "E"])
            t2 = rd.choice(["A", "B", "C", "D", "E"])
            if t1 != t2:
                self.G.add_edge(t1, t2)
        self.answer = self.G.number_of_edges() - 4
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(6, 6))
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", node_size=1500)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q226:
    # Euler path 1
    def __init__(self):
        self.trial = rd.randint(9, 27)
        self.G = nx.Graph()
        self.G.add_nodes_from("ABCDEFG")
        self.pos = {
            "A": (1, 1),
            "C": (0.6, 1),
            "D": (1.4, 1),
            "E": (0.8, 0.75),
            "B": (1.2, 0.75),
            "F": (0.4, 0.75),
            "G": (1.6, 0.75),
        }
        for i in range(0, self.trial):
            t1 = rd.choice(["A", "B", "C", "D", "E", "F", "G"])
            if t1 == "C":
                t2 = rd.choice(["A", "B", "C", "E", "F", "G"])
            elif t1 == "D":
                t2 = rd.choice(["A", "B", "E", "F", "G"])
            elif t1 == "F":
                t2 = rd.choice(["A", "C", "D", "E", "F"])
            elif t1 == "E":
                t2 = rd.choice(["A", "B", "C", "D", "E", "F"])
            elif t1 == "B":
                t2 = rd.choice(["A", "B", "C", "D", "E", "G"])
            elif t1 == "G":
                t2 = rd.choice(["A", "B", "C", "D", "G"])
            else:
                t2 = rd.choice(["A", "B", "C", "D", "E", "F", "G"])
            if t1 != t2:
                self.G.add_edge(t1, t2)
        self.query = "Is the following graph containing a Euler circuit?  choice: (A) Yes (B) No"
        if self.G.degree("A") % 2 == 0 and self.G.degree("B") % 2 == 0 and self.G.degree(
                "C") % 2 == 0 and self.G.degree("D") % 2 == 0 and self.G.degree("E") % 2 == 0 and self.G.degree(
            "G") % 2 == 0 and self.G.degree("F") % 2 == 0:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(6, 3))
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", node_size=1500)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q227:
    # Hamilton path 1
    def __init__(self):
        self.trial = rd.randint(9, 27)
        self.G = nx.Graph()
        self.G.add_nodes_from("ABCDEFG")
        self.pos = {
            "A": (1, 1),
            "C": (0.6, 1),
            "D": (1.4, 1),
            "E": (0.8, 0.75),
            "B": (1.2, 0.75),
            "F": (0.4, 0.75),
            "G": (1.6, 0.75),
        }
        for i in range(0, self.trial):
            t1 = rd.choice(["A", "B", "C", "D", "E", "F", "G"])
            if t1 == "C":
                t2 = rd.choice(["A", "B", "C", "E", "F", "G"])
            elif t1 == "D":
                t2 = rd.choice(["A", "B", "E", "F", "G"])
            elif t1 == "F":
                t2 = rd.choice(["A", "C", "D", "E", "F"])
            elif t1 == "E":
                t2 = rd.choice(["A", "B", "C", "D", "E", "F"])
            elif t1 == "B":
                t2 = rd.choice(["A", "B", "C", "D", "E", "G"])
            elif t1 == "G":
                t2 = rd.choice(["A", "B", "C", "D", "G"])
            else:
                t2 = rd.choice(["A", "B", "C", "D", "E", "F", "G"])
            if t1 != t2:
                self.G.add_edge(t1, t2)
        self.query = "Is the following graph containing a Hamiltonian circuit?  choice: (A) Yes (B) No"
        self.lst = [self.G.degree("A"), self.G.degree("B"), self.G.degree("C"), self.G.degree("D"), self.G.degree("E"),
                    self.G.degree("F"), self.G.degree("G")]
        if min(self.lst) >= 3:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(6, 3))
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", node_size=1500)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q228:
    # Euler path 2
    def __init__(self):
        self.trial = rd.randint(9, 36)
        self.G = nx.Graph()
        self.G.add_nodes_from("ABCDEFGHI")
        self.pos = {
            "A": (0.5, 1.5),
            "B": (1, 1.5),
            "C": (1.5, 1.5),
            "D": (0.5, 1),
            "E": (1, 1),
            "F": (1.5, 1),
            "G": (0.5, 0.5),
            "H": (1, 0.5),
            "I": (1.5, 0.5)
        }
        for i in range(0, self.trial):
            t1 = rd.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
            if t1 == "A":
                t2 = rd.choice(["A", "B", "D", "E", "F", "H"])
            elif t1 == "B":
                t2 = rd.choice(["A", "B", "C", "D", "E", "F", "G", "I"])
            elif t1 == "C":
                t2 = rd.choice([ "B", "C", "D", "E", "F", "H"])
            elif t1 == "D":
                t2 = rd.choice(["A", "B", "C", "D", "E", "G", "H", "I"])
            elif t1 == "F":
                t2 = rd.choice(["A", "B", "C", "E", "F", "G", "H", "I"])
            elif t1 == "G":
                t2 = rd.choice(["B", "D", "E", "F", "G", "H"])
            elif t1 == "H":
                t2 = rd.choice(["A", "C", "D", "E", "F", "G", "H", "I"])
            elif t1 == "I":
                t2 = rd.choice(["B", "D", "E", "F", "H", "I"])
            else:
                t2 = rd.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
            if t1 != t2:
                self.G.add_edge(t1, t2)
        self.query = "Is the following graph containing a Euler circuit?  choice: (A) Yes (B) No"
        if self.G.degree("A") % 2 == 0 and self.G.degree("B") % 2 == 0 and self.G.degree(
                "C") % 2 == 0 and self.G.degree("D") % 2 == 0 and self.G.degree("E") % 2 == 0 and self.G.degree(
            "G") % 2 == 0 and self.G.degree("F") % 2 == 0 and self.G.degree("H") % 2 == 0 and self.G.degree(
            "I") % 2 == 0:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(6, 6))
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", node_size=1500)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q229:
    # Hamilton path 2
    def __init__(self):
        self.trial = rd.randint(18, 36)
        self.G = nx.Graph()
        self.G.add_nodes_from("ABCDEFGHI")
        self.pos = {
            "A": (0.5, 1.5),
            "B": (1, 1.5),
            "C": (1.5, 1.5),
            "D": (0.5, 1),
            "E": (1, 1),
            "F": (1.5, 1),
            "G": (0.5, 0.5),
            "H": (1, 0.5),
            "I": (1.5, 0.5)
        }
        for i in range(0, self.trial):
            t1 = rd.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
            if t1 == "A":
                t2 = rd.choice(["A", "B", "D", "E", "F", "H"])
            elif t1 == "B":
                t2 = rd.choice(["A", "B", "C", "D", "E", "F", "G", "I"])
            elif t1 == "C":
                t2 = rd.choice(["B", "C", "D", "E", "F", "H"])
            elif t1 == "D":
                t2 = rd.choice(["A", "B", "C", "D", "E", "G", "H", "I"])
            elif t1 == "F":
                t2 = rd.choice(["A", "B", "C", "E", "F", "G", "H", "I"])
            elif t1 == "G":
                t2 = rd.choice(["B", "D", "E", "F", "G", "H"])
            elif t1 == "H":
                t2 = rd.choice(["A", "C", "D", "E", "F", "G", "H", "I"])
            elif t1 == "I":
                t2 = rd.choice(["B", "D", "E", "F", "H", "I"])
            else:
                t2 = rd.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
            if t1 != t2:
                self.G.add_edge(t1, t2)
        self.query = "Is the following graph containing a Hamiltonian circuit?  choice: (A) Yes (B) No"
        self.lst = [self.G.degree("A"), self.G.degree("B"), self.G.degree("C"), self.G.degree("D"), self.G.degree("E"),
                    self.G.degree("F"), self.G.degree("G"), self.G.degree("H"), self.G.degree("I")]
        self.min = min(self.lst)
        self.lst.remove(self.min)
        self.min2 = min(self.lst)
        if self.min >= 4 or self.min + self.min2 >= 4:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(6, 6))
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", node_size=1500)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q230:
    # Euler path 3
    def __init__(self):
        self.trial = rd.randint(6, 27)
        self.G = nx.Graph()
        self.G.add_nodes_from("ABCDEF")
        self.pos = {
            "A": (1, 1.5),
            "B": (1, 0.5),
            "C": (0.5, 1.25),
            "D": (1.5, 1.25),
            "E": (0.5, 0.75),
            "F": (1.5, 0.75)
        }
        for i in range(0, self.trial):
            t1 = rd.choice(["A", "B", "C", "D", "E", "F"])
            t2 = rd.choice(["A", "B", "C", "D", "E", "F"])
            if t1 != t2:
                self.G.add_edge(t1, t2)
        self.query = "Is the following graph containing a Euler circuit?  choice: (A) Yes (B) No"
        if self.G.degree("A") % 2 == 0 and self.G.degree("B") % 2 == 0 and self.G.degree(
                "C") % 2 == 0 and self.G.degree("D") % 2 == 0 and self.G.degree("E") % 2 == 0 and self.G.degree(
            "F") % 2 == 0:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(6, 6))
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", node_size=1500)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q231:
    # component 1
    def __init__(self):
        self.trial = rd.randint(4, 10)
        self.query = "How many components does the following graph have?"
        self.G = nx.Graph()
        self.G.add_nodes_from("ABCDEFGH")
        self.pos = {
            "A": (0.5, 1.5),
            "B": (0.5, 0.5),
            "C": (1, 0.5),
            "D": (1.5, 0.5),
            "E": (1, 1.5),
            "F": (1.5, 1.5),
            "G": (2.0, 1.5),
            "H": (2.0, 0.5)
        }
        for i in range(0, self.trial):
            t1 = rd.choice(["B", "C", "D", "H"])
            t2 = rd.choice(["A", "E", "F", "G"])
            self.G.add_edge(t1, t2)
        self.answer = nx.number_connected_components(self.G)
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(6, 4))
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="black", edgecolors="black", nodelist=self.pos, node_size=200,
                font_color="black")
        nx.draw_networkx_edges(self.G, self.pos, edge_color="black")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q232:
    # component 2
    def __init__(self):
        self.trial = rd.randint(4, 12)
        self.query = "How many components does the following graph have?"
        self.G = nx.Graph()
        self.G.add_nodes_from("ABCDEF")
        self.pos = {
            "A": (1, 1.5),
            "B": (1, 0.5),
            "C": (0.5, 1.25),
            "D": (1.5, 1.25),
            "E": (0.5, 0.75),
            "F": (1.5, 0.75)
        }
        for i in range(0, self.trial):
            t1 = rd.choice(["A", "B", "C", "D", "E", "F"])
            t2 = rd.choice(["A", "B", "C", "D", "E", "F"])
            if t1 != t2:
                self.G.add_edge(t1, t2)
        self.answer = nx.number_connected_components(self.G)
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(6, 6))
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="black", edgecolors="black", nodelist=self.pos, node_size=200,
                font_color="black")
        nx.draw_networkx_edges(self.G, self.pos, edge_color="black")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q233:
    # chromatic index 1
    def __init__(self):
        self.n = rd.randint(2, 9)
        self.query = "Find the chromatic index of the following graph."
        if self.n % 2 == 0:
            self.answer = self.n - 1
        else:
            self.answer = self.n
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.complete_graph(self.n, create_using=None)
        nx.draw(G, edgecolors='black', node_color='white')
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q234:
    # chromatic index 2
    def __init__(self):
        self.n = rd.randint(3, 9)
        self.query = "Find the chromatic index of the following graph."
        if self.n % 2 == 0:
            self.answer = 2
        else:
            self.answer = 3
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.cycle_graph(self.n, create_using=None)
        nx.draw(G, edgecolors='black', node_color='white')
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q235:
    # chromatic index 3
    def __init__(self):
        self.n = rd.randint(2, 11)
        self.query = "Find the chromatic index of the following graph."
        if self.n == 2:
            self.answer = 2
        else:
            self.answer = 3
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.ladder_graph(self.n, create_using=None)
        nx.draw(G, edgecolors='black', node_color='white')
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q236:
    # chromatic number 1
    def __init__(self):
        self.n = rd.randint(2, 9)
        self.query = "Find the chromatic number of the following graph."
        self.answer = self.n
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.complete_graph(self.n, create_using=None)
        nx.draw(G, edgecolors='black', node_color='white')
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q237:
    # chromatic number 2
    def __init__(self):
        self.n = rd.randint(3, 9)
        self.query = "Find the chromatic number of the following graph."
        if self.n % 2 == 0:
            self.answer = 2
        else:
            self.answer = 3
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.cycle_graph(self.n, create_using=None)
        nx.draw(G, edgecolors='black', node_color='white')
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q238:
    # chromatic number 3
    def __init__(self):
        self.n = rd.randint(2, 11)
        self.query = "Find the chromatic number of the following graph."
        self.answer = 2
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.ladder_graph(self.n, create_using=None)
        nx.draw(G, edgecolors='black', node_color='white')
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q239:
    # height of tree
    def __init__(self):
        self.query = "The root of the balanced tree is at the center of the image. What is the height of the " \
                     "following tree? "
        self.r = rd.randint(1, 3)
        self.h = rd.randint(1, 3)
        self.answer = self.h
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.balanced_tree(r=self.r, h=self.h)
        nx.draw(G, node_color="black", node_size=200)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q240:
    # planar graph 2
    def __init__(self):
        self.query = "Count the number of faces of the following graph."
        self.r = rd.randint(1, 3)
        self.h = rd.randint(1, 3)
        self.G = nx.balanced_tree(r=self.r, h=self.h)
        self.answer = nx.number_of_edges(self.G) - nx.number_of_nodes(self.G) + 2
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = self.G
        nx.draw(G, node_color="black", node_size=200)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()
