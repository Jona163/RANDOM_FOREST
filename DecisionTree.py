# Autor: Jonathan Hernández
# Fecha: 21 octubre 2024
# Descripción: Random Forests.
# GitHub: https://github.com/Jona163

import numpy as np
from collections import Counter

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None,*,value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value
        
    def is_leaf_node(self):
        return self.value is not None
