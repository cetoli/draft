#! /usr/bin/env python
# -*- coding: UTF8 -*-
# This file is part of  program Activ Spyder
# Copyright © 2022  Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
# SPDX-License-Identifier: (GPLv3-or-later AND LGPL-2.0-only) WITH bison-exception

"""Crawler for SuperGame -

    Obtem versões dos relatórios dos games.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    22.05
        Criação do raspador de página.

"""
import mechanize
import ssl
import json
import os

LABA = ""
try:
    LABA = os.environ['LABA']
except KeyError as err:
    print(f"Given key not found - {err}")

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


# ssl_version corrections are done


class Main:
    def __init__(self, plat=None, page="/wiki/MATERIAIS.DESIGN.ARQUITETURA/"):
        self.plat = plat or 'https://activufrj.nce.ufrj.br'
        self.page = page
        self.pages = []
        self.author_pages = {}
        self.mech = mechanize.Browser()

    def login(self):
        # self.page='https://activufrj.nce.ufrj.br/evaluation/result/Neuro_UM_XII'
        mech = self.mech
        mech.set_handle_robots(False)
        mech.open(self.plat)

        mech.select_form(nr=0)
        mech["user"] = "carlo"
        mech["passwd"] = LABA
        mech.submit().read()

    def scrap_from_page(self, author, page):
        """Recover versions of a given wiki page"""
        # soup(results)
        mech = self.mech
        print(self.plat + '/wiki/history' + page)
        mech.open(self.plat + '/wiki/history' + page).read()
        # self.events = [link.url.split('/')[-1] for link in mech.links()
        versions = [link.url for link in mech.links() if "wiki" + page in link.url]
        # [print(eve) for eve in versions]
        # versions = self.read_version(versions[1])
        all_vers = len(versions)
        return [dict(author=author, version=all_vers - ver, **self.read_version(version))
                for ver, version in enumerate(versions)]

    def read_version(self, page):
        """Recover a version"""

        avs = self.mech.open(self.plat + '/rest' + page).read()
        avs = json.loads(avs)["result"]["wikidata"]
        return avs

    def main(self):
        """Login and scrap page versions"""
        self.pages = [(taut := author.split("http"), taut[0], taut[1].split("wiki")[1])[1:]
                      for author in PAGES.split("\n")]
        self.login()
        author_data = [self.scrap_from_page(author, page) for author, page in self.pages]
        with open("author_data23_9.json", "w") as outfile:
            json.dump(author_data, outfile, indent=4)


# PAGES = """Tiago https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Tiago_Historia_do_Jogo_Mag_Toby
_PAGES = """Adrian https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Pizza_Sapo_Adrian_e_Tiago
Adriana https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Adriana
Alexandro https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Alexandro
Eduardo https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Eduardo
Isabela https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Isabela
Leon https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Leon
Letícia https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Leticia
Miguel Tavares https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Miguel_Tavares
Alvaro https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Alvaro
Miguel Belmonte https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Miguel_Belmonte
Diego Belmonte https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Diego_Belmonte
Isaque https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Isaque
Arthur https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/ARTHUR"""
PAGE = """Tiago https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Tiago__Historia_do_Jogo_Mag__Toby"""
PAGES = """Adrian https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Pizza_Sapo_Adrian_e_Tiago
Tiago https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Tiago__Historia_do_Jogo_Mag__Toby
Adriana https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Adriana
Alexsandro https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Alexandro
Eduardo https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Eduardo
Isabela https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Isabela
Leon https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Leon
Letícia https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Leticia
Miguel Tavares https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Miguel_Tavares
Alvaro https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Alvaro
Miguel Belmonte https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Miguel_Belmonte
Diego Belmonte https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Diego_Belmonte
Isaque https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/Isaque
Arthur https://activufrj.nce.ufrj.br/wiki/MATERIAIS.DESIGN.ARQUITETURA/ARTHUR"""
if __name__ == "__main__":
    Main().main()
