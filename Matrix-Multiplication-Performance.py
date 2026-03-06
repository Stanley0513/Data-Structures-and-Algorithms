import numpy as np
import time

class MatrixMultiplier:
    def __init__(self):
        self.mat1 = None
        self.mat2 = None
        self.result = None

    def readMat(self, file1, file2):
        # Read matrices from files
        self.mat1 = self._read_matrix(file1)
        self.mat2 = self._read_matrix(file2)

    def _read_matrix(self, file):
        with open(file, 'r') as f:
            lines = f.readlines()
            matrix = [list(map(float, line.strip().split(','))) for line in lines]
        return matrix

    def MatMul(self):
        # Check if matrices can be multiplied
        if len(self.mat1[0]) != len(self.mat2):
            print("Error: Matrices cannot be multiplied.")
            return

        # Convert matrices to numpy arrays for faster multiplication
        np_mat1 = np.array(self.mat1)
        np_mat2 = np.array(self.mat2)

        # Multiply matrices using numpy
        start_time_np = time.time()
        np_result = np_mat1.dot(np_mat2)
        end_time_np = time.time()
        np_elapsed_time = end_time_np - start_time_np

        # Multiply matrices using nested loops (List)
        start_time_list = time.time()
        result_rows = len(self.mat1)
        result_cols = len(self.mat2[0])
        list_result = [[0 for _ in range(result_cols)] for _ in range(result_rows)]
        for i in range(result_rows):
            for j in range(result_cols):
                for k in range(len(self.mat2)):
                    list_result[i][j] += self.mat1[i][k] * self.mat2[k][j]
        end_time_list = time.time()
        list_elapsed_time = end_time_list - start_time_list

        # Set self.result after successful calculation
        self.result = np_result

        # print results
        print("Matrices multiplied successfully.")
        print(self.result)
        print("NumPy Elapsed Time: {:.6f} seconds".format(np_elapsed_time))
        print("List Elapsed Time: {:.6f} seconds".format(list_elapsed_time))

    def dumpMat(self, output_file):
        # Check if result is available
        if self.result is not None:
            # Dump result matrix to a file
            with open(output_file, 'w') as f:
                for row in self.result:
                    f.write(','.join(map(str, row)) + '\n')
                print("Saved successfully")
        else:
            print("Error: No result to dump.")

matrix_multiplier = MatrixMultiplier()
path1 = input("Enter the path for matrix 1: ").strip('"').strip()
path2 = input("Enter the path for matrix 2: ").strip('"').strip()
matrix_multiplier.readMat(path1, path2)
matrix_multiplier.MatMul()
path3 = input("Enter the path for saving：").strip('"').strip()
matrix_multiplier.dumpMat(path3)
