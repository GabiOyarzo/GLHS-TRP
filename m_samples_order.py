import numpy as np
from utils import multiidx_gen

def get_m_samples_from_order(input_dim, n_size= 5):
    """
    Inputs:
    n_size....... order of the polynomial
    input_dim ... input dimension
    output:
    nb_basis .... number of basis 
    """
    # define the Hyperbolic Cross function
    HCfunc = lambda x: np.prod(x+1)-1

    # Generate the multi-index set 
    Lambda   = multiidx_gen(input_dim, HCfunc, n_size)
    nb_basis = len(Lambda)
    print('Using', nb_basis, 'basis functions')

    return nb_basis