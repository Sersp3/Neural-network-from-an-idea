class Tensor(list):
    def __init__(self,*args,**kwargs):
        super(Tensor, self).__init__(*args,**kwargs)
        if isinstance(self, list):
            if isinstance(self[0], list):
                for i in range(len(self)):
                    self[i] = Tensor(self[i])
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
def ones(shape):
    if isinstance(shape, int):
        return Tensor([1 for i in range(shape)])
    if len(shape) == 0:
        return 1
    return Tensor([ones(shape[1:]) for i in range(shape[0])])