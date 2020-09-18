class Group:

    def __init__(self, elements, operation):
        """
        :param elements: a list of the elements of the group
        :param operation: a lambda function representing the group operation

        """
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
        """
        takes two operands from the group, and returns their result after applying the
        group operation. if it is the case that one or more of the elements is not in the group, or the
        resulting value is not in the group, and error is raised.
        """

        if operand1 not in self.elements or operand2 not in self.elements:
            raise ValueError("One or both elements not a member of the group.")

        result = self.operation(operand1, operand2)
        if result not in self.elements:
            raise ValueError("Result not in group - operation is not closed.")

        return result

    def identity(self):
        """
        find and update the identity element, that is the element e such that eg = g = ge for all g in the group.
        :return: the identity element of the group.
        """
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
        """
        finds and returns the inverse of operand.
        :param operand: the element in the group which we want to find the inverse of.
        :return: the inverse element of the group.
        """
        if self.id is None:
            self.identity()

        for element in self.elements:
            if self.operation(operand, element) == self.id:
                return element

        raise ValueError("{} has no inverse - not a group.".format(operand))

    def cyclic(self):
        """
        tests whether the current group is cyclic. That is, it contains an element whose order is equal to that
        of the group.
        :return: True or False, based on whether or not group is Cyclic.
        """
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
        """
        find and return the order of operand. that is, the smallest n such that op^n = e.
        :param operand: the group element whose order we want to find.
        :return: the order of the given group element.
        """
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
        """
        fill the order_dict dictionary. it will contain each element as the key, and its order as the value.
        """
        for element in self.elements:
            self.order_of_element(element)

    def generate_subgroup(self, generator):
        """
        generates a cyclic subgroup using the given generator element.
        :param generator: the element to be used to generate the group.
        :return: the new group.
        """
        if self.id is None:
            self.identity()

        subgroup_elements = [generator]
        temp = generator

        while temp != self.id:
            temp = self.operation(temp, generator)
            subgroup_elements.append(temp)
        return Group(subgroup_elements, self.operation)

    def __pow__(self, operand, n):
        """
        returns operand^n
        :param operand: element to take the power of.
        :param n: the power which we want to raise operand to.
        :return: the resulting group element.
        """
        temp = operand
        for i in range(n-1):
            temp = self.operation(temp, operand)
        return temp


