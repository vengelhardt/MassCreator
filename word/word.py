from docx import Document

def make_word():
    document = Document()
    document.add_heading('Feuille de messe', 0)
    document.add_heading('Heading, level 1', level=1)
    document.add_paragraph('Intense quote', style='Intense Quote')
    document.add_paragraph(
        'first item in unordered list', style='List Bullet'
    )
    document.add_paragraph(
        'first item in ordered list', style='List Number'
    )
    document.add_page_break()
    document.save('demo.docx')

if __name__ =="__main__":
    make_word()
