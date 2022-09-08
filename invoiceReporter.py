import numpy as np

def report(arr1, arr2):
    #sort report and invoices

    u, c = np.unique(arr2, return_counts=True)
    duplicates = u[c > 1]

    arr1 = set(arr1)
    arr2 = set(arr2)

    missing = np.array((sorted(arr1 - arr2)))
    extras = np.array((sorted(arr2 - arr1)))

    completed = np.array([])
    for i in arr1:
        for j in arr2:
            if i == j :
                completed = np.append(completed, [i])

    np.sort(completed)

    print("Completed: ", completed)
    print("Duplicates: ", duplicates)
    print("Extras: ", extras)
    print("Missing: ", missing)

test1 = np.array(['111', '222', '333', '444', '555', '666', '777'])
test2 = np.array(['111', '222', '222', '444', '888', '999', '444'])

report(test1,test2)




