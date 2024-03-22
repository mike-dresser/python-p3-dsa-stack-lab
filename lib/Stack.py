class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return True if len(self.items) == 0 else False

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            # raise RuntimeError('The stack is full!')
            pass

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        return self.items[len(self.items) - 1] if len(self.items) != 0 else None
    
    def size(self):
        return len(self.items)

    def full(self):
        return True if len(self.items) >= self.limit else False


    def search(self, target):
        for index, element in enumerate(self.items):
            print(f'index: {index}, element: {element}')
            if element == target:
                return (len(self.items) - 1) - index
        return -1