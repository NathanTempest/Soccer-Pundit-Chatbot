'''Decorators in Python help us to achieve function warping. Often used for logging, caching, access control,
pre and post processing.
'''

#using a decorator to flatten a list of lists
inp = [1, [2, 3], [4, [5, 6], 7]]
op = [1, 2, 3, 4, 5, 6, 7]

#this outward function is the decorator, it accepts a function as an argument
def flatten(func):
    print("Flattening the list...")
    #this inward function is the wrapper, it is called instead of the original function
    def wrapper(*args, **kwargs):
        #call the original function
        func(*args, **kwargs)
        print("Flattening by calling the helper function")
        return flatten_recursively(args[0])  # Call the helper function to flatten the list
    return wrapper

#helper function that flattens the list recursively
def flatten_recursively(lst):
    res = []
    for item in lst:
        if isinstance(item, list):
            res.extend(flatten_recursively(item))
        else:
            res.append(item)
    return res


@flatten
#this will apply the decorator to the flatten_list function
def flatten_list(inp):
    print("This function is now wrapped by the decorator")
    
    

out = flatten_list(inp)  # Call the decorated function with the input list
print("the list after flattening is:", out)  # Output the flattened list