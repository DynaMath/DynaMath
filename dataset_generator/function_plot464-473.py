import os
import random as rd
from PIL import Image, ImageDraw, ImageFont
from matplotlib_venn import venn2, venn2_circles, venn3, venn3_circles
import matplotlib.pyplot as plt
import random


class Q464:
    def __init__(self, total=180):
        # Generate random numbers that sum to 180
        self.coffee_only = random.randint(40, 90)
        self.tea_only = random.randint(40, 90)
        self.both_beverages = random.randint(0, abs(total - self.coffee_only - self.tea_only))

        remainder = total - (self.coffee_only + self.tea_only + self.both_beverages)
        self.neither = remainder

        self.total = total

        # Calculate the sum of people who prefer either only Coffee or only Tea
        self.answer = self.coffee_only + self.tea_only

        # Define the question and answer options
        self.query = (
            f"{self.total} people were surveyed about their beverage preferences. The results are displayed in the Venn diagram below. What is the sum of people who prefer only Coffee or only Tea?"
        )

        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        plt.figure(figsize=(8, 6))
        venn = venn2(subsets=(self.coffee_only, self.tea_only, self.both_beverages), set_labels=('Coffee', 'Tea'))
        venn_circles = venn2_circles(subsets=(self.coffee_only, self.tea_only, self.both_beverages), linestyle='solid')
        for label in venn.set_labels:
            label.set_fontsize(20)
        for subset in venn.subset_labels:
            if subset:
                subset.set_fontsize(35)
        plt.text(-0.7, -0.6, f'Neither: {self.neither}', fontsize=20, ha='center')

        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q465:
    def __init__(self, total=210):
        # Generate random numbers that sum to 210
        self.organic_only = random.randint(30, 60)
        self.non_organic_only = random.randint(60, 90)
        self.both_products = random.randint(20, abs(total - self.organic_only - self.non_organic_only))

        remainder = total - (self.organic_only + self.non_organic_only + self.both_products)
        self.neither = remainder

        self.total = total

        # Calculate the difference between Non-Organic only and Organic only customers
        self.answer = abs(self.non_organic_only - self.organic_only)

        # Define the question and answer options
        self.query = (
            f"{self.total} customers were surveyed about their product preferences. The results are displayed in the Venn diagram below. How many more customers prefer only Non-Organic products than only Organic ones?"
        )

        self.answer_type = "single answer"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        plt.figure(figsize=(8, 6))
        venn = venn2(subsets=(self.organic_only, self.non_organic_only, self.both_products), set_labels=('Organic', 'Non-Organic'))
        venn_circles = venn2_circles(subsets=(self.organic_only, self.non_organic_only, self.both_products), linestyle='solid')
        for label in venn.set_labels:
            label.set_fontsize(20)
        for subset in venn.subset_labels:
            if subset:
                subset.set_fontsize(35)
        plt.text(-0.7, -0.6, f'Neither: {self.neither}', fontsize=20, ha='center')

        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q466:
    def __init__(self, total=200):
        # Generate random numbers that sum to 200
        self.climate_change_only = random.randint(40, 100)
        self.deforestation_only = random.randint(40, 100)
        self.both_concerns = random.randint(0, abs(total - self.deforestation_only - self.climate_change_only))

        remainder = total - (self.climate_change_only + self.deforestation_only + self.both_concerns)
        self.neither = remainder

        self.total = total

        # Calculate the number of people who are concerned about neither issue
        self.answer = self.neither

        # Define the question and answer options
        self.query = (
            f"{self.total} people were surveyed about their environmental concerns. The results are displayed in the Venn diagram below. How many people are not concerned about either Climate Change or Deforestation?"
        )

        self.answer_type = "single answer"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        plt.figure(figsize=(8, 6))
        venn = venn2(subsets=(self.climate_change_only, self.deforestation_only, self.both_concerns), set_labels=('Climate Change', 'Deforestation'))
        venn_circles = venn2_circles(subsets=(self.climate_change_only, self.deforestation_only, self.both_concerns), linestyle='solid')
        for label in venn.set_labels:
            label.set_fontsize(20)
        for subset in venn.subset_labels:
            if subset:
                subset.set_fontsize(35)
        plt.text(-0.7, 0.5, f'Neither: {self.neither}', fontsize=20, ha='center')

        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q467:
    def __init__(self, total=180):
        # Generate random numbers that sum to 180
        self.action_only = random.randint(30, 90)
        self.comedy_only = random.randint(30, 90)
        self.both_genres = random.randint(0, abs(total - self.action_only - self.comedy_only))

        remainder = total - (self.action_only + self.comedy_only + self.both_genres)
        self.neither = remainder

        self.total = total

        # Calculate the number of people who like both genres
        self.answer = self.both_genres

        # Define the question and answer options
        self.query = (
            f"{self.total} moviegoers were surveyed about their genre preference. The results are displayed in the Venn diagram below. How many people like both Action and Comedy movies?"
        )

        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        plt.figure(figsize=(8, 6))
        venn = venn2(subsets=(self.action_only, self.comedy_only, self.both_genres), set_labels=('Action', 'Comedy'))
        venn_circles = venn2_circles(subsets=(self.action_only, self.comedy_only, self.both_genres), linestyle='solid')
        for label in venn.set_labels:
            label.set_fontsize(20)
        for subset in venn.subset_labels:
            if subset:
                subset.set_fontsize(35)
        plt.text(-0.7, 0.5, f'Neither: {self.neither}', fontsize=20, ha='center')

        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q468:
    def __init__(self):
        while True:
            self.set_A = set(rd.sample(range(1, 20), rd.randint(5, 10)))
            self.set_B = set(rd.sample(range(1, 20), rd.randint(5, 10)))
            
            self.intersection = self.set_A & self.set_B
            self.union = self.set_A | self.set_B
            self.only_A = self.set_A - self.set_B
            self.only_B = self.set_B - self.set_A

            if self.intersection and self.only_A and self.only_B:
                break

        # Convert the sets to lists for display
        correct_answer = sorted(list(self.intersection))
        wrong_answers = [
            sorted(list(self.only_A)),
            sorted(list(self.only_B)),
            sorted(list(self.union - self.intersection))
        ]

        all_answers = wrong_answers + [correct_answer]
        rd.shuffle(all_answers)

        # Assign multiple choice options
        self.answer_options = {
            "A": all_answers[0],
            "B": all_answers[1],
            "C": all_answers[2],
            "D": all_answers[3],
        }
        
        # Determine the correct answer key
        for key, value in self.answer_options.items():
            if value == correct_answer:
                self.answer = key
                break

        # Incorporate choices into the query
        self.query = (
            "What is the intersection of sets A and B?\n"
            f"A: {self.answer_options['A']}\n"
            f"B: {self.answer_options['B']}\n"
            f"C: {self.answer_options['C']}\n"
            f"D: {self.answer_options['D']}\n"
        )

        self.answer_type = "multiple choice"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        plt.figure(figsize=(5, 5))
        venn = venn2([self.set_A, self.set_B], ('A', 'B'))
        venn_circles = venn2_circles([self.set_A, self.set_B], linestyle='solid')
        
        # Annotate the Venn diagram with the elements
        for label, subset in zip(('10', '01', '11'), [self.only_A, self.only_B, self.intersection]):
            venn.get_label_by_id(label).set_text('\n'.join(map(str, sorted(subset))))
        for label in venn.set_labels:
            label.set_fontsize(20)
        for subset in venn.subset_labels:
            if len(self.only_A) > 7 or len(self.only_B) > 7:
                subset.set_fontsize(16)
            else:
                subset.set_fontsize(20)
        # plt.title("Venn Diagram for Sets A and B")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q469:
    def __init__(self):
        while True:
            self.set_A = set(rd.sample(range(1, 20), rd.randint(5, 10)))
            self.set_B = set(rd.sample(range(1, 20), rd.randint(5, 10)))
            
            self.intersection = self.set_A & self.set_B
            self.union = self.set_A | self.set_B
            self.only_A = self.set_A - self.set_B
            self.only_B = self.set_B - self.set_A

            if self.intersection and self.only_A and self.only_B:
                break

        correct_answer = sorted(list(self.union))
        wrong_answers = [
            sorted(list(self.intersection)),
            sorted(list(self.only_A)),
            sorted(list(self.only_B))
        ]

        all_answers = [correct_answer] + wrong_answers
        rd.shuffle(all_answers)

        self.answer_options = {
            "A": all_answers[0],
            "B": all_answers[1],
            "C": all_answers[2],
            "D": all_answers[3],
        }

        for key, value in self.answer_options.items():
            if value == correct_answer:
                self.answer = key
                break

        self.query = (
            "What is the union of sets A and B?\n"
            f"A: {self.answer_options['A']}\n"
            f"B: {self.answer_options['B']}\n"
            f"C: {self.answer_options['C']}\n"
            f"D: {self.answer_options['D']}\n"
        )

        self.answer_type = "multiple choice"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        plt.figure(figsize=(5, 5))
        venn = venn2([self.set_A, self.set_B], ('A', 'B'))
        venn_circles = venn2_circles([self.set_A, self.set_B], linestyle='solid')
        
        # Annotate the Venn diagram with the elements
        for label, subset in zip(('10', '01', '11'), [self.only_A, self.only_B, self.intersection]):
            venn.get_label_by_id(label).set_text('\n'.join(map(str, sorted(subset))))
        for label in venn.set_labels:
            label.set_fontsize(20)
        for subset in venn.subset_labels:
            if len(self.only_A) > 7 or len(self.only_B) > 7:
                subset.set_fontsize(16)
            else:
                subset.set_fontsize(20)
        # plt.title("Venn Diagram for Sets A and B")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q470:
    def __init__(self):
        while True:
            self.set_A = set(rd.sample(range(1, 20), rd.randint(5, 10)))
            self.set_B = set(rd.sample(range(1, 20), rd.randint(5, 10)))
            
            self.intersection = self.set_A & self.set_B
            self.union = self.set_A | self.set_B
            self.only_A = self.set_A - self.set_B
            self.only_B = self.set_B - self.set_A

            if self.intersection and self.only_A and self.only_B:
                break

        correct_answer = sorted(list(self.only_A))
        wrong_answers = [
            sorted(list(self.intersection)),
            sorted(list(self.only_B)),
            sorted(list(self.union - self.only_A))
        ]

        all_answers = [correct_answer] + wrong_answers
        rd.shuffle(all_answers)

        self.answer_options = {
            "A": all_answers[0],
            "B": all_answers[1],
            "C": all_answers[2],
            "D": all_answers[3],
        }

        for key, value in self.answer_options.items():
            if value == correct_answer:
                self.answer = key
                break

        self.query = (
            "Which elements are unique to set A?\n"
            f"A: {self.answer_options['A']}\n"
            f"B: {self.answer_options['B']}\n"
            f"C: {self.answer_options['C']}\n"
            f"D: {self.answer_options['D']}\n"
        )

        self.answer_type = "multiple choice"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        plt.figure(figsize=(5, 5))
        venn = venn2([self.set_A, self.set_B], ('A', 'B'))
        venn_circles = venn2_circles([self.set_A, self.set_B], linestyle='solid')
        
        # Annotate the Venn diagram with the elements
        for label, subset in zip(('10', '01', '11'), [self.only_A, self.only_B, self.intersection]):
            venn.get_label_by_id(label).set_text('\n'.join(map(str, sorted(subset))))
        for label in venn.set_labels:
            label.set_fontsize(20)
        for subset in venn.subset_labels:
            if len(self.only_A) > 7 or len(self.only_B) > 7:
                subset.set_fontsize(16)
            else:
                subset.set_fontsize(20)
        # plt.title("Venn Diagram for Sets A and B")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q471:
    def __init__(self, total=150):
        # Generate random numbers that sum to 150
        self.programming_only = random.randint(20, 70)
        self.data_analysis_only = random.randint(20, 70)
        self.both_skills = random.randint(0, total - self.programming_only - self.data_analysis_only)

        remainder = total - (self.programming_only + self.data_analysis_only + self.both_skills)
        self.neither = remainder

        self.total = total

        # Calculate the number of people with unique skills
        self.answer = self.programming_only + self.data_analysis_only

        # Define the question and answer options
        self.query = (
            f"{self.total} employees were surveyed about their skills. The results are displayed in the Venn diagram below. How many people possess unique skills?"
        )

        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        plt.figure(figsize=(8, 6))
        venn = venn2(subsets=(self.programming_only, self.data_analysis_only, self.both_skills),
                     set_labels=('Programming', 'Data Analysis'))
        venn_circles = venn2_circles(subsets=(self.programming_only, self.data_analysis_only, self.both_skills),
                                     linestyle='solid')
        for label in venn.set_labels:
            label.set_fontsize(20)
        for subset in venn.subset_labels:
            if subset:
                subset.set_fontsize(35)
        plt.text(-0.7, 0.5, f'Neither: {self.neither}', fontsize=20, ha='center')

        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q472:
    def __init__(self, total=200):
        # Generate random numbers that sum to 200
        self.a_only = random.randint(20, 100)
        self.b_only = random.randint(20, 100)
        self.intersection = random.randint(0, abs(total - self.a_only - self.b_only))

        remainder = total - (self.a_only + self.b_only + self.intersection)
        self.neither = remainder  # People who don't like either option

        if remainder < 0:
            if random.choice([True, False]):
                self.a_only += remainder
            else:
                self.b_only += remainder

        self.total = total

        # Define the question and answer options
        self.query = (
            f"{self.total} people were surveyed about how they like to travel. The results are displayed in the Venn diagram below. How many people don't like to fly in an airplane?"
        )

        self.answer = self.a_only + self.neither
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        plt.figure(figsize=(8, 6))
        venn = venn2(subsets=(self.a_only, self.b_only, self.intersection), set_labels=('Car', 'Airplane'))
        venn_circles = venn2_circles(subsets=(self.a_only, self.b_only, self.intersection), linestyle='solid')

        # Add the "neither" group as text outside the Venn diagram
        for label in venn.set_labels:
            label.set_fontsize(20)
        for subset in venn.subset_labels:
            if subset:
                subset.set_fontsize(35)
        plt.text(-0.7, 0.5, f'Neither: {self.neither}', fontsize=20, ha='center')

        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q473:
    def __init__(self):
        while True:
            self.set_A = set(rd.sample(range(1, 20), rd.randint(5, 10)))
            self.set_B = set(rd.sample(range(1, 20), rd.randint(5, 10)))
            
            self.intersection = self.set_A & self.set_B
            self.union = self.set_A | self.set_B
            self.only_A = self.set_A - self.set_B
            self.only_B = self.set_B - self.set_A

            if self.intersection and self.only_A and self.only_B:
                break

        correct_answer = sorted(list(self.only_B))
        wrong_answers = [
            sorted(list(self.intersection)),
            sorted(list(self.only_A)),
            sorted(list(self.union - self.only_B))
        ]

        all_answers = [correct_answer] + wrong_answers
        rd.shuffle(all_answers)

        self.answer_options = {
            "A": all_answers[0],
            "B": all_answers[1],
            "C": all_answers[2],
            "D": all_answers[3],
        }

        for key, value in self.answer_options.items():
            if value == correct_answer:
                self.answer = key
                break

        self.query = (
            "Which elements are unique to set B?\n"
            f"A: {self.answer_options['A']}\n"
            f"B: {self.answer_options['B']}\n"
            f"C: {self.answer_options['C']}\n"
            f"D: {self.answer_options['D']}\n"
        )

        self.answer_type = "multiple choice"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        plt.figure(figsize=(5, 5))
        venn = venn2([self.set_A, self.set_B], ('A', 'B'))
        venn_circles = venn2_circles([self.set_A, self.set_B], linestyle='solid')
        
        # Annotate the Venn diagram with the elements
        for label, subset in zip(('10', '01', '11'), [self.only_A, self.only_B, self.intersection]):
            venn.get_label_by_id(label).set_text('\n'.join(map(str, sorted(subset))))
        for label in venn.set_labels:
            label.set_fontsize(20)
        for subset in venn.subset_labels:
            if len(self.only_A) > 7 or len(self.only_B) > 7:
                subset.set_fontsize(16)
            else:
                subset.set_fontsize(20)
        # plt.title("Venn Diagram for Sets A and B")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()











