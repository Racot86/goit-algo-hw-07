"""
Завдання 3

Напишіть алгоритм (функцію), який знаходить суму всіх значень у двійковому
дереві пошуку або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

"""
from random import randint

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def total_sum(root):
    def sum_left(root,sum=None):
        if sum == None:
            sum = 0
        if root is None:
            return sum
        sum += root.val
        return sum_left(root.left,sum)
    def sum_right(root,sum=None):
        if sum == None:
            sum = 0
        if root is None:
            return sum
        sum += root.val
        return sum_right(root.right,sum)
    return sum_left(root) + sum_right(root)
    
    
    
     

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)


print('Sum of values:',total_sum(root))