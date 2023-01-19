import string

import mysql.connector

import streamlit as st


class CDatabaseAPI:
    @st.experimental_singleton
    def __init__(self):
        self.connection = mysql.connector.connect(**st.secrets.songsdb)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def get_title_list(self):
        sql_query = "SELECT title from song ;"
        self.cursor.execute(sql_query)
        title_list = self.cursor.fetchall()
        return [title[0] for title in title_list]


class CSong:
    def __init__(self, database_api, song_title, refrain, verses, verses_nb):
        self.title = song_title
        self.database_api = database_api
        self.verses_nb = verses_nb
        self.refrain = refrain
        self.verses = verses

    def _init_refrain(self):
        sql_refrain_query = "SELECT refrain from song WHERE title LIKE '{}%';".format(
            self.title
        )
        self.database_api.cursor.execute(sql_refrain_query)
        refrain = self.database_api.cursor.fetchall()[0][0]
        return refrain

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

    def search_in_database(self):
        self.refrain = self._init_refrain()
        self._init_verses()

    def append(self):
        sql_query = "INSERT INTO song (title, refrain, couplet1, couplet2, couplet3, couplet4) VALUES({}, {}, {}, {}, {}, {});".format(
            self.title,
            self.refrain,
            self.verses[0],
            self.verses[1],
            self.verses[2],
            self.verses[3],
        )
        self.database_api.cursor.execute(sql_query)
        self.database_api.commit()

    def get_dict(self):
        return {"title": self.title, "refrain": self.refrain, "verses": self.verses}

    def display(self):
        print("Titre: {}".format(self.title))
        print("Refrain: {}".format(self.refrain))
        for verse in range(self.verses_nb):
            print("Verse {}: {}".format(verse, self.verses[verse]))


def get_song_list():
    database = CDatabaseAPI()
    song_list = database.get_title_list()
    database.close()
    return song_list


def get_song_dict_from_title(song_title: string, verses_nb: int) -> dict:
    database = CDatabaseAPI()
    song = CSong(database, song_title, "", [], verses_nb)
    song.search_in_database()
    database.close()
    return song.get_dict()


def append_song(title: string, refrain: string, verses: list):
    database = CDatabaseAPI()
    song = CSong(database, title, refrain, verses, len(verses))
    song.append()
    database.close()


if __name__ == "__main__":
    append_song("test", "salut", ["hello"])
