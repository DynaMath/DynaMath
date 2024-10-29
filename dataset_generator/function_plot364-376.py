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
from matplotlib.transforms import Affine2D
from plottable import Table
import mpl_toolkits.axisartist as ax
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image, ImageDraw, ImageFont
from matplotlib.patches import *
from scipy.spatial import cKDTree

import numpy as np
import matplotlib.pyplot as plt
import random


class Q364:
    def __init__(self):
        self.x = np.linspace(-20, 20, 100)  
        function_type = random.choice(['linear', 'quadratic', 'cubic'])
        
        if function_type == 'linear':
            a = random.uniform(-10, 10)
            b = random.uniform(-10, 10)
            self.y = a * self.x + b + np.random.normal(0, 6, self.x.shape)
            self.answer = "A"
        elif function_type == 'quadratic':
            a = random.uniform(-10, 10)
            b = random.uniform(-10, 10)
            c = random.uniform(-10, 10)
            self.y = a * self.x**2 + b * self.x + c + np.random.normal(0, 20, self.x.shape)
            self.answer = "B"
        elif function_type == 'cubic':
            a = random.uniform(-10, 10)
            b = random.uniform(-10, 10)
            c = random.uniform(-10, 10)
            d = random.uniform(-10, 10)
            self.y = a * self.x**3 + b * self.x**2 + c * self.x + d + np.random.normal(0, 20, self.x.shape)
            self.answer = "C"
        
        self.answer_type = "multiple choice"
        self.query = "Which type of function best describes the correlation? (A) Linear (B) Quadratic (C) Cubic"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure()
        plt.scatter(self.x, self.y, label='Data Points', color='blue')
        plt.xlabel("X", fontsize=20)
        plt.ylabel("Y", fontsize=20)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q365:
    def __init__(self):
        self.x = np.linspace(0.1, 10, 100)  # Avoid zero for logarithmic function
        
        function_type = random.choice(['exponential', 'logarithmic', 'sine'])
        
        if function_type == 'exponential':
            a = random.uniform(0.5, 2)
            b = random.uniform(0.1, 1)
            self.y = a * np.exp(b * self.x) + np.random.normal(0, 1, self.x.shape)
            self.answer = "A"
        elif function_type == 'logarithmic':
            a = random.uniform(1, 5)
            b = random.uniform(0.5, 2)
            self.y = a * np.log(b * self.x) + np.random.normal(0, 1, self.x.shape)
            self.answer = "B"
        elif function_type == 'sine':
            a = random.uniform(1, 5)
            b = random.uniform(0.5, 2)
            self.y = a * np.sin(b * self.x) + np.random.normal(0, 1, self.x.shape)
            self.answer = "C"
        
        self.answer_type = "multiple choice"
        self.query = "Which type of function best describes the correlation? (A) Exponential (B) Logarithmic (C) Sine"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure()
        plt.scatter(self.x, self.y, label='Data Points', color='blue')
        plt.xlabel("X", fontsize=20)
        plt.ylabel("Y", fontsize=20)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.title("Scatter Plot of Data", fontsize=20)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


# Example usage
# FunctionCorrelationMultipleChoice2().draw(499)


#generate multiple scatter lines and ask: which group has larger scope, which group has largest, smallest value, largest mean value, etc


class Q366:
    def __init__(self):
        self.query = "Which group has the largest Y value?\nA. Group 1\nB. Group 2\nC. Group 3"
        self.group1 = np.random.normal(loc=[np.random.randint(-10, 10), np.random.randint(-10, 10)], scale=[1, 1], size=(100, 2))
        self.group2 = np.random.normal(loc=[np.random.randint(-10, 10), np.random.randint(-10, 10)], scale=[1, 1], size=(100, 2))
        self.group3 = np.random.normal(loc=[np.random.randint(-10, 10), np.random.randint(-10, 10)], scale=[1, 1], size=(100, 2))
        
        max_y_group1 = np.max(self.group1[:, 1])
        max_y_group2 = np.max(self.group2[:, 1])
        max_y_group3 = np.max(self.group3[:, 1])
        
        if max_y_group1 > max_y_group2 and max_y_group1 > max_y_group3:
            self.answer = "A"
        elif max_y_group2 > max_y_group1 and max_y_group2 > max_y_group3:
            self.answer = "B"
        else:
            self.answer = "C"
        
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure()
        plt.scatter(self.group1[:, 0], self.group1[:, 1], label='Group 1', color='blue')
        plt.scatter(self.group2[:, 0], self.group2[:, 1], label='Group 2', color='red')
        plt.scatter(self.group3[:, 0], self.group3[:, 1], label='Group 3', color='green')
        plt.xlabel("X", fontsize=20)
        plt.ylabel("Y", fontsize=20)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.title("Scatter Plot of Groups", fontsize=20)
        plt.legend(fontsize=12)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q367:
    def __init__(self):
        self.query = "How many points are inside the circle?"
        self.radius = 5
        self.center = (0, 0)
        self.points = np.random.uniform(-10, 10, (10, 2))
        self.answer = np.sum(np.sqrt(np.sum((self.points - self.center) ** 2, axis=1)) <= self.radius)
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots()
        circle = plt.Circle(self.center, self.radius, color='blue', fill=False, linewidth=3)
        ax.add_artist(circle)
        ax.scatter(self.points[:, 0], self.points[:, 1], color='red', s=20)  # Adjusted point size to be smaller
        ax.set_xlim(-12, 12)
        ax.set_ylim(-12, 12)
        ax.set_aspect('equal', 'box')
        plt.xlabel("X coordinate", fontsize=18)
        plt.ylabel("Y coordinate", fontsize=18)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.title("Scatter Points and Circle", fontsize=20)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q368:
    def __init__(self):
        self.query = "How many red points are inside the blue circle?"
        self.radius = 5
        self.center = (0, 0)
        self.points = np.random.uniform(-10, 10, (10, 2))
        self.answer = np.sum(np.sqrt(np.sum((self.points - self.center) ** 2, axis=1)) <= self.radius)
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots()
        circle = plt.Circle(self.center, self.radius, color='blue', fill=False, linewidth=3)
        ax.add_artist(circle)
        ax.scatter(self.points[:, 0], self.points[:, 1], color='red', s=20)  # Adjusted point size to be smaller
        ax.set_xlim(-12, 12)
        ax.set_ylim(-12, 12)
        ax.set_aspect('equal', 'box')
        plt.xlabel("X coordinate", fontsize=18)
        plt.ylabel("Y coordinate", fontsize=18)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.title("Scatter Points and Circle", fontsize=20)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()



class Q369:
    def __init__(self):
        self.query = "How many points are inside the rectangle?"
        self.rect_width = 15
        self.rect_height = 10
        self.rect_center = (0, 0)
        self.rect_x = self.rect_center[0] - self.rect_width / 2
        self.rect_y = self.rect_center[1] - self.rect_height / 2
        self.points = np.random.uniform(-15, 15, (10, 2))
        self.answer = np.sum(
            (self.points[:, 0] >= self.rect_x) & (self.points[:, 0] <= self.rect_x + self.rect_width) &
            (self.points[:, 1] >= self.rect_y) & (self.points[:, 1] <= self.rect_y + self.rect_height)
        )
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots()
        rect = plt.Rectangle((self.rect_x, self.rect_y), self.rect_width, self.rect_height, color='blue', fill=False, linewidth=3)
        ax.add_artist(rect)
        ax.scatter(self.points[:, 0], self.points[:, 1], color='red', s=20)  # Adjusted point size to be smaller
        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)
        ax.set_aspect('equal', 'box')
        plt.xlabel("X coordinate", fontsize=18)
        plt.ylabel("Y coordinate", fontsize=18)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.title("Scatter Points and Rectangle", fontsize=20)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q370:
    def __init__(self):
        self.query = "How many points are inside the triangle?"
        self.triangle_vertices = np.array([[0, 5], [-5, -5], [5, -5]])
        self.points = np.random.uniform(-10, 10, (10, 2))
        self.answer = np.sum([self.is_inside_triangle(pt) for pt in self.points])
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "undergraduate"

    def is_inside_triangle(self, point):
        # Barycentric coordinates method
        def sign(p1, p2, p3):
            return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

        b1 = sign(point, self.triangle_vertices[0], self.triangle_vertices[1]) < 0.0
        b2 = sign(point, self.triangle_vertices[1], self.triangle_vertices[2]) < 0.0
        b3 = sign(point, self.triangle_vertices[2], self.triangle_vertices[0]) < 0.0

        return (b1 == b2) and (b2 == b3)

    def draw(self, num):
        fig, ax = plt.subplots()
        triangle = Polygon(self.triangle_vertices, closed=True, edgecolor='blue', fill=False, linewidth=3)
        ax.add_patch(triangle)
        ax.scatter(self.points[:, 0], self.points[:, 1], color='red', s=20)  # Adjusted point size to be smaller
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_aspect('equal', 'box')
        plt.xlabel("X coordinate", fontsize=18)
        plt.ylabel("Y coordinate", fontsize=18)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.title("Scatter Points and Triangle", fontsize=20)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q371:
    def __init__(self):
        self.query = "Please count how many points are outside the circle?"
        self.radius = 5
        self.center = (0, 0)
        self.points = np.random.uniform(-10, 10, (10, 2))
        self.answer = np.sum(np.sqrt(np.sum((self.points - self.center) ** 2, axis=1)) > self.radius)
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots()
        circle = plt.Circle(self.center, self.radius, color='blue', fill=False, linewidth=3)
        ax.add_artist(circle)
        ax.scatter(self.points[:, 0], self.points[:, 1], color='red', s=20)
        ax.set_xlim(-12, 12)
        ax.set_ylim(-12, 12)
        ax.set_aspect('equal', 'box')
        plt.xlabel("X coordinate", fontsize=18)
        plt.ylabel("Y coordinate", fontsize=18)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


# count how many points are located inside/outside the circle
class Q372:
    def __init__(self):
        self.query = "Please count how many red points are outside the blue circle?"
        self.radius = 5
        self.center = (0, 0)
        self.points = np.random.uniform(-10, 10, (10, 2))
        self.answer = np.sum(np.sqrt(np.sum((self.points - self.center) ** 2, axis=1)) > self.radius)
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots()
        circle = plt.Circle(self.center, self.radius, color='blue', fill=False, linewidth=3)
        ax.add_artist(circle)
        ax.scatter(self.points[:, 0], self.points[:, 1], color='red', s=20)
        ax.set_xlim(-12, 12)
        ax.set_ylim(-12, 12)
        ax.set_aspect('equal', 'box')
        plt.xlabel("X coordinate", fontsize=18)
        plt.ylabel("Y coordinate", fontsize=18)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q373:
    def __init__(self):
        self.query = "How many points are outside the ellipse?"
        self.ellipse_width = 15
        self.ellipse_height = 10
        self.center = (0, 0)
        self.points = np.random.uniform(-15, 15, (10, 2))
        self.answer = np.sum(
            ((self.points[:, 0] - self.center[0])**2 / (self.ellipse_width / 2)**2 +
             (self.points[:, 1] - self.center[1])**2 / (self.ellipse_height / 2)**2) > 1
        )
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots()
        ellipse = plt.Circle(self.center, self.ellipse_width / 2, color='blue', fill=False, linewidth=3, label="Ellipse")
        transform = Affine2D().scale(1, self.ellipse_height / self.ellipse_width) + ax.transData
        ellipse.set_transform(transform)
        ax.add_artist(ellipse)
        ax.scatter(self.points[:, 0], self.points[:, 1], color='red', s=20)  # Adjusted point size to be smaller
        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)
        ax.set_aspect('equal', 'box')
        plt.xlabel("X coordinate", fontsize=18)
        plt.ylabel("Y coordinate", fontsize=18)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.title("Scatter Points and Ellipse", fontsize=20)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q374:
    def __init__(self):
        self.query = "How many points are outside the rectangle?"
        self.rect_width = 15
        self.rect_height = 10
        self.rect_center = (0, 0)
        self.rect_x = self.rect_center[0] - self.rect_width / 2
        self.rect_y = self.rect_center[1] - self.rect_height / 2
        self.points = np.random.uniform(-15, 15, (10, 2))
        self.answer = np.sum(
            (self.points[:, 0] < self.rect_x) | (self.points[:, 0] > self.rect_x + self.rect_width) |
            (self.points[:, 1] < self.rect_y) | (self.points[:, 1] > self.rect_y + self.rect_height)
        )
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots()
        rect = plt.Rectangle((self.rect_x, self.rect_y), self.rect_width, self.rect_height, color='blue', fill=False, linewidth=3)
        ax.add_artist(rect)
        ax.scatter(self.points[:, 0], self.points[:, 1], color='red', s=20)  # Adjusted point size to be smaller
        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)
        ax.set_aspect('equal', 'box')
        plt.xlabel("X coordinate", fontsize=18)
        plt.ylabel("Y coordinate", fontsize=18)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.title("Scatter Points and Rectangle", fontsize=20)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q375:
    def __init__(self):
        self.query = "How many points are outside the triangle?"
        self.triangle_vertices = np.array([[0, 5], [-5, -5], [5, -5]])
        self.points = np.random.uniform(-10, 10, (10, 2))
        self.answer = np.sum([not self.is_inside_triangle(pt) for pt in self.points])
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "undergraduate"

    def is_inside_triangle(self, point):
        # Barycentric coordinates method
        def sign(p1, p2, p3):
            return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

        b1 = sign(point, self.triangle_vertices[0], self.triangle_vertices[1]) < 0.0
        b2 = sign(point, self.triangle_vertices[1], self.triangle_vertices[2]) < 0.0
        b3 = sign(point, self.triangle_vertices[2], self.triangle_vertices[0]) < 0.0

        return (b1 == b2) and (b2 == b3)

    def draw(self, num):
        fig, ax = plt.subplots()
        triangle = Polygon(self.triangle_vertices, closed=True, edgecolor='blue', fill=False, linewidth=3)
        ax.add_patch(triangle)
        ax.scatter(self.points[:, 0], self.points[:, 1], color='red', s=20)  # Adjusted point size to be smaller
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_aspect('equal', 'box')
        plt.xlabel("X coordinate", fontsize=18)
        plt.ylabel("Y coordinate", fontsize=18)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.title("Scatter Points and Triangle", fontsize=19)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q376:
    def __init__(self):
        self.query = "Which group has the smallest Y value?\nA. Group 1\nB. Group 2\nC. Group 3"
        self.group1 = np.random.normal(loc=[np.random.randint(-10, 10), np.random.randint(-10, 10)], scale=[0.5, 0.5],
                                       size=(100, 2))
        self.group2 = np.random.normal(loc=[np.random.randint(-10, 10), np.random.randint(-10, 10)], scale=[0.5, 0.5],
                                       size=(100, 2))
        self.group3 = np.random.normal(loc=[np.random.randint(-10, 10), np.random.randint(-10, 10)], scale=[0.5, 0.5],
                                       size=(100, 2))

        min_y_group1 = np.min(self.group1[:, 1])
        min_y_group2 = np.min(self.group2[:, 1])
        min_y_group3 = np.min(self.group3[:, 1])

        if min_y_group1 < min_y_group2 and min_y_group1 < min_y_group3:
            self.answer = "A"
        elif min_y_group2 < min_y_group1 and min_y_group2 < min_y_group3:
            self.answer = "B"
        else:
            self.answer = "C"

        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure()
        plt.scatter(self.group1[:, 0], self.group1[:, 1], label='Group 1', color='blue')
        plt.scatter(self.group2[:, 0], self.group2[:, 1], label='Group 2', color='red')
        plt.scatter(self.group3[:, 0], self.group3[:, 1], label='Group 3', color='green')
        plt.xlabel("X", fontsize=18)
        plt.ylabel("Y", fontsize=18)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.title("Scatter Plot of Groups")
        plt.legend(fontsize=12)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()
















