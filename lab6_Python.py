
def  arythmeticprogression(count,step,Firstnum):
    if (count == 1):
        a_n = Firstnum;
    else:
        a_n = arythmeticprogression(count-1,  step, Firstnum) + step;
    return a_n;

n=10
a1=10
d=2
print(((arythmeticprogression(n, d, a1) + a1)*n)/2 )