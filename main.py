from ctypes import CDLL, c_double, c_int
from pathlib import Path

# import shareable objects
shareable_lib = CDLL(Path('shareable.so').absolute())
basic_function_lib = CDLL(Path('basic_function_linux.so').absolute())

python_c_square = basic_function_lib.c_square


# reference https://reptate.readthedocs.io/developers/python_c_interface.html
def do_square_using_c(list_in):
    """Call C function to calculate squares"""
    n = len(list_in)
    c_arr_in = (c_double * n)(*list_in)
    c_arr_out = (c_double * n)()

    python_c_square(c_int(n), c_arr_in, c_arr_out)
    return c_arr_out[:]


if __name__ == "__main__":
    print(shareable_lib.sum(5, 3))
