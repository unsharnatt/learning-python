# module in the same folder
# give a name as snake case not camel case  
import converters
print(converters.kg_to_lbs(5))

from converters import kg_to_lbs as kg2lbs
print(kg2lbs(5))

# module in difference folder, 
# in folder /convert has __init__.py as an empty file
from convert import kg_to_lbs
print(kg_to_lbs.kg_to_lbs(4))

from convert.kg_to_lbs import kg_to_lbs as k2l
print(k2l(4))
 