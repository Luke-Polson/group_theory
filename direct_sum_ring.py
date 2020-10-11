class DirectSumRing:

    def __init__(self, ring_list):
        self.rings = ring_list
        self.additive_ops = [ring.addition for ring in ring_list]
        self.mult_ops = [ring.mult for ring in ring_list]

    def add(self, operand1, operand2):
        res = []
        for i in range(len(operand1)):
            res.append(self.additive_ops[i](operand1[i], operand2[i]))
        return res

    def multiply(self, operand1, operand2):
        res = []
        for i in range(len(operand1)):
            res.append(self.mult_ops[i](operand1[i], operand2[i]))
        return res