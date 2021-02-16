from astropy.io import ascii
import numpy as np


def test_square_table():
    """ Test square of x column"""
    data = ascii.read('data.txt')
    source = data['x'].data**2
    truth = np.array([1, 2, 3, 4, 5])**2

    comparison = source == truth
    equal_arrays = comparison.all()

    assert equal_arrays

test_square_table()