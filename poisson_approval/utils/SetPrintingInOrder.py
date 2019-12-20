class SetPrintingInOrder(set):
    """
    A set that prints in order.

        >>> s = SetPrintingInOrder({'b', 'a', 'c'})
        >>> print(s)
        {a, b, c}
        >>> print(repr(s))
        {'a', 'b', 'c'}
    """

    def __repr__(self):
        return "{" + ", ".join([
             "%r" % element for element in sorted(self)
        ]) + "}"

    def __str__(self):
        return "{" + ", ".join([
             "%s" % element for element in sorted(self)
        ]) + "}"

    def _repr_pretty_(self, p, cycle):
        # https://stackoverflow.com/questions/41453624/tell-ipython-to-use-an-objects-str-instead-of-repr-for-output
        p.text(str(self) if not cycle else '...')