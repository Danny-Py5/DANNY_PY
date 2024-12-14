from package_init_test.modules.module1 import Module1
from package_init_test.modules.module2 import Module2
import package_init_test as initial

class Main(initial.Parent):
    def __init__(self):
        self.variable = 'Main() Variable'

    def main_printer(self):
        print('Main printer method is called')

# the __init__ module of the package_init_test is
# authomatically called.
# uncomment to see output
# print(dir(initial))
# so importing only the package_init_test 
# calls all the variables, methods, and classes in the
# __init__ of package_init_test to this module and as well
# the modules in the directory
# it is posible to also print package_avariable
# because it is already in this module and use
# module1 and module2 without even importing them
# by using the . notation examples below

print(initial.package_avariable) # from __init__
module1 = initial.modules.module1.Module1()
print(module1.module1_printer())

main = Main()

print(main.printer())   #printer method of package_init_rest __init__ is called.
