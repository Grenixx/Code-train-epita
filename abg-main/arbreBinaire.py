#from algo_py import *
from algo_py import bintree
from algo_py import queue
from algo_py import timing


from bintrees import bintrees_examples

@timing.timing
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
    #while(i<1000000):
    #    i+=1


#timing.timing(BF(bintrees_examples.tree_fig1))
BF(bintrees_examples.tree_fig1)