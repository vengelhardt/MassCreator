from pylatex import Document, Section, Subsection
import aelf.aelf as aelf


def make_doc(date, zone):
    geometry_options = {"tmargin": "1cm", "lmargin": "10cm"}
    doc = Document(geometry_options=geometry_options)

    # Premiere lecture
    first_reading = aelf.get_first_reading(date, zone)
    with doc.create(Section("1ère Lecture: {}".format(first_reading["ref"]), numbering=False)):
        doc.append(first_reading["contenu"])

    # Psaume
    with doc.create(Section("Psaume", numbering=False)):
        doc.append("TODO")

    # Deuxieme lecture
    second_reading = aelf.get_second_reading(date, zone)
    with doc.create(Section("2eme Lecture: {}".format(second_reading["ref"]), numbering=False)):
        doc.append(second_reading["contenu"])

    # Evangile
    evangile = aelf.get_evangile(date, zone)
    with doc.create(Section("Évangile: {}".format(evangile["ref"]), numbering=False)):
        doc.append(evangile["contenu"])


    doc.generate_pdf('full', clean_tex=True)
