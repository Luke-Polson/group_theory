class Ring:

    def __init__(self, group, operation):
        self.elements = group.elements
        self.group = group
        self.mult = operation

        # initialise value to be set up later
        self.is_unital = None
        self.unity = None
        self.units = None

        self.is_field = None

        self.zero_divisors = None
        self.is_integral_domain = None

    def add(self, op1, op2):
        """
        return the sum of op1 and op2, using the group operation
        """
        return self.group.evaluate(op1, op2)

    def multiply(self, op1, op2):
        """
        return the product of op1 and op2, using the ring multiplication
        """
        return self.mult(op1, op2)

    def zero(self):
        """
        return the zero element, i.e the additive identity
        """
        return self.group.identity()

    def get_unity(self):
        """
        find the multiplicative identity (if it exists) and return it
        """
        id = self.group.identity()
        for op1 in self.elements:
            found = True
            if op1 == id:
                continue
            for op2 in self.elements:
                if self.multiply(op1, op2) != op2 or self.multiply(op2, op1) != op2:
                    found = False
                    break
            if found:
                self.unity = op1
                self.is_unital = True
                return op1

        self.is_unital = False
        return None

    def get_units(self):
        """
        find the elements that have a multiplicative inverse, and return them
        """
        if self.unity is None:
            self.get_unity()
        if self.unity is None:
            return None

        unit_list = []

        for op1 in self.elements:
            for op2 in self.elements:
                if self.multiply(op1, op2) == self.unity:
                    unit_list.append(op1)

        self.units = unit_list
        return unit_list

    def field(self):
        """
        return True if the ring is a field. i.e every nonzero element is a unit, otherwise False
        """
        if self.is_field is not None:
            return self.is_field

        if self.units is None:
            self.get_units()

        return len(self.units) == len(self.elements) - 1

    def get_zero_divisors(self):
        """
        find the zero-divisors of the ring, and return them.
        a nonzero ring element a is a zero-divisor if there exists some nonzero element x such that ax = 0
        """
        zero_divisors = []
        for op1 in self.elements:
            for op2 in self.elements:
                if ((self.multiply(op1, op2) == self.zero() or self.multiply(op2, op1) == self.zero())
                        and (op1 != self.zero() and op2 != self.zero())):
                    if op1 not in zero_divisors:
                        zero_divisors.append(op1)

        self.zero_divisors = zero_divisors
        return zero_divisors

    def integral_domain(self):
        """
        return True if the ring is an integral domain, that is, it contains no zero-divisors. otherwise return False.
        """
        if self.zero_divisors is None:
            self.get_zero_divisors()
        return len(self.zero_divisors) == 0






