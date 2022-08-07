
#whatever is inside module1_1 gets called
import module1_1

module1_1.sum(1,2)

#prints which module you are in
print(__name__)

#prints the specified module's name
print(module1_1.__name__)

