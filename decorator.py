'''The objective is to use decorators to wrap the functionality over another function such that the other function
will be responsible to add to a result and the wrapper function recursively calls this function
'''
inp = [1, [2, 3], [4, [5, 6], 7]]

def decorator(func):
    res = []
    def wrapper(*args, **kwargs):
        ele = func(*args, **kwargs)
        if not isinstance(ele, list):
            res.append(ele)
        else:
            func(ele)
    return res

@decorator
def flatten(inp):
    for ele in inp:
        return ele

flatten(inp)
