import numpy as np
from utils import multiidx_gen
from scipy.special import legendre
import matplotlib.pyplot as plt

def measurement_matrix(grid , input_dim, n_size=10):
    """
    ----------------------------------------------------------------------------
    Input:
    grid ......... grid on the domain dimensions: (nb_pts, input_dim)
    input_dim .... input dimension
    
    Output:
    A ............ measurement matrix
    ----------------------------------------------------------------------------
    """

    # create the 1d sparse grid generator
    Z_pts  = grid  
    
    # specify the dimension
    d      = input_dim
    nb_pts = Z_pts.shape[0]
    
    print(f"Grid size: {Z_pts.shape}")
    print(f"number of points: {nb_pts}") 
    
    # define the Hyperbolic Cross function
    HCfunc = lambda x: np.prod(x+1)-1

    # Generate the multi-index set
    #n_size   = 50
    Lambda   = multiidx_gen(d, HCfunc, n_size)
    nb_basis = len(Lambda)
    print('Using', nb_basis, 'basis functions')

    if input_dim == 2:
        plt.figure()
        plt.scatter(Z_pts[:,0],Z_pts[:,1])
        plt.title('Grid')
    
    # Generate measurement matrix 
    A = np.ones((nb_pts,nb_basis))
    
    for n in range(nb_basis):
        for k in range(d):
            leg_poly_1d = legendre(Lambda[n,k])
    
            x_vals = Z_pts[:,k]    
            A[:,n] = np.multiply(A[:,n], leg_poly_1d(x_vals)*np.sqrt(2*Lambda[n,k]+1))
    
    A = A/np.sqrt(nb_pts)
    print(f"measurement matrix A size: {A.shape}")
    plt.figure()
    plt.imshow(np.transpose(A).dot(A))
    plt.title('Verify orthogonality')
    cbar = plt.colorbar()
    
    return A
