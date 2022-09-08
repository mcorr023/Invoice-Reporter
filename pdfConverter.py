import tabula as tb
import PyPDF2 as pypdf
import re
import numpy as np

file = '2022_01_22.pdf'
def importReport():
    data = tb.read_pdf(file, area = (70, 70, 600, 115), pages = '1')
    dataRaw = np.array(data[0])
    dataArr = np.fromiter(dataRaw, dtype= int)
    return dataArr

object = pypdf.PdfFileReader(file)

def importInvoices():
    NumPages = object.getNumPages()
    astring = "INVOICE: "
    invoiceArr = np.array([])

    for i in range(1, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText() 
        match = re.search(astring, Text)
        if (match):
            invoiceNumSpan = match.span()
            lastSpan = invoiceNumSpan[1]
            invoiceNum = int(Text[lastSpan: lastSpan+ 6])
            invoiceArr = np.append(invoiceArr,invoiceNum)
            #invoiceArr = np.append(invoiceArr,np.array([i+1]).transpose(), axis=0)

    invoiceArr = invoiceArr.astype(int)
    return invoiceArr