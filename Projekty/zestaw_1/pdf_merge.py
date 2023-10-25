from PyPDF2 import PdfWriter


def merge_pdf(*filenames, output='merged-pdf.pdf'):
    merger = PdfWriter()

    for pdf in filenames:
        merger.append(pdf)

    merger.write(output)
    merger.close()


merge_pdf('file1.pdf', 'file2.pdf', output='merged1.pdf')
merge_pdf('file2.pdf', 'file1.pdf', output='merged2.pdf')
