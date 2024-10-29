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


class Q377:
    def __init__(self):
        self.query = "Which month shows the greatest increase in temperature from the previous month?"
        self.x = np.arange(12)
        self.y = random.sample(range(0, 43), 12)
        self.month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        max_increase = -float('inf')
        self.index = -1
        for i in range(1, len(self.y)):
            increase = self.y[i] - self.y[i - 1]
            if increase > max_increase:
                max_increase = increase
                self.index = i
        self.answer = self.month[self.index]
        self.answer_type = "text"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        plt.figure()
        plt.plot(self.x, self.y, color='orange', linewidth=1.5, marker='o', linestyle='dashed')
        for i, j in zip(self.x, self.y):
            plt.text(i, j, f'{j}', ha='center', va='bottom', fontsize=12)
        plt.xticks(np.arange(12), self.month)
        plt.yticks(np.arange(0, 46, 5))
        plt.ylabel("Temperature", fontsize=20)
        plt.title("Average temperature in Cape Town", fontsize=20)
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q378:
    def __init__(self):
        self.query = "Which quarter had the highest average rainfall?"
        self.x = np.arange(12)
        self.y = random.sample(range(50, 200), 12)
        self.month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.quarters = ['Q1', 'Q2', 'Q3', 'Q4']
        
        avg_rainfall = [np.mean(self.y[i:i+3]) for i in range(0, len(self.y), 3)]
        self.index = np.argmax(avg_rainfall)
        self.answer = self.quarters[self.index]
        self.answer_type = "text"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        plt.figure()
        plt.plot(self.x, self.y, color='blue', linewidth=1.5, marker='o', linestyle='dashed')
        plt.xticks(np.arange(12), self.month)
        plt.yticks([50, 70, 90, 110, 130, 150, 170, 190, 210])
        plt.tick_params(axis='both', which='major', labelsize=14)
        for i, j in zip(self.x, self.y):
            plt.text(i, j, f'{j}', ha='center', va='bottom', fontsize=12)
        plt.ylabel("Rainfall (mm)", fontsize=18)
        plt.title("Monthly Rainfall Over a Year", fontsize=18)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q379:
    def __init__(self):
        self.query = "Which city had the highest average temperature in July? Choices: (A) City 1 (B) City 2 (C) Both"
        self.months = np.arange(12)
        self.city1_temps = np.random.randint(10, 40, 12)
        self.city2_temps = np.random.randint(10, 40, 12)
        self.month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.july_index = 6  # Index for July
        if self.city1_temps[self.july_index] > self.city2_temps[self.july_index]:
            self.answer = 'A'
        elif self.city1_temps[self.july_index] < self.city2_temps[self.july_index]:
            self.answer = 'B'
        else:
            self.answer = 'C'
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        plt.figure()
        plt.plot(self.months, self.city1_temps, label='City 1', color='blue', linewidth=1.5, marker='o', linestyle='dashed')
        plt.plot(self.months, self.city2_temps, label='City 2', color='red', linewidth=1.5, marker='o', linestyle='dashed')
        plt.xticks(np.arange(12), self.month_names)
        plt.yticks(np.arange(10, 41, 5))
        plt.ylabel("Temperature", fontsize=18)
        plt.title("Monthly Average Temperatures", fontsize=18)
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q380:
    def __init__(self):
        self.query = "Which month has the highest average temperature after smoothing with a 3-month moving average?"
        self.x = np.arange(12)
        self.y = np.random.randint(10, 40, 12)
        self.month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        moving_avg = np.convolve(self.y, np.ones(3) / 3, mode='valid')
        self.index = np.argmax(moving_avg)
        self.answer = self.month[self.index + 1]  # +1 to align with the middle of the window
        self.answer_type = "text"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        plt.figure()
        plt.plot(self.x, self.y, color='red', linewidth=1.5, marker='o')
        plt.xticks(np.arange(12), self.month)
        plt.yticks(np.arange(0, 41, 5))
        plt.ylabel("Temperature", fontsize=18)
        plt.title("Average temperature in Cape Town, South Africa", fontsize=18)
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q381:
    def __init__(self):
        self.query = "Which year had the highest peak in stock prices? Choices: (A) Year 1 (B) Year 2 (C) Both"
        self.months = np.arange(12)
        self.year1_prices = np.random.uniform(100, 300, 12)
        self.year2_prices = np.random.uniform(100, 300, 12)
        self.month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        peak_year1 = np.max(self.year1_prices)
        peak_year2 = np.max(self.year2_prices)
        
        if peak_year1 > peak_year2:
            self.answer = "A"
        elif peak_year1 < peak_year2:
            self.answer = "B"
        else:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        plt.figure()
        plt.plot(self.months, self.year1_prices, label='Year 1', color='purple', linewidth=1.5, marker='o', linestyle='dashed')
        plt.plot(self.months, self.year2_prices, label='Year 2', color='orange', linewidth=1.5, marker='o', linestyle='dashed')
        plt.xticks(np.arange(12), self.month_names)
        plt.yticks(np.arange(100, 301, 20))
        plt.ylabel("Stock Prices", fontsize=18)
        plt.title("Monthly Stock Prices Over Two Years", fontsize=18)
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q382:
    def __init__(self):
        self.query = "What is the highest stock price recorded in the year?"
        self.x = np.arange(12)
        self.y = [i * 10 for i in random.sample(range(5, 51), 12)]
        self.month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        max_price = max(self.y)
        for i in range(len(self.y)):
            if self.y[i] == max_price:
                self.index = i
        self.answer = max_price
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        plt.figure()
        plt.plot(self.x, self.y, color='green', linewidth=1.5, marker='o', linestyle='dashed')
        plt.xticks(np.arange(12), self.month)
        plt.yticks(np.arange(0, 551, 50))
        plt.ylabel("Stock Price", fontsize=18)
        plt.title("Monthly Stock Prices Over a Year", fontsize=18)
        for i, j in zip(self.x, self.y):
            plt.text(i, j, f'{j}', ha='center', va='bottom', fontsize=12)
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q383:
    def __init__(self):
        self.query = "Which month had the highest number of visitors to the website?"
        self.x = np.arange(12)
        self.y = np.random.randint(1000, 5000, 12)
        self.month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        max_visitors = max(self.y)
        for i in range(len(self.y)):
            if self.y[i] == max_visitors:
                self.index = i
        self.answer = self.month[self.index]
        self.answer_type = "text"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        plt.figure()
        plt.plot(self.x, self.y, color='purple', linewidth=1.5, marker='o', linestyle='dashed')
        plt.xticks(np.arange(12), self.month)
        plt.yticks(np.arange(1000, 5001, 500))
        plt.ylabel("Number of Visitors", fontsize=18)
        plt.title("Monthly Website Visitors Over a Year", fontsize=18)
        for i, j in zip(self.x, self.y):
            plt.text(i, j, f'{j}', ha='center', va='bottom', fontsize=12)
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q384:
    def __init__(self):
        self.query = "Which region had the lowest average monthly temperature in winter? Choices: (A) Region 1 (B) Region 2 (C) Both"
        self.months = np.arange(12)
        self.region1_temps = np.random.randint(-10, 20, 12)
        self.region2_temps = np.random.randint(-10, 20, 12)
        self.month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        winter_indices = [0, 1, 11]  # Indices for Dec, Jan, Feb
        
        avg_winter_temp_region1 = np.mean([self.region1_temps[i] for i in winter_indices])
        avg_winter_temp_region2 = np.mean([self.region2_temps[i] for i in winter_indices])
        
        if avg_winter_temp_region1 < avg_winter_temp_region2:
            self.answer = "A"
        elif avg_winter_temp_region1 > avg_winter_temp_region2:
            self.answer = "B"
        else:
            self.answer = "C"
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        plt.figure()
        plt.plot(self.months, self.region1_temps, label='Region 1', color='blue', linewidth=1.5, marker='o')
        plt.plot(self.months, self.region2_temps, label='Region 2', color='green', linewidth=1.5, marker='o')
        plt.xticks(np.arange(12), self.month_names)
        plt.yticks(np.arange(-10, 21, 5))
        plt.ylabel("Temperature", fontsize=18)
        plt.title("Monthly Average Temperatures in Two Regions", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q385:
    def __init__(self):
        self.query = "What is the lowest heart rate recorded during the workout session?"
        self.x = np.arange(10)
        self.y = random.sample(range(60, 161), 10)
        self.times = [f"{i * 10}" for i in range(10)]

        min_heart_rate = min(self.y)
        for i in range(len(self.y)):
            if self.y[i] == min_heart_rate:
                self.index = i
        self.answer = min_heart_rate
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        plt.figure()
        plt.plot(self.x, self.y, color='red', linewidth=1.5, marker='o', linestyle='dashed')
        plt.xticks(np.arange(10), self.times)
        plt.yticks(np.arange(60, 181, 20))
        plt.ylabel("Heart Rate (bpm)", fontsize=16)
        plt.xlabel("Time (minutes)", fontsize=16)
        plt.title("Heart Rate During Workout Session", fontsize=18)
        for i, j in zip(self.x, self.y):
            plt.text(i, j, f'{j}', ha='center', va='bottom', fontsize=12)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q386:
    def __init__(self):
        self.query = "The performance score is always the multiple of ten. Which player had the most consistent performance throughout the season? Choice: (A) Player 1 (B) Player 2"
        self.games = np.arange(10)
        self.player1_scores = [i * 10 for i in np.random.randint(1, 10, 10)]
        self.player2_scores = [i * 10 for i in np.random.randint(1, 10, 10)]
        
        std_dev_player1 = np.std(self.player1_scores)
        std_dev_player2 = np.std(self.player2_scores)
        
        if std_dev_player1 < std_dev_player2:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        plt.figure()
        plt.plot(self.games, self.player1_scores, label='Player 1', color='red', linewidth=1.5, marker='o')
        plt.plot(self.games, self.player2_scores, label='Player 2', color='blue', linewidth=1.5, marker='o')
        plt.xticks(np.arange(10), [f'G{i+1}' for i in range(10)])
        plt.yticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        plt.ylabel("Performance Score", fontsize=16)
        plt.title("Player Performance Throughout the Season", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q387:
    # line plot for finding the coolest month
    def __init__(self):
        self.query = "Use the graph to answer the question below. Which month is the coolest on average in Cape Town?"
        self.x = np.arange(12)
        self.y = random.sample(range(0, 41), 12)
        self.month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        min_temp = min(self.y)
        for i in range(len(self.y)):
            if self.y[i] == min_temp:
                self.index = i
        self.answer = self.month[self.index]
        self.answer_type = "text"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        plt.figure()
        plt.plot(self.x, self.y, color='blue', linewidth=1.5, marker='o', linestyle='dashed')
        plt.xticks(np.arange(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        plt.yticks(np.arange(0, 46, 5))
        plt.ylabel("Temperature", fontsize=16)
        plt.title("Average temperature in Cape Town", fontsize=16)
        plt.tick_params(axis='y', which='major', labelsize=16)
        plt.tick_params(axis='x', which='major', labelsize=15)
        for i, j in zip(self.x, self.y):
            plt.text(i, j+1, f'{j}', ha='center', va='bottom', fontsize=14)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()
















