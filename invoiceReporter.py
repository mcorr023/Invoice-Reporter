import numpy as np
import convert2dArrays

def report(arr1, arr2):
    #sort report and invoices
    arr2a = np.array(arr2[:,0])
    u, c = np.unique(arr2a, return_counts=True)
    duplicates = u[c > 1]

    arr1 = set(arr1)
    arr2a = set(arr2a)

    missing = np.array((sorted(arr1 - arr2a)))
    extras = np.array((sorted(arr2a - arr1)))

    completed = np.array([])
    for i in arr1:
        for j in arr2a:
            if i == j :
                completed = np.append(completed, i)

    duplicates = convert2dArrays.convert2d(arr2, duplicates)
    completed = convert2dArrays.convert2d(arr2, completed)
    extras = convert2dArrays.convert2d(arr2, extras)

    str1 = "Completed: \n" + str(completed)
    str2 = "\nDuplicates: \n" + str(duplicates)
    str3 = "\nExtras: \n" + str(extras)
    str4 = "\nMissing: \n"+ str(missing)

    return str1 + str2 + str3 + str4 

# test1 = np.array([111, 222, 333, 444, 555, 666, 777])
# test2 = np.array([[111, 2], [222, 3], [222, 4], [444, 5], [888, 6], [999, 7], [444, 8]])

# report(test1,test2)




