import numpy as np

def report(arr1, arr2):
    #sort report and invoices
    np.sort(arr1)
    np.sort(arr2)

    completed = np.array([])
    duplicates = np.array([])

    for i in range(len(arr2)):
        if arr2[i] == arr2[i-1]:
            duplicates = np.append(duplicates,arr2[i])

    arr1 = set(arr1)
    arr2 = set(arr2)

    missing = list(sorted(arr1 - arr2))
    extras = list(sorted(arr2 - arr1))
    
    for i in arr1:
        for j in arr2:
            if i == j :
                completed = np.append(completed, i)

    print("Completed: ", completed)
    print("Duplicates: ",  duplicates)
    print("Extras: ", extras)
    print("Missing: ", missing)

test1 = np.array(['111','222','333','444','555','666','777'])
test2 = np.array(['111','222','222','444', '888'])

report(test1,test2)




