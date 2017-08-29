from numpy import zeros
def print_matrix(a):
    for i in range(len(a)):
        print('\t'.join(map(str,a[i])))

def transpose(a):

#transpose and then reverse each row
def rotate_matrix(a):
    new_a = transpose(a)

#assuming square
#space complexity n^2
def rotate_matrix(a):
    new_a = zeros((len(a),len(a))).astype(int)
    for i in range(len(a)):
        for j in range(len(a)):
            new_a[j][len(a) - i - 1] = a[i][j]
    return new_a

a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

print_matrix(a)
a_rot = rotate_matrix(a)
print_matrix(a_rot)