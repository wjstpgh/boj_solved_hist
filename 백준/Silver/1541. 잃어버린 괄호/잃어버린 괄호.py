sik=input()
def das(arr):
    return sum(map(int,arr.replace('-','+').split('+')))
try:
    div=sik.index('-')
    print(das(sik[:div])-das(sik[div+1:]))
except:
    print(das(sik))