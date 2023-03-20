from lib.animal import *
from lib.zoo import *
import ipdb
# code here

# e.g.  
#   z1 = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
#   a1 = Animal( 'Lion', 75, 'Luke', z1 )

seneca = Zoo('Seneca', 'Rochester, NY')
sanfran = Zoo('San Fran Zoo', 'San Fransisco')
rover = Animal('rover', 120, 'wolf', 'sanfran')  
katy = Animal('katy', 30, 'red panda', 'sanfran')  
smoky = Animal('smoky', 120, 'bear', 'sanfran')     
wf = Animal('white fang', 120, 'wolf', 'seneca')  




seneca.animals
#  DONE : Animal.find_by_species('wolf')
#  DONE : print(Zoo.all)




# do not remove 

# ipdb.set_trace()
