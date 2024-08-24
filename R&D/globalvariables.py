y = 'jerome is handsome' #global variables

def function():
    global x #global keyword
    x = "pogi kalang"
    # print("Is this true? " + y)

function()
print(" is this true? " + y)