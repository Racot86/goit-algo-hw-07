'''Завдання 1

Напишіть алгоритм (функцію), який знаходить найбільше значення у двійковому дереві
пошуку або в AVL-дереві. Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.
'''
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

def search_max(root):
    def s_max(root,val):
        if root is None:
            return val
        if root.val > val:
            val = root.val
            return s_max(root.right,val)
        return s_max(root.right,val)

    if root.right is None :
        return s_max(root.left,root.left.val)
    return s_max(root.right,root.right.val)
    
    

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)


print('Maximum value:',search_max(root))