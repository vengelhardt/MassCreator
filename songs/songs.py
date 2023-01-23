import string

import mysql.connector
import streamlit as st
import re


class CDatabaseAPI:
    def __init__(self):
        self.connection = mysql.connector.connect(**st.secrets.songsdb)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    @st.cache
    def get_title_list(self):
        sql_query = "SELECT title from song ;"
        self.cursor.execute(sql_query)
        title_list = self.cursor.fetchall()
        return [title[0] for title in title_list]

    @st.cache
    def get_song_list(self):
        song_list = self.get_title_list()
        return song_list

    @st.cache
    def get_song_dict_from_title(self, song_title: string, verses_nb: int) -> dict:
        song = CSong(self, song_title, "", [], verses_nb)
        song.search_in_database()
        return song.get_dict()

    @st.cache
    def append_song(self, title: string, refrain: string, verses: list):
        song = CSong(self, title, refrain, verses, len(verses))
        song.append()

    @st.cache
    def modify_song(self, title: string, refrain: string, verses: list):
        song = CSong(self, title, "", [], 0)
        song.search_in_database()
        song.modify(refrain, verses)

    @st.cache
    def delete_song(self, title: string):
        song = CSong(self, title, "", [], 0)
        song.search_in_database()
        song.delete()


class CSong:
    def __init__(self, database_api, song_title, refrain, verses, verses_nb):
        self.title = song_title
        self.database_api = database_api
        self.verses_nb = verses_nb
        self.refrain = refrain
        self.verses = verses

    @st.cache
    def _init_refrain(self):
        sql_refrain_query = "SELECT refrain from song WHERE title LIKE '{}%';".format(
            self.title
        )
        self.database_api.cursor.execute(sql_refrain_query)
        refrain = self.database_api.cursor.fetchall()[0][0]
        return refrain

    @st.cache
    def _init_verses(self):
        for verse_id in range(4):
            sql_verse_query = (
                "SELECT couplet{} from song WHERE title LIKE '{}%';".format(
                    verse_id + 1, self.title
                )
            )
            self.database_api.cursor.execute(sql_verse_query)
            verse = self.database_api.cursor.fetchall()[0][0]
            if verse and verse_id < self.verses_nb:
                self.verses.append(verse)
            else:
                self.verses.append("")

    @st.cache
    def search_in_database(self):
        self.refrain = self._init_refrain()
        self._init_verses()

    @st.cache
    def append(self):
        title = re.sub("'", "\\'", self.title)
        refrain = re.sub("'", "\\'", self.refrain)
        verse_0 = re.sub("'", "\\'", self.verses[0])
        verse_1 = re.sub("'", "\\'", self.verses[1])
        verse_2 = re.sub("'", "\\'", self.verses[2])
        verse_3 = re.sub("'", "\\'", self.verses[3])
        sql_query = f"INSERT INTO song (title, refrain, couplet1, couplet2, couplet3, couplet4) select '{title}', '{refrain}', '{verse_0}', '{verse_1}', '{verse_2}', '{verse_3}' where not exists (Select title from song where title = '{title}');"
        print(sql_query)
        self.database_api.cursor.execute(sql_query)
        self.database_api.connection.commit()

    @st.cache
    def modify(self, refrain, verses):
        refrain_filt = re.sub("'", "\\'", refrain)
        verse_0 = re.sub("'", "\\'", verses[0])
        verse_1 = re.sub("'", "\\'", verses[1])
        verse_2 = re.sub("'", "\\'", verses[2])
        verse_3 = re.sub("'", "\\'", verses[3])
        sql_query = "UPDATE song SET refrain = '{}', couplet1 = '{}', couplet2 = '{}', couplet3 = '{}', couplet4 = '{}' WHERE title = '{}'".format(
            refrain_filt, verse_0, verse_1, verse_2, verse_3, self.title
        )
        self.database_api.cursor.execute(sql_query)
        self.database_api.connection.commit()

    @st.cache
    def delete(self):
        sql_query = "DELETE FROM song WHERE title = '{}'".format(self.title)
        self.database_api.cursor.execute(sql_query)
        self.database_api.connection.commit()

    @st.cache
    def get_dict(self):
        return {"title": self.title, "refrain": self.refrain, "verses": self.verses}

    @st.cache
    def display(self):
        print("Titre: {}".format(self.title))
        print("Refrain: {}".format(self.refrain))
        for verse in range(self.verses_nb):
            print("Verse {}: {}".format(verse, self.verses[verse]))


if __name__ == "__main__":
    append_song("test", "salut", ["hello"])
