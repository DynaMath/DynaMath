import math
import shutil
import os.path
import matplotlib.pyplot as plt
import numpy as np
import random as rd
from matplotlib.patches import *


class Q81:
    # angle in circle
    def __init__(self):
        self.d = rd.randint(40, 60)
        self.query = f"As shown in the figure, AB is the diameter of ⊙O, point C is on ⊙O, passing point C to draw the " \
                     f"tangent of ⊙O and it intersects the extended line of AB at point D. Connect AC. If ∠D = {self.d}, " \
                     f"then what is the degree of ∠A?"
        self.answer = self.d / 2
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q100temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q100temp.png"), dest_image_path)


class Q82:
    # easy group 1
    def __init__(self):
        self.query = "There is a cycle graph of C6 in the image. Fill the number in the empty slot so that it becomes " \
                     "the integers modulo 6 under addition (Z6). "
        self.choice = rd.randint(0, 5)
        self.answer = self.choice
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        plt.xlim(-8 * 1.1, 8 * 1.1)
        plt.ylim(-8 * 1.1, 8 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(8, 8)
        circle = Circle((0, 0), 4, color="black", fill=False, linewidth=2)
        circle2 = Circle((0, 4), 1, fill=True, linewidth=2, edgecolor="red", facecolor="white")
        circle3 = Circle((0, -4), 1, fill=True, linewidth=2, edgecolor="red", facecolor="white")
        circle4 = Circle((2 * np.sqrt(3), 2), 1, fill=True, linewidth=2, edgecolor="red", facecolor="white")
        circle5 = Circle((-2 * np.sqrt(3), 2), 1, fill=True, linewidth=2, edgecolor="red", facecolor="white")
        circle6 = Circle((2 * np.sqrt(3), -2), 1, fill=True, linewidth=2, edgecolor="red", facecolor="white")
        circle7 = Circle((-2 * np.sqrt(3), -2), 1, fill=True, linewidth=2, edgecolor="red", facecolor="white")
        ax.add_patch(circle)
        ax.add_patch(circle4)
        ax.add_patch(circle5)
        ax.add_patch(circle2)
        ax.add_patch(circle3)
        ax.add_patch(circle6)
        ax.add_patch(circle7)
        if self.choice != 0:
            plt.text(-0.2, 3.8, "0", fontsize=20)
        if self.choice != 3:
            plt.text(-0.3, -4.3, "3", fontsize=20)
        if self.choice != 1:
            plt.text(2 * np.sqrt(3) - 0.2, 1.8, "1", fontsize=20)
        if self.choice != 5:
            plt.text(-2 * np.sqrt(3) - 0.3, 1.75, "5", fontsize=20)
        if self.choice != 2:
            plt.text(2 * np.sqrt(3) - 0.2, -2.3, "2", fontsize=20)
        if self.choice != 4:
            plt.text(-2 * np.sqrt(3) - 0.2, -2.3, "4", fontsize=20)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q83:
    # complementary angle
    def __init__(self):
        self.angle = rd.randint(10, 80)
        self.query = f"As shown in the figure, points A, O, and B are collinear, and DO is perpendicular to CO. If " \
                     f"∠BOC = {self.angle}°, what is the measure of ∠AOD? "
        self.answer = 90 - self.angle
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        length = 4
        length_s = 0.2
        angle_radians = np.radians(self.angle)
        angle_radians2 = np.radians(self.angle + 90)
        x_end = length * np.cos(angle_radians)
        y_end = length * np.sin(angle_radians)
        x_end2 = length * np.cos(angle_radians2)
        y_end2 = length * np.sin(angle_radians2)
        x_pos = length_s * np.cos(angle_radians)
        y_pos = length_s * np.sin(angle_radians)
        x_pos2 = length_s * np.cos(angle_radians2)
        y_pos2 = length_s * np.sin(angle_radians2)
        fig = plt.figure()
        fig.set_size_inches(4, 4)
        plt.plot([0, x_end], [0, y_end], color="black")
        plt.plot([0, x_end2], [0, y_end2], color="black")
        plt.plot([x_pos, x_pos + x_pos2], [y_pos, y_pos + y_pos2], color="black")
        plt.plot([x_pos2, x_pos2 + x_pos], [y_pos2, y_pos2 + y_pos], color="black")
        plt.plot([-4, 4], [0, 0], color="black")
        plt.xlim(-length, length)
        plt.ylim(-length, length)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.text(-4, -0.7, "A", fontsize=14)
        plt.text(3.8, -0.7, "B", fontsize=14)
        plt.text(-0.2, -0.7, "O", fontsize=14)
        plt.text(x_end, y_end + 0.3, "C", fontsize=14)
        plt.text(x_end2, y_end2 + 0.3, "D", fontsize=14)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q84:
    # rotation, flip, dilation
    def __init__(self):
        self.enlargesize = rd.randint(1, 3)
        self.query = "What type of transformation of the left triangle was applied to become the right triangle? " \
                     "choice: (A) flip (B) rotation (C) enlargement (D) reduction "
        self.answer = rd.choice(["A", "B", "C", "D"])
        self.answer_type = "multiple choice"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        triangle1 = plt.Polygon([(-4, 0), (-4, 4), (-2, 2)], closed=True, fill=True, edgecolor='black',
                                facecolor='azure')
        plt.xlim(-6 * 1.1, 6 * 1.1)
        plt.ylim(-6 * 1.1, 6 * 1.1)
        ax = plt.gca()
        ax.add_patch(triangle1)
        if self.answer == "A":
            triangle_f = plt.Polygon([(2, 2), (4, 4), (4, 0)], closed=True, fill=True, edgecolor='black',
                                     facecolor='azure')
            ax.add_patch(triangle_f)
        elif self.answer == "B":
            triangle_r = plt.Polygon([(1, 1), (3, 3), (5, 1)], closed=True, fill=True, edgecolor='black',
                                     facecolor='azure')
            ax.add_patch(triangle_r)
        elif self.answer == "C":
            triangle_e = plt.Polygon(
                [(6 * self.enlargesize, 2 * self.enlargesize), (2 * self.enlargesize, -2 * self.enlargesize),
                 (2 * self.enlargesize, 6 * self.enlargesize)], closed=True, fill=True, edgecolor='black',
                facecolor='azure')
            ax.add_patch(triangle_e)
            plt.autoscale()
        else:
            triangle_d = plt.Polygon([(3, 2), (2, 3), (2, 1)], closed=True, fill=True, edgecolor='black',
                                     facecolor='azure')
            ax.add_patch(triangle_d)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(-1, 1, r'$\rightarrow$', fontsize=45)
        plt.grid()
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q85:
    # Pythagoras theorem 2
    def __init__(self):
        self.B = rd.randint(10, 50)
        self.A = self.B + rd.randint(10, 50)
        self.C = self.B + self.A
        self.query = f"The image shows a pythagorean tree. If the area of A and B are {self.A} and {self.B}, " \
                     f"what is the area of C?"
        self.answer = self.C
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q84temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q84temp.png"), dest_image_path)


class Q86:
    # continuous 3
    def __init__(self):
        self.a = rd.randint(-2, 2)
        self.b = rd.randint(-3, 3)
        self.c = rd.randint(-2, 2)
        self.d = rd.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        self.e = rd.randint(-4, 4)
        self.query = "Is this function continuous at x = 1? choice: (A) Yes (B) No"
        if self.a + self.b + self.c == self.d + self.e:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x1 = np.linspace(-10, 1, 200, endpoint=True)
        x2 = np.linspace(1, 10, 200, endpoint=True)
        f1 = self.a * x1 ** 2 + self.b * x1 + self.c
        f2 = self.d * x2 + self.e
        plt.plot(x1, f1, color='blue', linewidth=2.5)
        plt.plot(x2, f2, color='blue', linewidth=2.5)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(1, self.a + self.b + self.c, color='white', edgecolor='black')
        plt.scatter(1, self.d + self.e, color='blue')
        coefficients1 = [self.a, self.b, self.c]
        variables1 = ['x^2', 'x', '']
        expr1 = build_expression(coefficients1, variables1)
        first_line = f'y = {expr1}, x < 1'
        coefficients2 = [self.d, self.e]
        variables2 = ['x', '']
        expr2 = build_expression(coefficients2, variables2)
        second_line = f'y = {expr2}, x >= 1'

        plt.title(f'{first_line}\n{second_line}', fontsize=14)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q87:
    # limit2
    def __init__(self):
        self.a = rd.randint(-2, 2)
        self.b = rd.randint(-3, 3)
        self.c = rd.randint(-2, 2)
        self.d = rd.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        self.e = rd.randint(-4, 4)
        self.query = "What is the limit of the function as x approaches 1 from the left side?"
        self.answer = self.a + self.b + self.c
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x1 = np.linspace(-10, 1, 200, endpoint=True)
        x2 = np.linspace(1, 10, 200, endpoint=True)
        f1 = self.a * x1 ** 2 + self.b * x1 + self.c
        f2 = self.d * x2 + self.e
        plt.plot(x1, f1, color='purple', linewidth=2.5)
        plt.plot(x2, f2, color='purple', linewidth=2.5)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(1, self.a + self.b + self.c, color='white', edgecolor='black')
        plt.scatter(1, self.d + self.e, color='blue')
        coefficients1 = [self.a, self.b, self.c]
        variables1 = ['x^2', 'x', '']
        expr1 = build_expression(coefficients1, variables1)
        first_line = f'y = {expr1}, x < 1'
        coefficients2 = [self.d, self.e]
        variables2 = ['x', '']
        expr2 = build_expression(coefficients2, variables2)
        second_line = f'y = {expr2}, x >= 1'

        plt.title(f'{first_line}\n{second_line}', fontsize=14)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q88:
    # limit3
    def __init__(self):
        self.a = rd.randint(-2, 2)
        self.b = rd.randint(-3, 3)
        self.c = rd.randint(-2, 2)
        self.d = rd.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        self.e = rd.randint(-4, 4)
        self.query = "What is the limit of the function as x approaches 1 from the right side?"
        self.answer = self.d + self.e
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "undergraduate"

    def draw(self, num):
        x1 = np.linspace(-10, 1, 200, endpoint=True)
        x2 = np.linspace(1, 10, 200, endpoint=True)
        f1 = self.a * x1 ** 2 + self.b * x1 + self.c
        f2 = self.d * x2 + self.e
        plt.plot(x1, f1, color='red', linewidth=2.5)
        plt.plot(x2, f2, color='red', linewidth=2.5)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(1, self.a + self.b + self.c, color='white', edgecolor='black')
        plt.scatter(1, self.d + self.e, color='red')
        coefficients1 = [self.a, self.b, self.c]
        variables1 = ['x^2', 'x', '']
        expr1 = build_expression(coefficients1, variables1)
        first_line = f'y = {expr1}, x < 1'
        coefficients2 = [self.d, self.e]
        variables2 = ['x', '']
        expr2 = build_expression(coefficients2, variables2)
        second_line = f'y = {expr2}, x >= 1'

        plt.title(f'{first_line}\n{second_line}', fontsize=14)
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


def build_expression(coefficients, variables):
    terms = []
    for coeff, var in zip(coefficients, variables):
        if coeff == 0:
            continue
        sign = '+' if coeff > 0 else '-'
        abs_coeff = abs(coeff)
        if abs_coeff == 1 and var != '':
            term = f'{var}'
        else:
            term = f'{abs_coeff}{var}'
        if terms:
            term = f'{sign} {term}'
        elif coeff < 0:
            term = f'-{term}'
        terms.append(term)
    return ' '.join(terms) if terms else '0'


class Q89:
    # injective, surjective, bijective 1
    def __init__(self):
        self.a = rd.randint(1, 3)
        self.b = rd.randint(1, 3)
        self.c = rd.randint(1, 3)
        self.query = "Is the function injective? choice: (A) Yes (B) No"
        bool_a = False
        bool_b = False
        bool_c = False
        if self.a == 1 or self.b == 1 or self.c == 1:
            bool_a = True
        if self.a == 2 or self.b == 2 or self.c == 2:
            bool_b = True
        if self.a == 3 or self.b == 3 or self.c == 3:
            bool_c = True
        if bool_a and bool_b and bool_c:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        domain = Ellipse((-2, 0), 2, 4, color="black", fill=False, linewidth=2)
        range = Ellipse((2, 0), 2, 4, color="black", fill=False, linewidth=2)
        ax.add_patch(domain)
        ax.add_patch(range)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(-2.2, 2.5, "x", fontsize=20)
        plt.text(1.7, 2.5, "f(x)", fontsize=20)
        plt.text(-2.2, 1, "1", fontsize=20)
        plt.text(1.7, 1, "A", fontsize=20)
        plt.text(-2.2, 0, "2", fontsize=20)
        plt.text(1.7, 0, "B", fontsize=20)
        plt.text(-2.2, -1, "3", fontsize=20)
        plt.text(1.7, -1, "C", fontsize=20)
        if self.a != 0:
            plt.plot([-1.8, 1.6], [1.2, self.a + 0.2 - 2], color="black")
            ax.annotate('', xy=(1.6, self.a + 0.2 - 2), xytext=(-1.8, 1.2),
                        arrowprops=dict(arrowstyle="->", color='black'))
        if self.b != 0:
            plt.plot([-1.8, 1.6], [0.2, self.b + 0.2 - 2], color="black")
            ax.annotate('', xy=(1.6, self.b + 0.2 - 2), xytext=(-1.8, 0.2),
                        arrowprops=dict(arrowstyle="->", color='black'))
        if self.c != 0:
            plt.plot([-1.8, 1.6], [-0.8, self.c + 0.2 - 2], color="black")
            ax.annotate('', xy=(1.6, self.c + 0.2 - 2), xytext=(-1.8, -0.8),
                        arrowprops=dict(arrowstyle="->", color='black'))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q90:
    # injective, surjective, bijective 2
    def __init__(self):
        self.a = rd.randint(1, 3)
        self.b = rd.randint(1, 3)
        self.c = rd.randint(1, 3)
        self.d = rd.randint(1, 3)
        self.query = "Is the function surjective? choice: (A) Yes (B) No"
        bool_a = False
        bool_b = False
        bool_c = False
        if self.a == 1 or self.b == 1 or self.c == 1 or self.d == 1:
            bool_a = True
        if self.a == 2 or self.b == 2 or self.c == 2 or self.d == 2:
            bool_b = True
        if self.a == 3 or self.b == 3 or self.c == 3 or self.d == 3:
            bool_c = True
        if bool_a and bool_b and bool_c:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        domain = Ellipse((-2, -0.5), 2, 5, color="black", fill=False, linewidth=2)
        range = Ellipse((2, 0), 2, 4, color="black", fill=False, linewidth=2)
        ax.add_patch(domain)
        ax.add_patch(range)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(-2.2, 2.5, "x", fontsize=20)
        plt.text(1.7, 2.5, "f(x)", fontsize=20)
        plt.text(-2.2, 1, "1", fontsize=20)
        plt.text(1.7, 1, "A", fontsize=20)
        plt.text(-2.2, 0, "2", fontsize=20)
        plt.text(1.7, 0, "B", fontsize=20)
        plt.text(-2.2, -1, "3", fontsize=20)
        plt.text(1.7, -1, "C", fontsize=20)
        plt.text(-2.2, -2, "4", fontsize=20)
        if self.a != 0:
            plt.plot([-1.8, 1.6], [1.2, self.a + 0.2 - 2], color="black")
            ax.annotate('', xy=(1.6, self.a + 0.2 - 2), xytext=(-1.8, 1.2),
                        arrowprops=dict(arrowstyle="->", color='black'))
        if self.b != 0:
            plt.plot([-1.8, 1.6], [0.2, self.b + 0.2 - 2], color="black")
            ax.annotate('', xy=(1.6, self.b + 0.2 - 2), xytext=(-1.8, 0.2),
                        arrowprops=dict(arrowstyle="->", color='black'))
        if self.c != 0:
            plt.plot([-1.8, 1.6], [-0.8, self.c + 0.2 - 2], color="black")
            ax.annotate('', xy=(1.6, self.c + 0.2 - 2), xytext=(-1.8, -0.8),
                        arrowprops=dict(arrowstyle="->", color='black'))
        if self.d != 0:
            plt.plot([-1.8, 1.6], [-1.8, self.d + 0.2 - 2], color="black")
            ax.annotate('', xy=(1.6, self.d + 0.2 - 2), xytext=(-1.8, -1.8),
                        arrowprops=dict(arrowstyle="->", color='black'))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q91:
    # select poker 2
    def __init__(self):
        self.m = rd.choice(["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])
        self.s = rd.choice(["\u2665", "\u2666"])
        self.query = "According to image, a card is randomly selected from a standard 52-card deck. Find the " \
                     "probability that the next card selected after selecting this card from the deck is a heart."
        if self.s == "\u2665":
            self.answer = 12 / 51
        else:
            self.answer = 13 / 51
        self.answer_type = "float"
        self.subject = "arithmetic"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        square1 = plt.Polygon([(-1.5, 2), (-1.5, -2), (1.5, -2), (1.5, 2)], closed=True, fill=True, edgecolor='black',
                              facecolor='white')
        ax.add_patch(square1)
        plt.text(-1.3, 1.5, f'{self.m}', fontsize=14, weight="bold", color='red')
        plt.text(-1.35, 1.05, f'{self.s}', fontsize=14, weight="bold", color='red')
        plt.text(0.9, -1.6, f'{self.m}', fontsize=14, weight="bold", rotation=180, color='red')
        plt.text(0.88, -1.15, f'{self.s}', fontsize=14, weight="bold", rotation=180, color='red')
        plt.text(-0.55, -0.5, f'{self.s}', fontsize=40, weight="bold", color='red')
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q92:
    # perpendicular
    def __init__(self):
        self.a = rd.choice([-4, -1 / 4, -3, -1 / 3, -2, -1 / 2, -1, 1, 1 / 2, 2, 1 / 3, 3, 1 / 4, 4])
        self.b = rd.choice([-4, -1 / 4, -3, -1 / 3, -2, -1 / 2, -1, 1, 1 / 2, 2, 1 / 3, 3, 1 / 4, 4])
        self.c = rd.randint(-2, 2)
        self.d = rd.choice([-4, -3, 3, 4])
        self.query = "Are the red line and the blue line perpendicular to each other? choice: (A) Yes (B) No"
        if self.a * self.b == -1:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-10, 10, 200, endpoint=True)
        func1 = self.a * x + self.c
        func2 = self.b * x + self.d
        plt.plot(x, func1, color='red', linewidth=1.5)
        plt.plot(x, func2, color='Blue', linewidth=1.5)
        plt.xlim(-10 * 1.1, 10 * 1.1)
        plt.ylim(-10 * 1.1, 10 * 1.1)

        plt.xticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        plt.yticks([-10, -8, -6, -4, -2, 2, 4, 6, 8, 10])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q93:
    # angle bisector
    def __init__(self):
        self.A = rd.randint(100, 130)
        self.query = "Given triangle △ABC with internal angle bisectors OB and OC intersecting at point O, " \
                     f"if ∠A = {self.A}°, find the measure of ∠BOC."
        self.answer = self.A + (180 - self.A) / 2
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        shutil.copy2("temp_image/Q92temp.png", os.path.join(destination_folder, "image"))
        if os.path.exists(dest_image_path):
            os.remove(dest_image_path)
        os.rename(os.path.join(destination_folder, "image/Q92temp.png"), dest_image_path)


class Q94:
    # complementary angle 2
    def __init__(self):
        self.angle = rd.randint(10, 80)
        self.query = f"As shown in the figure, points A, O, and B are collinear, and DE is perpendicular to CO. If " \
                     f"∠BOC = {self.angle}°, what is the measure of ∠AOE? "
        self.answer = 90 + self.angle
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        length = 4
        length_s = 0.2
        angle_radians = np.radians(self.angle)
        angle_radians2 = np.radians(self.angle + 90)
        x_end = length * np.cos(angle_radians)
        y_end = length * np.sin(angle_radians)
        x_start = length * np.cos(angle_radians2 + np.radians(180))
        y_start = length * np.sin(angle_radians2 + np.radians(180))
        x_end2 = length * np.cos(angle_radians2)
        y_end2 = length * np.sin(angle_radians2)
        x_pos = length_s * np.cos(angle_radians)
        y_pos = length_s * np.sin(angle_radians)
        x_pos2 = length_s * np.cos(angle_radians2)
        y_pos2 = length_s * np.sin(angle_radians2)
        fig = plt.figure()
        fig.set_size_inches(4, 4)
        plt.plot([x_start, 0], [y_start, 0], color="black")
        plt.plot([0, x_end], [0, y_end], color="black")
        plt.plot([0, x_end2], [0, y_end2], color="black")
        plt.plot([x_pos, x_pos + x_pos2], [y_pos, y_pos + y_pos2], color="black")
        plt.plot([x_pos2, x_pos2 + x_pos], [y_pos2, y_pos2 + y_pos], color="black")
        plt.plot([-4, 4], [0, 0], color="black")
        plt.xlim(-length, length)
        plt.ylim(-length, length)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.text(-4, -0.7, "A", fontsize=14)
        plt.text(3.8, -0.7, "B", fontsize=14)
        plt.text(-0.2, -0.7, "O", fontsize=14)
        plt.text(x_end, y_end + 0.3, "C", fontsize=14)
        plt.text(x_end2, y_end2 + 0.3, "D", fontsize=14)
        plt.text(x_start + 0.2, y_start, "E", fontsize=14)
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q95:
    # triangle perimeter 2
    def __init__(self):
        self.a = rd.randint(3, 9)
        self.b = self.a - rd.randint(1, 2)
        self.c = self.b - rd.randint(0, 1)
        self.d = self.a - rd.randint(0, 1)
        self.query = "Two equilateral triangles of different sizes are placed on top of each other so that a hexagon " \
                     "is formed on the inside whose opposite sides are parallel. Four of the side lengths of the " \
                     "hexagon are stated in the diagram. How big is the perimeter of the hexagon? "
        self.answer = self.a + self.d + 2 * self.b + 2 * self.c
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        triangle = plt.Polygon([(1, 1), (3, 1), (2, 1 + np.sqrt(3))], closed=True, fill=False, edgecolor='black')
        triangle2 = plt.Polygon([(1, 2), (3, 2), (2, 2 - np.sqrt(3))], closed=True, fill=False, edgecolor='black')
        fig, ax = plt.subplots()
        fig.set_size_inches(4, 4)
        ax.add_patch(triangle)
        ax.add_patch(triangle2)
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        plt.text(1.9, 1.7, f"{self.a}", fontsize=12)
        plt.text(2.4, 1.3, f"{self.b}", fontsize=12)
        plt.text(1.5, 1.5, f"{self.c}", fontsize=12)
        plt.text(1.9, 1.1, f"{self.d}", fontsize=12)
        plt.xticks([])
        plt.yticks([])
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q96:
    # distance of two points 1
    def __init__(self):
        self.d = rd.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        self.e = rd.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        self.query = "What is the distance between the x-intercept and y-intercept of blue line?"
        self.answer = np.sqrt(self.e * self.e + (-self.e/self.d) * (-self.e/self.d))
        self.answer_type = "float"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x1 = np.linspace(-10, 10, 200, endpoint=True)
        f1 = self.d * x1 + self.e
        plt.plot(x1, f1, color='blue', linewidth=1.5)
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)

        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.tick_params(axis='both', which='major', labelsize=12)
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.scatter(-self.e / self.d, 0, color='blue')
        plt.scatter(0, self.e, color='blue')
        plt.grid()
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()


class Q97:
    # find shadow area in circle
    def __init__(self):
        self.r = rd.randint(1, 10)
        self.query = "Find the area of the shaded part."
        self.answer = self.r * self.r * (np.pi/4 - 1/2)
        self.answer_type = "float"
        self.subject = "plane geometry"
        self.level = "high school"

    def draw(self, num):
        random_a = 90
        plt.xlim(-3 * 1.1, 3 * 1.1)
        plt.ylim(-3 * 1.1, 3 * 1.1)
        plt.xticks([])
        plt.yticks([])
        ax = plt.gca()
        plt.gcf().set_size_inches(4, 4)
        triangle = plt.Polygon([(0, 2), (2, 0), (0, 0)], closed=True, fill=True, edgecolor='black', facecolor='white')
        wedge = Wedge((0, 0), 2, 0, random_a, facecolor="gray", edgecolor="black")
        circle = Circle((0, 0), 2, color="black", fill=False)
        ax.add_patch(wedge)
        ax.add_patch(triangle)
        ax.add_patch(circle)
        plt.text(0.5, -0.5, f'r = {self.r}', fontsize=12)
        plt.hlines(0.2, 0, 0.2, color='black')
        plt.vlines(0.2, 0, 0.2, color='black')
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path)
        plt.close()


class Q98:
    # period function 1
    def __init__(self):
        self.a = rd.choice([-2, -1, 1, 2, 3, 4])
        self.query = "Is this function a period function? choice: (A) Yes (B) No"
        if self.a == 1:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200, endpoint=True)
        cos = np.cos(x ** self.a)
        plt.plot(x, cos, color='red', linewidth=1.5)
        plt.xlim(-2 * np.pi * 1.1, 2 * np.pi * 1.1)
        plt.ylim(cos.min() * 1.1, cos.max() * 1.1)
        plt.xticks(
            [-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
            [r'-$2\pi$', r'-$3\pi/2$', r'-$\pi$', r'-$\pi/2$', r'$\pi/2$', r'$\pi$', r'-$3\pi/2$', r'$2\pi$']
        )
        plt.yticks([-3, -2, -1, 1, 2, 3])
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


class Q99:
    # period function 2
    def __init__(self):
        self.a = rd.choice([-2, -1, 1, 2, 3, 4])
        self.query = "Is this function a period function? choice: (A) Yes (B) No"
        if self.a == 1:
            self.answer = "A"
        else:
            self.answer = "B"
        self.answer_type = "multiple choice"
        self.subject = "analytic geometry"
        self.level = "high school"

    def draw(self, num):
        x = np.linspace(-2 * np.pi, 2 * np.pi, 200, endpoint=True)
        sin = np.sin(x ** self.a)
        plt.plot(x, sin, color='blue', linewidth=1.5)
        plt.xlim(-2 * np.pi * 1.1, 2 * np.pi * 1.1)
        plt.ylim(sin.min() * 1.1, sin.max() * 1.1)
        plt.xticks(
            [-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
            [r'-$2\pi$', r'-$3\pi/2$', r'-$\pi$', r'-$\pi/2$', r'$\pi/2$', r'$\pi$', r'-$3\pi/2$', r'$2\pi$']
        )
        plt.yticks([-3, -2, -1, 1, 2, 3])
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


class Q100:
    # bio graph 1
    def __init__(self):
        self.level4 = rd.choice(["tiger", "lion", "bear"])
        self.level3 = ["wolf", "leopard", "fox", "cheetah", "hyena", "coyote"]
        self.l31 = rd.choice(self.level3)
        self.level3.remove(self.l31)
        self.l32 = rd.choice(self.level3)
        self.level3.remove(self.l32)
        self.l33 = rd.choice(self.level3)
        self.level2 = ["sheep", "goat", "moose", "deer", "cattle", "camel"]
        self.l21 = rd.choice(self.level2)
        self.level2.remove(self.l21)
        self.l22 = rd.choice(self.level2)
        self.level2.remove(self.l22)
        self.l23 = rd.choice(self.level2)
        self.level1 = rd.choice(["grass"])
        self.query = f"Using the food web above, what would happen to the other organisms if the number " \
                     f"of {self.level4} were decreased? choice: (A) {self.l31} will increase " \
                     f"(B) {self.l32} will decrease (C) {self.l22} will increase (D) Nothing happen"
        self.answer = "A"
        self.answer_type = "multiple choice"
        self.subject = "scientific figure"
        self.level = "high school"

    def draw(self, num):
        plt.xlim(-4 * 1.1, 4 * 1.1)
        plt.ylim(-4 * 1.1, 4 * 1.1)

        plt.xticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        plt.yticks([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])
        ax = plt.gca()
        ax.spines['top'].set_color("none")
        ax.spines['right'].set_color("none")
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.text(-1, 8, self.level4, fontsize=22)
        plt.text(-1, 3, self.l31, fontsize=22)
        plt.text(-1, -3, self.l21, fontsize=22)
        plt.text(-6, 3, self.l32, fontsize=22)
        plt.text(-6, -3, self.l22, fontsize=22)
        plt.text(4, 3, self.l33, fontsize=22)
        plt.text(4, -3, self.l23, fontsize=22)
        plt.text(-1, -8, self.level1, fontsize=22)
        ax.annotate('', xy=(0, -3), xytext=(0, -7), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        ax.annotate('', xy=(-5, -3), xytext=(0, -7), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        ax.annotate('', xy=(5, -3), xytext=(0, -7), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        ax.annotate('', xy=(0, 3), xytext=(0, -2), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        ax.annotate('', xy=(-5, 3), xytext=(-5, -2), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        ax.annotate('', xy=(5, 3), xytext=(5, -2), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        ax.annotate('', xy=(0, 7.5), xytext=(0, 4), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        ax.annotate('', xy=(0, 7.5), xytext=(-5, 4), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        ax.annotate('', xy=(0, 7.5), xytext=(5, 4), arrowprops=dict(arrowstyle="->", color='black', linewidth=2))
        plt.axis("off")
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        plt.savefig(dest_image_path, bbox_inches='tight')
        plt.close()



