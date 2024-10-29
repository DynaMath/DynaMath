import math
import random
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
from plottable import Table
import mpl_toolkits.axisartist as ax
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image, ImageDraw, ImageFont
from matplotlib.patches import *


class Q427:
    def __init__(self):
        self.num_girls = np.random.randint(50, 100)
        self.num_boys = np.random.randint(50, 100)
        self.sizes = [self.num_girls, self.num_boys]
        self.labels = ['Girls', 'Boys']
        total_students = self.num_girls + self.num_boys
        self.query = "The pie chart below represents the number of girls and boys at a United States elementary school. What is the percentage of the boys? The answer should be a percentage between 0 and 100"
        self.answer = round((self.num_boys / total_students) * 100, 1)  # Answer rounded to one decimal place
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "elementary school"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(5, 5))
        wedges, texts, autotexts = ax.pie(self.sizes, labels=None, autopct=lambda p: '{:.0f}'.format(p * sum(self.sizes) / 100), startangle=90,
                colors=['deeppink', 'blue'])
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(28)
        plt.legend(self.labels)
        plt.title("Number of Girls and Boys at Elementary School")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q428:
    def __init__(self):
        self.num_grade1 = np.random.randint(50, 100)
        self.num_grade2 = np.random.randint(50, 100)
        self.num_grade3 = np.random.randint(50, 100)
        self.num_grade4 = np.random.randint(50, 100)
        self.num_grade5 = np.random.randint(50, 100)
        self.sizes = [self.num_grade1, self.num_grade2, self.num_grade3, self.num_grade4, self.num_grade5]
        self.labels = ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5']
        total_students = sum(self.sizes)
        self.query = "The pie chart below represents the number of each grade at a United States elementary school. What is the percentage of Grade 2? The answer should be a percentage between 0 and 100."
        self.answer = round((self.num_grade2 / total_students) * 100, 1)  # Answer rounded to one decimal place
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "elementary school"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(5,5))
        wedges, texts, autotexts = ax.pie(self.sizes, labels=None, autopct=lambda p: '{:.0f}'.format(p * sum(self.sizes) / 100), startangle=90, colors=['red', 'blue', 'green', 'orange', 'purple'])
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(20)
        plt.legend(self.labels)
        plt.title("Number of Students in Each Grade")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q429:
    def __init__(self):
        self.num_dogs = np.random.randint(2000, 4000)
        self.num_cats = np.random.randint(2000, 4000)
        self.num_birds = np.random.randint(500, 2000)
        self.num_fish = np.random.randint(500, 2000)
        self.sizes = [self.num_dogs, self.num_cats, self.num_birds, self.num_fish]
        self.labels = ['Dogs', 'Cats', 'Birds', 'Fish']
        self.query = "The pie chart below represents the types of pets pet owners have in City A. Suppose City A has 10000 pets in total, what is the most popular pet in City A? Choices: (A) Dogs (B) Cats (C) Birds (D) Fish"
        max_index = np.argmax(self.sizes)
        self.answer = ['A', 'B', 'C', 'D'][max_index]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "elementary school"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(5, 5))
        wedges, texts, autotexts = ax.pie(self.sizes, labels=None, autopct='%1.1f%%', startangle=90, colors=['gold', 'skyblue', 'lightgreen', 'lightcoral'])
        for autotext in autotexts:
            #autotext.set_color('white')
            autotext.set_fontsize(20)
        plt.legend(self.labels)
        plt.title("Types of Pets in City A")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q430:
    def __init__(self):
        self.sizes = random.sample(range(1, 10), 4)
        self.query = "Which color has the largest slice? Choices: (A) Red (B) Blue (C) Orange (D) Purple"
        max_index = np.argmax(self.sizes)
        self.answer = ['A', 'B', 'C', 'D'][max_index]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "elementary school"

    def draw(self, num):
        labels = ['Red', 'Blue', 'Orange', 'Purple']
        fig, ax = plt.subplots(figsize=(5, 5))
        wedges, texts, autotexts = ax.pie(self.sizes, labels=None, autopct='%1.1f%%', startangle=90, colors=['red', 'blue', 'orange', 'purple'])

        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(18)
        plt.legend(labels)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q431:
    def __init__(self):
        self.sizes = np.random.randint(1, 10, 4)
        total = np.sum(self.sizes)
        self.query = "Is the orange slice larger than 25%? Choices: (A) Yes (B) No"
        orange_percentage = self.sizes[2] / total * 100
        if orange_percentage > 25:
            self.answer = 'A'
        else:
            self.answer = 'B'
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "elementary school"

    def draw(self, num):
        labels = ['Red', 'Blue', 'Orange', 'Purple']
        fig, ax = plt.subplots(figsize=(5, 5))
        wedges, texts, autotexts = ax.pie(self.sizes, labels=None, autopct='%1.1f%%', startangle=90, colors=['red', 'blue', 'orange', 'purple'])
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(18)
        plt.legend(labels)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q432:
    def __init__(self):
        self.sizes = np.random.randint(1, 10, 4)
        self.query = "Is the total size of orange and purple greater than red and blue combined? Choices: (A) Yes (B) No"
        if self.sizes[2] + self.sizes[3] > self.sizes[0] + self.sizes[1]:
            self.answer = 'A'
        else:
            self.answer = 'B'
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "elementary school"

    def draw(self, num):
        labels = ['Red', 'Blue', 'Orange', 'Purple']
        fig, ax = plt.subplots(figsize=(5, 5))
        wedges, texts, autotexts = ax.pie(self.sizes, labels=None, autopct='%1.1f%%', startangle=90, colors=['red', 'blue', 'orange', 'purple'])
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(18)
        plt.legend(labels)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q433:
    def __init__(self):
        self.sizes = np.random.randint(1, 10, 4)
        total = np.sum(self.sizes)
        self.query = "What is the combined percentage of red and blue slices? Choices: (A) <30% (B) 30%-60% (C) >60%"
        combined_percentage = (self.sizes[0] + self.sizes[1]) / total * 100
        if combined_percentage < 30:
            self.answer = 'A'
        elif combined_percentage <= 60:
            self.answer = 'B'
        else:
            self.answer = 'C'
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "elementary school"

    def draw(self, num):
        labels = ['Red', 'Blue', 'Orange', 'Purple']
        fig, ax = plt.subplots(figsize=(5, 5))
        wedges, texts, autotexts = ax.pie(self.sizes, labels=None, autopct='%1.1f%%', startangle=90, colors=['red', 'blue', 'orange', 'purple'])

        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(18)
        plt.legend(labels)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()
        

class Q434:
    def __init__(self):
        self.sizes = np.random.randint(1, 10, 4)
        self.query = "Are the slices for red and blue equal? Choices: (A) Yes (B) No"
        if self.sizes[0] == self.sizes[1]:
            self.answer = 'A'
        else:
            self.answer = 'B'
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "elementary school"

    def draw(self, num):
        labels = ['Red', 'Blue', 'Orange', 'Purple']
        fig, ax = plt.subplots(figsize=(5, 5))
        wedges, texts, autotexts = ax.pie(self.sizes, labels=None, autopct='%1.1f%%', startangle=90, colors=['red', 'blue', 'orange', 'purple'])
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(18)
        plt.legend(labels)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q435:
    def __init__(self):
        self.sizes = np.random.randint(1, 10, 4)
        self.query = "Is the red slice smaller than the blue slice? Choices: (A) Yes (B) No"
        if self.sizes[0] < self.sizes[1]:
            self.answer = 'A'
        else:
            self.answer = 'B'
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "elementary school"

    def draw(self, num):
        labels = ['Red', 'Blue', 'Orange', 'Purple']
        fig, ax = plt.subplots(figsize=(5, 5))
        wedges, texts, autotexts = ax.pie(self.sizes, labels=None, autopct='%1.1f%%', startangle=90, colors=['red', 'blue', 'orange', 'purple'])
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(18)
        plt.legend(labels)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q436:
    def __init__(self):
        self.sizes = np.random.randint(1, 10, 4)
        self.query = "Which color has the smallest slice? Choices: (A) Red (B) Blue (C) Orange (D) Purple"
        min_index = np.argmin(self.sizes)
        self.answer = ['A', 'B', 'C', 'D'][min_index]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "elementary school"

    def draw(self, num):
        labels = ['Red', 'Blue', 'Orange', 'Purple']
        fig, ax = plt.subplots(figsize=(5, 5))
        wedges, texts, autotexts = ax.pie(self.sizes, labels=None, autopct='%1.1f%%', startangle=90, colors=['red', 'blue', 'orange', 'purple'])
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(18)
        plt.legend(labels)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()













