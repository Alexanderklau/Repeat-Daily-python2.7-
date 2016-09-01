from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager#,process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    restr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr,restr,laparams=laparams)

    #process_pdf(rsrcmgr,device,pdfFile)
    device.close()
    content = restr.getvalue()
    restr.close()
    return content
pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()


