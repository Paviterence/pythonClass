import a
import b

# obj1=a.animal()
# obj1.display()
# obj2=b.bird()
# obj2.display()
from a import animal
obj1=animal()
from b import bird
obj2=bird()
obj1.display()
obj2.display()