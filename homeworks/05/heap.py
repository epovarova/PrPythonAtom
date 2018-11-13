import operator
from heapq import heappush as insert
class Heap():
    
    def __init__(self, array, is_max_heap, comparator):
        self.array = array[:]
        self.is_max_heap = is_max_heap
        self.comparator = comparator
        self._build_heap()
                        
    def add(self, elem_with_priority):
        self.array.insert(0,elem_with_priority)
        self._shift(0)
    
    def _build_heap(self):
        heap_size = len(self.array) 
        for i in range(0, heap_size//2  )[::-1]:
            self._shift(i)
   
    def _shift(self, i):
        left = 2 * i + 1
        right = 2 * i  + 2
        largest = i
        heap_size = len(self.array) - 1
        if left <= heap_size and  self.comparator(self.array[left], self.array[largest]):
            largest = left
        if right <= heap_size and  self.comparator(self.array[right], self.array[largest]):
            largest = right
        
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self._shift( largest)
        #return self
    
    def show_tree(self, total_width=33, fill=' '):
        # метод для поможет отлаживаться
        
        tree = self.array
        
        import math
        from io import StringIO
        output = StringIO()
        last_row = -1
        for i, n in enumerate(tree):
            if i:
                row = int(math.floor(math.log(i+1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2**row
            col_width = int(math.floor((total_width * 1.0) / columns))
            output.write(str(n).center(col_width, fill))
            last_row = row
        print (output.getvalue())
        print ('-' * total_width)
        print()
class MaxHeap(Heap):
    
    def __init__(self, array):
        super().__init__(array, True, operator.gt)
        
    def extract_maximum(self):
        max = self.array[0]
        if len (self.array)>1:
            self.array[0] = self.array.pop()
            self._shift(0)
        else:
            self.array.pop()
        return max    
    
class MinHeap(Heap):
    
    def __init__(self, array):
        super().__init__(array, False, operator.lt)
        
    def extract_minimum(self):
        min = self.array[0]
        if len (self.array)>1:
            self.array[0] = self.array.pop()
            self._shift(0)
        else:
            self.array.pop()
        return min