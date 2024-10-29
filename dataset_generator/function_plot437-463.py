import os
import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import pi


class Q437:
    def __init__(self):
        self.months = np.arange(1, 13)
        self.regions = ['North', 'South', 'East', 'West']
        self.rainfall = {region: [i * random.randint(1, 5) + random.randint(-3, 3) for i in random.sample(range(10, 40), 12)] for region in self.regions}
        self.query = "The area chart below represents monthly rainfall in different regions. Which region had the highest rainfall in any single month? Choices: (A) North (B) South (C) East (D) West"
        max_rainfall = {region: np.max(rain) for region, rain in self.rainfall.items()}
        max_rainfall_region = max(max_rainfall, key=max_rainfall.get)
        self.answer = {'North': 'A', 'South': 'B', 'East': 'C', 'West': 'D'}[max_rainfall_region]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(10, 6))
        color_theme = ['blue', 'green', 'orange', 'purple']
        for i, region in enumerate(self.regions):
            plt.fill_between(self.months, self.rainfall[region], label=region, color=color_theme[i], alpha=0.5)
        plt.xlabel('Month', fontsize=20)
        plt.ylabel('Rainfall (mm)', fontsize=20)
        plt.title('Monthly Rainfall in Different Regions', fontsize=20)
        plt.tick_params(axis='both', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q438:
    def __init__(self):
        self.months = np.arange(1, 13)
        self.categories = ['Electronics', 'Clothing', 'Groceries', 'Furniture']
        self.sales = {category: [i * random.randint(10, 50) for i in random.sample(range(40, 100), 12)] for category in self.categories}
        self.query = "The area chart below represents monthly sales in different product categories. Which category had the highest sales in any single month? Choices: (A) Electronics (B) Clothing (C) Groceries (D) Furniture"
        max_sales = {category: np.max(sales) for category, sales in self.sales.items()}
        max_sales_category = max(max_sales, key=max_sales.get)
        self.answer = {'Electronics': 'A', 'Clothing': 'B', 'Groceries': 'C', 'Furniture': 'D'}[max_sales_category]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(10, 6))
        color_theme = ['blue', 'green', 'orange', 'purple']
        for i, category in enumerate(self.categories):
            plt.fill_between(self.months, self.sales[category], label=category, color=color_theme[i], alpha=0.5)
        plt.xlabel('Month', fontsize=20)
        plt.ylabel('Sales ($)', fontsize=20)
        plt.title('Monthly Sales in Different Product Categories', fontsize=20)
        plt.tick_params(axis='both', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q439:
    def __init__(self):
        self.months = np.arange(1, 13)
        self.cities = ['City A', 'City B', 'City C', 'City D']
        self.temperatures = {city: [i * random.randint(10, 20)/10 for i in random.sample(range(-10, 20), 12)] for city in self.cities}
        self.query = "The area chart below represents monthly temperatures in different cities. Which city had the highest temperature in any single month? Choices: (A) City A (B) City B (C) City C (D) City D"
        max_temperatures = {city: np.max(temp) for city, temp in self.temperatures.items()}
        max_temp_city = max(max_temperatures, key=max_temperatures.get)
        self.answer = {'City A': 'A', 'City B': 'B', 'City C': 'C', 'City D': 'D'}[max_temp_city]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(10, 6))
        color_theme = ['blue', 'green', 'orange', 'purple']
        for i, city in enumerate(self.cities):
            plt.fill_between(self.months, self.temperatures[city], label=city, color=color_theme[i], alpha=0.5)
        plt.xlabel('Month', fontsize=20)
        plt.ylabel('Temperature (°C)', fontsize=20)
        plt.title('Monthly Temperatures in Different Cities', fontsize=20)
        plt.tick_params(axis='both', which='major', labelsize=20)
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q440:
    def __init__(self):
        self.departments = ['HR', 'IT', 'Finance', 'Marketing']
        self.salaries = {
            'HR': np.random.randint(30000, 60000, 50),
            'IT': np.random.randint(50000, 100000, 50),
            'Finance': np.random.randint(35000, 80000, 50),
            'Marketing': np.random.randint(40000, 70000, 50)
        }
        self.query = "The box plot below represents the salaries of employees in different departments. Which department has the highest median salary? Choices: (A) HR (B) IT (C) Finance (D) Marketing"
        medians = {dept: np.median(sal) for dept, sal in self.salaries.items()}
        max_median_dept = max(medians, key=medians.get)
        self.answer = {'HR': 'A', 'IT': 'B', 'Finance': 'C', 'Marketing': 'D'}[max_median_dept]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        boxplot = ax.boxplot([self.salaries[dept] for dept in self.departments], labels=self.departments)
        ax.set_title('Salary Distribution by Department', fontsize=20)
        ax.set_ylabel('Salary ($)', fontsize=20)
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=24)
        for median in boxplot['medians']:
            median.set_linewidth(4)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q441:
    def __init__(self):
        self.branches = ['Branch A', 'Branch B', 'Branch C', 'Branch D']
        self.scores = {
            'Branch A': np.random.randint(1, 10, 10),
            'Branch B': np.random.randint(1, 10, 10),
            'Branch C': np.random.randint(1, 10, 10),
            'Branch D': np.random.randint(1, 10, 10)
        }
        self.query = "The box plot below represents the customer satisfaction scores for different branches. Which branch has the smallest interquartile range (IQR) for customer satisfaction scores? Choices: (A) Branch A (B) Branch B (C) Branch C (D) Branch D"
        iqrs = {branch: np.percentile(score, 75) - np.percentile(score, 25) for branch, score in self.scores.items()}
        min_iqr_branch = min(iqrs, key=iqrs.get)
        self.answer = {'Branch A': 'A', 'Branch B': 'B', 'Branch C': 'C', 'Branch D': 'D'}[min_iqr_branch]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        boxplot = ax.boxplot([self.scores[branch] for branch in self.branches], vert=False, patch_artist=True, labels=self.branches)
        ax.set_title('Customer Satisfaction Scores Distribution by Branch', fontsize=20)
        ax.set_ylabel('Satisfaction Scores', fontsize=20)
        ax.tick_params(axis='y', labelsize=24)
        ax.tick_params(axis='x', labelsize=20)
        for median in boxplot['medians']:
            median.set_linewidth(4)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q442:
    def __init__(self):
        self.grades = ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4']
        self.scores = {
            'Grade 1': np.random.randint(60, 100, 10),
            'Grade 2': np.random.randint(60, 100, 10),
            'Grade 3': np.random.randint(60, 100, 10),
            'Grade 4': np.random.randint(60, 100, 10)
        }
        self.query = "The box plot below represents the test scores of students in different grade levels. Which grade level has the greatest range of test scores? Choices: (A) Grade 1 (B) Grade 2 (C) Grade 3 (D) Grade 4"
        ranges = {grade: np.ptp(score) for grade, score in self.scores.items()}
        max_range_grade = max(ranges, key=ranges.get)
        self.answer = {'Grade 1': 'A', 'Grade 2': 'B', 'Grade 3': 'C', 'Grade 4': 'D'}[max_range_grade]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        boxplot = ax.boxplot([self.scores[grade] for grade in self.grades], labels=self.grades)
        ax.set_title('Test Scores Distribution by Grade Level', fontsize=20)
        ax.set_ylabel('Test Scores', fontsize=20)
        ax.tick_params(axis='y', labelsize=16)
        ax.tick_params(axis='x', labelsize=24)
        for median in boxplot['medians']:
            median.set_linewidth(4)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()

        
class Q443:
    def __init__(self):
        self.categories = ['A', 'B', 'C', 'D', 'E']
        self.data = pd.DataFrame({
            'Category': np.repeat(self.categories, 100),
            'Value': np.concatenate([np.random.normal(np.random.randint(40, 60), np.random.randint(5, 15), 100) for _ in self.categories])
        })
        medians = self.data.groupby('Category')['Value'].median()
        self.query = "The boxen plot below represents different categories. Which category has the highest median value? Choices: (A) A (B) B (C) C (D) D (E) E"
        self.answer = medians.idxmax()
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(10, 6))
        boxplot = sns.boxenplot(x='Category', y='Value', data=self.data)
        plt.title('Boxen Plot', fontsize=20)
        plt.tick_params(axis='x', which='major', labelsize=24)
        plt.tick_params(axis='y', which='major', labelsize=16)
        plt.xlabel("Category", fontsize=20)
        plt.ylabel("Value", fontsize=20)
        for line in boxplot.lines:
            if line.get_linestyle() == '-':
                line.set_linewidth(4)
                line.set_color('black')
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q444:
    def __init__(self):
        self.datasets = {
            'Dataset A': np.random.normal(np.random.randint(40, 60), np.random.randint(5, 15), 1000),
            'Dataset B': np.random.normal(np.random.randint(20, 60), np.random.randint(5, 15), 1000),
            'Dataset C': np.random.normal(np.random.randint(30, 60), np.random.randint(5, 15), 1000),
            'Dataset D': np.random.normal(np.random.randint(40, 60), np.random.randint(5, 15), 1000)
        }
        self.query = "The density plot below represents different datasets. Which dataset has the highest mean? Choices: (A) Dataset A (B) Dataset B (C) Dataset C (D) Dataset D"
        means = {name: np.mean(data) for name, data in self.datasets.items()}
        max_mean = max(means, key=means.get)
        self.answer = {'Dataset A': 'A', 'Dataset B': 'B', 'Dataset C': 'C', 'Dataset D': 'D'}[max_mean]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(10, 6))
        color_theme = sns.color_palette("magma", len(self.datasets))
        for i, (name, data) in enumerate(self.datasets.items()):
            sns.kdeplot(data, label=name, color=color_theme[i], linewidth=2)
        plt.xlabel('Value', fontsize=20)
        plt.ylabel('Density', fontsize=20)
        plt.title('Density Plot of Different Datasets', fontsize=20)
        plt.tick_params(axis='x', which='major', labelsize=20)
        plt.tick_params(axis='y', which='major', labelsize=18)
        plt.legend(fontsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q445:
    def __init__(self):
        self.datasets = {
            'Dataset A': np.random.normal(np.random.randint(40, 70), np.random.randint(5, 15), 1000),
            'Dataset B': np.random.normal(np.random.randint(20, 60), np.random.randint(5, 15), 1000),
            'Dataset C': np.random.normal(np.random.randint(30, 60), np.random.randint(5, 15), 1000),
            'Dataset D': np.random.normal(np.random.randint(40, 60), np.random.randint(5, 15), 1000)
        }
        self.query = "The density plot below represents different datasets. Which dataset has the lowest variance? Choices: (A) Dataset A (B) Dataset B (C) Dataset C (D) Dataset D"
        variances = {name: np.var(data) for name, data in self.datasets.items()}
        min_variance = min(variances, key=variances.get)
        self.answer = {'Dataset A': 'A', 'Dataset B': 'B', 'Dataset C': 'C', 'Dataset D': 'D'}[min_variance]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(10, 6))
        color_theme = sns.color_palette("cubehelix", len(self.datasets))
        for i, (name, data) in enumerate(self.datasets.items()):
            sns.kdeplot(data, label=name, color=color_theme[i], linewidth=2)
        plt.xlabel('Value', fontsize=20)
        plt.ylabel('Density', fontsize=20)
        plt.title('Density Plot of Different Datasets', fontsize=20)
        plt.tick_params(axis='x', which='major', labelsize=20)
        plt.tick_params(axis='y', which='major', labelsize=16)
        plt.legend(fontsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q446:
    def __init__(self):
        self.datasets = {
            'Dataset A': np.random.normal(10, np.random.randint(10, 40), 1000),
            'Dataset B': np.random.normal(10, np.random.randint(5, 20), 1000),
            'Dataset C': np.random.normal(10, np.random.randint(5, 10), 1000),
            'Dataset D': np.random.normal(10, np.random.randint(5, 30), 1000)
        }
        self.query = "The density plot below represents different datasets. Which dataset has the widest spread? Choices: (A) Dataset A (B) Dataset B (C) Dataset C (D) Dataset D"
        spreads = {name: np.std(data) for name, data in self.datasets.items()}
        max_spread = max(spreads, key=spreads.get)
        self.answer = {'Dataset A': 'A', 'Dataset B': 'B', 'Dataset C': 'C', 'Dataset D': 'D'}[max_spread]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(10, 6))
        color_theme = sns.color_palette("viridis", len(self.datasets))
        for i, (name, data) in enumerate(self.datasets.items()):
            sns.kdeplot(data, label=name, color=color_theme[i], linewidth=2)
        plt.xlabel('Value', fontsize=20)
        plt.ylabel('Density', fontsize=20)
        plt.title('Density Plot of Different Datasets', fontsize=20)
        plt.tick_params(axis='x', which='major', labelsize=20)
        plt.tick_params(axis='y', which='major', labelsize=16)
        plt.legend(fontsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q447:
    def __init__(self):
        self.tasks = ['A', 'B', 'C', 'D', 'E']
        self.start_times = np.random.randint(0, 10, size=len(self.tasks))
        self.durations = np.random.randint(1, 10, size=len(self.tasks))
        self.end_times = self.start_times + self.durations
        self.data = pd.DataFrame({
            'Task': self.tasks,
            'Start': self.start_times,
            'Duration': self.durations,
            'End': self.end_times
        })
        self.query = "The Gantt chart below represents different tasks. Which task starts the earliest? Choices: (A) Task A (B) Task B (C) Task C (D) Task D (E) Task E"
        self.answer = self.data.loc[self.data['Start'].idxmin(), 'Task']
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        for i, task in enumerate(self.tasks):
            ax.barh(task, self.durations[i], left=self.start_times[i], color='skyblue')
        ax.set_xlabel('Time', fontsize=20)
        ax.set_title('Gantt Chart', fontsize=20)
        plt.tick_params(axis='x', which='major', labelsize=20)
        plt.tick_params(axis='y', which='major', labelsize=24)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q448:
    def __init__(self):
        self.tasks = ['A', 'B', 'C', 'D', 'E']
        self.start_times = np.random.randint(0, 10, size=len(self.tasks))
        self.durations = np.random.randint(1, 10, size=len(self.tasks))
        self.end_times = self.start_times + self.durations
        self.data = pd.DataFrame({
            'Task': self.tasks,
            'Start': self.start_times,
            'Duration': self.durations,
            'End': self.end_times
        })
        self.query = "The Gantt chart below represents different tasks. Which task ends the latest? Choices: (A) Task A (B) Task B (C) Task C (D) Task D (E) Task E"
        self.answer = self.data.loc[self.data['End'].idxmax(), 'Task']
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        for i, task in enumerate(self.tasks):
            ax.barh(task, self.durations[i], left=self.start_times[i], color='gray')
        ax.set_xlabel('Time', fontsize=20)
        ax.set_title('Gantt Chart', fontsize=20)
        plt.tick_params(axis='x', which='major', labelsize=20)
        plt.tick_params(axis='y', which='major', labelsize=16)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q449:
    def __init__(self):
        self.tasks = ['A', 'B', 'C', 'D', 'E']
        self.start_times = np.random.randint(0, 10, size=len(self.tasks))
        self.durations = np.random.randint(1, 10, size=len(self.tasks))
        self.end_times = self.start_times + self.durations
        self.data = pd.DataFrame({
            'Task': self.tasks,
            'Start': self.start_times,
            'Duration': self.durations,
            'End': self.end_times
        })
        self.query = "The Gantt chart below represents different tasks. Which task has the longest duration? Choices: (A) Task A (B) Task B (C) Task C (D) Task D (E) Task E"
        self.answer = self.data.loc[self.data['Duration'].idxmax(), 'Task']
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        for i, task in enumerate(self.tasks):
            ax.barh(task, self.durations[i], left=self.start_times[i], color='skyblue')
        ax.set_xlabel('Time', fontsize=20)
        ax.set_title('Gantt Chart', fontsize=20)
        plt.tick_params(axis='x', which='major', labelsize=20)
        plt.tick_params(axis='y', which='major', labelsize=16)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q450:
    def __init__(self):
        self.tasks = ['A', 'B', 'C', 'D', 'E']
        self.start_times = np.random.randint(0, 10, size=len(self.tasks))
        self.durations = np.random.randint(1, 10, size=len(self.tasks))
        self.end_times = self.start_times + self.durations
        self.data = pd.DataFrame({
            'Task': self.tasks,
            'Start': self.start_times,
            'Duration': self.durations,
            'End': self.end_times
        })
        overlaps = {task: 0 for task in self.tasks}
        for i, task1 in enumerate(self.tasks):
            for j, task2 in enumerate(self.tasks):
                if i != j and not (self.end_times[i] <= self.start_times[j] or self.start_times[i] >= self.end_times[j]):
                    overlaps[task1] += 1
        self.query = "The Gantt chart below represents different tasks. Which task overlaps with the most other tasks? Choices: (A) Task A (B) Task B (C) Task C (D) Task D (E) Task E"
        self.answer = max(overlaps, key=overlaps.get)
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        for i, task in enumerate(self.tasks):
            ax.barh(task, self.durations[i], left=self.start_times[i], color='skyblue')
        ax.set_xlabel('Time', fontsize=20)
        ax.set_title('Gantt Chart', fontsize=20)
        plt.tick_params(axis='x', which='major', labelsize=20)
        plt.tick_params(axis='y', which='major', labelsize=16)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q451:
    def __init__(self):
        self.tasks = ['A', 'B', 'C', 'D', 'E']
        self.start_times = np.random.randint(0, 10, size=len(self.tasks))
        self.durations = np.random.randint(1, 10, size=len(self.tasks))
        self.end_times = self.start_times + self.durations
        self.data = pd.DataFrame({
            'Task': self.tasks,
            'Start': self.start_times,
            'Duration': self.durations,
            'End': self.end_times
        })
        self.query = "The Gantt chart below represents different tasks. Which task has the shortest duration? Choices: (A) Task A (B) Task B (C) Task C (D) Task D (E) Task E"
        self.answer = self.data.loc[self.data['Duration'].idxmin(), 'Task']
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(10, 6))
        for i, task in enumerate(self.tasks):
            ax.barh(task, self.durations[i], left=self.start_times[i], color='red')
        ax.set_xlabel('Time', fontsize=20)
        ax.set_title('Gantt Chart', fontsize=20)
        plt.tick_params(axis='x', which='major', labelsize=20)
        plt.tick_params(axis='y', which='major', labelsize=16)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q452:
    def __init__(self):
        self.branches = ['Branch A', 'Branch B', 'Branch C', 'Branch D']
        self.months = ['January', 'February', 'March', 'April', 'May', 'June']
        self.attendance = np.random.randint(100, 1000, (4, 6))
        self.df = pd.DataFrame(self.attendance, index=self.branches, columns=self.months)
        self.query = "The heatmap below represents the monthly attendance in different gym branches. Which month had the highest attendance across all branches? Choices: (A) January (B) February (C) March (D) April (E) May (F) June"
        total_attendance_per_month = self.df.sum(axis=0)
        max_attendance_month_index = np.argmax(total_attendance_per_month)
        self.answer = ['A', 'B', 'C', 'D', 'E', 'F'][max_attendance_month_index]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(10, 6))
        ax = sns.heatmap(self.df, annot=True,  annot_kws={"size": 20}, fmt="d", cmap="PuBu")
        plt.title('Monthly Gym Attendance by Branch', fontsize=20)
        plt.tick_params(axis='x', which='major', labelsize=16)
        plt.tick_params(axis='y', which='major', labelsize=16)
        cbar = ax.collections[0].colorbar
        cbar.ax.tick_params(labelsize=14)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q453:
    def __init__(self):
        self.regions = ['Region A', 'Region B', 'Region C', 'Region D']
        self.seasons = ['Winter', 'Spring', 'Summer', 'Fall']
        self.pollution = np.random.randint(20, 100, (4, 4))
        self.df = pd.DataFrame(self.pollution, index=self.regions, columns=self.seasons)
        self.query = "The heatmap below represents the pollution levels in different regions across four seasons. Which region had the lowest average pollution level in the summer? Choices: (A) Region A (B) Region B (C) Region C (D) Region D"
        min_pollution_region_index = np.argmin(self.df['Summer'])
        self.answer = ['A', 'B', 'C', 'D'][min_pollution_region_index]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(10, 6))
        ax = sns.heatmap(self.df, annot=True, annot_kws={"size": 24}, fmt="d", cmap="BrBG")
        plt.title('Pollution Levels by Region and Season', fontsize=20)
        plt.tick_params(axis='x', which='major', labelsize=18)
        plt.tick_params(axis='y', which='major', labelsize=16)
        cbar = ax.collections[0].colorbar
        cbar.ax.tick_params(labelsize=14)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q454:
    def __init__(self):
        self.stores = ['Store A', 'Store B', 'Store C', 'Store D']
        self.products = ['Product 1', 'Product 2', 'Product 3', 'Product 4']
        self.sales = np.random.randint(100, 500, (4, 4))
        self.df = pd.DataFrame(self.sales, index=self.stores, columns=self.products)
        self.query = "The heatmap below represents the sales of different products across four stores. Which product had the highest total sales across all stores? Choices: (A) Product 1 (B) Product 2 (C) Product 3 (D) Product 4"
        total_sales = self.df.sum(axis=0)
        max_sales_product_index = np.argmax(total_sales)
        self.answer = ['A', 'B', 'C', 'D'][max_sales_product_index]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(10, 6))
        ax = sns.heatmap(self.df, annot=True, annot_kws={"size": 24}, fmt="d", cmap="RdBu")
        plt.title('Sales of Products in Different Stores', fontsize=20)
        plt.tick_params(axis='x', which='major', labelsize=18)
        plt.tick_params(axis='y', which='major', labelsize=16)
        cbar = ax.collections[0].colorbar
        cbar.ax.tick_params(labelsize=14)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q455:
    def __init__(self):
        self.regions = ['North', 'South', 'East', 'West']
        self.months = ['January', 'February', 'March', 'April', 'May', 'June']
        self.sales = np.random.randint(100, 1000, (4, 6))
        self.df = pd.DataFrame(self.sales, index=self.regions, columns=self.months)
        self.query = "The heatmap below represents the sales in different regions over six months. Which month had the highest sales in the East region? Choices: (A) January (B) February (C) March (D) April (E) May (F) June"
        max_sales_month_index = np.argmax(self.df.loc['East'])
        self.answer = ['A', 'B', 'C', 'D', 'E', 'F'][max_sales_month_index]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(10, 6))
        ax = sns.heatmap(self.df, annot=True, fmt="d", annot_kws={"size": 24}, cmap="RdYlBu")
        plt.title('Monthly Sales in Different Regions', fontsize=20)
        plt.tick_params(axis='x', which='major', labelsize=18)
        plt.tick_params(axis='y', which='major', labelsize=16)
        cbar = ax.collections[0].colorbar
        cbar.ax.tick_params(labelsize=14)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q456:
    def __init__(self):
        self.teams = ['Team A', 'Team B', 'Team C', 'Team D']
        self.half_season = ['First Half', 'Second Half']
        self.wins = np.random.randint(0, 20, (4, 2))
        self.df = pd.DataFrame(self.wins, index=self.teams, columns=self.half_season)
        self.query = "The heatmap below represents the number of wins by different teams in two halves of the season. Which team had the highest number of wins in the second half of the season? Choices: (A) Team A (B) Team B (C) Team C (D) Team D"
        max_wins_team_index = np.argmax(self.df['Second Half'])
        self.answer = ['A', 'B', 'C', 'D'][max_wins_team_index]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(10, 6))
        ax = sns.heatmap(self.df, annot=True, fmt="d", annot_kws={"size": 28}, cmap="YlGnBu")
        plt.title('Number of Wins by Teams in Each Half of the Season', fontsize=18)
        plt.tick_params(axis='x', which='major', labelsize=24)
        plt.tick_params(axis='y', which='major', labelsize=20)
        cbar = ax.collections[0].colorbar
        cbar.ax.tick_params(labelsize=14)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q457:
    def __init__(self):
        self.data = pd.DataFrame({
            'Feature A': np.random.normal(np.random.randint(40, 60), np.random.randint(5, 35), 100),
            'Feature B': np.random.normal(np.random.randint(40, 60), np.random.randint(5, 10), 100),
            'Feature C': np.random.normal(np.random.randint(40, 60), np.random.randint(5, 25), 100),
            'Feature D': np.random.normal(np.random.randint(40, 60), np.random.randint(5, 10), 100)
        })
        self.query = "The pair plot below represents different features. Which feature has the highest variance? Choices: (A) Feature A (B) Feature B (C) Feature C (D) Feature D"
        variances = self.data.var()
        max_variance_feature = variances.idxmax()
        self.answer = {'Feature A': 'A', 'Feature B': 'B', 'Feature C': 'C', 'Feature D': 'D'}[max_variance_feature]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(12, 12))
        pair = sns.pairplot(self.data, plot_kws={'alpha': 0.6})
        for ax in pair.axes.flat:
            ax.tick_params(axis='both', labelsize=20)
            ax.set_xlabel(ax.get_xlabel(), fontsize=20)
            ax.set_ylabel(ax.get_ylabel(), fontsize=20)
        for ax in pair.diag_axes:
            for patch in ax.patches:
                height = patch.get_height()
                ax.text(patch.get_x() + patch.get_width() / 2, height + 1, f'{int(height)}',
                        ha='center', fontsize=12)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q458:
    def __init__(self):
        self.categories = ['A', 'B', 'C', 'D', 'E']
        self.values = np.random.randint(10, 100, size=len(self.categories))
        self.sorted_indices = np.argsort(self.values)[::-1]
        self.sorted_categories = np.array(self.categories)[self.sorted_indices]
        self.sorted_values = self.values[self.sorted_indices]
        self.cumulative_percentage = np.cumsum(self.sorted_values) / np.sum(self.sorted_values) * 100
        self.query = "The Pareto chart below represents the contributions of different categories. Which category contributes to the highest percentage of the total? Choices: (A) A (B) B (C) C (D) D (E) E"
        self.answer = self.sorted_categories[0]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(10, 6))
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        ax1.bar(self.sorted_categories, self.sorted_values, color='C0')
        ax2.plot(self.sorted_categories, self.cumulative_percentage, color='C1', marker='o', ms=5)
        ax1.set_xlabel('Category', fontsize=18)
        ax1.set_ylabel('Value', fontsize=18)
        ax2.set_ylabel('Cumulative Percentage', fontsize=18)
        ax2.set_ylim([0, 100])
        plt.title('Pareto Chart', fontsize=20)
        ax1.tick_params(axis='x', which='major', labelsize=20)
        ax1.tick_params(axis='y', which='major', labelsize=20)
        ax2.tick_params(axis='y', which='major', labelsize=20)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q459:
    def __init__(self):
        self.categories = ['A', 'B', 'C', 'D', 'E']
        self.values = np.random.randint(10, 100, size=len(self.categories))
        self.sorted_indices = np.argsort(self.values)
        self.sorted_categories = np.array(self.categories)[self.sorted_indices]
        self.sorted_values = self.values[self.sorted_indices]
        self.cumulative_percentage = np.cumsum(self.sorted_values) / np.sum(self.sorted_values) * 100
        self.query = "The Pareto chart below represents the contributions of different categories. Which category is the smallest contributor? Choices: (A) A (B) B (C) C (D) D (E) E"
        self.answer = self.sorted_categories[0]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        plt.figure(figsize=(10, 6))
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        ax1.bar(self.sorted_categories, self.sorted_values, color='C0')
        ax2.plot(self.sorted_categories, self.cumulative_percentage, color='C1', marker='o', ms=5)
        ax1.set_xlabel('Category', fontsize=18)
        ax1.set_ylabel('Value', fontsize=18)
        ax2.set_ylabel('Cumulative Percentage', fontsize=18)
        ax2.set_ylim([0, 100])
        plt.title('Pareto Chart', fontsize=20)
        ax1.tick_params(axis='x', which='major', labelsize=20)
        ax1.tick_params(axis='y', which='major', labelsize=20)
        ax2.tick_params(axis='y', which='major', labelsize=20)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q460:
    def __init__(self):
        self.categories = ['A', 'B', 'C', 'D', 'E']
        self.values = random.sample(range(1, 20), 5)
        self.values = [i * 5 for i in self.values]
        self.query = "The radar chart below represents different categories. Which category has the highest value? Choices: (A) A (B) B (C) C (D) D (E) E"
        self.answer = self.categories[np.argmax(self.values)]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        self._draw_radar_chart(self.values, num)


    def _draw_radar_chart(self, values, num):
        N = len(self.categories)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        values = np.append(values, values[0])
        angles += angles[:1]

        ax = plt.subplot(111, polar=True)
        plt.xticks(angles[:-1], self.categories)
        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.1)
        ax.set_yticks([20, 40, 60, 80, 100])
        ax.tick_params(axis='both', labelsize=18)
        plt.title('Radar Chart', fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q461:
    def __init__(self):
        self.categories = ['A', 'B', 'C', 'D', 'E']
        self.values = random.sample(range(1, 20), 5)
        self.values = [i * 5 for i in self.values]
        self.query = "The radar chart below represents different categories. Which category has the lowest value? Choices: (A) A (B) B (C) C (D) D (E) E"
        self.answer = self.categories[np.argmin(self.values)]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        self._draw_radar_chart(self.values, num)


    def _draw_radar_chart(self, values, num):
        N = len(self.categories)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        values = np.append(values, values[0])
        angles += angles[:1]

        ax = plt.subplot(111, polar=True)
        plt.xticks(angles[:-1], self.categories)
        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.1)
        ax.set_yticks([20, 40, 60, 80, 100])
        ax.tick_params(axis='both', labelsize=18)
        plt.title('Radar Chart', fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q462:
    def __init__(self):
        self.categories = ['A', 'B', 'C', 'D', 'E']
        self.values = random.sample(range(1, 20), 5)
        self.values = [i * 5 for i in self.values]
        self.query = "The radar chart below represents different categories. Which category is second highest? Choices: (A) A (B) B (C) C (D) D (E) E"
        sorted_indices = np.argsort(self.values)
        self.answer = self.categories[sorted_indices[-2]]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        self._draw_radar_chart(self.values, num)

    def _draw_radar_chart(self, values, num):
        N = len(self.categories)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        values = np.append(values, values[0])
        angles += angles[:1]

        ax = plt.subplot(111, polar=True)
        plt.xticks(angles[:-1], self.categories)
        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.1)
        ax.set_yticks([20, 40, 60, 80, 100])
        ax.tick_params(axis='both', labelsize=18)
        plt.title('Radar Chart', fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q463:
    def __init__(self):
        self.categories = ['A', 'B', 'C', 'D', 'E']
        self.values = random.sample(range(1, 20), 5)
        self.values = [i * 5 for i in self.values]
        self.query = "The radar chart below represents different categories. Which category is second lowest? Choices: (A) A (B) B (C) C (D) D (E) E"
        sorted_indices = np.argsort(self.values)
        self.answer = self.categories[sorted_indices[1]]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "undergraduate"

    def draw(self, num):
        self._draw_radar_chart(self.values, num)

    def _draw_radar_chart(self, values, num):
        N = len(self.categories)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        values = np.append(values, values[0])
        angles += angles[:1]

        ax = plt.subplot(111, polar=True)
        plt.xticks(angles[:-1], self.categories)
        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.1)
        ax.set_yticks([20, 40, 60, 80, 100])
        ax.tick_params(axis='x', labelsize=18)
        ax.tick_params(axis='y', labelsize=16)
        plt.title('Radar Chart', fontsize=18)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()




