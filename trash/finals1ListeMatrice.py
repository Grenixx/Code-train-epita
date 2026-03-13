def check_stock(stock, capa):
    c=0
    i=0
    l = len(stock)
    while c<= capa and i<l:
        _,incr = stock[i]
        c+= incr
        i+=1

    return c <= capa


stock = ([('A',5),('B',5),('C',5),('D',5)])
def get_stock2(stock,obj,request):
    i = 0
    for type, quant in stock:
        if type == obj:
            skireste = quant - request
            if skireste > 0 :
                stock[i] = (type, skireste)
                return True
            else:
                stock.pop(i)
                return False
        i+=1
    return False

def get_stock(stock,obj,request):
    i = 0
    sortir = False
    lereturn = False
    while sortir == False and i < len(stock):
        type,quant = stock[i]
        if type == obj:
            skireste = quant - request
            if skireste > 0 :
                stock[i] = (type, skireste)
                sortir = True
                lereturn = True
            else:
                while i < len(stock)-1:
                    o,r = stock[i+1]
                    stock[i] = (o,r)
                    i+=1
                stock.pop()
                sortir = True
                lereturn = False
        else:
            lereturn = False

        i+=1

    return lereturn

    

def shopping(stock, request):
    lereturn = True
    for o,r in request:
        r = get_stock(stock, o,r)

        if not r:
            lereturn = False

    return lereturn


stock = ([('A',5),('B',5),('C',5),('D',5)])
stockretirer = ([('A',4),('Z',4)])

print(stock)
print(shopping(stock, stockretirer))
print(stock)