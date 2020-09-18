class Group:

    def __init__(self, elements, operation):
        self.elements = elements
        self.operation = operation
        self.order = len(elements)

        # identity placeholder
        self.id = None

        # placeholder value. to be updated when is_cyclic() is first called.
        self.is_cyclic = None

        # initialise empty dict to store order of elements
        # will be filled as the order_of_element() function is called
        self.order_dict = {}

    def evaluate(self, operand1, operand2):
        """ takes two operands from the group, and returns their result after applying the
        group operation. if it is the case that one or more of the elements is not in the group, or the
        resulting value is not in the group, and error is raised."""

        if operand1 not in self.elements or operand2 not in self.elements:
            raise ValueError("One or both elements not a member of the group.")

        result = self.operation(operand1, operand2)
        if result not in self.elements:
            raise ValueError("Result not in group - operation is not closed.")

        return result

    def identity(self):

        if self.id is not None:
            return self.id

        for op1 in self.elements:
            for op2 in self.elements:
                if not self.evaluate(op1, op2):
                    break
            # if loop didn't break, we've found our identity
            self.id = op1
            return op1

        raise ValueError("Identity does not exist - not a group.")

    def inverse(self, operand):

        if self.id is None:
            self.identity()

        for element in self.elements:
            if self.operation(operand, element) == self.id:
                return element

        raise ValueError("{} has no inverse - not a group.".format(operand))

    def cyclic(self):

        if self.is_cyclic is not None:
            return self.is_cyclic

        else:
            for element in self.elements:
                if self.order_of_element(element) == self.order:
                    self.is_cyclic = True
                    return True

        self.is_cyclic = False
        return False

    def conjugate(self, x, g):
        """ returns the conjugate of x by g, i.e gxg^-1 """

        return self.operation(g, self.operation(x, self.inverse(g)))

    def order_of_element(self, operand):

        if operand in self.order_dict:
            return self.order_dict[operand]

        if self.id is None:
            self.identity()

        order = 1
        temp = operand
        while temp != self.id:
            temp = self.operation(temp, operand)
            order += 1

        self.order_dict[operand] = order

        return order

    def fill_order_dict(self):
        for element in self.elements:
            self.order_of_element(element)

    def generate_subgroup(self, generator):
        if self.id is None:
            self.identity()

        subgroup_elements = [generator]
        temp = generator

        while temp != self.id:
            temp = self.operation(temp, generator)
            subgroup_elements.append(temp)
        return Group(subgroup_elements, self.operation)

    def __pow__(self, operand, n):
        temp = operand
        for i in range(n-1):
            temp = self.operation(temp, operand)
        return temp





Z = Group([0,1,2,3,4,5], lambda x,y: (x+y)%6)

print(Z.evaluate(2, 3))
print(Z.evaluate(1, 3))
print(Z.identity())
print(Z.order_of_element(3))
Z.fill_order_dict()

print(Z.order_dict)

print(Z.conjugate(2, 3))

print(Z.cyclic())