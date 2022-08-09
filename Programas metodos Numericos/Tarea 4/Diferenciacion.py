import numpy as np


def funcion(x):
    #return np.arccosh(x)
    return np.arcsinh(x)

def forward(x,h):
    return (funcion(x+h) - funcion(x)) / h

def backward(x,h):
    return (funcion(x) - funcion(x - h)) / h

def central(x,h):
    return (funcion(x + h) - funcion(x - h)) / (2 * h)