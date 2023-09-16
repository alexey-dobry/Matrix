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

