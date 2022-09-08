import tabula as tb
import pandas as pd
import re
import numpy as np

file = '2022_01_22.pdf'
data = tb.read_pdf(file, area = (80, 70, 600, 115), pages = '1')

#print(data)

dataArr = np.array(data)
print (dataArr)