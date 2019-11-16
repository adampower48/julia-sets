def mandelbrot(c, bound, max_iters=100):
    z = 0
    i = 0
    while i < max_iters and abs(z) < bound:
        z = z * z + c
        i += 1
        
    if i == max_iters:
        return None
    
    return i