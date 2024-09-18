import numpy as np

#numerical

#np.sort()
np1 = np.array([6,7,4,9,0,2,1])

#print(np.sort(np1))


#alphabetical
#np2 = np.array(["john", "tina", "anjali", "aviral", "mittal"])
#print(np.sort(np2))

# boolean
#np3 = np.array([True, False, True])
#print(np.sort(np3))

#return a copy not change the original
print(np1)
print(np.sort(np1))  # just returning a copy - not changes in original
print(np1)

# 2-d
np4 = np.array([[6,7,1,9],[4,6,7,2]])
print(np.sort(np4))