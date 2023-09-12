class MatrixSizeDifferentError(Exception):
    pass

class Matrix:
    def __init__(self,values,m,n):
        self.stroka = m
        self.stolb = n
        self.matrix = self.create_matrix(values,m,n)

    @staticmethod
    def create_matrix(values,m,n):
        _matrix = dict()
        i = 0
        for stroka in range(1,m + 1):
            for stolb in range(1,n + 1):
                _matrix[str(stroka) + str(stolb)] = values[i]
                i += 1
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