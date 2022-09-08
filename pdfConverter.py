import tabula as tb
import pandas as pd
import re
import numpy as np

file = '2022_01_22.pdf'
data = tb.read_pdf(file, area = (70, 70, 600, 115), pages = '1')
#print(data)

dataRaw = np.array(data[0])
#print(dataRaw)

dataArr = np.fromiter(dataRaw, dtype= int)
print(dataArr)

