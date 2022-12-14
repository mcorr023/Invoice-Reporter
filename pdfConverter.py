import tabula as tb
import PyPDF2 as pypdf
import re
import numpy as np

astring = "INVOICE: "
bstring = "Invoice Report"

def importReport(file):
    object = pypdf.PdfFileReader(file)
    NumPages = object.getNumPages()
    
    for i in range(0,NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText() 
        match = re.search(bstring, Text)
        if(match):
            data = tb.read_pdf(file, area = (70, 70, 600, 115), pages = str(i+1))
            dataRaw = np.array(data[0])
            dataArr = np.fromiter(dataRaw, dtype= int)
    return dataArr


def importInvoices(file):
    object = pypdf.PdfFileReader(file)
    NumPages = object.getNumPages()
    invoiceArr = np.empty([0,2])

    for i in range(1, NumPages):
        PageObj = object.getPage(i)
        Text = PageObj.extractText() 
        match = re.search(astring, Text)
        if (match):
            invoiceNumSpan = match.span()
            lastSpan = invoiceNumSpan[1]
            invoiceNum = int(Text[lastSpan: lastSpan+ 6])
            invoiceArr = np.append(invoiceArr, np.array([[invoiceNum, i+1]]), axis =0)

    invoiceArr = invoiceArr.astype(int)
    return invoiceArr
   
