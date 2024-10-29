import math
import shutil
import networkx as nx
import os.path
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from PIL import Image, ImageDraw, ImageFont
from matplotlib.patches import *


class Q241:
    # DFS 1
    def __init__(self):
        self.lst = rd.sample(["A", "B", "C", "D", "E", "F", "G"], 7)
        self.query = "Which node will be visited first if using pre-order DFS on the following tree graph?"
        self.answer = self.lst[0]
        self.answer_type = "text"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.Graph()
        plt.figure(figsize=(7, 6))
        lst = self.lst
        G.add_nodes_from(lst)
        pos = {
            f"{lst[0]}": (0.8, 1.2),
            f"{lst[2]}": (0.4, 1),
            f"{lst[3]}": (1.2, 1),
            f"{lst[4]}": (0, 0.8),
            f"{lst[1]}": (0.9, 0.8),
            f"{lst[5]}": (0.7, 0.8),
            f"{lst[6]}": (1.6, 0.8),
        }
        G.add_edges_from([[lst[0], lst[2]], [lst[0], lst[3]], [lst[2], lst[4]], [lst[2], lst[5]], [lst[3], lst[1]],
                          [lst[3], lst[6]]])
        nx.draw(G, with_labels=True, pos=pos, node_color="white", edgecolors="black", node_size=1500)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q242:
    # DFS 2
    def __init__(self):
        self.lst = rd.sample(["A", "B", "C", "D", "E", "F", "G"], 7)
        self.query = "Which node will be visited first if using inorder DFS on the following tree graph?"
        self.answer = self.lst[4]
        self.answer_type = "text"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.Graph()
        plt.figure(figsize=(7, 6))
        lst = self.lst
        G.add_nodes_from(lst)
        pos = {
            f"{lst[0]}": (0.8, 1.2),
            f"{lst[2]}": (0.4, 1),
            f"{lst[3]}": (1.2, 1),
            f"{lst[4]}": (0, 0.8),
            f"{lst[1]}": (0.9, 0.8),
            f"{lst[5]}": (0.7, 0.8),
            f"{lst[6]}": (1.6, 0.8),
        }
        G.add_edges_from([[lst[0], lst[2]], [lst[0], lst[3]], [lst[2], lst[4]], [lst[2], lst[5]], [lst[3], lst[1]],
                          [lst[3], lst[6]]])
        nx.draw(G, with_labels=True, pos=pos, node_color="white", edgecolors="black", node_size=1500)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q243:
    # DFS 3
    def __init__(self):
        self.lst = rd.sample(["A", "B", "C", "D", "E", "F", "G"], 7)
        self.query = "Which node will be secondly visited if using post-order DFS on the following tree graph?"
        self.answer = self.lst[5]
        self.answer_type = "text"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.Graph()
        plt.figure(figsize=(7, 6))
        lst = self.lst
        G.add_nodes_from(lst)
        pos = {
            f"{lst[0]}": (0.8, 1.2),
            f"{lst[2]}": (0.4, 1),
            f"{lst[3]}": (1.2, 1),
            f"{lst[4]}": (0, 0.8),
            f"{lst[1]}": (0.9, 0.8),
            f"{lst[5]}": (0.7, 0.8),
            f"{lst[6]}": (1.6, 0.8),
        }
        G.add_edges_from([[lst[0], lst[2]], [lst[0], lst[3]], [lst[2], lst[4]], [lst[2], lst[5]], [lst[3], lst[1]],
                          [lst[3], lst[6]]])
        nx.draw(G, with_labels=True, pos=pos, node_color="white", edgecolors="black", node_size=1500)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q244:
    # binary search tree 1
    def __init__(self):
        self.G = nx.Graph()
        rlst = rd.sample(list(range(1, 101)), 7)
        lst = sorted(rlst)
        self.G.add_nodes_from(lst)
        self.pos = {
            lst[3]: (0.8, 1.2),
            lst[1]: (0.4, 1),
            lst[5]: (1.2, 1),
            lst[0]: (0, 0.8),
            lst[4]: (0.9, 0.8),
            lst[2]: (0.7, 0.8),
            lst[6]: (1.6, 0.8),
        }
        self.G.add_edges_from([[lst[3], lst[1]], [lst[5], lst[3]], [lst[1], lst[0]], [lst[2], lst[1]], [lst[4], lst[5]],
                          [lst[5], lst[6]]])
        self.node = rd.randint(1, 101)
        self.query = f"If we want to add a node with value {self.node} to this binary tree, under which node should " \
                     f"it be added?  choice: (A) {lst[0]} (B) {lst[2]} (C) {lst[4]} (D) {lst[6]} "
        if self.node < lst[1]:
            self.answer = "A"
        elif lst[3] >= self.node >= lst[1]:
            self.answer = "B"
        elif self.node > lst[5]:
            self.answer = "C"
        elif lst[3] <= self.node <= lst[5]:
            self.answer = "D"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(7, 6))
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", node_size=1500, font_size=20)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q245:
    # binary search tree 5
    def __init__(self):
        self.G = nx.Graph()
        rlst = rd.sample(list(range(1, 101)), 7)
        lst = sorted(rlst)
        self.G.add_nodes_from(lst)
        self.pos = {
            lst[3]: (0.8, 1.2),
            lst[1]: (0.4, 1),
            lst[5]: (1.2, 1),
            lst[0]: (0, 0.8),
            lst[4]: (0.9, 0.8),
            lst[2]: (0.7, 0.8),
            lst[6]: (1.6, 0.8),
        }
        self.G.add_edges_from([[lst[3], lst[1]], [lst[5], lst[3]], [lst[1], lst[0]], [lst[2], lst[1]], [lst[4], lst[5]],
                          [lst[5], lst[6]]])
        self.node = rd.randint(1, 101)
        self.query = "Which data structure is the following graph shown?  (A) heap (B) stack (C) binary tree (D) " \
                     "planted tree "
        self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(7, 6))
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", node_size=1500,  font_size=20)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q246:
    # binary search tree 3
    def __init__(self):
        rlst = rd.sample(list(range(1, 101)), 6)
        self.lst = sorted(rlst)
        self.query = f"Insert 6 keys {rlst[0]}, {rlst[1]}, {rlst[2]}, {rlst[3]}, {rlst[4]}, {rlst[5]} into an " \
                     f"initially empty binary search tree. Suppose that the structure of the resulting tree is given " \
                     f"in the figure. What is the possible value of the root? "
        self.answer = self.lst[3]
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q246temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q246temp.png"), dest_image_path)


class Q247:
    # number of nodes 1
    def __init__(self):
        self.num = rd.randint(1, 50)
        self.query = "How many nodes are in this empty graph?"
        self.answer = self.num
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.empty_graph(self.num)
        nx.draw_random(G, node_size=150, edgecolors='black')
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q248:
    # number of nodes 2
    def __init__(self):
        self.num = rd.randint(1, 50)
        self.num2 = rd.randint(1, 30)
        self.query = "How many pink nodes are in this empty graph?"
        self.answer = self.num
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.empty_graph(self.num)
        nx.draw_random(G, node_size=150, edgecolors='black')
        G2 = nx.empty_graph(self.num2)
        nx.draw_random(G2, node_size=150, node_color = 'pink', edgecolors='black')
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q249:
    # number of nodes 3
    def __init__(self):
        self.num = rd.randint(1, 50)
        self.num2 = rd.randint(1, 30)
        self.query = "Find the difference between the number of blue nodes and red nodes."
        self.answer = abs(self.num - self.num2)
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.empty_graph(self.num)
        nx.draw_random(G, node_size=150, edgecolors='black')
        G2 = nx.empty_graph(self.num2)
        nx.draw_random(G2, node_size=150, node_color = 'red', edgecolors='black')
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q250:
    # number of nodes 4
    def __init__(self):
        self.num = rd.sample(list(range(1, 20)), 4)
        self.a1 = [self.num[0], "lightblue"]
        self.a2 = [self.num[1], "lightpink"]
        self.a3 = [self.num[2], "lightgreen"]
        self.a4 = [self.num[3], "orange"]
        self.am = max(self.a1, self.a2, self.a3, self.a4)
        self.query = "What color has the largest number of nodes?  choice: (A) blue (B) pink (C) green (D) orange"
        if self.am[1] == "lightblue":
            self.answer = "A"
        elif self.am[1] == "lightpink":
            self.answer = "B"
        elif self.am[1] == "lightgreen":
            self.answer = "C"
        elif self.am[1] == "orange":
            self.answer = "D"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.empty_graph(self.a1[0])
        nx.draw_random(G, node_size=150, node_color=self.a1[1], edgecolors='black')
        G2 = nx.empty_graph(self.a2[0])
        nx.draw_random(G2, node_size=150, node_color=self.a2[1], edgecolors='black')
        G3 = nx.empty_graph(self.a3[0])
        nx.draw_random(G3, node_size=150, node_color=self.a3[1], edgecolors='black')
        G4 = nx.empty_graph(self.a4[0])
        nx.draw_random(G4, node_size=150, node_color=self.a4[1], edgecolors='black')
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q251:
    # strongly connected 1
    def __init__(self):
        self.num = rd.randint(3, 12)
        self.G = nx.DiGraph()
        for i in range(0, self.num):
            t1 = rd.choice(["A", "B", "C", "D"])
            t2 = rd.choice(["A", "B", "C", "D"])
            self.G.add_edge(t1, t2)
        self.pos = nx.spring_layout(self.G)
        self.query = "Is the following directed graph strongly connected?  choice: (A) Yes (B) No"
        if nx.is_strongly_connected(self.G):
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", nodelist=self.pos,
                node_size=1000, font_color="black")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q252:
    # isomorphic 1
    def __init__(self):
        self.num = rd.randint(3, 8)
        self.G = nx.Graph()
        self.G2 = nx.diamond_graph()
        i = 0
        while i < self.num:
            t1 = rd.choice(["A", "B", "C", "D"])
            t2 = rd.choice(["A", "B", "C", "D"])
            if t1 != t2:
                self.G.add_edge(t1, t2)
                i += 1
        self.pos = nx.spring_layout(self.G)
        self.query = "Is the left graph isomorphic with the right graph?  choice: (A) Yes (B) No"
        if nx.is_isomorphic(self.G, self.G2):
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure()
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", nodelist=self.pos, node_size=1000,
                font_color="black")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        plt.savefig(os.path.join(destination_folder, f"image/Q{num}temp1.png"))
        plt.figure()
        nx.draw(self.G2, node_color="white", edgecolors="black")
        plt.savefig(os.path.join(destination_folder, f"image/Q{num}temp2.png"))
        plt.close()
        image1 = Image.open(os.path.join(destination_folder, f"image/Q{num}temp1.png"))
        image2 = Image.open(os.path.join(destination_folder, f"image/Q{num}temp2.png"))
        width = image1.width + image2.width
        new_image = Image.new('RGB', (width, max(image1.height, image2.height)))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (image1.width, 0))
        new_image.save(os.path.join(destination_folder, f"image/image{num}.png"), dpi=(600, 600))
        plt.close()
        if os.path.exists(os.path.join(destination_folder, f"image/Q{num}temp1.png")):
            os.remove(os.path.join(destination_folder, f"image/Q{num}temp1.png"))
        if os.path.exists(os.path.join(destination_folder, f"image/Q{num}temp2.png")):
            os.remove(os.path.join(destination_folder, f"image/Q{num}temp2.png"))


class Q253:
    # isomorphic 2
    def __init__(self):
        self.num = rd.randint(8, 12)
        self.G = nx.Graph()
        self.G2 = nx.hypercube_graph(3)
        i = 0
        while i < self.num:
            t1 = rd.choice(["A", "B", "C", "D", "E", "F", "G", "H"])
            t2 = rd.choice(["A", "B", "C", "D", "E", "F", "G", "H"])
            if t1 != t2:
                self.G.add_edge(t1, t2)
                i += 1
        self.pos = nx.spring_layout(self.G)
        self.query = "Is the left graph isomorphic with the right graph?  choice: (A) Yes (B) No"
        if nx.is_isomorphic(self.G, self.G2):
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure()
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", nodelist=self.pos, node_size=1000,
                font_color="black")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        plt.savefig(os.path.join(destination_folder,f"image/Q{num}temp1.png"))
        plt.figure()
        nx.draw(self.G2, node_color="white", edgecolors="black")
        plt.savefig(os.path.join(destination_folder,f"image/Q{num}temp2.png"))
        plt.close()
        image1 = Image.open(os.path.join(destination_folder,f"image/Q{num}temp1.png"))
        image2 = Image.open(os.path.join(destination_folder,f"image/Q{num}temp2.png"))
        width = image1.width + image2.width
        new_image = Image.new('RGB', (width, max(image1.height, image2.height)))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (image1.width, 0))
        new_image.save(os.path.join(destination_folder,f"image/image{num}.png"), dpi=(600, 600))
        plt.close()
        if os.path.exists(os.path.join(destination_folder,f"image/Q{num}temp1.png")):
            os.remove(os.path.join(destination_folder,f"image/Q{num}temp1.png"))
        if os.path.exists(os.path.join(destination_folder,f"image/Q{num}temp2.png")):
            os.remove(os.path.join(destination_folder,f"image/Q{num}temp2.png"))


class Q254:
    # isomorphic 3
    def __init__(self):
        self.num = rd.randint(8, 12)
        self.G = nx.Graph()
        self.G2 = nx.cycle_graph(8)
        i = 0
        while i < self.num:
            t1 = rd.choice(["A", "B", "C", "D", "E", "F", "G", "H"])
            t2 = rd.choice(["A", "B", "C", "D", "E", "F", "G", "H"])
            if t1 != t2:
                self.G.add_edge(t1, t2)
                i += 1
        self.pos = nx.spring_layout(self.G)
        self.query = "Is the left graph isomorphic with the right graph?  choice: (A) Yes (B) No"
        if nx.is_isomorphic(self.G, self.G2):
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure()
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", nodelist=self.pos, node_size=1000,
                font_color="black")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        plt.savefig(os.path.join(destination_folder,f"image/Q{num}temp1.png"))
        plt.figure()
        nx.draw(self.G2, node_color="white", edgecolors="black")
        plt.savefig(os.path.join(destination_folder, f"image/Q{num}temp2.png"))
        plt.close()
        image1 = Image.open(os.path.join(destination_folder,f"image/Q{num}temp1.png"))
        image2 = Image.open(os.path.join(destination_folder,f"image/Q{num}temp2.png"))
        width = image1.width + image2.width
        new_image = Image.new('RGB', (width, max(image1.height, image2.height)))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (image1.width, 0))
        new_image.save(os.path.join(destination_folder,f"image/image{num}.png"), dpi=(600, 600))
        plt.close()
        if os.path.exists(os.path.join(destination_folder,f"image/Q{num}temp1.png")):
            os.remove(os.path.join(destination_folder,f"image/Q{num}temp1.png"))
        if os.path.exists(os.path.join(destination_folder,f"image/Q{num}temp2.png")):
            os.remove(os.path.join(destination_folder,f"image/Q{num}temp2.png"))


class Q255:
    # expression in tree
    def __init__(self):
        self.constant = rd.sample(list(range(1, 100)), 5)
        self.rlst = rd.sample(list(range(1, 101)), 9)
        self.query = "The tree shown in image reserves an expression. Calculate this expression and output the result."
        self.answer = (self.constant[0] * (self.constant[1] + self.constant[2])) + (self.constant[3] * self.constant[4])
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.Graph()
        plt.figure(figsize=(7, 6))
        rlst = self.rlst
        constant = self.constant
        lst = sorted(rlst)
        G.add_nodes_from(lst)
        pos = {
            lst[3]: (0.8, 1.2),
            lst[1]: (0.4, 1),
            lst[5]: (1.2, 1),
            lst[0]: (0, 0.8),
            lst[4]: (0.9, 0.8),
            lst[2]: (0.7, 0.8),
            lst[6]: (1.6, 0.8),
            lst[7]: (0.3, 0.6),
            lst[8]: (1.1, 0.6)
        }
        G.add_edges_from(
            [[lst[3], lst[1]], [lst[5], lst[3]], [lst[1], lst[0]], [lst[2], lst[1]], [lst[4], lst[5]], [lst[5], lst[6]],
             [lst[7], lst[2]], [lst[8], lst[2]]])
        nx.draw(G, with_labels=True, pos=pos, node_color="white", edgecolors="black", node_size=1500,
                font_color='white')
        plt.text(1.2 - 0.02, 1 - 0.015, "*", fontsize=20)
        plt.text(0.4 - 0.02, 1 - 0.015, "*", fontsize=20)
        plt.text(0.8 - 0.03, 1.2 - 0.01, "+", fontsize=20)
        plt.text(0.7 - 0.03, 0.8 - 0.01, "+", fontsize=20)
        plt.text(0 - 0.04, 0.8 - 0.015, f"{constant[0]}", fontsize=18)
        plt.text(0.3 - 0.04, 0.6 - 0.015, f"{constant[1]}", fontsize=18)
        plt.text(1.1 - 0.04, 0.6 - 0.015, f"{constant[2]}", fontsize=18)
        plt.text(0.9 - 0.04, 0.8 - 0.015, f"{constant[3]}", fontsize=18)
        plt.text(1.6 - 0.04, 0.8 - 0.015, f"{constant[4]}", fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q256:
    # longest path
    def __init__(self):
        self.lst = [rd.randint(1, 100) for _ in range(10)]
        self.G = nx.DiGraph()
        self.G.add_nodes_from("SABCDG")
        plt.figure(figsize=(6, 3))
        self.pos = {
            "S": (0, 1),
            "A": (0.5, 1.5),
            "B": (0.5, 0.5),
            "D": (1.5, 0.5),
            "C": (1.5, 1.5),
            "G": (2, 1)
        }
        self.G.add_edges_from(
            [("S", "A", {"cost": self.lst[0]}), ("S", "B", {"cost": self.lst[1]}), ("A", "C", {"cost": self.lst[2]}), ("C", "G", {"cost": self.lst[3]}),
             ("B", "C", {"cost": self.lst[4]}), ("C", "D", {"cost": self.lst[5]}), ("D", "G", {"cost": self.lst[6]}), ("B", "A", {"cost": self.lst[7]}),
             ("A", "D", {"cost": self.lst[8]}), ("B", "D", {"cost": self.lst[9]})])
        self.query = "Find the longest path length in the following directed acyclic graph."
        self.answer = nx.dag_longest_path_length(self.G, weight="cost")
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(6, 3))
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", node_size=1000)
        plt.text(0.1, 1.25, f"{self.lst[0]}", fontsize=12)
        plt.text(0.1, 0.7, f"{self.lst[1]}", fontsize=12)
        plt.text(0.95, 1.55, f"{self.lst[2]}", fontsize=12)
        plt.text(0.95, 0.4, f"{self.lst[9]}", fontsize=12)
        plt.text(0.6, 1.2, f"{self.lst[8]}", fontsize=12)
        plt.text(1.3, 1.2, f"{self.lst[4]}", fontsize=12)
        plt.text(1.8, 1.25, f"{self.lst[3]}", fontsize=12)
        plt.text(1.8, 0.7, f"{self.lst[6]}", fontsize=12)
        plt.text(0.4, 1, f"{self.lst[7]}", fontsize=12)
        plt.text(1.52, 1, f"{self.lst[5]}", fontsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q257:
    # shortest path
    def __init__(self):
        self.lst = [rd.randint(1, 100) for _ in range(10)]
        self.G = nx.DiGraph()
        self.G.add_nodes_from("SABCDG")
        plt.figure(figsize=(6, 3))
        self.pos = {
            "S": (0, 1),
            "A": (0.5, 1.5),
            "B": (0.5, 0.5),
            "D": (1.5, 0.5),
            "C": (1.5, 1.5),
            "G": (2, 1)
        }
        self.G.add_edges_from(
            [("S", "A", {"cost": self.lst[0]}), ("S", "B", {"cost": self.lst[1]}), ("A", "C", {"cost": self.lst[2]}),
             ("C", "G", {"cost": self.lst[3]}),
             ("B", "C", {"cost": self.lst[4]}), ("C", "D", {"cost": self.lst[5]}), ("D", "G", {"cost": self.lst[6]}),
             ("B", "A", {"cost": self.lst[7]}),
             ("A", "D", {"cost": self.lst[8]}), ("B", "D", {"cost": self.lst[9]})])
        self.query = "Find the shortest path length in the following directed acyclic graph."
        self.answer = nx.shortest_path_length(self.G, "S", "G", weight="cost")
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(6, 3))
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", node_size=1000)
        plt.text(0.1, 1.25, f"{self.lst[0]}", fontsize=12)
        plt.text(0.1, 0.7, f"{self.lst[1]}", fontsize=12)
        plt.text(0.95, 1.55, f"{self.lst[2]}", fontsize=12)
        plt.text(0.95, 0.4, f"{self.lst[9]}", fontsize=12)
        plt.text(0.6, 1.2, f"{self.lst[8]}", fontsize=12)
        plt.text(1.3, 1.2, f"{self.lst[4]}", fontsize=12)
        plt.text(1.8, 1.25, f"{self.lst[3]}", fontsize=12)
        plt.text(1.8, 0.7, f"{self.lst[6]}", fontsize=12)
        plt.text(0.4, 1, f"{self.lst[7]}", fontsize=12)
        plt.text(1.52, 1, f"{self.lst[5]}", fontsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q258:
    # Prüfer code 1
    def __init__(self):
        self.sequence = [rd.randint(0, 6) for _ in range(5)]
        self.query = "Give the Prüfer code of the following graph. Please answer in the format like '[1, 2, 3, 4, 5]'"
        self.answer = str(self.sequence)
        self.answer_type = "text"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        tree2 = nx.from_prufer_sequence(self.sequence)
        nx.draw(tree2, node_color='white', edgecolors='black', font_size=18, with_labels=True, node_size=1000)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q259:
    # expression in tree 2
    def __init__(self):
        self.constant = rd.sample(list(range(1, 100)), 5)
        self.rlst = rd.sample(list(range(1, 101)), 9)
        self.query = "The tree shown in image reserves an expression. Calculate this expression and output the result."
        self.answer = (self.constant[0] + (self.constant[1] * self.constant[2])) * (self.constant[3] + self.constant[4])
        self.answer_type = "float"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        G = nx.Graph()
        plt.figure(figsize=(7, 6))
        rlst = self.rlst
        constant = self.constant
        lst = sorted(rlst)
        G.add_nodes_from(lst)
        pos = {
            lst[3]: (0.8, 1.2),
            lst[1]: (0.4, 1),
            lst[5]: (1.2, 1),
            lst[0]: (0, 0.8),
            lst[4]: (0.9, 0.8),
            lst[2]: (0.7, 0.8),
            lst[6]: (1.6, 0.8),
            lst[7]: (0.3, 0.6),
            lst[8]: (1.1, 0.6)
        }
        G.add_edges_from(
            [[lst[3], lst[1]], [lst[5], lst[3]], [lst[1], lst[0]], [lst[2], lst[1]], [lst[4], lst[5]], [lst[5], lst[6]],
             [lst[7], lst[2]], [lst[8], lst[2]]])
        nx.draw(G, with_labels=True, pos=pos, node_color="white", edgecolors="black", node_size=1500,
                font_color='white')
        plt.text(1.2 - 0.02, 1 - 0.015, "+", fontsize=20)
        plt.text(0.4 - 0.02, 1 - 0.015, "+", fontsize=20)
        plt.text(0.8 - 0.03, 1.2 - 0.01, "*", fontsize=20)
        plt.text(0.7 - 0.03, 0.8 - 0.01, "*", fontsize=20)
        plt.text(0 - 0.04, 0.8 - 0.015, f"{constant[0]}", fontsize=18)
        plt.text(0.3 - 0.04, 0.6 - 0.015, f"{constant[1]}", fontsize=18)
        plt.text(1.1 - 0.04, 0.6 - 0.015, f"{constant[2]}", fontsize=18)
        plt.text(0.9 - 0.04, 0.8 - 0.015, f"{constant[3]}", fontsize=18)
        plt.text(1.6 - 0.04, 0.8 - 0.015, f"{constant[4]}", fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q260:
    # tournament
    def __init__(self):
        self.num = rd.randint(3, 12)
        self.G = nx.DiGraph()
        for i in range(0, self.num):
            t1 = rd.choice(["A", "B", "C", "D"])
            t2 = rd.choice(["A", "B", "C", "D"])
            self.G.add_edge(t1, t2)
        self.pos = nx.spring_layout(self.G)
        self.query = "Is the following directed graph a tournament?  choice: (A) Yes (B) No"
        if nx.is_tournament(self.G):
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "graph theory"
        self.level = "undergraduate"

    def draw(self, num):
        nx.draw(self.G, with_labels=True, pos=self.pos, node_color="white", edgecolors="black", nodelist=self.pos,
                node_size=1000, font_color="black")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()
