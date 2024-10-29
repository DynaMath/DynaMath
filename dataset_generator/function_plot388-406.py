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
from plottable import Table
import mpl_toolkits.axisartist as ax
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image, ImageDraw, ImageFont
from matplotlib.patches import *


class Q388:
    def __init__(self):
        self.countries = ['USA', 'Canada', 'UK', 'Australia']
        self.donations = [np.random.randint(10, 200, 100) for _ in self.countries]
        self.bins = [10, 50, 100, 150, 200]
        self.query = "The histograms below represent donation amounts in different countries. Which country has the most people to donate between $50 and $100? Choices: (A) USA (B) Canada (C) UK (D) Australia"
        counts = [np.sum((donation >= 50) & (donation <= 100)) for donation in self.donations]
        max_donations_index = np.argmax(counts)
        self.answer = ['A', 'B', 'C', 'D'][max_donations_index]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(12, 10))
        for i, country in enumerate(self.countries):
            plt.subplot(2, 2, i + 1)
            plt.hist(self.donations[i], bins=self.bins, color='green', edgecolor='black')
            plt.title(country, fontsize=18)
            if country == 'UK' or country == 'Australia':
                plt.xlabel('Donation Amount ($)', fontsize=18)
            plt.ylabel('Number of Donations', fontsize=18)
            plt.tick_params(axis='both', which='major', labelsize=18)
        plt.suptitle('Donation Amount Distribution by Country', fontsize=24)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q389:
    def __init__(self):
        self.cities = ['City A', 'City B']
        self.rainy_days_a = np.random.randint(0, 30, 12)
        self.rainy_days_b = np.random.randint(0, 30, 12)
        self.bins = np.arange(0, 31, 5)
        self.query = "The histograms below represent the number of rainy days per month in two cities. Which city has a higher number of rainy days? Choices: (A) City A (B) City B"
        total_rainy_days_a = np.sum(self.rainy_days_a)
        total_rainy_days_b = np.sum(self.rainy_days_b)
        self.answer = 'A' if total_rainy_days_a > total_rainy_days_b else 'B'
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.hist(self.rainy_days_a, bins=self.bins, color='blue', edgecolor='black')
        plt.yticks(np.arange(0, 8, 2))
        plt.title('City A', fontsize=20)
        plt.xlabel('Number of Rainy Days', fontsize=18)
        plt.ylabel('Number of Months', fontsize=18)
        plt.tick_params(axis='both', which='major', labelsize=20)

        plt.subplot(1, 2, 2)
        plt.hist(self.rainy_days_b, bins=self.bins, color='green', edgecolor='black')
        plt.yticks(np.arange(0, 8, 2))
        plt.title('City B', fontsize=20)
        plt.xlabel('Number of Rainy Days', fontsize=18)
        plt.tick_params(axis='both', which='major', labelsize=20)

        plt.suptitle('Monthly Rainy Days Distribution by City', fontsize=22)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q390:
    def __init__(self):
        self.scores = np.random.randint(50, 100, 30)
        self.bins = [50, 60, 70, 80, 90, 100]
        self.query = "The histogram below represents the scores of students in a class. What is the most common range of scores in the class? Choices: (A) 50-60 (B) 60-70 (C) 70-80 (D) 80-90 (E) 90-100"
        hist, bin_edges = np.histogram(self.scores, bins=self.bins)
        max_bin_index = np.argmax(hist)
        self.answer = ['A', 'B', 'C', 'D', 'E'][max_bin_index]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(8, 5))
        plt.hist(self.scores, bins=self.bins, color='blue', edgecolor='black')
        plt.xlabel('Score Range', fontsize=16)
        plt.ylabel('Number of Students', fontsize=16)
        plt.title('Distribution of Scores', fontsize=18)
        plt.yticks([1, 2, 3, 4, 5, 6, 7, 8])
        plt.tick_params(axis='both', which='major', labelsize=20)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q391:
    def __init__(self):
        self.departments = ['HR', 'IT', 'Finance', 'Marketing']
        self.work_hours = [np.random.randint(30, 60, 50) for _ in self.departments]
        self.bins = [30, 35, 40, 45, 50, 55, 60]
        self.query = "The histograms below represent the work hours of employees in different departments. Which department has the highest number of employees working more than 40 hours per week? Choices: (A) HR (B) IT (C) Finance (D) Marketing"
        counts = [np.sum(hours > 40) for hours in self.work_hours]
        max_hours_index = np.argmax(counts)
        self.answer = ['A', 'B', 'C', 'D'][max_hours_index]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(12, 10))
        for i, department in enumerate(self.departments):
            plt.subplot(2, 2, i + 1)
            plt.hist(self.work_hours[i], bins=self.bins, color='blue', edgecolor='black')
            plt.title(department, fontsize=20)
            if department == 'Finance' or department == 'Marketing':
                plt.xlabel('Hours', fontsize=18)
            if department == 'HR' or department == 'Finance':
                plt.ylabel('Number of Employees', fontsize=18)
            plt.tick_params(axis='both', which='major', labelsize=20)
        plt.suptitle('Work Hours Distribution by Department', fontsize=24)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q392:
    def __init__(self):
        self.category1 = np.random.randint(1, 11, 3)
        self.category2 = np.random.randint(1, 11, 3)
        self.category3 = np.random.randint(1, 11, 3)
        self.constant = rd.randint(1, 11)
        self.query = f"All values are integers. What is the sum of all values strictly greater than {self.constant} across all categories?"
        self.answer = np.sum(self.category1[self.category1 > self.constant]) + \
                        np.sum(self.category2[self.category2 > self.constant]) + \
                        np.sum(self.category3[self.category3 > self.constant])
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        total_width = 0.6
        n = 3
        width = total_width / n
        x = np.arange(3)
        plt.bar(x, self.category1, width, label='Category 1', color='blue')
        plt.bar(x + width, self.category2, width, label='Category 2', color='green')
        plt.bar(x + 2 * width, self.category3, width, label='Category 3', color='red')
        plt.xticks(np.arange(3), ['Item 1', 'Item 2', 'Item 3'], ha='center')
        plt.tick_params(axis='both', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.ylabel("Values", fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q393:
    def __init__(self):
        self.category1 = np.random.randint(1, 11, 4)
        self.category2 = np.random.randint(1, 11, 4)
        self.category3 = np.random.randint(1, 11, 4)
        self.query = f"All values are integers. What is the minimum value across all categories?"
        self.answer = min(np.min(self.category1), np.min(self.category2), np.min(self.category3))
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        total_width = 0.6
        n = 4
        width = total_width / n
        x = np.arange(4)
        plt.bar(x, self.category1, width, label='Category 1', color='blue')
        plt.bar(x + width, self.category2, width, label='Category 2', color='green')
        plt.bar(x + 2 * width, self.category3, width, label='Category 3', color='red')
        plt.xticks(np.arange(4), ['Item 1', 'Item 2', 'Item 3', 'Item 4'], fontsize=18)
        plt.tick_params(axis='y', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.ylabel("Values", fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q394:
    def __init__(self):
        self.category1 = np.random.randint(1, 11, 4)
        self.category2 = np.random.randint(1, 11, 4)
        self.category3 = np.random.randint(1, 11, 4)
        self.query = f"All values are integers. What is the sum of the squares of the differences between each value in Category 1 and the mean of Category 1?"
        mean_cat1 = np.mean(self.category1)
        diff_square_sum = np.sum((self.category1 - mean_cat1) ** 2)
        self.answer = diff_square_sum
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        total_width = 0.6
        n = 4
        width = total_width / n
        x = np.arange(4)
        plt.bar(x, self.category1, width, label='Category 1', color='blue')
        plt.bar(x + width, self.category2, width, label='Category 2', color='green')
        plt.bar(x + 2 * width, self.category3, width, label='Category 3', color='red')
        plt.xticks(np.arange(4), ['Item 1', 'Item 2', 'Item 3', 'Item 4'], fontsize=18)
        plt.tick_params(axis='y', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.ylabel("Values", fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q395:
    def __init__(self):
        self.category1 = np.random.randint(1, 11, 4)
        self.category2 = np.random.randint(1, 11, 4)
        self.category3 = np.random.randint(1, 11, 4)
        self.query = f"All values are integers. What is the sum of the squares of the differences between each value in Category 1 and the mean of Category 2?"
        mean_cat2 = np.mean(self.category2)
        diff_square_sum = np.sum((self.category1 - mean_cat2) ** 2)
        self.answer = diff_square_sum
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        total_width = 0.6
        n = 4
        width = total_width / n
        x = np.arange(4)
        plt.bar(x, self.category1, width, label='Category 1', color='blue')
        plt.bar(x + width, self.category2, width, label='Category 2', color='green')
        plt.bar(x + 2 * width, self.category3, width, label='Category 3', color='red')
        plt.xticks(np.arange(4), ['Item 1', 'Item 2', 'Item 3', 'Item 4'], fontsize=18)
        plt.tick_params(axis='y', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.ylabel("Values", fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q396:
    def __init__(self):
        self.category1 = np.random.randint(1, 11, 3)
        self.category2 = np.random.randint(1, 11, 3)
        self.category3 = np.random.randint(1, 11, 3)

        self.query = "All values are integers. What is the smallest range (difference between the maximum and minimum values) among the three categories?"

        range_cat1 = np.max(self.category1) - np.min(self.category1)
        range_cat2 = np.max(self.category2) - np.min(self.category2)
        range_cat3 = np.max(self.category3) - np.min(self.category3)

        self.answer = min(range_cat1, range_cat2, range_cat3)
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        total_width = 0.6
        n = 3
        width = total_width / n
        x = np.arange(3)
        plt.bar(x, self.category1, width, label='Category 1', color='blue')
        plt.bar(x + width, self.category2, width, label='Category 2', color='pink')
        plt.bar(x + 2 * width, self.category3, width, label='Category 3', color='gray')
        plt.xticks(np.arange(3), ['Item 1', 'Item 2', 'Item 3'], fontsize=18)
        plt.tick_params(axis='y', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.ylabel("Values", fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q397:
    def __init__(self):
        self.category1 = np.random.randint(1, 11, 3)
        self.category2 = np.random.randint(1, 11, 3)
        self.category3 = np.random.randint(1, 11, 3)

        self.query = "All values are integers. What is the product of the maximum values from each category?"

        max_value_cat1 = np.max(self.category1)
        max_value_cat2 = np.max(self.category2)
        max_value_cat3 = np.max(self.category3)

        self.answer = max_value_cat1 * max_value_cat2 * max_value_cat3
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        total_width = 0.6
        n = 3
        width = total_width / n
        x = np.arange(3)
        plt.bar(x, self.category1, width, label='Category 1', color='blue')
        plt.bar(x + width, self.category2, width, label='Category 2', color='green')
        plt.bar(x + 2 * width, self.category3, width, label='Category 3', color='orange')
        plt.xticks(np.arange(3), ['Item 1', 'Item 2', 'Item 3'], fontsize=18)
        plt.tick_params(axis='y', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.ylabel("Values", fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q398:
    def __init__(self):
        self.category1 = np.random.randint(1, 11, 3)
        self.category2 = np.random.randint(1, 11, 3)
        self.category3 = np.random.randint(1, 11, 3)

        self.query = "All values are integers. What is the average of the middle values from each category?"

        middle_value_cat1 = np.median(np.sort(self.category1))
        middle_value_cat2 = np.median(np.sort(self.category2))
        middle_value_cat3 = np.median(np.sort(self.category3))

        self.answer = np.mean([middle_value_cat1, middle_value_cat2, middle_value_cat3])
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        total_width = 0.6
        n = 3
        width = total_width / n
        x = np.arange(3)
        plt.bar(x, self.category1, width, label='Category 1', color='blue')
        plt.bar(x + width, self.category2, width, label='Category 2', color='purple')
        plt.bar(x + 2 * width, self.category3, width, label='Category 3', color='brown')
        plt.xticks(np.arange(3), ['Item 1', 'Item 2', 'Item 3'], fontsize=18)
        plt.tick_params(axis='y', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.ylabel("Values", fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q399:
    def __init__(self):
        self.category1 = np.random.randint(1, 11, 2)
        self.category2 = np.random.randint(1, 11, 2)
        self.category3 = np.random.randint(1, 11, 2)
        self.constant = rd.randint(1, 11)
        self.query = f"All values are integers. What is the sum of all values strictly smaller than {self.constant} across all categories?"
        self.answer = np.sum(self.category1[self.category1 < self.constant]) + \
                        np.sum(self.category2[self.category2 < self.constant]) + \
                        np.sum(self.category3[self.category3 < self.constant])
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"
        
    def draw(self, num):
        total_width = 0.6
        n = 2
        width = total_width / n
        x = np.arange(2)
        plt.bar(x, self.category1, width, label='Category 1', color='blue')
        plt.bar(x + width, self.category2, width, label='Category 2', color='green')
        plt.bar(x + 2 * width, self.category3, width, label='Category 3', color='red')
        plt.xticks(np.arange(2), ['Item 1', 'Item 2'], fontsize=18)
        plt.tick_params(axis='y', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.ylabel("Values", fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q400:
    def __init__(self):
        self.category1 = np.random.randint(1, 11, 3)
        self.category2 = np.random.randint(1, 11, 3)
        self.category3 = np.random.randint(1, 11, 3)
        self.query = f"All values are integers. What is the mean value of category with the highest sum?"
        sum_cat1 = np.sum(self.category1)
        sum_cat2 = np.sum(self.category2)
        sum_cat3 = np.sum(self.category3)
        max_sum = max(sum_cat1, sum_cat2, sum_cat3)
        if max_sum == sum_cat1:
            self.answer = np.mean(self.category1)
        elif max_sum == sum_cat2:
            self.answer = np.mean(self.category2)
        else:
            self.answer = np.mean(self.category3)
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"
        
    def draw(self, num):
        total_width = 0.6
        n = 3
        width = total_width / n
        x = np.arange(3)
        plt.bar(x, self.category1, width, label='Category 1', color='blue')
        plt.bar(x + width, self.category2, width, label='Category 2', color='green')
        plt.bar(x + 2 * width, self.category3, width, label='Category 3', color='red')
        plt.xticks(np.arange(3), ['Item 1', 'Item 2', 'Item 3'], fontsize=18)
        plt.tick_params(axis='y', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.ylabel("Values", fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q401:
    def __init__(self):
        self.category1 = np.random.randint(1, 11, 3)
        self.category2 = np.random.randint(1, 11, 3)
        self.category3 = np.random.randint(1, 11, 3)
        self.query = f"All values are integers. What is the maximum value across all categories?"
        self.answer = max(np.max(self.category1), np.max(self.category2), np.max(self.category3))
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"
        
    def draw(self, num):
        total_width = 0.6
        n = 3
        width = total_width / n
        x = np.arange(3)
        plt.bar(x, self.category1, width, label='Category 1', color='blue')
        plt.bar(x + width, self.category2, width, label='Category 2', color='green')
        plt.bar(x + 2 * width, self.category3, width, label='Category 3', color='red')
        plt.xticks(np.arange(3), ['Item 1', 'Item 2', 'Item 3'], fontsize=18)
        plt.tick_params(axis='y', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.ylabel("Values", fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q402:
    def __init__(self):
        self.category1 = np.random.randint(1, 11, 3)
        self.category2 = np.random.randint(1, 11, 3)
        self.category3 = np.random.randint(1, 11, 3)
        self.query = f"All values are integers. What is the minimum value across all categories?"
        self.answer = min(np.min(self.category1), np.min(self.category2), np.min(self.category3))
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"
        
    def draw(self, num):
        total_width = 0.6
        n = 3
        width = total_width / n
        x = np.arange(3)
        plt.bar(x, self.category1, width, label='Category 1', color='blue')
        plt.bar(x + width, self.category2, width, label='Category 2', color='green')
        plt.bar(x + 2 * width, self.category3, width, label='Category 3', color='red')
        plt.xticks(np.arange(3), ['Item 1', 'Item 2', 'Item 3'], fontsize=18)
        plt.tick_params(axis='y', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.ylabel("Values", fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q403:
    def __init__(self):
        self.category1 = np.random.randint(1, 11, 3)
        self.category2 = np.random.randint(1, 11, 3)
        self.category3 = np.random.randint(1, 11, 3)
        self.query = f"All values are integers. How many categories for each item is shown in this bar plot?"
        self.answer = 3
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "elementary school"
        
    def draw(self, num):
        total_width = 0.6
        n = 3
        width = total_width / n
        x = np.arange(3)
        plt.bar(x, self.category1, width, label='Category 1', color='blue')
        plt.bar(x + width, self.category2, width, label='Category 2', color='green')
        plt.bar(x + 2 * width, self.category3, width, label='Category 3', color='red')
        plt.xticks(np.arange(3), ['Item 1', 'Item 2', 'Item 3'], fontsize=18)
        plt.tick_params(axis='y', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.ylabel("Values", fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q404:
    def __init__(self):
        self.category1 = np.random.randint(1, 11, 2)
        self.category2 = np.random.randint(1, 11, 2)
        # self.category3 = np.random.randint(1, 11, 2)
        self.query = f"All values are integers. How many items is shown in this bar plot?"
        self.answer = 2
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "elementary school"
        
    def draw(self, num):
        total_width = 0.6
        n = 2
        width = total_width / n
        x = np.arange(2)
        plt.bar(x, self.category1, width, label='Category 1', color='blue')
        plt.bar(x + width, self.category2, width, label='Category 2', color='green')
        # plt.bar(x + 2 * width, self.category3, width, label='Category 3', color='red')
        plt.xticks(np.arange(2), ['Item 1', 'Item 2'], fontsize=18)
        plt.tick_params(axis='y', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.ylabel("Values", fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q405:
    def __init__(self):
        self.category1 = np.random.randint(1, 11, 4)
        self.category2 = np.random.randint(1, 11, 4)
        self.category3 = np.random.randint(1, 11, 4)
        self.query = f"All values are integers. What is the mean value of category with the highest sum?"
        sum_cat1 = np.sum(self.category1)
        sum_cat2 = np.sum(self.category2)
        sum_cat3 = np.sum(self.category3)
        max_sum = max(sum_cat1, sum_cat2, sum_cat3)
        if max_sum == sum_cat1:
            self.answer = np.mean(self.category1)
        elif max_sum == sum_cat2:
            self.answer = np.mean(self.category2)
        else:
            self.answer = np.mean(self.category3)
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"
        
    def draw(self, num):
        total_width = 0.6
        n = 4
        width = total_width / n
        x = np.arange(4)
        plt.bar(x, self.category1, width, label='Category 1', color='blue')
        plt.bar(x + width, self.category2, width, label='Category 2', color='green')
        plt.bar(x + 2 * width, self.category3, width, label='Category 3', color='red')
        plt.xticks(np.arange(4), ['Item 1', 'Item 2', 'Item 3', 'Item 4'], fontsize=18)
        plt.tick_params(axis='y', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.ylabel("Values", fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q406:
    def __init__(self):
        self.category1 = np.random.randint(1, 11, 4)
        self.category2 = np.random.randint(1, 11, 4)
        self.category3 = np.random.randint(1, 11, 4)
        self.query = f"All values are integers. What is the maximum value across all categories?"
        self.answer = max(np.max(self.category1), np.max(self.category2), np.max(self.category3))
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"
        
    def draw(self, num):
        total_width = 0.6
        n = 4
        width = total_width / n
        x = np.arange(4)
        plt.bar(x, self.category1, width, label='Category 1', color='blue')
        plt.bar(x + width, self.category2, width, label='Category 2', color='green')
        plt.bar(x + 2 * width, self.category3, width, label='Category 3', color='red')
        plt.xticks(np.arange(4), ['Item 1', 'Item 2', 'Item 3', 'Item 4'], fontsize=18)
        plt.tick_params(axis='y', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.ylabel("Values", fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()






