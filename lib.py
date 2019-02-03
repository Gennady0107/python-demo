def cashback(monthly_expenses):
    """
    >>> cashback(10_000)
    300.0
    """
    percent = 3
    result = percent * monthly_expenses / 100
    return result


def mass_index(weight, height):
    """
    >>> mass_index(106, 1.68) # doctest: +ELLIPSIS
    37.55...
    """
    result_imt = weight / (height * height)
    return result_imt
