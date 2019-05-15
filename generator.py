import random
import numpy as np

def generate_bits(quantity):
    return [random.randint(0,1) for i in range(0, quantity)]