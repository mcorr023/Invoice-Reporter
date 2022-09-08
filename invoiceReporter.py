
def report(arr1, arr2):
    #sort report and invoices
    arr1.sort()
    arr2.sort()

    completed= []
    duplicates = []

    for i in range(len(arr2)):
        if arr2[i] == arr2[i-1]:
            duplicates.append(arr2[i])

    arr2 = list(set(arr2))

    missing = list(arr1-arr2)
    extras = list(arr2-arr1) 
    
    for i in arr1:
        for j in arr2:
            if i == j :
                completed.append(i)

    print("Completed: ", completed)
    print("Missing: ", missing)
    print("Duplicates: ",  duplicates)
    print("Extras: ", extras)

test1 = ["111","222","333","444","555","666","777"]
test2 = ["111","222","222","444", "888"]

report(test1,test2)




