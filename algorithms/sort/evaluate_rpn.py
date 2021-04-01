t = {'+':lambda x,y:x+y,'-':lambda x,y:x-y,'x':lambda x,y:x*y,'/':lambda x,y:x/y,'^':lambda x,y:x**y}
def rpn(i):
    e,o = i.split(),[]
    for n in e:
        if n.isdigit():o.append(int(n))
        else: o[-2:]=[t[n](*o[-2:])]
    return o[0]
