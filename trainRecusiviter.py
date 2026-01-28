def reverse(n):
    if n < 0 :
        n=-n
        return -rec_reverse(n,0)
    else:
        return rec_reverse(n,0)

def rec_reverse(n,res):
    res += n%10 
    n //= 10
    if n <= 0:
        return res
    else:
        res*=10
        return rec_reverse(n,res)


#print(reverse(-1234))

def fibo_rec(n, call):
    call +=1
    if n < 2 :
        return (1,call)
    else:
        res1, call = fibo_rec(n-1, call)
        res2, call = fibo_rec(n-2, call)
        return (res1+res2, call)
    
def fibo(n):
    return fibo_rec(n,0)

def Rom(s, res, currentIdx, nb_of_i, len_s):
    if currentIdx >= len_s:
        if nb_of_i > 0:
            res+=nb_of_i
            nb_of_i = 0
        return res
    if s[len_s - currentIdx - 1] == "I":
        nb_of_i += 1
        return Rom(s, res, currentIdx+1,nb_of_i)
    elif s[len_s - currentIdx - 1] == "V":
        res += 5
        if nb_of_i > 0:
            res-= nb_of_i
            nb_of_i = 0
        return Rom(s, res, currentIdx+1,nb_of_i)
    else:
        if nb_of_i > 0:
            res+=nb_of_i
            nb_of_i = 0

    if s[len_s - currentIdx - 1] == "X":
        res+= 10
        return Rom(s,res,currentIdx+1,nb_of_i)

def Ro_main(s):
    return Rom(s,0,0,0,len(s))

print(Rom("XVII",0,0,0,len("XVII"))) 