#from algo_py import *
from algo_py import bintree
from algo_py import queue
from algo_py import timing

from bintrees import bintrees_examples

def new_empty_heap():
    return [None]

def is_empty(n):
    return n<=1

def heap_root():
    return 1

def is_root(i):
    return i == 1

def left(i):
    return 2*i

def right(i):
    return 2*i+1

def parent(i):
    return i//2

def leaf(i,n):
    return 2*i >= n

def single(i, n):
    return 2*i == n-1

vec = [None, (1,'C'), (8,'P'), (9,'Z')]

def bubble_up(H, i, val, elt):
    p = parent(i)
    while not is_root(i) and H[i][0] < H[p][0]:
        H[i] = H[p]    
        i = p    
        p = parent(i)

    H[i] = (val, elt)

def heap_push_v1(H, val, elt):
    H.append((val, elt))
    i = len(H) - 1  

    while i > 1:
        parent = i // 2
        if H[i][0] < H[parent][0]:  
            H[i], H[parent] = H[parent], H[i]  
            i = parent
        else:
            break
def heap_push_v2(H, val, elt):
    H.append((val, elt))
    i = len(H) - 1  
    p = i
    while i > 1:
        p = i//2
        if H[i][0] < H[p][0]:  
            H[i] = H[p]    
            i = p    
        else:
            break
    H[i] = (val,elt)
def heap_push_v3(H: list, val: int, elt) -> tuple:
    H.append((val, elt))
    i = len(H) - 1  
    bubble_up(H,i,val,elt)
    
#print(vec)
#heap_push_v3(vec,4,'N')
#print(vec)

def bubble_down(H, n, i, val):
    pass

def heap_pop(H):
    n = len(H)
    if is_empty(n):
        raise RuntimeError("Connot pop form empty heap")
    else:
        i = heap_root()
        to_return = H[i] # 6 de carraux de enzo
        (val, elt) = H.pop() # 10 carraux de mathaux
        #H[i] = (val,elt) # tmp placement 
        if single(i, n):
            if (H[heap_pop()][0] > H[2*i][0]):
                H[i] = H[2*i][0]
                H[2*i][0] = (val,elt)


    return to_return

#[None, (1,'C'), (8,'P'), (9,'Z')] size = 4 so 3
def min_child(H, size, i):
    return min(H[i*2][0], H[(i*2)+1][0])

def minBST(B):
    if B.left == None:
        return B.key
    return minBST(B.left)

def minBST_iterative(B):
    while(B.left != None):
        return minBST(B.left)
    return B.key

def maxBST(B):
    if (B.right == None):
        return B.right
    return maxBST(B.right)

def maxBST_iterative(B):
    while(B.right != None):
        B = B.right
    return B

#def search(B, x):
    if (B.keys == x):
        return B
    if (B.left == None and B.right ==None):
        return None
    elif (B.left != None):
        search(B.right)

    
def leaf_inser(B, key):
    if B == None:
        return bintree.BinTree(key, None, None)
    else:
        if B.key <= key:
            if B.right == None:
                B.right = bintree.BinTree(key, None, None)
            else: 
                B.right = leaf_inser(B.right, key)
            return B
        elif B.key > key:
            if B.left == None:
                B.left = bintree.BinTree(key, None, None)
            else: 
                B.left = leaf_inser(B.left, key)
            return B


def BF(bintree):
    q = queue.Queue()
    q.enqueue(bintree)
    while(not q.isempty()):
        currentBin = q.dequeue()
        print(currentBin.key, end=" ")
        left = currentBin.left
        right = currentBin.right
        if (left != None):
            q.enqueue(left)
        if (right != None):
            q.enqueue(right)



def search(B, key):
    if B == None:
        return None
    elif B.key == key:
        return B
    else:
        if B.key < key:
            return search(B.left, key)
        elif B.key > key:
            return search(B.right, key)

#def pop_max_bst(non_empty):
#    max = maxBST(non_empty)
 #   if (max != None): # normalemnt c est impossible
  #      non_empty.key = max.key
     #   max = max.left # vu que c est le max il est tout a droite si il a un arbre droit 
   #                     # c est que c est pas le max parcotre il peux avoir un gauche
    #return (non_empty.key, non_empty)

def pop_max_bst(non_empty):
    if non_empty.right == None:
        return (non_empty.key, non_empty.left)

    max, non_empty.right = pop_max_bst(non_empty.right)
    return max, non_empty


def del_bst(non_empty):
    if non_empty.left != None:
        if non_empty.right != None:
            non_empty.key, non_empty.left = pop_max_bst(non_empty.left)
        else:
            non_empty = non_empty.left
    else:
        non_empty = non_empty.right
    return non_empty

def delete(x, bst):
    if bst!= None:
        if bst.key == x:
            return del_bst(bst)
        else:
            if x < bst.key:
                bst.left = delete(x,bst.left)
            else:
                bst.right = delete(x, bst.right)
            return bst
    else:
        raise KeyError(str(x) + " was not found")
    

def cut(B, key):
    if B != None:
            
        if B.key <= key:
            smaller, larger = cut(B.right, key)
            B.right = smaller
            return (B, larger)
        else :
            smaller, larger = cut(B.left, key)
            B.left = larger
            return (smaller, B)
    else :
        return (None, None)

def root_insert(B, key):
    left, right = cut(B, key)
    return bintree.BinTree(key, left, right)        

B = None
B =leaf_inser(B, 13)
B =leaf_inser(B, 20)
B =leaf_inser(B, 5)
B =leaf_inser(B, 7)
B =leaf_inser(B, 15)
B =leaf_inser(B, 10)
B = root_insert(B, 1)
#BF(B)


def hat_sec_min(B):
    if (B == None):
        return None
    else:
        return sec_min(B)
    
def sec_min(B):
    if B.left == None and B.right == None:
        return None
    elif B.left == None:
        return minBST(B.right)
    else: #clarter
        return sec_min(B.left)
    
B2 = bintree.BinTree(13, bintree.BinTree(5, bintree.BinTree(1, None, bintree.BinTree(4, None, None)), bintree.BinTree(10, bintree.BinTree(7, None, None), bintree.BinTree(12, None, None))), bintree.BinTree(20, bintree.BinTree(15, None, bintree.BinTree(18, None, None)), bintree.BinTree(25, bintree.BinTree(21, None, None), bintree.BinTree(27, None, None))))
B3 = bintree.BinTree(12, bintree.BinTree(2, None, bintree.BinTree(4, bintree.BinTree(3, None, None), bintree.BinTree(5, None, None))), bintree.BinTree(21, bintree.BinTree(18, None, None), None))
#print(sec_min(B3))

def size(bintree):
    if (bintree == None):
        return 0
    else:
        return 1 + size(bintree.left) + size(bintree.right)

def both_x(B, x):
    if B == None:
        return (0,0)
    if x <= B.key:
        (s,g) = both_x(B.left, x)
        return (s ,g + 1 + size(B.right))
    else:
        (s,g) = both_x(B.right, x)
        return (s + 1 + size(B.left), g)

#print(both_x(B2, 20))

def lca(B, x, y):
    if (x < B.key):
        if (y < B.key):
            return lca(B.left, x, y)
        else:
            return B.key
    else:
        if (y > B.key):
            return lca(B.right, x, y)
        else:
            return B.key
        
B1 = bintree.BinTree(15,bintree.BinTree(8, bintree.BinTree(1, None, None), bintree.BinTree(12, bintree.BinTree(10, None, None), None)),bintree.BinTree(28, bintree.BinTree(20, None, bintree.BinTree(23, None, None)), bintree.BinTree(42, bintree.BinTree(35, None, None), bintree.BinTree(66, None, None))))
#print(lca(B1, 10,15))
        
def height(bintree):
    if (bintree == None):
        return -1
    else:
        return 1 + max(height(bintree.left), height(bintree.right))

class AVL(bintree.BinTree):
    def __init__(self, key, left, right, bal):
        super().__init__(key, left, right)
        self.bal = bal

def is_equilibrer(B):
    if B.left != None:
        if  B.right != None:
            return is_equilibrer(B.left) and is_equilibrer(B.right)
        else: 
            

    