class BTNode:
    def __init__(self, value=None, parent=None):
        self.value = value
        self.LHS = None
        self.RHS = None
        self.parent = parent

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value
    
    def set_left(self, left):
        self.LHS = left

    def get_left(self):
        return self.LHS

    def set_right(self, right):
        self.RHS = right

    def get_right(self):
        return self.RHS
    
    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent