from ctypes import CDLL

mandelbrot_class = CDLL("mandelbrot.dll")
print(mandelbrot_class.mandelbrot_wrapper(1, 1, 10, 100))