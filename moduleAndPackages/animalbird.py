
#approch 1 there is no confusion because python able understand because we are mentioining the module name
import animals
import bird
animals.fly()
bird.fly()
animals.color()
bird.color()
print("*"*50)
# approch 2 It will call the latest module here

from animals import *
from bird import *
fly()
color()#It will call the latest module here so we need to proceed step by step
from animals import *
fly()
color()
# its not best approach when module have same functions
print("*"*50)