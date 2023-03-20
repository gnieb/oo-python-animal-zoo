from lib.animal import *
from lib.zoo import *
import ipdb

# domain is like... the whole thing 
# model is like the idea of a thing, aka classes

# zoo ------ < animals
# a zoo has many animals

# code here

# e.g.  
#   z1 = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
#   a1 = Animal( 'Lion', 75, 'Luke', z1 )

seneca = Zoo('Seneca', 'Rochester, NY')
sanfran = Zoo('San Fran Zoo', 'San Fransisco')
sams = Zoo('Sams Spot', 'San Fransisco')
rover = Animal('wolf', 120, 'rudy', sanfran)  
katy = Animal('bear', 30, 'katy', sanfran)  
smoky = Animal('bear', 120, 'smoky', sams)     
wf = Animal('wolf', 120, 'white fang', 'seneca')  




# seneca.animals
#  DONE : Animal.find_by_species('wolf')
#  DONE : print(Zoo.all)




# do not remove 

ipdb.set_trace()
