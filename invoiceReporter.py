

def report(arr1, arr2):
    #sort report and invoices
    arr1.sort()
    arr2.sort(key=lambda x: x[1])

    missing = []
    completed, duplicate, extra = [[]]

    for i in range (len(arr1)-1,0,-1):
        for j in range (len(arr2)-1,0,-1):
            if arr2[j,:] == arr1[i]:
                completed.append(arr2[j,:])
            if arr1[i] not in arr2[j,:]:
                missing.append(arr1[i])
            if arr2[j,:] not in arr1[i]:
                extra.append(arr2[j,:])
            if arr2[j,:] == arr2[j-1,:]:
                duplicate.append(arr2[j,:])

    print("Completed: " + completed)
    print("Missing: " + missing)
    print("Duplicates: " + duplicate)
    print("Extras: " + extra)

test1 = [111,222,333,444,555,666,777]
test2 = [[111,2],[222,3],[222,4],[444,5]]

report(test1,test2)




