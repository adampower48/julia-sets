import cmath
import matplotlib.pyplot as plt
import numpy as np
import time
from mandelbrot import mandelbrot
import ctypes

mandelbrot_class = ctypes.CDLL("mandelbrot.dll")
mandelbrot_class.mandelbrot_wrapper.restype = ctypes.c_int
mandelbrot_class.mandelbrot_wrapper.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
mandelbrot_class.mandelbrotArr.restype = np.ctypeslib.ndpointer(dtype=ctypes.c_int)
mandelbrot_class.mandelbrotInplace.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_double, ctypes.c_int, np.ctypeslib.ndpointer(dtype=np.uintp, flags='C') ]
mandelbrot_class.mandelbrotInplace.restype = None

def make_func(c):
    def f(z):
        return z*z + c
        
    return f
    
    
    
def compute_iters(func, z, bound, max_iters=100):
    for i in range(max_iters):
        if abs(z) > bound:
            return i
            
        z = func(z)
    
    return np.nan
        
def mandelbrotty(x_space, y_space, bound, max_iters):
    return [[compute_iters(make_func(complex(i, j)), 0, bound, max_iters)
             for i in x]
             for j in y]
             
def mandelbrot_fast(c, bound, max_iters=100):
    z = 0
    i = 0
    while i < max_iters and abs(z) < bound:
        z = z * z + c
        i += 1
        
    if i == max_iters:
        return np.nan
    
    return i


    
    

if __name__ == "__main__":
    #x = np.linspace(-2, 2, 1000)
    #c = x + x[:, None] * 1j
    #cc = np.stack([np.real(c), np.imag(c)], axis=-1)

    #st = time.time()
    #res = np.apply_along_axis(lambda x: mandelbrot_class.mandelbrot_wrapper(*x, 100, 100), -1, cc)
    #res = np.vectorize(mandelbrot_class.mandelbrot_wrapper, [np.float])(cc, 100, 100)
    #print(time.time() - st)
    
    #res = mandelbrot_class.mandelbrotArr(-2, 2, 1000, 100, 100)
    #res = np.ctypeslib.as_array(res, (1000, 1000))
    #print(res[0])
    
    

    #plt.imshow(res)
    #plt.show()
    
    x = np.zeros_like(np.zeros((10, 10)))
    xpp = (x.__array_interface__['data'][0] 
      + np.arange(x.shape[0]) * x.strides[0]).astype(np.uintp)
    print(xpp)
    
    print(x.shape[0])
    
    mandelbrot_class.mandelbrotInplace(-2, 2, x.shape[0], 100, 100, xpp)
    print(x[0,0])
    print(x)
    plt.imshow(x)
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    