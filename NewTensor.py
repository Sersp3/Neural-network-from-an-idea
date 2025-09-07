import random
class Tensor(list):
    def __init__(self,*args,**kwargs):
        super(Tensor, self).__init__(*args,**kwargs)
        if isinstance(self, list):
            if isinstance(self[0], list):
                for i in range(len(self)):
                    self[i] = Tensor(self[i])
    def float(self):
        if isinstance(self, Tensor):
            for i in range(len(self)):
                if isinstance(self[i], Tensor):
                    self[i] = self[i].float()
                else:
                    self[i] = float(self[i])
        return self
    def __add__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return Tensor([self[i] + other[i] for i in range(len(self))])
        elif other.__class__.__name__ == 'int'or other.__class__.__name__ == 'float':
            return Tensor([self[i] + other for i in range(len(self))])
    def __sub__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return Tensor([self[i] - other[i] for i in range(len(self))])
        elif other.__class__.__name__ == 'int'or other.__class__.__name__ == 'float':
            return Tensor([self[i] - other for i in range(len(self))])
    def __mul__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return Tensor([self[i] * other[i] for i in range(len(self))])
        elif other.__class__.__name__ == 'int'or other.__class__.__name__ == 'float':
            return Tensor([self[i] * other for i in range(len(self))])
    def __neg__(self):
        return Tensor([-self[i] for i in range(len(self))])
    def __round__(self, n=None):
        if n is None:
            return self
        return Tensor([round(self[i],n) for i in range(len(self))])
    def __truediv__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return Tensor([self[i] / other[i] for i in range(len(self))])
        elif other.__class__.__name__ == 'int'or other.__class__.__name__ == 'float':
            return Tensor([self[i] / other for i in range(len(self))])
    def __floordiv__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return Tensor([self[i] // other[i] for i in range(len(self))])
        elif other.__class__.__name__ == 'int'or other.__class__.__name__ == 'float':
            return Tensor([self[i] // other for i in range(len(self))])
    def __radd__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return Tensor([self[i] + other[i] for i in range(len(self))])
        elif other.__class__.__name__ == 'int'or other.__class__.__name__ == 'float':
            return Tensor([self[i] + other for i in range(len(self))])
    def __rsub__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return Tensor([self[i] - other[i] for i in range(len(self))])
        elif other.__class__.__name__ == 'int'or other.__class__.__name__ == 'float':
            return Tensor([self[i] - other for i in range(len(self))])
    def __rmul__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return Tensor([self[i] * other[i] for i in range(len(self))])
        elif other.__class__.__name__ == 'int'or other.__class__.__name__ == 'float':
            return Tensor([self[i] * other for i in range(len(self))])
    def __rtruediv__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return Tensor([self[i] / other[i] for i in range(len(self))])
        elif other.__class__.__name__ == 'int'or other.__class__.__name__ == 'float':
            return Tensor([self[i] / other for i in range(len(self))])
    def __rfloordiv__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return Tensor([self[i] // other[i] for i in range(len(self))])
        elif other.__class__.__name__ == 'int'or other.__class__.__name__ == 'float':
            return Tensor([self[i] // other for i in range(len(self))])
    def shape(self):
        shape = []
        if isinstance(self, list):
            shape.append(len(self))
            if self[0].__class__.__name__ == 'Tensor':
                shape = shape+self[0].shape()
        return shape
    def transpose(self):
        result = zeros([self.shape()[1],self.shape()[0]])
        for i in range(len(self)):
            for j in range(len(self[0])):
                result[j][i] = self[i][j]
        return result
def matmul(A,B):
    result = zeros([A.shape()[0],B.shape()[1]])
    for i in range(A.shape()[0]):
        for j in range(B.shape()[1]):
            for k in range(A.shape()[1]):
                result[i][j] += A[i][k] * B[k][j]
    return result
def ones(shape):
    if isinstance(shape, int):
        return Tensor([1 for i in range(shape)])
    if len(shape) == 0:
        return 1
    return Tensor([ones(shape[1:]) for i in range(shape[0])])
def zeros(shape):
    if isinstance(shape, int):
        return Tensor([0 for i in range(shape)])
    if len(shape) == 0:
        return 0
    return Tensor([zeros(shape[1:]) for i in range(shape[0])])
def rand_tensor(shape,seed=None):
    random.seed(seed)
    if isinstance(shape, int):
        return Tensor([random.random() for i in range(shape)])
    if len(shape) == 0:
        return random.random()
    return Tensor([rand_tensor(shape[1:]) for i in range(shape[0])])