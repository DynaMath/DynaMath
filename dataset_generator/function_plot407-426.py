import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Q407:
    def __init__(self):
        self.data = {
            'Grade': ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5'],
            'Number of Students': np.random.randint(20, 50, 5) * 10
        }
        self.df = pd.DataFrame(self.data)
        self.query = "The table below represents the number of students in each grade at an elementary school. What is the average number of students per grade?"
        self.answer = self.df['Number of Students'].mean()
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(6, 4))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=self.df.values, colLabels=self.df.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(24)
        the_table.scale(1.5, 3)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q408:
    def __init__(self):
        self.data = {
            'City': ['City A', 'City B', 'City C', 'City D'],
            'January': np.random.randint(-10, 20, 4),
            'February': np.random.randint(-10, 20, 4),
            'March': np.random.randint(-10, 20, 4),
        }
        self.df = pd.DataFrame(self.data)
        self.df['Average Q1'] = self.df[['January', 'February', 'March']].mean(axis=1)
        self.query = "The table below represents the monthly temperatures in different cities. What is the average monthly temperature in City D for the first quarter?"
        self.answer = self.df.loc[self.df['City'] == 'City D', 'Average Q1'].values[0]
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        df_to_display = self.df.drop(columns=['Average Q1'])
        fig, ax = plt.subplots(figsize=(8, 4))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df_to_display.values, colLabels=df_to_display.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(24)
        the_table.scale(1.5, 3)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q409:
    def __init__(self):
        self.data = {
            'Department': ['HR', 'IT', 'Finance', 'Marketing'],
            'January': np.random.randint(1000, 5000, 4),
            'February': np.random.randint(1000, 5000, 4),
            'March': np.random.randint(1000, 5000, 4),
            'April': np.random.randint(1000, 5000, 4),
        }
        self.df = pd.DataFrame(self.data)
        self.df['Average Expense'] = self.df[['January', 'February', 'March', 'April']].mean(axis=1)
        max_average_index = self.df['Average Expense'].idxmax()
        self.query = "The table below represents the monthly expenses of different departments. Which department has the highest average monthly expense? Choices: (A) HR (B) IT (C) Finance (D) Marketing"
        self.answer = ['A', 'B', 'C', 'D'][max_average_index]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        df_to_display = self.df.drop(columns=['Average Expense'])
        fig, ax = plt.subplots(figsize=(10, 4))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df_to_display.values, colLabels=df_to_display.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(24)
        the_table.scale(1.5, 3)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q410:
    def __init__(self):
        self.data = {
            'Department': ['HR', 'IT', 'Finance', 'Marketing'],
            'Revenue': np.random.randint(5000, 15000, 4),
            'Expenses': np.random.randint(3000, 10000, 4),
        }
        self.df = pd.DataFrame(self.data)
        self.df['Savings'] = self.df['Revenue'] - self.df['Expenses']
        max_savings_index = self.df['Savings'].idxmax()
        self.query = "The table below represents the monthly revenue and expenses of different departments. Which department had the highest average monthly savings if savings are calculated as (Revenue - Expenses)? Choices: (A) HR (B) IT (C) Finance (D) Marketing"
        self.answer = ['A', 'B', 'C', 'D'][max_savings_index]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        df_to_display = self.df.drop(columns=['Savings'])
        fig, ax = plt.subplots(figsize=(10, 5))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df_to_display.values, colLabels=df_to_display.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(26)
        the_table.scale(1.5, 4)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q411:
    def __init__(self):
        self.data = {
            'Grade': ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5'],
            'Number of Students': np.random.randint(20, 50, 5) * 10
        }
        self.df = pd.DataFrame(self.data)
        self.query = "The table below represents the number of students in each grade at an elementary school. What is the difference between the highest and lowest number of students?"
        self.answer = self.df['Number of Students'].max() - self.df['Number of Students'].min()
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(6, 2))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=self.df.values, colLabels=self.df.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(24)
        the_table.scale(1.5, 3)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q412:
    def __init__(self):
        self.data = {
            'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
            'Total Sales': np.random.randint(10000, 50000, 4),
            'Hours Worked': np.random.randint(100, 200, 4),
        }
        self.df = pd.DataFrame(self.data)
        self.df['Efficiency'] = self.df['Total Sales'] / self.df['Hours Worked']
        max_efficiency_index = self.df['Efficiency'].idxmax()
        self.query = "The table below represents the total sales and hours worked by employees. Which employee had the highest efficiency if efficiency is calculated as (Total Sales / Total Hours Worked)? Choices: (A) Alice (B) Bob (C) Charlie (D) David"
        self.answer = ['A', 'B', 'C', 'D'][max_efficiency_index]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        df_to_display = self.df.drop(columns=['Efficiency'])
        fig, ax = plt.subplots(figsize=(6, 4))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df_to_display.values, colLabels=df_to_display.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(24)
        the_table.scale(1.7, 4)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q413:
    def __init__(self):
        self.data = {
            'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'January': np.random.randint(100, 200, 5),
            'February': np.random.randint(100, 200, 5),
            'March': np.random.randint(100, 200, 5),
            'April': np.random.randint(100, 200, 5),
        }
        self.df = pd.DataFrame(self.data)
        total_hours = self.df[['January', 'February', 'March', 'April']].sum(axis=1)
        max_hours_index = total_hours.idxmax()
        self.query = "The table below represents the monthly hours worked by employees. Which employee worked the most total hours? Choices: (A) Alice (B) Bob (C) Charlie (D) David (E) Eve"
        self.answer = ['A', 'B', 'C', 'D', 'E'][max_hours_index]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(8, 3))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=self.df.values, colLabels=self.df.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(24)
        the_table.scale(1.5, 3)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q414:
    def __init__(self):
        self.data = {
            'Grade': ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5'],
            'Number of Students': np.random.randint(20, 50, 5) * 10
        }
        self.df = pd.DataFrame(self.data)
        self.query = "The table below represents the number of students in each grade at an elementary school. What is the total number of students in Grade 3?"
        self.answer = self.df.loc[self.df['Grade'] == 'Grade 3', 'Number of Students'].values[0]
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(6, 2)) # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=self.df.values, colLabels=self.df.columns, cellLoc = 'center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(24)
        the_table.scale(1.5, 3)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q415:
    def __init__(self):
        self.data = {
            'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
            'Q1 Sales': np.random.randint(100, 500, 5) * 10,
            'Q2 Sales': np.random.randint(100, 500, 5) * 10,
            'Q3 Sales': np.random.randint(100, 500, 5) * 10,
            'Q4 Sales': np.random.randint(100, 500, 5) * 10,
        }
        self.df = pd.DataFrame(self.data)
        average_sales = self.df.set_index('Product').mean(axis=1)
        max_average_sales_index = average_sales.idxmax()
        self.query = "The table below represents the quarterly sales of different products. Which product has the highest average quarterly sales? Choices: (A) Product A (B) Product B (C) Product C (D) Product D (E) Product E"
        self.answer = ['A', 'B', 'C', 'D', 'E'][self.df.index[self.df['Product'] == max_average_sales_index][0]]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(8, 3))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=self.df.values, colLabels=self.df.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(24)
        the_table.scale(1.5, 3)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q416:
    def __init__(self):
        self.data = {
            'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
            'Q1 Sales': np.random.randint(100, 500, 5) * 10,
            'Q2 Sales': np.random.randint(100, 500, 5) * 10,
            'Q3 Sales': np.random.randint(100, 500, 5) * 10,
            'Q4 Sales': np.random.randint(100, 500, 5) * 10,
        }
        self.df = pd.DataFrame(self.data)
        self.query = "The table below represents the quarterly sales of different products. What is the total sales of Product B?"
        self.answer = self.df.loc[self.df['Product'] == 'Product B', ['Q1 Sales', 'Q2 Sales', 'Q3 Sales', 'Q4 Sales']].sum(axis=1).values[0]
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(8, 3))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=self.df.values, colLabels=self.df.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(24)
        the_table.scale(1.5, 3)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q417:
    def __init__(self):
        self.data = {
            'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
            'Q1 Sales': np.random.randint(500, 1500, 4),
            'Q2 Sales': np.random.randint(500, 1500, 4),
            'Q3 Sales': np.random.randint(500, 1500, 4),
            'Q4 Sales': np.random.randint(500, 1500, 4),
        }
        self.df = pd.DataFrame(self.data)
        self.query = "The table below represents the quarterly sales of different products. Which product has the highest total sales in Q2?"
        max_sales_index = self.df['Q2 Sales'].idxmax()
        self.answer = self.df.loc[max_sales_index, 'Product']
        self.answer_type = "text"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(8, 4))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=self.df.values, colLabels=self.df.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(24)
        the_table.scale(1.5, 3)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q418:
    def __init__(self):
        self.data = {
            'Region': ['Region A', 'Region B', 'Region C', 'Region D'],
            'Q1 Revenue': np.random.randint(1000, 5000, 4) * 10,
            'Q2 Revenue': np.random.randint(1000, 5000, 4) * 10,
            'Q3 Revenue': np.random.randint(1000, 5000, 4) * 10,
            'Q4 Revenue': np.random.randint(1000, 5000, 4) * 10,
        }
        self.df = pd.DataFrame(self.data)
        self.df['Average Growth Rate'] = self.df[['Q2 Revenue', 'Q3 Revenue', 'Q4 Revenue']].pct_change(axis=1).mean(axis=1)
        self.df['Projected Revenue Next Year'] = self.df['Q4 Revenue'] * (1 + self.df['Average Growth Rate'])
        self.query = "The table below represents the quarterly revenues of different regions. What is the projected revenue for Region A next year if the growth rate is the average quarterly growth rate this year?"
        self.answer = round(self.df.loc[self.df['Region'] == 'Region A', 'Projected Revenue Next Year'].values[0], 2)
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        df_to_display = self.df.drop(columns=['Average Growth Rate', 'Projected Revenue Next Year'])
        fig, ax = plt.subplots(figsize=(8, 5))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df_to_display.values, colLabels=df_to_display.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(26)
        the_table.scale(2, 4)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q419:
    def __init__(self):
        self.data = {
            'Region': ['North', 'South', 'East', 'West'],
            'Q1 Revenue': np.random.randint(1000, 5000, 4) * 10,
            'Q2 Revenue': np.random.randint(1000, 5000, 4) * 10,
            'Q3 Revenue': np.random.randint(1000, 5000, 4) * 10,
            'Q4 Revenue': np.random.randint(1000, 5000, 4) * 10,
        }
        self.df = pd.DataFrame(self.data)
        self.query = "The table below represents the quarterly revenue from different regions. What is the total revenue in Q3?"
        self.answer = self.df['Q3 Revenue'].sum()
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(8, 5))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=self.df.values, colLabels=self.df.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(26)
        the_table.scale(2, 4)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q420:
    def __init__(self):
        self.data = {
            'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
            'Q1 Sales': np.random.randint(500, 1500, 4),
            'Q2 Sales': np.random.randint(500, 1500, 4),
            'Q3 Sales': np.random.randint(500, 1500, 4),
            'Q4 Sales': np.random.randint(500, 1500, 4),
        }
        self.df = pd.DataFrame(self.data)
        total_sales_by_quarter = self.df[['Q1 Sales', 'Q2 Sales', 'Q3 Sales', 'Q4 Sales']].sum()
        self.query = "The table below represents the quarterly sales of different products. Which quarter had the highest total sales for all products combined? Choices: (A) Q1 (B) Q2 (C) Q3 (D) Q4"
        max_sales_index = total_sales_by_quarter.idxmax()
        self.answer = ['A', 'B', 'C', 'D'][['Q1 Sales', 'Q2 Sales', 'Q3 Sales', 'Q4 Sales'].index(max_sales_index)]
        self.answer_type = "multiple choice"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(10, 4))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=self.df.values, colLabels=self.df.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(24)
        the_table.scale(1.5, 3)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q421:
    def __init__(self):
        self.data = {
            'Store': ['Store A', 'Store B', 'Store C', 'Store D'],
            'Q1 Revenue': np.random.randint(1000, 5000, 4) * 10,
            'Q2 Revenue': np.random.randint(1000, 5000, 4) * 10,
            'Q1 Cost': np.random.randint(500, 2500, 4) * 10,
            'Q2 Cost': np.random.randint(500, 2500, 4) * 10,
        }
        self.df = pd.DataFrame(self.data)
        self.df['Q1 Profit'] = self.df['Q1 Revenue'] - self.df['Q1 Cost']
        self.df['Q2 Profit'] = self.df['Q2 Revenue'] - self.df['Q2 Cost']
        self.df['Total Profit H1'] = self.df['Q1 Profit'] + self.df['Q2 Profit']
        self.query = "The table below represents the revenue and costs for different stores. What is the total profit for Store C in the first half of the year?"
        self.answer = self.df.loc[self.df['Store'] == 'Store C', 'Total Profit H1'].values[0]
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        df_to_display = self.df.drop(columns=['Q1 Profit', 'Q2 Profit', 'Total Profit H1'])
        fig, ax = plt.subplots(figsize=(8, 5))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df_to_display.values, colLabels=df_to_display.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(26)
        the_table.scale(2, 4)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q422:
    def __init__(self):
        self.data = {
            'Student': ['Student A', 'Student B', 'Student C', 'Student D', 'Student E'],
            'Math': np.random.randint(60, 100, 5),
            'Science': np.random.randint(60, 100, 5),
            'English': np.random.randint(60, 100, 5),
            'History': np.random.randint(60, 100, 5),
        }
        self.df = pd.DataFrame(self.data)
        self.query = "The table below represents the scores of students in different subjects. What is the average score for Student C?"
        self.answer = self.df.loc[self.df['Student'] == 'Student C', ['Math', 'Science', 'English', 'History']].mean(axis=1).values[0]
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(8, 3))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=self.df.values, colLabels=self.df.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(24)
        the_table.scale(1.5, 3)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q423:
    def __init__(self):
        self.data = {
            'Student': ['Student A', 'Student B', 'Student C', 'Student D', 'Student E'],
            'Math': np.random.randint(60, 100, 5),
            'Science': np.random.randint(60, 100, 5),
            'English': np.random.randint(60, 100, 5),
            'History': np.random.randint(60, 100, 5),
        }
        self.df = pd.DataFrame(self.data)
        self.df['Median Score'] = self.df[['Math', 'Science', 'English', 'History']].median(axis=1)
        self.query = "The table below represents the scores of students in different subjects. What is the median score for Student B?"
        self.answer = self.df.loc[self.df['Student'] == 'Student B', 'Median Score'].values[0]
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        df_to_display = self.df.drop(columns=['Median Score'])
        fig, ax = plt.subplots(figsize=(8, 3))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df_to_display.values, colLabels=df_to_display.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(24)
        the_table.scale(1.5, 3)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q424:
    def __init__(self):
        self.data = {
            'Student': ['Student A', 'Student B', 'Student C', 'Student D', 'Student E'],
            'Math': np.random.randint(60, 100, 5),
            'Science': np.random.randint(60, 100, 5),
            'English': np.random.randint(60, 100, 5),
            'History': np.random.randint(60, 100, 5),
        }
        self.df = pd.DataFrame(self.data)
        self.df['Variance'] = self.df[['Math', 'Science', 'English', 'History']].var(axis=1)
        self.query = "The table below represents the scores of students in different subjects. What is the variance of the scores for Student D?"
        self.answer = self.df.loc[self.df['Student'] == 'Student D', 'Variance'].values[0]
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        df_to_display = self.df.drop(columns=['Variance'])
        fig, ax = plt.subplots(figsize=(8, 3))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df_to_display.values, colLabels=df_to_display.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(24)
        the_table.scale(1.5, 3)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q425:
    def __init__(self):
        self.data = {
            'Grade': ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5'],
            'Number of Students': np.random.randint(20, 50, 5) * 10
        }
        self.df = pd.DataFrame(self.data)
        self.query = "The table below represents the number of students in each grade at an elementary school. What is the total number of students across all grades?"
        self.answer = self.df['Number of Students'].sum()
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        fig, ax = plt.subplots(figsize=(6, 2))  # set size frame
        ax.axis('off')
        the_table = ax.table(cellText=self.df.values, colLabels=self.df.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(24)
        the_table.scale(1.5, 3)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()
        

class Q426:
    def __init__(self):
        self.data = {
            'Student': ['Student A', 'Student B', 'Student C', 'Student D'],
            'Math': np.random.randint(60, 100, 4),
            'Science': np.random.randint(60, 100, 4),
            'English': np.random.randint(60, 100, 4),
            'History': np.random.randint(60, 100, 4),
        }
        self.df = pd.DataFrame(self.data)
        self.df['Weighted Average'] = (
            self.df['Math'] * 0.4 +
            self.df['Science'] * 0.3 +
            self.df['English'] * 0.2 +
            self.df['History'] * 0.1
        )
        self.query = "The table below represents the scores of students in different subjects. What is the weighted average grade for Student A considering Math has a weight of 40%, Science 30%, English 20%, and History 10%?"
        self.answer = round(self.df.loc[self.df['Student'] == 'Student A', 'Weighted Average'].values[0], 2)
        self.answer_type = "float"
        self.subject = "statistics"
        self.level = "high school"

    def draw(self, num):
        df_to_display = self.df.drop(columns=['Weighted Average'])
        fig, ax = plt.subplots(figsize=(8, 3))  # set size frame
        ax.axis('tight')
        ax.axis('off')
        the_table = ax.table(cellText=df_to_display.values, colLabels=df_to_display.columns, cellLoc='center', loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(26)
        the_table.scale(1.5, 3)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()







