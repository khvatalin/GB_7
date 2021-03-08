class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrica = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matrica[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrica]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrica]))

my_matrix = Matrix([[10, 12, 89],
                    [2, 17, 34],
                    [41, 23, 11]],
                   [[69, 1, 3],
                    [1, 74, 52],
                    [56, 23, 6]])

print(my_matrix.__add__())
