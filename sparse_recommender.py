class SparseMatrix:
    def __init__(self):
        self.data = {}

    #Set Function
    def set(self, row, col, value):
        if(row < 0 or col < 0 or value < 0):
            raise ValueError("Row and columns must be positive.")
        if (row, col) in self.data:
            self.data[(row, col)] = value
        else:
            self.data[(row, col)] = value
       
    #Get Function
    def get(self, row, col):
        if(row < 0 or col < 0):
            raise ValueError("Row and columns must be positive.")
        if (row, col) in self.data:
            return self.data[(row, col)]
        else:
            return 0

    #Recommend Function
    def recommend(self, vector):
        num_rows = 0
        num_cols = 0

        for row, col in self.data.keys():
            num_rows = max(num_rows, row)
            num_cols = max(num_cols, col)
        num_rows += 1
        num_cols += 1

        if (num_cols != len(vector)):
            raise ValueError("The multiplication of matrix and vector dimensions is not possible.")
        # Initializing list to recommendations.
        recommendations = [0] * num_rows
        # Multiplying matrix with the vector and getting recommendations.
        for (row, col), value in self.data.items():
            recommendations[row] += value * vector[col]
        return recommendations


    #add_movie Function
    def add_movie(self, matrix):
        if len(matrix.data) != len(self.data):
            raise ValueError("Addition cannot be performed on matrix dimensions.")
        
        # Looping through each element in the new matrix.
        for (row, col), value in matrix.data.items():
            # Checking if the element already exists.
            if (row, col) in self.data:
                # If it exists, add the new value to the existing value.
                self.data[(row, col)] += value
            else:
                # else, set the new value.
                self.data[(row, col)] = value

    #to_dense Function
    def to_dense(self):
        # Find the dimensions of the dense matrix and initialize it with zeros.
        num_rows = 0
        num_cols = 0

        # Looping through elements in self.data.
        for row, col in self.data.keys():
            num_rows = max(num_rows, row)
            num_cols = max(num_cols, col)

        # Increment by 1 to account for zero.
        num_rows += 1
        num_cols += 1

        if not self.data:
            return []

        # Creating a dense matrix filled with zeros.
        dense_matrix = []
        for _ in range(num_rows):
            row = [0] * num_cols
            dense_matrix.append(row)

        # Filling in the values from the sparse matrix.
        for (row, col), value in self.data.items():
            dense_matrix[row][col] = value
        return dense_matrix