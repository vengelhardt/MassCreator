import streamlit as st

import aelf.aelf as aelf
import ordinaire.ordinaire as ordinaire
import songs.songs as songs
import word.word as word

st.set_page_config(layout="centered", page_icon="📝", page_title="Feuille de Messe")
st.header("Générateur de livret de Messe 😇")
st.write(
    "Séléctionnez la date souhaitée pour la messe, ainsi que les différents chants, puis cliquez sur Générer. Vous pouvez aussi aujouter un chant si celui-ci n'est pas encore dans la base de donnée."
)

tab1, tab2, tab3 = st.tabs(["Génération", "Ajout de chants", "Modifier un chant"])

# Tab 1 : Generate songbook
with tab1:
    # Date
    massDate = st.date_input("📆 Date de la messe")

    # Texte Before
    before = st.text_input("Before")

    # Texte PU
    pu = st.text_input("Prière Universelle")

    # Ordinaire
    st.write("🗞️ Sélectionner l'ordinaire")
    ordinairedb = ordinaire.COrdinaire()
    with st.container():
        left, right = st.columns(2)
        kyrieTitle = left.selectbox("Kyrie", (ordinairedb.get_kyrie_list()))
        kyrieText = ordinairedb.get_kyrie_text(kyrieTitle)
        right.write(kyrieText)
    with st.container():
        left, right = st.columns(2)
        sanctusTitle = left.selectbox("Sanctus", (ordinairedb.get_sanctus_list()))
        sanctusText = ordinairedb.get_sanctus_text(sanctusTitle)
        right.write(sanctusText)
    with st.container():
        left, right = st.columns(2)
        agnusTitle = left.selectbox("Agnus", (ordinairedb.get_agnus_list()))
        agnusText = ordinairedb.get_agnus_text(agnusTitle)
        right.write(agnusText)
    with st.container():
        left, right = st.columns(2)
        gloriaTitle = left.selectbox("Gloria", (ordinairedb.get_gloria_list()))
        gloriaText = ordinairedb.get_gloria_text(gloriaTitle)
        right.write(gloriaText)

    ordinairedb.close()

    # Chants
    st.write("🎹 Sélectionner les chants")
    songsdb = songs.CDatabaseAPI()
    with st.container():
        left, center, right = st.columns(3)
        entrySongTitle = left.selectbox("Chant d'entrée", (songsdb.get_song_list()))
        entrySongNb = center.slider("Couplet 1", 1, 4, 4)
        entrySong = songsdb.get_song_dict_from_title(entrySongTitle, entrySongNb)
        right.write(entrySong["refrain"])
    with st.container():
        left, center, right = st.columns(3)
        communionSongTitle = left.selectbox(
            "Chant de communion", (songsdb.get_song_list())
        )
        communionSongNb = center.slider("Couplet 2", 1, 4, 4)
        communionSong = songsdb.get_song_dict_from_title(
            communionSongTitle, communionSongNb
        )
        right.write(communionSong["refrain"])
    with st.container():
        left, center, right = st.columns(3)
        sortieSongTitle = left.selectbox("Chant de sortie", (songsdb.get_song_list()))
        sortieSongNb = center.slider("Couplet 3", 1, 4, 4)
        sortieSong = songsdb.get_song_dict_from_title(sortieSongTitle, sortieSongNb)
        right.write(sortieSong["refrain"])

    songsdb.close()

    # Génération
    generate = st.button(
        "Générer",
        None,
        "Appuyer ici après avoir sélectionné tous le champs.",
        None,
        None,
        None,
    )
    if generate:
        doc = word.CWord("word/template.docx")
        # Géneration lecture
        firstLecture = aelf.get_first_reading(str(massDate), "france")
        print(firstLecture)
        doc.find_and_replace(firstLectureTitle=firstLecture["intro_lue"])
        doc.find_and_replace(firstLectureText=firstLecture["contenu"])
        secondLecture = aelf.get_second_reading(str(massDate), "france")
        doc.find_and_replace(secondLectureTitle=secondLecture["intro_lue"])
        doc.find_and_replace(secondLectureText=secondLecture["contenu"])
        goodNews = aelf.get_evangile(str(massDate), "france")
        doc.find_and_replace(goodnewsTitle=goodNews["intro_lue"])
        doc.find_and_replace(goodnewsText=goodNews["contenu"])
        psalm = aelf.get_psalm(str(massDate), "france")
        doc.find_and_replace(psalmRefrain=psalm["refrain_psalmique"])
        doc.find_and_replace(psalmText=psalm["contenu"])
        # Date
        date = aelf.get_date(str(massDate), "france")
        week = aelf.get_week(str(massDate), "france")
        doc.find_and_replace(dateText=date)
        doc.find_and_replace(dateWeek=week)
        # Before
        doc.find_and_replace(beforeText=before)
        # PU
        doc.find_and_replace(puText=pu)
        # Ordinaire
        doc.find_and_replace(kyrieText=kyrieText)
        doc.find_and_replace(sanctusText=sanctusText)
        doc.find_and_replace(agnusText=agnusText)
        doc.find_and_replace(gloriaText=gloriaText)
        # Songs
        doc.find_and_replace(accueilRefrain=entrySong["refrain"])
        print(entrySong)
        doc.find_and_replace(
            accueilVerse1=entrySong["verses"][0],
            accueilVerse2=entrySong["verses"][1],
            accueilVerse3=entrySong["verses"][2],
            accueilVerse4=entrySong["verses"][3],
        )
        doc.find_and_replace(communionRefrain=communionSong["refrain"])
        doc.find_and_replace(
            communionVerse1=communionSong["verses"][0],
            communionVerse2=communionSong["verses"][1],
            communionVerse3=communionSong["verses"][2],
            communionVerse4=communionSong["verses"][3],
        )
        doc.find_and_replace(sortieRefrain=sortieSong["refrain"])
        doc.find_and_replace(
            sortieVerse1=sortieSong["verses"][0],
            sortieVerse2=sortieSong["verses"][1],
            sortieVerse3=sortieSong["verses"][2],
            sortieVerse4=sortieSong["verses"][3],
        )
        # Done
        st.balloons()
        st.success("🎉 La feuille est disponible au téléchargement !")
        # Download
        with open("word/template_filled.docx", "rb") as f:
            st.download_button(
                label="Telecharger la feuille de messe",
                data=f,
                file_name="messe.docx",
                mime="word/docx",
            )

# Second tab : add song
with tab2:
    songsdb = songs.CDatabaseAPI()
    st.write("Coucou")
    titre = st.text_input("Titre")
    refrain = st.text_input("Refrain")
    couplet1 = st.text_input("Couplet 1")
    couplet2 = st.text_input("Couplet 2")
    couplet3 = st.text_input("Couplet 3")
    couplet4 = st.text_input("Couplet 4")

    ajouter = st.button(
        "Ajouter",
        None,
        "Appuyer ici pour ajouter le chant à la base de donnée.",
        None,
        None,
        None,
    )
    if ajouter:
        print(songsdb.get_song_list())
        if (
            couplet1
            and couplet2
            and couplet3
            and couplet4
            and refrain
            and titre not in songsdb.get_song_list()
        ):
            songsdb.append_song(titre, refrain, [couplet1, couplet2, couplet3, couplet4])
            songsdb.close()

# Third tab : modify
with tab3:
    songsdb = songs.CDatabaseAPI()
    songToModify = st.selectbox("Chant à modifier", (songsdb.get_song_list()))
    oldSong = songsdb.get_song_dict_from_title(songToModify, 4)
    mod_refrain = st.text_input("Nouveau Refrain", oldSong["refrain"])
    mod_couplet1 = st.text_input("Nouveau Couplet 1", oldSong["verses"][0])
    mod_couplet2 = st.text_input("Nouveau Couplet 2", oldSong["verses"][1])
    mod_couplet3 = st.text_input("Nouveau Couplet 3", oldSong["verses"][2])
    mod_couplet4 = st.text_input("Nouveau Couplet 4", oldSong["verses"][3])
    modify = st.button(
        "Modifier",
        None,
        "Appuyer ici après avoir sélectionné tous le champs.",
        None,
        None,
        None,
    )
    if modify:
        songsdb.modify_song(
            songToModify,
            mod_refrain,
            [mod_couplet1, mod_couplet2, mod_couplet3, mod_couplet4],
        )
        songsdb.close()

    delete = st.button(
        "Supprimer",
        None,
        "Appuyer ici pour supprimer le chant sélectionné",
        None,
        None,
        None,
    )
    if delete:
        songsdb.delete_song(songToModify)
        songsdb.close()
