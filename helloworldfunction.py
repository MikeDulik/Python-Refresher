# helloworld invoked as a function
# Below is the function, with both implicit 'print' returned, as well as explicit 'return'
def helloworld():
    print "HelloWorld! (Implicit)"
    return "Hello World! (Explicit)"

# And here is the function being used
print helloworld()
