class ProductIterator:
    def __init__(self, category_obj):
        self.category = category_obj
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.list_product) - 1:
            self.index += 1
            return self.category.list_product[self.index]
        else:
            raise StopIteration
