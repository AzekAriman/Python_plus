import numpy as np

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __add__(self, other):
        if self.cols != other.cols or self.rows != other.rows:
            raise ValueError('матрицы некорректной размерности')
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def __mul__(self, other):
        if self.cols != other.cols or self.rows != other.rows:
            raise ValueError('матрицы некорректной размерности')
        return Matrix([[self.matrix[i][j] * other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Матрицы неподходящих размеров для матричного умножения")
        result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        # Проходим по каждой строке первой матрицы
        for i in range(self.rows):
            # Проходим по каждому столбцу второй матрицы
            for j in range(other.cols):
                # Вычисляем элемент результирующей матрицы
                for k in range(self.cols):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(result)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

np.random.seed(0)
mat_A_data = np.random.randint(0, 10, (10, 10)).tolist()
mat_B_data = np.random.randint(0, 10, (10, 10)).tolist()
mat_A = Matrix(mat_A_data)
mat_B = Matrix(mat_B_data)

add_result = mat_A + mat_B
mul_result = mat_A * mat_B
matmul_result = mat_A @ mat_B

# Запись результатов в текстовые файлы
with open('artifacts/3.1/matrix+.txt', 'w') as f:
    f.write(str(add_result))

with open('artifacts/3.1/matrix_mul.txt', 'w') as f:
    f.write(str(mul_result))

with open('artifacts/3.1/matrix@.txt', 'w') as f:
    f.write(str(matmul_result))
