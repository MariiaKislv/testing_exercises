from functions.level_2.two_square_equation import solve_square_equation

def test__solve_square_equation__real_roots():
    square_coefficient = 1
    linear_coefficient = -3
    const_coefficient = 2

    actual_result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert actual_result == (1.0, 2.0)

def test__solve_square_equation__one_real_root():

    square_coefficient = 1
    linear_coefficient = -2
    const_coefficient = 1

    actual_result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert actual_result == (1.0, 1.0)
def test__solve_square_equation__complex_roots():
    square_coefficient = 2
    linear_coefficient = 1
    const_coefficient = 2

    actual_result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert actual_result == (None, None)

def test__solve_square_equation__no_square_coefficient():

    square_coefficient = 0
    linear_coefficient = 2
    const_coefficient = 3

    actual_result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
    assert actual_result == (-1.5, None)

def test__solve_square_equation__no_linear_coefficient():

    square_coefficient = 2
    linear_coefficient = 0
    const_coefficient = -8

    actual_result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert actual_result == (-2.0, 2.0)

def test__solve_square_equation__no_coefficients():

    square_coefficient = 0
    linear_coefficient = 0
    const_coefficient = 0

    actual_result = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert actual_result == (None, None)
