import numpy as np

def convert2d(arr2, reportArr):

    for i in range(1,len(arr2)-1):
        if arr2[i-1,0] == arr2[i,0]:
            arr2 = np.delete(arr2, (i), axis = 0)

    pageArr = np.array([])

    for i in range (0,len(arr2)):
        for j in reportArr:
            if arr2[i,0] == j :
                pageArr = np.append(pageArr, arr2[i,1])

    reportArr = np.stack((reportArr, pageArr), axis=1)
    reportArr = reportArr.astype(int)
    np.sort(reportArr)
    return reportArr
