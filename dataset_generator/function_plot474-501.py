import math
import os
import shutil
from IPython.lib.latextools import latex_to_png
import random as rd
from PIL import Image, ImageDraw, ImageFont
from matplotlib.patches import *


# Include matrix computations

class Q474:
    def __init__(self):
        self.A = np.array([[rd.randint(-100, 100) / 10 for _ in range(3)] for _ in range(3)])
        self.det_A = np.linalg.det(self.A)
        self.query = "Matrix A is given in the image. What is the determinant of the matrix A?"
        self.answer = self.det_A
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        equation1 = r"""
                                       \begin{equation*}
                                       A=
                                       \begin{bmatrix}
                                       """
        matrix1 = fr"""\
                                       {self.A[0][0]} & {self.A[0][1]} & {self.A[0][2]} \\
                                       {self.A[1][0]} & {self.A[1][1]} & {self.A[1][2]} \\
                                       {self.A[2][0]} & {self.A[2][1]} & {self.A[2][2]}
                                       """
        end = r"""
                                       \end{bmatrix}
                                       \end{equation*}
                                       """
        equation = equation1 + matrix1 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q475:
    def __init__(self):
        self.A = np.array([[rd.randint(-5, 5), rd.randint(-5, 5)], [rd.randint(-5, 5), rd.randint(-5, 5)]])
        self.B = np.array([[rd.randint(-5, 5), rd.randint(-5, 5)], [rd.randint(-5, 5), rd.randint(-5, 5)]])
        self.product_A_B = np.dot(self.A, self.B)
        self.det_product_A_B = np.linalg.det(self.product_A_B)
        self.query = "Matrix A and B are given in the image. What is the determinant of the matrix (A * B)?"
        self.answer = self.det_product_A_B
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        # LaTeX equation
        equation1 = r"""
                \begin{equation*}
                A=
                \begin{bmatrix}
                """
        matrix1 = fr"""\
                {self.A[0][0]} & {self.A[0][1]} \\
                {self.A[1][0]} & {self.A[1][1]} 
                """
        equation2 = r"""
                \end{bmatrix}
                \quad
                B=
                \begin{bmatrix}
                """
        matrix2 = fr"""\
                        {self.B[0][0]} & {self.B[0][1]} \\
                        {self.B[1][0]} & {self.B[1][1]} 
                        """
        end = r"""
                \end{bmatrix}
                \end{equation*}
                """
        equation = equation1 + matrix1 + equation2 + matrix2 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q476:
    def __init__(self):
        self.A = np.array([[rd.randint(-100, 100) / 10 for _ in range(3)] for _ in range(3)])
        self.element_sum_A = np.sum(self.A)
        self.query = "Matrix A is given in the image. What is the sum of all elements in the matrix A?"
        self.answer = self.element_sum_A
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        equation1 = r"""
                               \begin{equation*}
                               A=
                               \begin{bmatrix}
                               """
        matrix1 = fr"""\
                               {self.A[0][0]} & {self.A[0][1]} & {self.A[0][2]} \\
                               {self.A[1][0]} & {self.A[1][1]} & {self.A[1][2]} \\
                               {self.A[2][0]} & {self.A[2][1]} & {self.A[2][2]}
                               """
        end = r"""
                               \end{bmatrix}
                               \end{equation*}
                               """
        equation = equation1 + matrix1 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q477:
    def __init__(self):
        self.A = np.array([[rd.randint(-100, 100) / 10 for _ in range(4)] for _ in range(4)])
        self.element_sum_A = np.sum(self.A)
        self.query = "Matrix A is given in the image. What is the sum of all elements in the matrix A?"
        self.answer = self.element_sum_A
        self.answer_type = "int"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        equation1 = r"""
                                       \begin{equation*}
                                       A=
                                       \begin{bmatrix}
                                       """
        matrix1 = fr"""\
                                       {self.A[0][0]} & {self.A[0][1]} & {self.A[0][2]} & {self.A[0][3]} \\
                                       {self.A[1][0]} & {self.A[1][1]} & {self.A[1][2]} & {self.A[1][3]} \\
                                       {self.A[2][0]} & {self.A[2][1]} & {self.A[2][2]} & {self.A[2][3]} \\
                                       {self.A[3][0]} & {self.A[3][1]} & {self.A[3][2]} & {self.A[3][3]}
                                       """
        end = r"""
                                       \end{bmatrix}
                                       \end{equation*}
                                       """
        equation = equation1 + matrix1 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q478:
    def __init__(self):
        self.A = np.array([[rd.randint(1, 5), rd.randint(1, 5)], [rd.randint(1, 5), rd.randint(1, 5)]])
        self.B = np.array([[rd.randint(1, 5), rd.randint(1, 5)], [rd.randint(1, 5), rd.randint(1, 5)]])
        self.C = np.array([[rd.randint(1, 5), rd.randint(1, 5)], [rd.randint(1, 5), rd.randint(1, 5)]])
        self.sum_A_B_C = np.add(np.add(self.A, self.B), self.C)
        self.element_sum_A_B_C = np.sum(self.sum_A_B_C)
        self.query = "Matrices A, B, and C are given in the image. What is the sum of all elements in the matrix (A + B + C)?"
        self.answer = self.element_sum_A_B_C
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        # LaTeX equation
        equation1 = r"""
                       \begin{equation*}
                       A=
                       \begin{bmatrix}
                       """
        matrix1 = fr"""\
                       {self.A[0][0]} & {self.A[0][1]} \\
                       {self.A[1][0]} & {self.A[1][1]} 
                       """
        equation2 = r"""
                       \end{bmatrix}
                       \quad
                       B=
                       \begin{bmatrix}
                       """
        matrix2 = fr"""\
                               {self.B[0][0]} & {self.B[0][1]} \\
                               {self.B[1][0]} & {self.B[1][1]} 
                               """
        equation3 = r"""
                               \end{bmatrix}
                               \quad
                               C=
                               \begin{bmatrix}
                               """
        matrix3 = fr"""\
                                       {self.C[0][0]} & {self.C[0][1]} \\
                                       {self.C[1][0]} & {self.C[1][1]} 
                                       """
        end = r"""
                       \end{bmatrix}
                       \end{equation*}
                       """
        equation = equation1 + matrix1 + equation2 + matrix2 + equation3 + matrix3 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q479:
    def __init__(self):
        self.A = np.array([[rd.randint(-100, 100) / 10 for _ in range(3)] for _ in range(3)])
        self.frobenius_norm_A = np.linalg.norm(self.A, 'fro')
        self.query = "Matrix A is given in the image. What is the Frobenius norm of the matrix A?"
        self.answer = self.frobenius_norm_A
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        equation1 = r"""
                                       \begin{equation*}
                                       A=
                                       \begin{bmatrix}
                                       """
        matrix1 = fr"""\
                                       {self.A[0][0]} & {self.A[0][1]} & {self.A[0][2]} \\
                                       {self.A[1][0]} & {self.A[1][1]} & {self.A[1][2]} \\
                                       {self.A[2][0]} & {self.A[2][1]} & {self.A[2][2]}
                                       """
        end = r"""
                                       \end{bmatrix}
                                       \end{equation*}
                                       """
        equation = equation1 + matrix1 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q480:
    def __init__(self):
        self.A = np.array([[rd.randint(-100, 100) / 10 for _ in range(3)] for _ in range(3)])
        self.trace_A = np.trace(self.A)
        self.query = "Matrix A is given in the image. What is the trace of the matrix A?"
        self.answer = self.trace_A
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        equation1 = r"""
                                       \begin{equation*}
                                       A=
                                       \begin{bmatrix}
                                       """
        matrix1 = fr"""\
                                       {self.A[0][0]} & {self.A[0][1]} & {self.A[0][2]} \\
                                       {self.A[1][0]} & {self.A[1][1]} & {self.A[1][2]} \\
                                       {self.A[2][0]} & {self.A[2][1]} & {self.A[2][2]}
                                       """
        end = r"""
                                       \end{bmatrix}
                                       \end{equation*}
                                       """
        equation = equation1 + matrix1 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q481:
    def __init__(self):
        self.A = np.array([[rd.randint(100, 500)/100, rd.randint(100, 500)/100],
                           [rd.randint(100, 500)/100, rd.randint(100, 500)/100]])
        self.trace_A = np.trace(self.A)
        self.query = "Matrix A is given in the image. What is the trace of the matrix A?"
        self.answer = self.trace_A
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        equation1 = r"""
                                               \begin{equation*}
                                               A=
                                               \begin{bmatrix}
                                               """
        matrix1 = fr"""\
                                               {self.A[0][0]} & {self.A[0][1]} \\
                                               {self.A[1][0]} & {self.A[1][1]} \\
                                               """
        end = r"""
                                               \end{bmatrix}
                                               \end{equation*}
                                               """
        equation = equation1 + matrix1 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q482:
    def __init__(self):
        self.A = np.array([[rd.randint(100, 500)/100 for _ in range(3)] for _ in range(3)])
        self.trace_A = np.trace(self.A)
        self.query = "Matrix A is given in the image. What is the trace of the matrix A?"
        self.answer = self.trace_A
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        equation1 = r"""
                                               \begin{equation*}
                                               A=
                                               \begin{bmatrix}
                                               """
        matrix1 = fr"""\
                                               {self.A[0][0]} & {self.A[0][1]} & {self.A[0][2]} \\
                                               {self.A[1][0]} & {self.A[1][1]} & {self.A[1][2]} \\
                                               {self.A[2][0]} & {self.A[2][1]} & {self.A[2][2]} \\
                                               
                                               """
        end = r"""
                                               \end{bmatrix}
                                               \end{equation*}
                                               """
        equation = equation1 + matrix1 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q483:
    def __init__(self):
        self.A = np.array([[rd.randint(100, 500)/100 for _ in range(4)] for _ in range(4)])
        self.trace_A = np.trace(self.A)
        self.query = "Matrix A is given in the image. What is the trace of the matrix A?"
        self.answer = self.trace_A
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        equation1 = r"""
                                               \begin{equation*}
                                               A=
                                               \begin{bmatrix}
                                               """
        matrix1 = fr"""\
                                               {self.A[0][0]} & {self.A[0][1]} & {self.A[0][2]} & {self.A[0][3]} \\
                                               {self.A[1][0]} & {self.A[1][1]} & {self.A[1][2]} & {self.A[1][3]} \\
                                               {self.A[2][0]} & {self.A[2][1]} & {self.A[2][2]} & {self.A[2][3]} \\
                                               {self.A[3][0]} & {self.A[3][1]} & {self.A[3][2]} & {self.A[3][3]}
                                               """
        end = r"""
                                               \end{bmatrix}
                                               \end{equation*}
                                               """
        equation = equation1 + matrix1 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q484:
    def __init__(self):
        self.A = np.array([[rd.randint(100, 500)/100 for _ in range(5)] for _ in range(5)])
        self.trace_A = np.trace(self.A)
        self.query = "Matrix A is given in the image. What is the trace of the matrix A?"
        self.answer = self.trace_A
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        equation1 = r"""
                                               \begin{equation*}
                                               A=
                                               \begin{bmatrix}
                                               """
        matrix1 = fr"""\
                                               {self.A[0][0]} & {self.A[0][1]} & {self.A[0][2]} & {self.A[0][3]} & {self.A[0][4]}\\
                                               {self.A[1][0]} & {self.A[1][1]} & {self.A[1][2]} & {self.A[1][3]} & {self.A[1][4]}\\
                                               {self.A[2][0]} & {self.A[2][1]} & {self.A[2][2]} & {self.A[2][3]} & {self.A[2][4]}\\
                                               {self.A[3][0]} & {self.A[3][1]} & {self.A[3][2]} & {self.A[3][3]} & {self.A[3][4]}\\
                                               {self.A[4][0]} & {self.A[4][1]} & {self.A[4][2]} & {self.A[4][3]} & {self.A[4][4]}
                                               """
        end = r"""
                                               \end{bmatrix}
                                               \end{equation*}
                                               """
        equation = equation1 + matrix1 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q485:
    def __init__(self):
        self.A = np.array([[rd.randint(-5, 5), rd.randint(-5, 5)], [rd.randint(-5, 5), rd.randint(-5, 5)]])
        self.B = np.array([[rd.randint(-5, 5), rd.randint(-5, 5)], [rd.randint(-5, 5), rd.randint(-5, 5)]])
        self.product_A_B = np.dot(self.A, self.B)
        self.trace_product_A_B = np.trace(self.product_A_B)
        self.query = "Matrix A and B are given in the image. What is the trace of the matrix (A * B)?"
        self.answer = self.trace_product_A_B
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        # LaTeX equation
        equation1 = r"""
                \begin{equation*}
                A=
                \begin{bmatrix}
                """
        matrix1 = fr"""\
                {self.A[0][0]} & {self.A[0][1]} \\
                {self.A[1][0]} & {self.A[1][1]} 
                """
        equation2 = r"""
                \end{bmatrix}
                \quad
                B=
                \begin{bmatrix}
                """
        matrix2 = fr"""\
                        {self.B[0][0]} & {self.B[0][1]} \\
                        {self.B[1][0]} & {self.B[1][1]} 
                        """
        end = r"""
                \end{bmatrix}
                \end{equation*}
                """
        equation = equation1 + matrix1 + equation2 + matrix2 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q486:
    def __init__(self):
        self.A = np.array([[rd.randint(-10, 10), rd.randint(-10, 10)], [rd.randint(-10, 10), rd.randint(-10, 10)]])
        self.B = np.array([[rd.randint(-10, 10), rd.randint(-10, 10)], [rd.randint(-10, 10), rd.randint(-10, 10)]])
        self.C = np.array([[rd.randint(-10, 10), rd.randint(-10, 10)], [rd.randint(-10, 10), rd.randint(-10, 10)]])
        self.product_A_B_C = np.dot(np.dot(self.A, self.B), self.C)
        self.trace_product_A_B_C = np.trace(self.product_A_B_C)
        self.query = "Matrices A, B, and C are given in the image. What is the trace of the matrix (A * B * C)?"
        self.answer = self.trace_product_A_B_C
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        equation1 = r"""
                               \begin{equation*}
                               A=
                               \begin{bmatrix}
                               """
        matrix1 = fr"""\
                               {self.A[0][0]} & {self.A[0][1]} \\
                               {self.A[1][0]} & {self.A[1][1]} 
                               """
        equation2 = r"""
                               \end{bmatrix}
                               \quad
                               B=
                               \begin{bmatrix}
                               """
        matrix2 = fr"""\
                                       {self.B[0][0]} & {self.B[0][1]} \\
                                       {self.B[1][0]} & {self.B[1][1]} 
                                       """
        equation3 = r"""
                                       \end{bmatrix}
                                       \quad
                                       C=
                                       \begin{bmatrix}
                                       """
        matrix3 = fr"""\
                                               {self.C[0][0]} & {self.C[0][1]} \\
                                               {self.C[1][0]} & {self.C[1][1]} 
                                               """
        end = r"""
                               \end{bmatrix}
                               \end{equation*}
                               """
        equation = equation1 + matrix1 + equation2 + matrix2 + equation3 + matrix3 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q487:
    def __init__(self):
        self.A = np.array([[rd.randint(-10, 10), rd.randint(-10, 10)], [rd.randint(-10, 10), rd.randint(-10, 10)]])
        self.B = np.array([[rd.randint(-10, 10), rd.randint(-10, 10)], [rd.randint(-10, 10), rd.randint(-10, 10)]])
        self.C = np.array([[rd.randint(-10, 10), rd.randint(-10, 10)], [rd.randint(-10, 10), rd.randint(-10, 10)]])
        self.sub_A_B_C = np.subtract(np.subtract(self.A, self.B), self.C)
        self.trace_sub_A_B_C = np.trace(self.sub_A_B_C)
        self.query = "Matrices A, B, and C are given in the image. What is the trace of the matrix (A - B - C)?"
        self.answer = self.trace_sub_A_B_C
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        equation1 = r"""
                               \begin{equation*}
                               A=
                               \begin{bmatrix}
                               """
        matrix1 = fr"""\
                               {self.A[0][0]} & {self.A[0][1]} \\
                               {self.A[1][0]} & {self.A[1][1]} 
                               """
        equation2 = r"""
                               \end{bmatrix}
                               \quad
                               B=
                               \begin{bmatrix}
                               """
        matrix2 = fr"""\
                                       {self.B[0][0]} & {self.B[0][1]} \\
                                       {self.B[1][0]} & {self.B[1][1]} 
                                       """
        equation3 = r"""
                                       \end{bmatrix}
                                       \quad
                                       C=
                                       \begin{bmatrix}
                                       """
        matrix3 = fr"""\
                                               {self.C[0][0]} & {self.C[0][1]} \\
                                               {self.C[1][0]} & {self.C[1][1]} 
                                               """
        end = r"""
                               \end{bmatrix}
                               \end{equation*}
                               """
        equation = equation1 + matrix1 + equation2 + matrix2 + equation3 + matrix3 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q488:
    def __init__(self):
        self.A = np.array([[rd.randint(-5, 5), rd.randint(-5, 5)], [rd.randint(-5, 5), rd.randint(-5, 5)]])
        self.B = np.array([[rd.randint(-5, 5), rd.randint(-5, 5)], [rd.randint(-5, 5), rd.randint(-5, 5)]])
        self.sum_A_B = np.add(self.A, self.B)
        self.trace_sum_A_B = np.trace(self.sum_A_B)
        self.query = "Matrix A and B are given in the image. What is the trace of the matrix (A + B)?"
        self.answer = self.trace_sum_A_B
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        # LaTeX equation
        equation1 = r"""
        \begin{equation*}
        A=
        \begin{bmatrix}
        """
        matrix1 = fr"""\
        {self.A[0][0]} & {self.A[0][1]} \\
        {self.A[1][0]} & {self.A[1][1]} 
        """
        equation2 = r"""
        \end{bmatrix}
        \quad
        B=
        \begin{bmatrix}
        """
        matrix2 = fr"""\
                {self.B[0][0]} & {self.B[0][1]} \\
                {self.B[1][0]} & {self.B[1][1]} 
                """
        end = r"""
        \end{bmatrix}
        \end{equation*}
        """
        equation = equation1 + matrix1 + equation2 + matrix2 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q489:
    def __init__(self):
        self.A = np.array([[rd.randint(-10, 10), rd.randint(-10, 10)], [rd.randint(-10, 10), rd.randint(-10, 10)]])
        self.B = np.array([[rd.randint(-10, 10), rd.randint(-10, 10)], [rd.randint(-10, 10), rd.randint(-10, 10)]])
        self.C = np.array([[rd.randint(-10, 10), rd.randint(-10, 10)], [rd.randint(-10, 10), rd.randint(-10, 10)]])
        self.sum_A_B_C = np.add(np.add(self.A, self.B), self.C)
        self.trace_sum_A_B_C = np.trace(self.sum_A_B_C)
        self.query = "Matrices A, B, and C are given in the image. What is the trace of the matrix (A + B + C)?"
        self.answer = self.trace_sum_A_B_C
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        equation1 = r"""
                               \begin{equation*}
                               A=
                               \begin{bmatrix}
                               """
        matrix1 = fr"""\
                               {self.A[0][0]} & {self.A[0][1]} \\
                               {self.A[1][0]} & {self.A[1][1]} 
                               """
        equation2 = r"""
                               \end{bmatrix}
                               \quad
                               B=
                               \begin{bmatrix}
                               """
        matrix2 = fr"""\
                                       {self.B[0][0]} & {self.B[0][1]} \\
                                       {self.B[1][0]} & {self.B[1][1]} 
                                       """
        equation3 = r"""
                                       \end{bmatrix}
                                       \quad
                                       C=
                                       \begin{bmatrix}
                                       """
        matrix3 = fr"""\
                                               {self.C[0][0]} & {self.C[0][1]} \\
                                               {self.C[1][0]} & {self.C[1][1]} 
                                               """
        end = r"""
                               \end{bmatrix}
                               \end{equation*}
                               """
        equation = equation1 + matrix1 + equation2 + matrix2 + equation3 + matrix3 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q490:
    def __init__(self):
        self.A = np.array([[rd.randint(-10, 10), rd.randint(-10, 10)], [rd.randint(-10, 10), rd.randint(-10, 10)]])
        self.B = np.array([[rd.randint(-10, 10), rd.randint(-10, 10)], [rd.randint(-10, 10), rd.randint(-10, 10)]])
        self.C = np.array([[rd.randint(-10, 10), rd.randint(-10, 10)], [rd.randint(-10, 10), rd.randint(-10, 10)]])
        self.sum_prod_A_B_C = np.dot(np.add(self.A, self.B), self.C)
        self.trace_sum_prod_A_B_C = np.trace(self.sum_prod_A_B_C)
        self.query = "Matrices A, B, and C are given in the image. What is the trace of the matrix ((A + B) * C)?"
        self.answer = self.trace_sum_prod_A_B_C
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        equation1 = r"""
                               \begin{equation*}
                               A=
                               \begin{bmatrix}
                               """
        matrix1 = fr"""\
                               {self.A[0][0]} & {self.A[0][1]} \\
                               {self.A[1][0]} & {self.A[1][1]} 
                               """
        equation2 = r"""
                               \end{bmatrix}
                               \quad
                               B=
                               \begin{bmatrix}
                               """
        matrix2 = fr"""\
                                       {self.B[0][0]} & {self.B[0][1]} \\
                                       {self.B[1][0]} & {self.B[1][1]} 
                                       """
        equation3 = r"""
                                       \end{bmatrix}
                                       \quad
                                       C=
                                       \begin{bmatrix}
                                       """
        matrix3 = fr"""\
                                               {self.C[0][0]} & {self.C[0][1]} \\
                                               {self.C[1][0]} & {self.C[1][1]} 
                                               """
        end = r"""
                               \end{bmatrix}
                               \end{equation*}
                               """
        equation = equation1 + matrix1 + equation2 + matrix2 + equation3 + matrix3 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q491:
    def __init__(self):
        self.A = np.array([[rd.randint(-10, 10), rd.randint(-10, 10)], [rd.randint(-10, 10), rd.randint(-10, 10)]])
        self.B = np.array([[rd.randint(-10, 10), rd.randint(-10, 10)], [rd.randint(-10, 10), rd.randint(-10, 10)]])
        self.C = np.array([[rd.randint(-10, 10), rd.randint(-10, 10)], [rd.randint(-10, 10), rd.randint(-10, 10)]])
        self.sum_sub_A_B_C = np.add(np.subtract(self.A, self.B), self.C)
        self.trace_sum_sub_A_B_C = np.trace(self.sum_sub_A_B_C)
        self.query = "Matrices A, B, and C are given in the image. What is the trace of the matrix (A - B + C)?"
        self.answer = self.trace_sum_sub_A_B_C
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "undergraduate"

    def draw(self, num):
        equation1 = r"""
                               \begin{equation*}
                               A=
                               \begin{bmatrix}
                               """
        matrix1 = fr"""\
                               {self.A[0][0]} & {self.A[0][1]} \\
                               {self.A[1][0]} & {self.A[1][1]} 
                               """
        equation2 = r"""
                               \end{bmatrix}
                               \quad
                               B=
                               \begin{bmatrix}
                               """
        matrix2 = fr"""\
                                       {self.B[0][0]} & {self.B[0][1]} \\
                                       {self.B[1][0]} & {self.B[1][1]} 
                                       """
        equation3 = r"""
                                       \end{bmatrix}
                                       \quad
                                       C=
                                       \begin{bmatrix}
                                       """
        matrix3 = fr"""\
                                               {self.C[0][0]} & {self.C[0][1]} \\
                                               {self.C[1][0]} & {self.C[1][1]} 
                                               """
        end = r"""
                               \end{bmatrix}
                               \end{equation*}
                               """
        equation = equation1 + matrix1 + equation2 + matrix2 + equation3 + matrix3 + end
        # The following function will directly render your LaTeX to a PNG.
        # Scale = 2.0 controls image size. Increase to make PNG larger.
        png_data = latex_to_png(equation, backend='dvipng', scale=2.0)

        # Save the PNG image to a file
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        with open(dest_image_path, 'wb') as file:
            file.write(png_data)


class Q492:
    def __init__(self):
        # Randomly choose values for x and y
        self.x = rd.randint(-10, 10)
        self.y = rd.randint(-10, 10)

        # Randomly generate coefficients for the first equation
        self.a1 = rd.randint(-10, 10)
        self.b1 = rd.randint(-10, 10)

        # Calculate the constant for the first equation
        self.c1 = self.a1 * self.x + self.b1 * self.y

        # Generate coefficients for the second equation ensuring they are not proportional to the first
        while True:
            self.a2 = rd.randint(-10, 10)
            self.b2 = rd.randint(-10, 10)
            if self.a1 * self.b2 != self.a2 * self.b1:  # Ensures the equations are not linearly dependent
                break

        # Calculate the constant for the second equation
        self.c2 = self.a2 * self.x + self.b2 * self.y

        self.query = "x and y are the solutions of the above equations. What is the sum of x and y?"
        self.answer = self.x + self.y
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        text_eq1 = f"{self.a1}x + {self.b1}y = {self.c1}"
        text_eq2 = f"{self.a2}x + {self.b2}y = {self.c2}"
        question_text = self.query

        text = text_eq1 + "\n" + text_eq2 + "\n\n"
        width = 400
        height = 200
        image = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except IOError:
            font = ImageFont.load_default()

        draw.text((20, 20), text, fill=(0, 0, 0), font=font)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        image.save(dest_image_path)


class Q493:
    def __init__(self):
        # Randomly choose values for x, y, and z
        self.x = rd.randint(-10, 10)
        self.y = rd.randint(-10, 10)
        self.z = rd.randint(-10, 10)

        # Randomly generate coefficients for the first equation
        self.A = np.random.randint(-10, 10, (3, 3))

        # Ensure the system has a unique solution by checking if the determinant is non-zero
        while np.linalg.det(self.A) == 0:
            self.A = np.random.randint(-10, 10, (3, 3))

        # Calculate the constants vector B based on the chosen x, y, and z
        self.B = self.A @ np.array([self.x, self.y, self.z])

        self.query = "x, y, and z are the solutions of the above equations. What is x*y*z?"
        self.answer = self.x * self.y * self.z
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        text_eq1 = f"{self.A[0, 0]}x + {self.A[0, 1]}y + {self.A[0, 2]}z = {self.B[0]}"
        text_eq2 = f"{self.A[1, 0]}x + {self.A[1, 1]}y + {self.A[1, 2]}z = {self.B[1]}"
        text_eq3 = f"{self.A[2, 0]}x + {self.A[2, 1]}y + {self.A[2, 2]}z = {self.B[2]}"
        question_text = self.query

        text = text_eq1 + "\n" + text_eq2 + "\n" + text_eq3 + "\n\n"
        width = 400
        height = 200
        image = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except IOError:
            font = ImageFont.load_default()

        draw.text((20, 20), text, fill=(0, 0, 0), font=font)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        image.save(dest_image_path)


class Q494:
    def __init__(self):
        # Randomly choose values for x, y, and z
        self.x = rd.randint(-10, 10)
        self.y = rd.randint(-10, 10)
        self.z = rd.randint(-10, 10)

        # Randomly generate coefficients for the first equation
        self.A = np.random.randint(-10, 10, (3, 3))

        # Ensure the system has a unique solution by checking if the determinant is non-zero
        while np.linalg.det(self.A) == 0:
            self.A = np.random.randint(-10, 10, (3, 3))

        # Calculate the constants vector B based on the chosen x, y, and z
        self.B = self.A @ np.array([self.x, self.y, self.z])

        self.query = "x, y, and z are the solutions of the above equations. What is x + y + z?"
        self.answer = self.x + self.y + self.z
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        text_eq1 = f"{self.A[0, 0]}x + {self.A[0, 1]}y + {self.A[0, 2]}z = {self.B[0]}"
        text_eq2 = f"{self.A[1, 0]}x + {self.A[1, 1]}y + {self.A[1, 2]}z = {self.B[1]}"
        text_eq3 = f"{self.A[2, 0]}x + {self.A[2, 1]}y + {self.A[2, 2]}z = {self.B[2]}"
        question_text = self.query

        text = text_eq1 + "\n" + text_eq2 + "\n" + text_eq3 + "\n\n"
        width = 400
        height = 200
        image = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except IOError:
            font = ImageFont.load_default()

        draw.text((20, 20), text, fill=(0, 0, 0), font=font)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        image.save(dest_image_path)


class Q495:
    def __init__(self):
        self.a = rd.randint(1, 10)
        self.b = rd.randint(1, 10)
        self.c = rd.randint(1, 10)
        self.eq1 = self.a + self.b
        self.eq2 = self.a - self.b
        self.eq3 = self.a * self.b + self.c
        self.eq4 = self.b + self.c
        self.query = "What is the value of a * b + c?"
        self.answer = self.eq3
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        text = f"a + b = {self.eq1}\na - b = {self.eq2}\na * b + c = ?\nb + c = {self.eq4}"
        width = 400
        height = 400
        image = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", 30)
        except IOError:
            font = ImageFont.load_default()

        x1, y1, x2, y2 = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = x2 - x1, y2 - y1
        x = (width - text_width) / 2
        y = (height - text_height) / 2
        draw.text((x, y), text, fill=(0, 0, 0), font=font)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        image.save(dest_image_path)


class Q496:
    def __init__(self):
        self.e = rd.randint(10, 20)
        self.f = rd.randint(1, 9)
        self.g = rd.randint(1, 5)
        self.h = rd.randint(1, 5)
        self.eq1 = self.e - self.f
        self.eq2 = self.g * self.h
        self.eq3 = (self.e - self.f) / self.g
        self.eq4 = self.e - self.f + self.g
        self.query = "What is the value of (e - f) / g?"
        self.answer = self.eq3
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        text = f"e - f = {self.eq1}\ng * h = {self.eq2}\n(e - f) / g = ?\ne - f + g = {self.eq4}"
        width = 400
        height = 400
        image = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", 30)
        except IOError:
            font = ImageFont.load_default()

        x1, y1, x2, y2 = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = x2 - x1, y2 - y1
        x = (width - text_width) / 2
        y = (height - text_height) / 2
        draw.text((x, y), text, fill=(0, 0, 0), font=font)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        image.save(dest_image_path)


class Q497:
    def __init__(self):
        self.i = rd.randint(1, 5)
        self.j = rd.randint(1, 5)
        self.k = rd.randint(1, 10)
        self.eq1 = self.i ** self.j
        self.eq2 = self.k * self.j
        self.eq3 = (self.i ** self.j) * self.k
        self.eq4 = (self.i ** self.j) + self.k
        self.query = "What is the value of (i ^ j) * k?"
        self.answer = self.eq3
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        text = f"i ^ j = {self.eq1}\nk * j = {self.eq2}\n(i ^ j) * k = ?\n(i ^ j) + k = {self.eq4}"
        width = 400
        height = 400
        image = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", 30)
        except IOError:
            font = ImageFont.load_default()

        x1, y1, x2, y2 = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = x2 - x1, y2 - y1
        x = (width - text_width) / 2
        y = (height - text_height) / 2
        draw.text((x, y), text, fill=(0, 0, 0), font=font)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        image.save(dest_image_path)


class Q498:
    def __init__(self):
        self.m = rd.randint(1, 10)
        self.n = rd.randint(1, 10)
        self.o = rd.randint(1, 10)
        self.eq1 = self.m + self.n * self.o
        self.eq2 = (self.m + self.n) / self.o
        self.eq3 = self.m * self.n - self.o
        self.eq4 = self.n * self.m + self.o
        self.query = "Given positive integers m, n, and o. From the system equation in the image. What is the value of m * n - o?"
        self.answer = self.eq3
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        text = f"m + n * o = {self.eq1}\n(m + n) / o = {self.eq2:.2f}\nm * n - o = ?\nn * m + o = {self.eq4}"
        width = 400
        height = 400
        image = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", 30)
        except IOError:
            font = ImageFont.load_default()

        x1, y1, x2, y2 = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = x2 - x1, y2 - y1
        x = (width - text_width) / 2
        y = (height - text_height) / 2
        draw.text((x, y), text, fill=(0, 0, 0), font=font)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        image.save(dest_image_path)


class Q499:
    def __init__(self):
        self.a = rd.randint(1, 10)
        self.b = rd.randint(1, 10)
        self.c = rd.randint(1, 10)
        self.eq1 = self.a + self.b
        self.eq2 = self.a - self.b
        self.eq3 = self.a ** 2 + self.c
        self.eq4 = self.b ** 2 + self.c
        self.query = "What is the value of a^2 + c?"
        self.answer = self.eq3
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        text = f"a + b = {self.eq1}\na - b = {self.eq2}\na^2 + c = ?\nb^2 + c = {self.eq4}"
        width = 400
        height = 400
        image = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", 30)
        except IOError:
            font = ImageFont.load_default()

        x1, y1, x2, y2 = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = x2 - x1, y2 - y1
        x = (width - text_width) / 2
        y = (height - text_height) / 2
        draw.text((x, y), text, fill=(0, 0, 0), font=font)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        image.save(dest_image_path)


class Q500:
    def __init__(self):
        self.a = rd.randint(1, 10)
        self.b = rd.randint(1, 10)
        self.c = rd.randint(1, 10)
        self.operations = ["+", "-", "*", "/"]
        if self.b != 1:
            self.omitted_op = rd.choice(self.operations)
        else:
            self.omitted_op = rd.choice(["+", "-"])
        # Generate equations with the omitted operation
        self.eq1 = round(self.create_equation(self.a, self.b, self.omitted_op), 3)

        self.query = f"Which operation is omitted in the equation as shown in the image? Choices: (A) + (B) - (C) * (D) /"
        if self.omitted_op == "+":
            self.answer = "A"
        elif self.omitted_op == "-":
            self.answer = "B"
        elif self.omitted_op == "*":
            self.answer = "C"
        elif self.omitted_op == "/":
            self.answer = "D"

        self.answer_type = "multiple choice"
        self.subject = "algebra"
        self.level = "elementary school"

    def create_equation(self, x, y, op, z=None):
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y + (z if z else 0)
        elif op == "/":
            return x / y
        else:
            return "?"

    def draw(self, num):
        text = f"{self.a} ? {self.b} = {self.eq1}"
        width = 400
        height = 400
        image = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", 60)
        except IOError:
            font = ImageFont.load_default()

        x1, y1, x2, y2 = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = x2 - x1, y2 - y1
        x = (width - text_width) / 2
        y = (height - text_height) / 2
        draw.text((x, y), text, fill=(0, 0, 0), font=font)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        image.save(dest_image_path)


class Q501:
    def __init__(self):
        self.a = rd.randint(1, 10)
        self.b = rd.randint(1, 10)
        self.c = rd.randint(1, 10)
        self.operations = ["+", "-", "*", "/"]
        if self.c != 1:
            self.omitted_op = rd.choice(self.operations)
        else:
            self.omitted_op = rd.choice(["+", "-"])

        # Generate equations with the omitted operation
        self.eq1 = round(self.create_equation(self.a, self.b, self.c, self.omitted_op), 3)

        self.query = f"Which operation is omitted in the equation as shown in the image? Choices: (A) + (B) - (C) * (D) /"
        if self.omitted_op == "+":
            self.answer = "A"
        elif self.omitted_op == "-":
            self.answer = "B"
        elif self.omitted_op == "*":
            self.answer = "C"
        elif self.omitted_op == "/":
            self.answer = "D"

        self.answer_type = "multiple choice"
        self.subject = "algebra"
        self.level = "elementary school"

    def create_equation(self, x, y, c, op, z=None):
        if op == "+":
            return x + y + c
        elif op == "-":
            return x + y - c
        elif op == "*":
            return x + y * c
        elif op == "/":
            return x + y / c
        else:
            return "?"

    def draw(self, num):
        text = f"{self.a} + {self.b} ? {self.c} = {self.eq1}"
        width = 600
        height = 400
        image = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", 60)
        except IOError:
            font = ImageFont.load_default()

        x1, y1, x2, y2 = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = x2 - x1, y2 - y1
        x = (width - text_width) / 2
        y = (height - text_height) / 2
        draw.text((x, y), text, fill=(0, 0, 0), font=font)
        destination_folder = os.path.join(os.path.dirname(os.getcwd()), "dataset")
        dest_image_path = os.path.join(destination_folder, f"image/image{num}.png")
        image.save(dest_image_path)


"""class QSystemOfEquations2x2:
    def __init__(self):
        # Randomly choose values for x and y
        self.x = rd.randint(-10, 10)
        self.y = rd.randint(-10, 10)

        # Randomly generate coefficients for the first equation
        self.a1 = rd.randint(-10, 10)
        self.b1 = rd.randint(-10, 10)

        # Calculate the constant for the first equation
        self.c1 = self.a1 * self.x + self.b1 * self.y

        # Generate coefficients for the second equation ensuring they are not proportional to the first
        while True:
            self.a2 = rd.randint(-10, 10)
            self.b2 = rd.randint(-10, 10)
            if self.a1 * self.b2 != self.a2 * self.b1:  # Ensures the equations are not linearly dependent
                break

        # Calculate the constant for the second equation
        self.c2 = self.a2 * self.x + self.b2 * self.y

        self.query = "x and y are the solutions of the above equations. What is the product of x and y?"
        self.answer = (self.x * self.y)
        self.answer_type = "float"
        self.subject = "algebra"
        self.level = "high school"

    def draw(self, num):
        text_eq1 = f"{self.a1}x + {self.b1}y = {self.c1}"
        text_eq2 = f"{self.a2}x + {self.b2}y = {self.c2}"
        question_text = self.query

        text = text_eq1 + "\n" + text_eq2 + "\n\n" + question_text
        width = 800
        height = 600
        image = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except IOError:
            font = ImageFont.load_default()

        draw.text((20, 20), text, fill=(0, 0, 0), font=font)
        image.save(f"image/image{num}.png")"""

