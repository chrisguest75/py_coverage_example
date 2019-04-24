

class binary_search_tree():
    def __init__(self, initial_value=None):
        self.left = None
        self.right = None
        self.value = initial_value

    def __len__(self):
        return self.num_nodes()

    def num_nodes(self):
        if self.value is None:
            return 0
        else:
            count = 1
            if self.left is not None:
                count += self.left.num_nodes()
            if self.right is not None:
                count += self.right.num_nodes()

        return count

    def contains(self, value):
        if self.value == value:
            return True
        else:
            if value < self.value:
                if self.left is not None:
                    return self.left.contains(value)
                else:
                    return False
            else:
                if self.right is not None:
                    return self.right.contains(value)
                else:
                    return False

    def add(self, value):
        if self.value is None:
            self.value = value
            return self

        node = binary_search_tree(value)

        if value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.add(value)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.add(value)

        return self
