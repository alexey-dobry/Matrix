class MatrixNotSquareError(Exception):
    pass

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
            return obj.find_2_det(obj)
        else:
            return obj.find_n_det(obj)

    @staticmethod
    def find_2_det(obj):
        return obj.matrix['11'] * obj.matrix['22'] - obj.matrix['12'] * obj.matrix['21']

    @staticmethod
    def find_n_det(obj):
        __value_of_det = 0
        for coefficient_pozition in range(1,obj.stroka + 1):
            new_matrix_values = []
            stroki_new_det = ''.join([str(x) for x in range(1,obj.stroka + 1) if x != coefficient_pozition])
            stolbs_new_det = ''.join([str(x) for x in range(2,obj.stroka + 1)])
            for i in stroki_new_det:
                for j in stolbs_new_det:
                    new_matrix_values.append(obj.matrix[str(i) + str(j)])
            Minor = Determinant(Matrix(new_matrix_values,obj.stroka - 1,obj.stroka - 1))
            Delta_det = (-1)**(coefficient_pozition + 1)*obj.matrix[str(coefficient_pozition) + '1']* Minor.find_det
            __value_of_det += Delta_det
        return __value_of_det

    @staticmethod
    def check_for_square(m,n):
        if m != n: raise MatrixNotSquareError

