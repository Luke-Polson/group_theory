import math


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


class DirectSum:

    def __init__(self, group_list):
        self.groups = group_list

        prod = 1
        for group in self.groups:
            prod *= group.order
        self.order = prod

        self.operations = [group.operation for group in group_list]

    def order_of_element(self, element):
        if len(element) == 1:
            return self.groups[-1].order_of_element(element[0])
        else:
            return lcm(self.groups[0].order_of_element(element[0]),
                       self.order_of_element(element[1:]))

    def evaluate(self, operand1, operand2):
        res = []
        for i in range(len(operand1)):
            res.append(self.groups[i].evaluate(operand1[i], operand2[i]))
        return res

    
