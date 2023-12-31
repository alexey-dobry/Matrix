class MatrixNotSquareError(Exception):
    pass

class MatrixSizeDifferentError(Exception):
    pass

class Matrix:
    def __init__(self,values,m,n):
        self.stroka = m
        self.stolb = n
        self.matrix = self.create_matrix(values,m,n)

    @staticmethod
    def create_matrix(values, m, n):
        _matrix = dict()
        if len(values) != 1:
            i = 0
            for stroka in range(1, m + 1):
                for stolb in range(1, n + 1):
                    _matrix[str(stroka) + str(stolb)] = values[i]
                    i += 1
        else:
            _matrix['11'] = values[0]
        return _matrix

    def __add__(self,obj):
        if obj.stroka != self.stroka or obj.stolb != self.stolb:
            raise MatrixSizeDifferentError

        else:
            __values = list()
            for stroka in range(1,self.stroka + 1):
                for stolb in range(1,self.stolb + 1):
                    new_value = self.matrix[str(stroka) + str(stolb)] + obj.matrix[str(stroka) + str(stolb)]
                    __values.append(new_value)

            return Matrix(tuple(__values),self.stroka,self.stolb)

    def __str__(self):
        print_result = list()
        for stroka in range(1,self.stroka + 1):
            for stolb in range(1,self.stolb + 1):
                print_result.append(str(self.matrix[str(stroka) + str(stolb)])+'\t')
                if stolb == self.stolb:
                    print_result.append('\n')
        return ''.join(print_result)


    def __sub__(self,obj):
        if obj.stroka != self.stroka or obj.stolb != self.stolb:
            raise MatrixSizeDifferentError

        else:
            __values = list()
            for stroka in range(1, self.stroka + 1):
                for stolb in range(1, self.stolb + 1):
                    new_value = self.matrix[str(stroka) + str(stolb)] - obj.matrix[str(stroka) + str(stolb)]
                    __values.append(new_value)

            return Matrix(tuple(__values), self.stroka, self.stolb)

    def __mul__(self,obj):
        __values = list()
        summa = 0
        if self.stolb == obj.stroka:
            for i in range(1,self.stroka+1):
                for j in range(1, obj.stolb+1):
                    for k in range(1, self.stolb + 1):
                        index1 = str(i) + str(k)
                        index2 = str(k) + str(j)
                        summa = summa + self.matrix[index1] * obj.matrix[index2]
                    __values.append(summa)
                    summa = 0

        return Matrix(tuple(__values),self.stroka,obj.stolb)

class Determinant:
    def __init__(self,obj):
        self.matrix = obj.matrix
        self.stroka = obj.stroka
        self.stolb = obj.stolb
        self.check_for_square(self.stroka,self.stolb)

    @property
    def find_det(obj):
        if obj.stroka == 1:
            return obj.matrix['11']
        elif obj.stroka == 2:
            return obj.det_2(obj)
        else:
            return obj.det_n(obj)

    @staticmethod
    def det_2(obj):
        return obj.matrix['11'] * obj.matrix['22'] - obj.matrix['12'] * obj.matrix['21']

    @staticmethod
    def det_n(obj):
        __value_of_det = 0
        for coefficient_position in range(1,obj.stroka + 1):
            Minor = obj.find_Minor(obj,coefficient_position)
            Algebraic_complement = (-1)**(coefficient_position + 1)*Minor.find_det
            Coefficent = obj.matrix[str(coefficient_position) + '1']
            __value_of_det += Coefficent*Algebraic_complement
        return __value_of_det

    @staticmethod
    def find_Minor(obj,coefficient_position):
        new_matrix_values = []
        stroki_new_det = ''.join([str(x) for x in range(1, obj.stroka + 1) if x != coefficient_position])
        stolbs_new_det = ''.join([str(x) for x in range(2, obj.stroka + 1)])
        for i in stroki_new_det:
            for j in stolbs_new_det:
                new_matrix_values.append(obj.matrix[str(i) + str(j)])
        return Determinant(Matrix(new_matrix_values,obj.stroka - 1,obj.stroka - 1))
    @staticmethod
    def check_for_square(m,n):
        if m != n: raise MatrixNotSquareError

A = Matrix((5,2,0,10,3,5,2,5,20,0,0,0),3,4)

B = Matrix((1.2,0.5,2.8,0.4,5,1,2,1.5),4,2)

C = A * B

print(C)



