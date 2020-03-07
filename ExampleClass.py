#!/usr/bin/python

import configparser

"""@package ExampleClass
Documentation for this module.

More details.
"""

""" Class information """
# https://docs.python.org/3/tutorial/classes.html

""" Naming convenctions """
# https://www.python.org/dev/peps/pep-0008/#naming-conventions

""" Short explanation """
# https://www.geeksforgeeks.org/private-variables-python/


class ExampleClass:
    """ ExampleClass class.
    Args:
        p0, first Point of the Line
        p1, second Point of the Line

    Examples:
        >>> new_instance = ExampleClass(1, 2, 3, 4))
    """  

    def __init__(self, p0, p1, p2, p3):
        """ The constructor. """    
        
        config = configparser.ConfigParser()
        config.read("config.ini")    

        # "Public" variables        
        self.p0 = p0
        self.p1 = p1
        self.config_param1 = int(config["CONFIG_TOPIC1"]["PARAM1"])
        self.config_param2 = str(config["CONFIG_TOPIC1"]["PARAM2"])

        # "Private" variables        
        self._p2 = p2
        self._config_param3 = float(config["CONFIG_TOPIC2"]["PARAM3"])
        
        print('Class instance initialized')

    def public_method(self, other_inputs):
        """ public_method 
        Args:
            other_inputs, other inputs used in the function
        Return:
            output, the output of the method
        """   
        print(other_inputs)
        print(self._config_param3)
        print(self._private_method(other_inputs))

    def _private_method(self, other_inputs):
        """ _private_method 
        Args:
            other_inputs, other inputs used in the function
        Return:
            output, the output of the method
        """   
        output = other_inputs
        return output

##################################################

#Just another funtcion
def another_funtcion(input1, input2, input3=0.01, input4=True):
    """
    Spiral generator.
    Args:
        input1 -
        input2 -
        input3 - 0.01
        input4 - True
    Return:
        output, the output of the method
    """   
    print(input1, input2, input3, input4)
    output = [input1, input2, input3, input4]

    return output

##################################################

def main():

    var = ExampleClass(1, 2, 3, 'four')
    var.public_method(4)
    
    print(var.p0, var.p1, var.config_param1, var.config_param2)

    print(another_funtcion(1, 2))
  
if __name__== "__main__":
  main()
  




