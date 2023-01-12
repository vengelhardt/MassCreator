import streamlit as st

import aelf.aelf as aelf
import songs.songs as songs
import ordinaire.ordinaire as ordinaire
import word.word as word

st.set_page_config(layout="centered", page_icon="📝", page_title="Feuille de Messe")
st.header("Générateur de livret de Messe 😇")
st.write(
    "Séléctionnez la date souhaitée pour la messe, ainsi que les différents chants, puis cliquez sur Générer. Vous pouvez aussi aujouter un chant si celui-ci n'est pas encore dans la base de donnée."
)

tab1, tab2, tab3 = st.tabs(["Génération", "Ajout de chants", "Modifier un chant"])
# Tab 1
with tab1:
    # Date
    massDate = st.date_input("📆 Date de la messe")

    # Texte Before
    before = st.text_input("Before")

    # Texte PU
    pu = st.text_input("Prière Universelle")

    # Ordinaire
    st.write("🗞️ Sélectionner l'ordinaire")
    with st.container():
        left, right = st.columns(2)
        kyrieTitle = left.selectbox("Kyrie", (ordinaire.get_kyrie_list()))
        kyrieText = ordinaire.get_kyrie_text(kyrieTitle)
        right.write(kyrieText)

    with st.container():
        left, right = st.columns(2)
        sanctusTitle = left.selectbox("Sanctus", (ordinaire.get_sanctus_list()))
        sanctusText = ordinaire.get_sanctus_text(sanctusTitle)
        right.write(sanctusText)

    with st.container():
        left, right = st.columns(2)
        agnusTitle = left.selectbox("Agnus", (ordinaire.get_agnus_list()))
        agnusText = ordinaire.get_agnus_text(agnusTitle)
        right.write(agnusText)

    with st.container():
        left, right = st.columns(2)
        gloriaTitle = left.selectbox("Gloria", (ordinaire.get_gloria_list()))
        gloriaText = ordinaire.get_gloria_text(gloriaTitle)
        right.write(gloriaText)

    # Chants
    st.write("🎹 Sélectionner les chants")
    with st.container():
        left, center, right = st.columns(3)
        entrySongTitle = left.selectbox("Chant d'entrée", (songs.get_song_list()))
        entrySongNb = center.slider("Couplet 1", 1, 4, 4)
        entrySong = songs.get_song_dict_from_title(entrySongTitle, entrySongNb)
        right.write(entrySong["refrain"])

    with st.container():
        left, center, right = st.columns(3)
        communionSongTitle = left.selectbox(
            "Chant de communion", (songs.get_song_list())
        )
        communionSongNb = center.slider("Couplet 2", 1, 4, 4)
        communionSong = songs.get_song_dict_from_title(
            communionSongTitle, communionSongNb
        )
        right.write(communionSong["refrain"])

    with st.container():
        left, center, right = st.columns(3)
        sortieSongTitle = left.selectbox("Chant de sortie", (songs.get_song_list()))
        sortieSongNb = center.slider("Couplet 3", 1, 4, 4)
        sortieSong = songs.get_song_dict_from_title(sortieSongTitle, sortieSongNb)
        right.write(sortieSong["refrain"])

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

# Second tab
with tab2:
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
        print(songs.get_song_list())
        if (
            couplet1
            and couplet2
            and couplet3
            and couplet4
            and refrain
            and titre not in songs.get_song_list()
        ):
            print(refrain)

# Third tab
with tab3:
    songToModify = st.selectbox("Chant à modifier", (songs.get_song_list()))
