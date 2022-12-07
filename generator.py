# def funcA(list):
#     ret = []
#     for n in list:
#         ret.append(n*2)
#     return ret

# for n in funcA([1,2,3,4,5]):
#     print(n)

def funcA(list):
    # ret = []
    for n in list:
        yield n * 2

for n in funcA([1,2,3,4,5]):
    print(n)
