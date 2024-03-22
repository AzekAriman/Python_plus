# -*- coding: utf-8 -*-
import numpy as np

class MatrixOperationsMixin:
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Операция сложения возможна только между матрицами")
        return Matrix(self.matrix + other.matrix)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            # Покомпонентное умножение на скаляр
            return Matrix(self.matrix * other.matrix)
        else:
            raise ValueError(
                "Покомпонентное умножение возможно только со скаляром, используйте '@' для матричного умножения.")

    def __matmul__(self, other):
        if isinstance(other, Matrix):
            # Матричное умножение
            return Matrix(self.matrix @ other.matrix)
        else:
            raise ValueError("Матричное умножение возможно только между матрицами.")

class MatrixFileMixin:
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for row in self.matrix:
                f.write(' '.join(map(str, row)) + '\n')

class Matrix(MatrixOperationsMixin, MatrixFileMixin):
    def __init__(self, matrix):
        self.matrix = matrix  # Используется setter
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        if not isinstance(value, np.ndarray):
            value = np.array(value)
        self._matrix = value
        self.rows = len(value)
        self.cols = len(value[0]) if self.rows > 0 else 0

# Генерация и использование матриц
np.random.seed(0)
mat1 = Matrix(np.random.randint(0, 10, (10, 10)))
mat2 = Matrix(np.random.randint(0, 10, (10, 10)))

# Арифметические операции
add_result = mat1 + mat2
mul_result = mat1 * mat2
matmul_result = mat1 @ mat2

# Сохранение результатов
add_result.save_to_file('artifacts/3.2/matrix_add.txt')
mul_result.save_to_file('artifacts/3.2/matrix_mul.txt')
matmul_result.save_to_file('artifacts/3.2/matrix_matmul.txt')


