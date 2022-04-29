# import sys
# sys.path.append("E:\python\pythonClass\moduleAndPackages\package1")
# sys.path.append("E:\python\pythonClass\moduleAndPackages\package1\package2")
# import module1
# import module2
# module1.display()
# module2.show()

# import sys
# sys.path.append("E:\python\pythonClass\moduleAndPackages\package1")
# sys.path.append("E:\python\pythonClass\moduleAndPackages\package1\package2")
# from module1 import *
# from module2 import *
# display()
# show()

from package1 import module1
from package1.package2 import module2
from package1.module1 import *
from package1.package2.module2 import *
display()
show()
