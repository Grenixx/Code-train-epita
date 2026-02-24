#from algo_py import *
from algo_py import bintree
from algo_py import queue
from algo_py import timing


from bintrees import bintrees_examples

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
    #i = 0
    #while(i<100000000):
    #    i+=1

#BF = timing.timing(BF)
#BF(bintrees_examples.tree_fig1)

#timing.timing(BF(bintrees_examples.tree_fig1))
#BF(bintrees_examples.tree_fig1)

def size(bintree):
    if (bintree == None):
        return 0
    else:
        return 1 + size(bintree.left) + size(bintree.right)
    
def height(bintree):
    if (bintree == None):
        return -1
    else:
        return 1 + max(height(bintree.left), height(bintree.right))
    
#print("size:", size(bintrees_examples.tree_fig1))
#print("height:", height(bintrees_examples.tree_fig1))


def to_linear(bintree, res):
    res += "("
    res += str(bintree.key)
    if (bintree.left != None):
        res += to_linear(bintree.left, "")
    else:
        res += "()"
    if(bintree.right != None):
        res += to_linear(bintree.right, "")
    else:
        res += "()"
    res += ")"
    return res
    
    

#print(to_linear(bintrees_examples.tree_b2, ""))

def rec_search_hier(bintree, x, i):
    #if (bintree

    if bintree.key == x:
        return i
    res = None
    if (bintree.left != None):
        res = rec_search_hier(bintree.left, x , 2*i)
        
    if(bintree.right != None and res == None):
        res = rec_search_hier(bintree.right, x , (2*i)+1)
        
    return res
    
def search_hier(bintree, x):
    return rec_search_hier(bintree, x, 1)

#print(search_hier(bintree.BinTree("",None,None), "1"))

def code_list(t, bin):
    bin.key = ''
    for i in t:
        letter = i[0]
        pos = i[1]

        current = bin
        for c in pos: #je prend le premier de mon string '100' je cree un noeud en 1 puis en 0 etc 
            if (c == '0'):
                if current.left == None:
                    current.left = bintree.BinTree("", None,None)
                    current.left.key = current.key + "0"

                current = current.left      
            elif (c == '1'):
                if current.right == None:
                    current.right = bintree.BinTree("", None,None)
                    current.right.key = current.key + "1"

                current = current.right

        current.key = letter

#arr = {('a', '0'),('u', '100'),('n', '101'),('H', '111'),('f', '1100'),('m', '1101')}
arr = {('a', '0'),('u', '100'),('n', '101'),('H', '111'),('f', '1100'),('m', '1101')}
bin = bintree.BinTree('',None,None)
code_list(arr, bin)
#print(bin.right.right.right.key)

def search_code(T, c):
    return rec_search_code(T,c,"")

def rec_search_code(T,c, Nodepath):
    if T.key == c:
        return Nodepath
    res = None
    if (T.left != None):
        res = rec_search_code(T.left, c , Nodepath+"0")
        
    if(T.right != None and res == None):
        res = rec_search_code(T.right, c ,  Nodepath+"1")
        
    return res

#print(search_code(bin,'m'))


def height(node):
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


def linar_to_bin(linar):
    #print(linar)
    key = ""
    c = 0
    if (linar[0] == '('):
        c = 1
        while (linar[c] != '(' and linar[c] != ')'):
            key += linar[c]
            c+=1

    if (key == ""):
        return bintree.BinTree("",None,None)
    
    ouvert = 1
    iter = c + 1  
    while (ouvert != 0):
        if (linar[iter] == '('):
            ouvert+=1
        elif (linar[iter] == ')'):
            ouvert-=1
        
        iter+=1

    ouvert2 = 1
    iter2 = iter+1
    while (ouvert2 != 0):
        if (linar[iter2] == '('):
            ouvert2+=1
        elif (linar[iter2] == ')'):
            ouvert2-=1
        
        iter2+=1
    return bintree.BinTree(key,linar_to_bin(linar[c:iter]),linar_to_bin(linar[iter:iter2]))

linar = "(7123(8(5()())())(hehehe()()))"
#linar_to_bin_tree = linar_to_bin(linar)
#BF(linar_to_bin_tree)

def hier_size(tree, size):
    vector = []
    for _ in range(size):
        vector.append(None)
    _fill_prebuilt_vector(tree,vector,1)
    return vector
    
def _fill_prebuilt_vector(arb, vector, i):
    if arb != None:
        vector[i] = arb.key
        if arb.left != None:
            _fill_prebuilt_vector(arb.left,vector,2*i)
        if arb.right != None:
            _fill_prebuilt_vector(arb.right,vector,2*i + 1)
#print(hier_size(bintrees_examples.tree_b, 16))

def occ(arb):
    vec = []
    rec_occ(arb, vec, "")
    print(vec)

def rec_occ(arb, vec, key):
    if arb != None:
        vec.append(key)
        rec_occ(arb.left, vec, key+"0")
        rec_occ(arb.right, vec, key+"1")

#occ(bintrees_examples.tree_b)
#BF(bintrees_examples.tree_b)

def vec_to_bin(vecbin, i, len):
    if vecbin[i] != None:
        if len > i*2 and vecbin[i*2] != None:
            resR = vec_to_bin(vecbin, i*2, len)
        else:
            resR = None
        if len > i*2+1 and vecbin[i*2+1] != None:
            resL = vec_to_bin(vecbin, i*2+1, len)
        else:
            resL = None
        return bintree.BinTree("A"+str(i), resL ,resR)

    return None

vecbin = [1,2,3,None,5,6]
#BF(vec_to_bin(vecbin, 1, len(vecbin)))

def rec_transpose(bin):
    res1 ,res2 = None, None
    if bin != None:
        res1 = rec_transpose(bin.right) 
        res2 = rec_transpose(bin.left)

    return bintree.BinTree(bin.key * 2, res1, res2)

#BF(bintrees_examples.tree_b)
#BF(rec_transpose(bintrees_examples.tree_b))

def copyWithSize(B):
    q = queue.Queue()
    q.enqueue(B)
    while(not q.isempty()):
        currentBin = q.dequeue()
        print(currentBin.key, end=" ")  
        currentBin.size = size(currentBin)
        left = currentBin.left
        right = currentBin.right
        if (left != None):
            q.enqueue(left)
        if (right != None):
            q.enqueue(right)
    
def BF_size(bintree):
    q = queue.Queue()
    q.enqueue(bintree)
    while(not q.isempty()):
        currentBin = q.dequeue()
        print(currentBin.key , "->" , currentBin.size, "||", end=" ")
        left = currentBin.left
        right = currentBin.right
        if (left != None):
            q.enqueue(left)
        if (right != None):
            q.enqueue(right)

#BF(bintrees_examples.tree_b)
#copyWithSize(bintrees_examples.tree_b)
#print("\n")
#BF_size(bintrees_examples.tree_b)

def kinship(B,x,y):
    if B == None:
        return -1
    else:
        return get_kinship(B,x,y)


def get_kinship(B : bintree.BinTree, x, y):
    
    #trouver l elem
    result = -1
    if B.key == x:
        #start the relative search with the first found
        result = rec_kinship(B,y, 0)
        return result
        
    elif B.key == y: 
        #start the relative search with the first found
        result = rec_kinship(B,x, 0)
        return result
    
    
    elif B.left != None:
        return get_kinship(B.left, x,y)
    
    elif B.right != None:
        return get_kinship(B.right, x,y)
    else :
        return -1
    
def rec_kinship(B,s, i):
    res = -1
    if B.key == s:
        return i
    
    if  B.left != None:
        res = rec_kinship(B.left,s,i+1)
        if res != -1: return res

    if B.right != None:
        res = rec_kinship(B.right,s,i+1)
    
    
    return res

    
#print(get_kinship(bintrees_examples.tree_b, 0,7))

print(kinship(bintrees_examples.tree_fig2, 'Q', 'U')) # == 1
#print(get_kinship(bintrees_examples.tree_fig2, 'D', 'T')) # == 2
#print(get_kinship(bintrees_examples.tree_fig2, 'T', 'V')) # == 3
#print(get_kinship(bintrees_examples.tree_fig2, 'S', 'R')) # == -1
#print(get_kinship(None, 'A', 'B')) # == -1

def check_sum_rec(BT) -> bool:
    if BT.left == None:
        if BT.right == None:
            return True  # leaf
        else:
            return check_sum(BT.right) # internal single node (right)
    else:
        if BT.right == None:
            return check_sum(BT.left) # internal single node (left)
        else:
            if (BT.left.key + BT.right.key == BT.key):
                return check_sum(BT.left) and check_sum(BT.right) # double nodes
            else:
                return False
             
            # internal double node


def check_sum(BT) -> bool:
    if BT == None:
        return True
    else:
        return check_sum_rec(BT)
    
#BF(bintrees_examples.tree_fig11)
#print()
#print("  "  , check_sum(bintrees_examples.tree_fig11))
