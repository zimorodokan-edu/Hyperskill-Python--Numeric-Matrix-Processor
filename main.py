import copy


def det(mtx):
    amount_of_rows = len(mtx)
    amount_of_columns = len(mtx[0])
    if amount_of_rows == amount_of_columns and amount_of_rows > 0:
        size = len(mtx)
        if size == 1:
            return mtx[0][0]
        elif size == 2:
            return mtx[0][0] * mtx[1][1] - mtx[0][1] * mtx[1][0]
        elif size == 3:
            return (mtx[0][0] * mtx[1][1] * mtx[2][2] +
                    mtx[1][0] * mtx[2][1] * mtx[0][2] +
                    mtx[0][1] * mtx[1][2] * mtx[2][0] -
                    mtx[2][0] * mtx[1][1] * mtx[0][2] -
                    mtx[0][1] * mtx[1][0] * mtx[2][2] -
                    mtx[1][2] * mtx[2][1] * mtx[0][0])
        elif size > 3:
            determinant = 0
            for n in range(size):
                new_mtx = copy.deepcopy(mtx)
                new_mtx = new_mtx[1:]
                for i in new_mtx:
                    del i[n:n + 1]
                determinant += mtx[0][n] * (-1) ** ((n + 2) % 2) * det(new_mtx)
            return determinant
    return False


def matrix_transpose_main(mtx):
    amount_of_rows = len(mtx)
    amount_of_columns = len(mtx[0])
    if amount_of_rows > 0 and amount_of_columns > 0:
        return [[mtx[row][col] for row in range(amount_of_rows)] for col in range(amount_of_columns)]
    return False


def matrix_cofactor(mtx):
    amount_of_rows = len(mtx)
    amount_of_columns = len(mtx[0])
    if amount_of_rows == amount_of_columns and amount_of_rows > 1:
        mtx_cofactor = [['' for r in range(amount_of_rows)]
                        for c in range(amount_of_columns)]
        for row in range(amount_of_rows):
            for col in range(amount_of_columns):
                submatrix = copy.deepcopy(mtx)
                del submatrix[row:row + 1]
                for r in submatrix:
                    del r[col:col + 1]
                mtx_cofactor[row][col] = det(submatrix) * (-1) ** (row + col)
        return mtx_cofactor
    return False


def inverse_matrix(mtx):
    amount_of_rows = len(mtx)
    amount_of_columns = len(mtx[0])
    if amount_of_rows == amount_of_columns and amount_of_rows > 1:
        mtx_determinant = det(mtx)
        if mtx_determinant != 0:
            mtx_inverse = [['' for r in range(amount_of_rows)]
                           for c in range(amount_of_columns)]
            mtx_cofactor = matrix_cofactor(mtx)
            mtx_adjugate = matrix_transpose_main(mtx_cofactor)
            for row in range(amount_of_rows):
                for col in range(amount_of_columns):
                    mtx_inverse[row][col] = round(
                        mtx_adjugate[row][col] / mtx_determinant, 4)
            for r in mtx_inverse:
                for c in r:
                    print(f'{c:>10}', end='', )
                print('')
        else:
            print('This matrix doesn\'t have an inverse.')


while True:
    print("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    choice = input('Your choice: ')

    if choice == '1':
        r1, c1 = [int(i)
                  for i in input('Enter size of first matrix: ').split()]
        print('Enter first matrix:')
        m1 = []
        for r in range(r1):
            m1.append([float(i) for i in input().split()])
        r2, c2 = [int(i)
                  for i in input('Enter size of second matrix: ').split()]
        print('Enter second matrix:')
        m2 = []
        for r in range(r2):
            m2.append([float(i) for i in input().split()])
        if r1 != r2 and c1 != c2:
            print('ERROR')
        else:
            print('The result is:')
            for r in range(r1):
                mr = []
                for c in range(c1):
                    mr.append(m1[r][c] + m2[r][c])
                print(*mr)

    elif choice == '2':
        r1, c1 = [int(i) for i in input('Enter size of matrix: ').split()]
        print('Enter matrix:')
        m1 = []
        for r in range(r1):
            m1.append([float(i) for i in input().split()])
        mp = float(input('Enter constant: '))
        print('The result is:')
        for r in range(r1):
            for c in range(c1):
                m1[r][c] *= mp
            print(*m1[r])

    elif choice == '3':
        r1, c1 = [int(i)
                  for i in input('Enter size of first matrix: ').split()]
        print('Enter first matrix:')
        m1 = []
        for r in range(r1):
            m1.append([float(i) for i in input().split()])
        r2, c2 = [int(i)
                  for i in input('Enter size of second matrix: ').split()]
        print('Enter second matrix:')
        m2 = []
        for r in range(r2):
            m2.append([float(i) for i in input().split()])
        if c1 != r2:
            print('ERROR')
        else:
            print('The result is:')
            for r in range(r1):
                mr = []
                for c_ in range(c2):
                    value = 0
                    for c in range(c1):
                        value += m1[r][c] * m2[c][c_]
                    mr.append(value)
                print(*mr)

    elif choice == '4':
        print('')
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        sub_choice = input('Your choice: ')
        r1, c1 = [int(i) for i in input('Enter matrix size: ').split()]
        print('Enter matrix:')
        m1 = []
        for r in range(r1):
            m1.append([float(i) for i in input().split()])
        if sub_choice == '1':
            # m2 = [['' for c in range(r1)] for r in range(c1)]
            # for r in range(r1):
            #     for c in range(c1):
            #         m2[c][r] = m1[r][c]
            m2 = [[m1[r][c] for r in range(r1)] for c in range(c1)]
        elif sub_choice == '2':
            # m2 = [['' for c in range(r1)] for r in range(c1)]
            # for r in range(r1):
            #     for c in range(c1):
            #         m2[c1 - c - 1][r1 - r - 1] = m1[r][c]
            m2 = [[m1[r][c] for r in range(r1 - 1, -1, -1)]
                  for c in range(c1 - 1, -1, -1)]
        elif sub_choice == '3':
            # m2 = [['' for c in range(c1)] for r in range(r1)]
            # for r in range(r1):
            #     for c in range(c1):
            #         m2[r][c1 - c - 1] = m1[r][c]
            m2 = [reversed(r) for r in m1]
        elif sub_choice == '4':
            # m2 = [['' for c in range(c1)] for r in range(r1)]
            # for r in range(r1):
            #     for c in range(c1):
            #         m2[r1 - r - 1][c] = m1[r][c]
            m2 = reversed(m1)
        print('The result is:')
        for r in m2:
            print(*r)

    elif choice == '5':
        r1, c1 = [int(i) for i in input('Enter matrix size: ').split()]
        print('Enter matrix:')
        m1 = []
        for r in range(r1):
            m1.append([float(i) for i in input().split()])
        print('The result is:')
        print(det(m1))

    elif choice == '6':
        rows, columns = [int(i) for i in input('Enter matrix size: ').split()]
        print('Enter matrix:')
        m = []
        for r in range(rows):
            m.append([float(i) for i in input().split()])
        inverse_matrix(m)

    elif choice == '0':
        exit()
