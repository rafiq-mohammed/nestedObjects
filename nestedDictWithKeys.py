# Function to navigate through nested dictionary using specified keys
def get_values(value, key):
    # split keys based on delimiter
    keys = key.split('/')
    print(value)
    # iterate through the keys and pop out the final 
    for k in keys:
        value = value.pop(k)
        print(value)
    return value

object = {'x': {'y': {'z': 'a'}}}
key = 'x/y/z'
print ("Result is", get_values(object, key))

object = {'a': {'b': {'c': 'd'}}}
key = 'a/b/c'
print ("Result is", get_values(object, key))
