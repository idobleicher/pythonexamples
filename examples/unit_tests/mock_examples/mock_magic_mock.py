from unittest import mock


#Mock supports the mocking of Python magic methods.
# The easiest way of using magic methods is with the MagicMock class. It allows you to do things like:

mymock = mock.MagicMock()
mymock.__str__.return_value = 'foobarbaz'
print(str(mymock))
#'foobarbaz'

print(mymock.__str__.assert_called_with())

#Mock allows you to assign functions (or other Mock instances) to magic methods and they will be called appropriately. The MagicMock class is just a Mock variant that has all of the magic methods pre-created for you (well, all the useful ones anyway).



#The following is an example of using magic methods with the ordinary Mock class:
mymock2 = mock.Mock()
mymock2.__str__ =mock.Mock(return_value='wheeeeee')
print(str(mymock2))