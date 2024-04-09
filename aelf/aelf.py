import datetime
import re

import requests
import streamlit as st

AELF_API_SITE = "https://api.aelf.org"
AELF_CMD_INFORMATIONS = "/v1/informations/"  # /v1/informations/{date}/{zone}
AELF_CMD_MESSES = "/v1/messes/"  # /v1/messes/{date}/{zone}

TAG_RE = re.compile(r"<[^>]+>")

zone_list = [
    "afrique",
    "belgique",
    "canada",
    "france",
    "luxembourg",
    "romain",
    "suisse",
]


class CAELF:
    def __init__(self, date, zone) -> None:
        # Ensure input format
        format = "%Y-%m-%d"
        try:
            datetime.datetime.strptime(date, format)
            if zone in zone_list:
                self._date = date
                self._zone = zone
        except ValueError:
            print("date incorrect string format. It should be YYYY-MM-D")
            print("or")
            print("zone incorrect. Should be in {}".format(zone_list))

    def unhtml(self, string):
        string = re.sub(r"<[^>]*>", "", string)
        string = re.sub(r"\s{2,}", " ", string)
        string = re.sub(r"\n", " ", string)
        string = re.sub(r"Parole du Seigneur", " ", string)
        string = re.sub(r"Acclamons la Parole de Dieu.", " ", string)
        return string.strip()

    def cleanup(self, element):
        if isinstance(element, list):
            for i, item in enumerate(element):
                element[i] = self.cleanup(item)
        elif isinstance(element, dict):
            for key in element.keys():
                element[key] = self.cleanup(element[key])
        elif isinstance(element, str):
            element = self.unhtml(element)

        return element

    def get_informations(self):
        r = requests.get(
            "{}{}{}/{}".format(
                AELF_API_SITE, AELF_CMD_INFORMATIONS, self._date, self._zone
            )
        )
        return r.json()

    def get_messe(self):
        r = requests.get(
            "{}{}{}/{}".format(AELF_API_SITE, AELF_CMD_MESSES, self._date, self._zone)
        )
        return r.json()

    def get_reading(self, lecture_name):
        messe_json = self.get_messe()
        for messe in messe_json["messes"]:
            if "Messe du jour" in messe["nom"]:
                for lecture in messe["lectures"]:
                    if lecture["type"] == lecture_name:
                        return self.cleanup(lecture)


def get_psalm(date, zone):
    aelf = CAELF(date, zone)
    return aelf.get_reading("psaume")


def get_first_reading(date, zone):
    aelf = CAELF(date, zone)
    return aelf.get_reading("lecture_1")


def get_second_reading(date, zone):
    aelf = CAELF(date, zone)
    return aelf.get_reading("lecture_2")


def get_evangile(date, zone):
    aelf = CAELF(date, zone)
    return aelf.get_reading("evangile")


def get_date(date, zone):
    aelf = CAELF(date, zone)
    infos = aelf.get_informations()
    return infos["informations"]["date"]


def get_week(date, zone):
    aelf = CAELF(date, zone)
    infos = aelf.get_informations()
    return infos["informations"]["semaine"]


if __name__ == "__main__":
    aelf = CAELF("2024-03-31", "france")
    aelf.get_informations()
    first_reading = get_first_reading("2024-03-31", "france")

    text = get_psalm("2022-12-18", "france")
    print(text)
