# Python – Insertion at the beginning in OrderedDict
from collections import OrderedDict
 
# Initialising ordered_dict
iniordered_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])
 
# Inserting items in starting of dict
iniordered_dict.update({'manjeet': '3'})
iniordered_dict.move_to_end('manjeet', last=False)
 
# Printing result
print("Resultant Dictionary : "+str(iniordered_dict))