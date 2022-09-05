import sqlite3
import string


class CDatabaseAPI:
    def __init__(self):
        self.connection = sqlite3.connect("songs/song.db")
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def get_title_list(self):
        sql_query = "SELECT title from song ;"
        self.cursor.execute(sql_query)
        title_list = self.cursor.fetchall()
        return [title[0] for title in title_list]


class CSong:
    def __init__(self, database_api, song_title, verses_nb):
        self.title = song_title
        self.database_api = database_api
        self.verses_nb = verses_nb
        self.refrain = self._init_refrain()
        self.verses = []
        self._init_verses()

    def _init_refrain(self):
        sql_refrain_query = "SELECT refrain from song WHERE title GLOB '{}*';".format(
            self.title
        )
        self.database_api.cursor.execute(sql_refrain_query)
        refrain = self.database_api.cursor.fetchall()[0][0]
        return refrain

    def _init_verses(self):
        for verse_id in range(4):
            sql_verse_query = (
                "SELECT couplet{} from song WHERE title GLOB '{}*';".format(
                    verse_id + 1, self.title
                )
            )
            self.database_api.cursor.execute(sql_verse_query)
            verse = self.database_api.cursor.fetchall()[0][0]
            if verse and verse_id < self.verses_nb:
                self.verses.append(verse)
            else:
                self.verses.append("")

    def get_dict(self):
        return {"title": self.title, "refrain": self.refrain, "verses": self.verses}

    def display(self):
        print("Titre: {}".format(self.title))
        print("Refrain: {}".format(self.refrain))
        for verse in range(self.verses_nb):
            print("Verse {}: {}".format(verse, self.verses[verse]))


def get_song_list() -> list:
    database = CDatabaseAPI()
    song_list = database.get_title_list()
    database.close()
    return song_list


def get_song_dict_from_title(song_title: string, verses_nb: int) -> dict:
    database = CDatabaseAPI()
    song = CSong(database, song_title, verses_nb)
    database.close()
    return song.get_dict()


if __name__ == "__main__":
    song_list = get_song_list()
    print(song_list)
    dico = get_song_dict_from_title(song_list[1], 2)
    print(dico)
