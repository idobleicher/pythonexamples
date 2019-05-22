
def  create_set (*arguments) :
    return  set(arguments)

set_a = create_set (1 , 2)
set_b = create_set (3 , 4)

#BaseSchema._AVAILABLE_SCHEMES |= set(schemes)

set_c = set()
set_c |= set_a

set_c = set_c | set_b


print(set_c)
#{1, 2, 3, 4}