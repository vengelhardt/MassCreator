import string

import mysql.connector
import streamlit as st


class COrdinaire:
    st.cache(allow_output_mutation=True)

    def __init__(self):
        self.connection = mysql.connector.connect(**st.secrets.ordinairedb)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def search_in_database(self, title: string, type: string) -> string:
        sql_query = "SELECT text from {} WHERE title = '{}';".format(type, title)
        self.cursor.execute(sql_query)
        return self.cursor.fetchall()[0][0]

    st.cache(allow_output_mutation=True)

    def get_list(self, type: string) -> string:
        sql_query = "SELECT title from {} ;".format(type)
        self.cursor.execute(sql_query)
        kyrie_list = self.cursor.fetchall()
        return [title[0] for title in kyrie_list]

    st.cache(allow_output_mutation=True)

    def get_kyrie_list(self):
        kyrie_list = self.get_list("kyrie")
        return kyrie_list

    st.cache(allow_output_mutation=True)

    def get_kyrie_text(self, kyrie_title: string) -> string:
        kyrie_text = self.search_in_database(kyrie_title, "kyrie")
        return kyrie_text

    st.cache(allow_output_mutation=True)

    def get_sanctus_list(self):
        sanctus_list = self.get_list("sanctus")
        return sanctus_list

    st.cache(allow_output_mutation=True)

    def get_sanctus_text(self, sanctus_title: string) -> string:
        sanctus_text = self.search_in_database(sanctus_title, "sanctus")
        return sanctus_text

    st.cache(allow_output_mutation=True)

    def get_agnus_list(self):
        agnus_list = self.get_list("agnus")
        return agnus_list

    st.cache(allow_output_mutation=True)

    def get_agnus_text(self, agnus_title: string) -> string:
        agnus_text = self.search_in_database(agnus_title, "agnus")
        return agnus_text

    st.cache(allow_output_mutation=True)

    def get_gloria_list(self):
        gloria_list = self.get_list("gloria")
        return gloria_list

    st.cache(allow_output_mutation=True)

    def get_gloria_text(self, gloria_title: string) -> string:
        gloria_text = self.search_in_database(gloria_title, "gloria")
        return gloria_text


if __name__ == "__main__":
    ordinairedb = COrdinaire()
    print(ordinairedb.get_kyrie_list())
    ordinairedb.close()
