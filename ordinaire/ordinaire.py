import string

import mysql.connector

import streamlit as st


class COrdinaire:
    def __init__(self):
        self.connection = mysql.connector.connect(**st.secrets.ordinairedb)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def search_in_database(self, title: string, type: string) -> string:
        sql_query = "SELECT text from {} WHERE title = '{}';".format(type, title)
        self.cursor.execute(sql_query)
        return self.cursor.fetchall()[0][0]

    def get_list(self, type: string) -> string:
        sql_query = "SELECT title from {} ;".format(type)
        self.cursor.execute(sql_query)
        kyrie_list = self.cursor.fetchall()
        return [title[0] for title in kyrie_list]


def get_kyrie_list():
    database = COrdinaire()
    kyrie_list = database.get_list("kyrie")
    database.close()
    return kyrie_list


def get_kyrie_text(kyrie_title: string) -> string:
    database = COrdinaire()
    kyrie_text = database.search_in_database(kyrie_title, "kyrie")
    database.close()
    return kyrie_text


def get_sanctus_list():
    database = COrdinaire()
    sanctus_list = database.get_list("sanctus")
    database.close()
    return sanctus_list


def get_sanctus_text(sanctus_title: string) -> string:
    database = COrdinaire()
    sanctus_text = database.search_in_database(sanctus_title, "sanctus")
    database.close()
    return sanctus_text


def get_agnus_list():
    database = COrdinaire()
    agnus_list = database.get_list("agnus")
    database.close()
    return agnus_list


def get_agnus_text(agnus_title: string) -> string:
    database = COrdinaire()
    agnus_text = database.search_in_database(agnus_title, "agnus")
    database.close()
    return agnus_text


def get_gloria_list():
    database = COrdinaire()
    gloria_list = database.get_list("gloria")
    database.close()
    return gloria_list


def get_gloria_text(gloria_title: string) -> string:
    database = COrdinaire()
    gloria_text = database.search_in_database(gloria_title, "gloria")
    database.close()
    return gloria_text


if __name__ == "__main__":
    get_kyrie_list()
    print(get_kyrie_list())
    print(get_kyrie_text("Latin"))
