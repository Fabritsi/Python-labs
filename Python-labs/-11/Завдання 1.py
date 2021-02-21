class TArray:
    def __init__(self, array):
        self.array = array
        self.array_elem_count = len(array)+1

    def get_min(self):
        return min(self.array)

    def get_max(self):
        return max(self.array)

    def sort_a(self):
        self.array.sort()

    def get_sum(self):
        return sum(self.array)

    def __add__(self, other):
        return [self.array[i] + other.array[i] for i in range(len(self.array))]

    def __sub__(self, other):
        return [self.array[i] - other.array[i] for i in range(len(self.array))]

    def __mul__(self, other):
        return [el*other for el in self.array]
