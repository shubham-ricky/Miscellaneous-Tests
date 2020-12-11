# -*- coding: utf-8 -*-

#Solution for Question 3
"""
Question 3:
Return the list of indices. The indices is a sublist points to the same person. 
The same persons means they have the same name or email or phone. eg:
data = [
("username1","phone_number1", "email1"),
("usernameX","phone_number1", "emailX"),
("usernameZ","phone_numberZ", "email1Z"),
("usernameY","phone_numberY", "emailX"),
]
expected: [[0,1,3][2]]
"""

import numpy as np

data = [("username1","phone_number1", "email1"), 
              ("usernameX","phone_number1", "emailX"), 
              ("usernameZ","phone_numberZ", "email1Z"), 
              ("usernameY","phone_numberY", "emailX"),
               ] 

data = np.array(data)

# Matrix indicating same name or email or phone
datamatrix = sum(user == data for user in data)

# Persons not with same name or email or phone
notsame = set(np.where(np.sum(datamatrix, axis=1) == data.shape[1])[0])

# Persons with same name or email or phone
same = set(range(len(data))) ^ set(notsame)

# Return the list of indices
ListofIndices = [same, notsame]
print(ListofIndices)





