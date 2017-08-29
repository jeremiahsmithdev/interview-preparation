#2x^3 + 1x^2 + 5x^1 + 3x^0

class Exponent:
    def __init__(self, a, b):
        self.coefficient = a
        self.exponent = b

def calculate_derivative(A):
    for i in range(len(A)):
        if A[i].exponent == 0:
            A.remove(A[i])
        else:
            A[i].coefficient = A[i].coefficient * A[i].exponent
            A[i].exponent = A[i].exponent - 1
    return A

A = [Exponent(2,3), Exponent(1,2), Exponent(5,1), Exponent(3,0)]
A_der = calculate_derivative(A)

for i in range(len(A_der)):
    print(A_der[i].coefficient, A_der[i].exponent)