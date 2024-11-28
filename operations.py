class BinaryOp:
    def __init__(self,_first,_second):
        self._first=_first
        self._second=_second
    def addition(self):
        return self._first+self._second
    def subtraction(self):
        return self._first-self._second
    def multiplication(self):
        return self._first*self._second
    def division(self):
        return self._first/self._second
    def power(self):
        return self._first**self._second
    def max(self):
        return self._first if self._first>self._second else self._second
    def min(self):
        return self._first if self._first<self._second else self._second
    def avg(self):
        return (self._first+self._second)/2


