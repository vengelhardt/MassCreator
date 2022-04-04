import re

from docx import Document


class CWord:
    def __init__(self, template_path):
        self.template_path = template_path
        self.file_path = template_path.split('.')[0] + "-filled.docx"
        self.docx = Document(template_path)
        self.section_list = self.get_keywords()

    def print(self):
        for section in self.section_list:
            print(section)

    def get_keywords(self):
        section_list = []
        for para in self.docx.paragraphs:
            match = re.match(r"^<(.*)\.(.*)>", para.text)
            if match:
                section_name = match.group(1)
                section_type = match.group(2)
                section_list.append({section_name: section_type})
        return section_list

    def find_and_replace(self, item):
        for key, value in item.items():
            for para in self.docx.paragraphs:
                match = re.match(rf"^<{key}>", para.text)
                if match:
                    print("Found")
                    para.text = value
                    self.docx.save(self.file_path)
                else:
                    print(f"Item {key} was not found in the word file.")


if __name__ == "__main__":
    word = CWord("template.docx")
    word.find_and_replace({"sortie.text": "coucou"})
    word.print()
