import numpy as np
class HashMixin:
    def __hash__(self):
        # Преобразуем матрицу в плоский список элементов для упрощения вычислений
        flat_matrix = [item for sublist in self.matrix for item in sublist]
        # Вычисляем хеш, комбинируя количество строк и столбцов с суммой элементов матрицы
        # В этом примере мы просто складываем хеши всех интересующих нас значений
        return hash(self.rows) + hash(self.cols) + hash(sum(flat_matrix))

class Matrix(HashMixin):
    cache = {}
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
        # Создаём ключ для кэша на основе хешей текущей и второй матрицы
        cache_key = (hash(self), hash(other))
        # Проверяем, есть ли уже результат в кэше
        if cache_key in Matrix.cache:
            return Matrix.cache[cache_key]
        result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
        # Проходим по каждой строке первой матрицы
        for i in range(self.rows):
            # Проходим по каждому столбцу второй матрицы
            for j in range(other.cols):
                # Вычисляем элемент результирующей матрицы
                for k in range(self.cols):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        # Сохраняем результат в кэш перед возвратом
        Matrix.cache[cache_key] = Matrix(result)
        return Matrix(result)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

def save_matrix_to_file(matrix, filename):
    """Сохранение матрицы в файл."""
    with open(filename, "w") as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

np.random.seed(0)
# mat_A_data = np.random.randint(0, 10, (10, 10)).tolist()
# mat_B_data = np.random.randint(0, 10, (10, 10)).tolist()
# mat_C_data = np.random.randint(0, 10, (10, 10)).tolist()
# mat_A = Matrix(mat_A_data)
# mat_B = Matrix(mat_B_data)
# mat_C = Matrix(mat_C_data)
A = Matrix([[10, 3, 1], [1, 4, 6]])
C = Matrix([[5, 5, 1], [1, 2, 4], [2, 1, 3]])
B = Matrix([[7, 5, 2], [4, 2, 71], [42, 4, 58]])
D = Matrix([[7, 5, 2], [4, 2, 71], [42, 4, 58]])

AB = A @ B
CD = C @ D

print(AB.matrix)
print(CD.matrix)
hash_ABCD = f'AB = {A.__hash__()}\nCD = {C.__hash__()}'
print(hash_ABCD)

save_matrix_to_file(A.matrix, "artifacts/3.3/A.txt")
save_matrix_to_file(B.matrix, "artifacts/3.3/B.txt")
save_matrix_to_file(C.matrix, "artifacts/3.3/C.txt")
save_matrix_to_file(D.matrix, "artifacts/3.3/D.txt")
save_matrix_to_file(AB.matrix, "artifacts/3.3/AB.txt")
save_matrix_to_file(CD.matrix, "artifacts/3.3/CD.txt")

# Сохранение хешей матриц AB и CD
with open("artifacts/3.3/hash.txt", "w") as file:
    file.write(f"AB = {hash(AB)}\nCD = {hash(CD)}")