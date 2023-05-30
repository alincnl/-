class Item:
    def __init__(self, count=3, max_count=16):
        self._count = count
        self._max_count = 16
        
    def update_count(self, val):
        if val <= self._max_count:
            self._count = val
            return True
        else:
            return False

#1,2
    def __add__(self,val):
        if self._count + val <= self._max_count and self._count + val >= 0:
            self._count += val
            return True
        return False
    def __sub__(self,val):
        if self._count - val <= self._max_count and self._count - val >= 0:
            self._count -= val
            return True
        return False
    def __mul__(self,val):
        if self._count * val <= self._max_count and self._count * val >= 0:
            self._count *= val
            return True
        return False
    def __div__(self,val):
        if self._count / val <= self._max_count and self._count / val >= 0:
            self._count /= val
            return True
        return False

    def __gt__(self,val):
        if self._count > val:
            return True
        return False
    def __lt__(self,val):
        if self._count < val:
            return True
        return False
    def __gte__(self,val):
        if self._count >= val:
            return True
        return False
    def __lte__(self,val):
        if self._count <= val:
            return True
        return False

    @property
    def count(self):
        return self._count

class Fruit(Item):
    def __init__(self, ripe=True, **kwargs):
        super().__init__(**kwargs)
        self._ripe = ripe


class Food(Item):
    def __init__(self, saturation, **kwargs):
        super().__init__(**kwargs)
        self._saturation = saturation
        
    @property
    def eatable(self):
        return self._saturation > 0

#3
class Peach(Fruit, Food):
    def __init__(self, ripe, count=1, max_count=32, color='pink', saturation=7):
        super().__init__(saturation=saturation, ripe=ripe, count=count, max_count=max_count)
        self._color = color
    
    @property
    def color(self):
        return self._color
        
    @property
    def eatable(self):
        return super().eatable and self._ripe
    
    def __add__(self, num):
        return self.count + num
    
    def __mul__(self, num):
        return self.count * num
    
    def __lt__(self, num):
        return self.count < num
    
    def __len__(self):
        return self.count

class Mango(Fruit, Food):
    def __init__(self, ripe, count=1, max_count=32, color='yellow', saturation=15):
        super().__init__(saturation=saturation, ripe=ripe, count=count, max_count=max_count)
        self._color = color
    
    @property
    def color(self):
        return self._color
        
    @property
    def eatable(self):
        return super().eatable and self._ripe
    
    def __add__(self, num):
        return self.count + num
    
    def __mul__(self, num):
        return self.count * num
    
    def __lt__(self, num):
        return self.count < num
    
    def __len__(self):
        return self.count

class Halva(Food):
    def __init__(self, count=1, max_count=32, color='gray', saturation=100):
        super().__init__(saturation=saturation, count=count, max_count=max_count)
        self._color = color
    
    @property
    def color(self):
        return self._color
    
    def __add__(self, num):
        return self.count + num
    
    def __mul__(self, num):
        return self.count * num
    
    def __lt__(self, num):
        return self.count < num
    
    def __len__(self):
        return self.count

class Cucumber(Food):
    def __init__(self, count=1, max_count=32, color='green', saturation=5):
        super().__init__(saturation=saturation, count=count, max_count=max_count)
        self._color = color
    
    @property
    def color(self):
        return self._color
    
    def __add__(self, num):
        return self.count + num
    
    def __mul__(self, num):
        return self.count * num
    
    def __lt__(self, num):
        return self.count < num
    
    def __len__(self):
        return self.count

#4
class Inventory:
    def __init__(self, len): 
        self._len = len
        self._list = [None] * len

    def get_cell(self, index):
        return self._list[index]

    def add(self, Food, index):
        if eatable(Food) and index < len and index >= 0:
            self._list[index] = Food;

    def reduce(self, index):
        if self._len < index or index < 0:
            return False
        elif self._len - index == 0:
            del(self)
        else:
            self._len -= index
            return True
    def __del__(self):
        print('Delete')

#5
class Queue:
    def __init__(self):
        self.__items = []

    def push_back(self, item):
        self.__items.insert(len(self.__items),item)

    def pop_front(self):
        return self.__items.pop(0)

    def __items__(self):
        xs = self.__items
        return xs.copy()
