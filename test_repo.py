from astropy.io import ascii
import numpy as np


def test_square_table():
    """ Test square of x column"""
    data = ascii.read('data.txt')
    source = data['x']**2
    truth = np.array([1, 2, 3, 4, 5])**2
    assert np.testing.assert_array_equal(source, truth)