from tkinter import font
from docx import Document
from docx.shared import Pt

import aelf.aelf as aelf


def make_word(date, zone):
    document = Document()
    document.add_heading("Feuille de messe", 0)

    # Entête TODO
    mass_date = aelf.get_date(date, zone)
    mass_week = aelf.get_week(date, zone)
    document.add_paragraph(mass_date, style="Intense Quote")
    document.add_paragraph(mass_week, style="Intense Quote")

    # Before TODO
    # Chant d'entrée (Accueuil) TODO
    # Rite pénitentiel (Kyrie) TODO

    # Premiere lecture
    first_reading = aelf.get_first_reading(date, zone)
    document.add_heading(f"Premiere Lecture : {first_reading['ref']}", level=1)
    document.add_paragraph(first_reading["contenu"], style="Intense Quote")

    # Psaume (TODO)

    # Deuxieme lecture
    second_reading = aelf.get_second_reading(date, zone)
    document.add_heading(f"Seconde Lecture : {second_reading['ref']}", level=1)
    document.add_paragraph(second_reading["contenu"], style="Intense Quote")

    # Acclamation de l'Evangile TODO

    # Evangile
    evangile = aelf.get_evangile(date, zone)
    document.add_heading(f"Evangile : {evangile['ref']}", level=1)
    document.add_paragraph(evangile["contenu"], style="Intense Quote")

    # Sanctus TODO

    # Anamnèse
    document.add_heading("Anamnèse", level=1)

    # Doxologie
    document.add_heading("Doxologie", level=1)

    # Notre père
    document.add_heading("Notre Père", level=1)

    # Agnus TODO

    # Communion TODO

    # TIC
    document.add_heading("TIC", level=1)

    # Envoi TODO

    document.save("demo1.docx")


if __name__ == "__main__":
    make_word()
