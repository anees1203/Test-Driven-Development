import pytest
from sparse_recommender import SparseMatrix

def test_set():
    matrix = SparseMatrix()
    matrix.set(20, 23, 54)
    assert matrix.get(20, 23) == 54

def test_get():
    matrix = SparseMatrix()
    matrix.set(20, 23, 54)
    assert matrix.get(20, 23) == 54

def test_recommend():
    matrix = SparseMatrix()
    matrix.set(0, 0, 12)
    matrix.set(1, 1, 23)
    matrix.set(2, 2, 34)
    vector = [45, 56, 67]
    recommendations = matrix.recommend(vector)
    expected_recommendations = [12 * vector[0] + 0 * vector[1] + 0 * vector[2],
                                0 * vector[0] + 23 * vector[1] + 0 * vector[2],
                                0 * vector[0] + 0 * vector[1] + 34 * vector[2]]
    assert recommendations == expected_recommendations

def test_add_movie():
    matrix_1 = SparseMatrix()
    matrix_1.set(0, 0, 7)
    matrix_1.set(1, 1, 8)
    matrix_2 = SparseMatrix()
    matrix_2.set(0, 0, 9)
    matrix_2.set(1, 1, 10)
    matrix_1.add_movie(matrix_2)
    assert matrix_1.get(0, 0) == 16 
    assert matrix_1.get(1, 1) == 18  
    assert matrix_1.get(2, 2) == 0   

def test_to_dense():
    matrix = SparseMatrix()
    matrix.set(0, 0, 5)
    matrix.set(1, 1, 6)
    matrix.set(2, 2, 7)
    dense_matrix = matrix.to_dense()
    expected_dense_matrix = [[5, 0, 0], [0, 6, 0], [0, 0, 7]]
    assert dense_matrix == expected_dense_matrix


def test_set_row_col_negeativevalue():
    matrix = SparseMatrix()
    with pytest.raises(ValueError):
        matrix.set(-1, 0, 34)

def test_get_row_col_negeativevalue():
    matrix = SparseMatrix()
    with pytest.raises(ValueError):
        matrix.get(-1, 0)

def test_set_value_negativevalue():
    matrix = SparseMatrix()
    with pytest.raises(ValueError):
        matrix.set(0, 0, -34)

def test_recommend_dimension_errorcheck():
    matrix = SparseMatrix()
    matrix.set(0, 0, 11)
    matrix.set(1, 1, 21)
    matrix.set(2, 2, 31)
    vector = [66, 75] 
    with pytest.raises(ValueError):
        matrix.recommend(vector)

def test_add_movie_dimension_errorcheck():
    matrix_1 = SparseMatrix()
    matrix_1.set(0, 0, 32)
    matrix_1.set(1, 1, 16)
    matrix_2 = SparseMatrix()
    matrix_2.set(0, 0, 11)
    matrix_2.set(1, 1, 15)
    matrix_2.set(2, 2, 19) 
    with pytest.raises(ValueError):
        matrix_1.add_movie(matrix_2)


