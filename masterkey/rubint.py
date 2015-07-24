from . import open_class

open_class(int)

def times(self, func):
    for x in range(0, self):
        func(x)

def downto(self, limit, func):
    for x in reversed(range(limit, self)):
        func(x)

def upto(self, limit, func):
    for x in range(self, limit):
        func(x)

int.times = times
int.downto = downto
int.upto = upto
