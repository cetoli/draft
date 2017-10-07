#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Criação de slots para a matéria de psicologia geral
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: $Date: 2017/10/06  $
:Status: This is a "work in progress"
:Revision: $Revision: 0.01 $
:Home: `Labase <http://labase.nce.ufrj.br/>`__
:Copyright: ©2017, `GPL <http://is.gd/3Udt>__.
"""
import mechanize
import ssl
import PIL.Image as Imger
import face_recognition
from BeautifulSoup import BeautifulSoup

import os

NTU = 2

NUM_JITTERS = 80
TOLERANCE = 0.595
STYLE = """<style> a { border: 8px solid rgba(255,0,0,.4); }
          a:hover{ border:8px solid rgba(0,0,255,.7); }</style>"""
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<body>
  {style}
  <div style="position:relative">
    {photo}
    {mape}
    <div style="position:relative; float:left">
    {lines}
    </div>
  </div>
</body>
"""
IMG = '<p><img src="{}" usemap=#Map /></p>'
LINE = '\t\t<div style="position:relative; float:left"; min-width:400px>' \
       '<a id="{nome}" name="{nome}"></a><img alt="{title}" title="{title}" height="350" src="{src}" width="350" />' \
       '<p><span style="font-size:48px;">{nome}</span></p>' \
       '</div>'
# AREA = '<area alt="{nome}" coords="{l},{t},{b},{r}" href="#{nome}" shape="rect" title="{nome}">'
AREA = """
        <a href="#{nome}" alt="{nome}" title="{nome}"
         style="display:block; width:{r}px; height: {b}px; left: {l}px; top: {t}px;
         position:absolute;"></a>"""
MAP = '\t<p>\n{}\n</p>'
NOLO = """
margaridas
gabiandrade21
paulacaldeira
MateusGontijo
Wallace
""".split("\n")
# NOLO=[]
LOGIN = """danielleveloso
Tayza
SaraHellen

Wallace
Lara.Pazos
PizzoCardoso
beatriztomaz

BeaCris
ayellenbatista
carolinna_marques

Laurentinoday
MarianaFelix
J.L

NathaliaBessa
margaridas
Bruna033
m_azevedo7

IngridCristine
rayane
MateusGontijo
leticiaant

anac
crisleitao
LuanaPalladino
saridielly

Marlonrocha97
juliane20
dayana
rayanebeltrao

ressanferreira
marianadias
India

carolmavila
paulanovoa

Matheusfernandes
paulacaldeira
mariah0rosa
gabiandrade21
DafneMoreira
Palomasantos
""".split("\n")
LOGIN = [l for l in LOGIN if l and (l not in NOLO)]
print(LOGIN)
'aulasf17_2/IMG_20170926_131951583.jpg'
PHOTOS = """aulasf17_2/IMG_20170926_131951583.jpg
aulasf17_2/IMG_20170926_174356728.jpg
aulasf17_2/IMG_20171003_132001297.jpg
aulasf17_2/IMG_20171003_132029786.jpg
aulasf17_2/IMG_20171003_151030548.jpg""".split("\n")

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


def get_k(filen):
    try:
        return face_recognition.face_encodings(face_recognition.load_image_file(filen))[0]
    except:
        return []


class Main:
    def __init__(self, plat=None):
        self.known_faces = {}
        self.known_faces_list = []
        self.faces_image = '/home/carlo/Documentos/dev/draft/src/activmech/fono17_2'
        self.plat = plat or 'https://activufrj.nce.ufrj.br'
        self.events = self.norms = self.grades = self.titles = self.range = self.members = self.speers = None
        self.logins = LOGIN

    def train_recgnizable_faces(self):
        def is_login(fono_name):
            is_it = fono_name.split("_")[-2] in LOGIN
            print('fono_name.split("_")[-1]: {} in fono:{} in :{}'.format(
                fono_name.split("_")[-2], fono_name, is_it))
            return is_it
        import os
        fonos = ["fono17_2/" + fon for fon in os.listdir("fono17_2") if is_login(fon)]
        # fonos = ["fono17_2/" + fon for fon in os.listdir("fono17_2") if fon[:-4] in LOGIN]
        self.known_faces_list = [k for k in [get_k(filen) for filen in fonos] if k != []]
        self.known_faces = {
            ordinal:
                fono.split(".png")[0] for ordinal, fono in enumerate(fonos)
        }

    def name_all_photos(self):
        self.train_recgnizable_faces()
        for photo in PHOTOS:
            self.name_photos(photo)

    def name_photos(self, photo):
        img = Imger.open(photo)
        import PIL.ExifTags
        exif = {
            PIL.ExifTags.TAGS[k]: v
            for k, v in img._getexif().items()
            if k in PIL.ExifTags.TAGS
        }
        print(photo, exif["DateTimeOriginal"])
        phono_loc_dict = self.reco_faces(photo)
        for phono, loc in phono_loc_dict.items():
            print("fono {} at {}".format(phono, loc))
        return photo, exif["DateTimeOriginal"], phono_loc_dict

    def reco_faces(self, class_face):
        def match_fono(location_, image_):
            top, right, bottom, left = location_
            # You can access the actual face itself like this:
            face_image = image_[top:bottom, left:right]
            try:
                unknown_face_encoding = face_recognition.face_encodings(face_image, num_jitters=NUM_JITTERS)[0]
                recos = face_recognition.compare_faces(
                    self.known_faces_list, unknown_face_encoding, tolerance=TOLERANCE)
            except:
                recos = []

            face_dict = {
                self.known_faces[index]: location_ for index, is_there in
                enumerate(recos) if is_there}
            print(
                "location Locs: {}  Top: {}, Left: {}, Bottom: {}, Right: {}"
                .format(face_dict, top, left, bottom, right))
            return face_dict

        # Load the jpg file into a numpy array
        image = face_recognition.load_image_file(class_face)

        # Find all the faces in the image using a pre-trained convolutional neural network.
        # This method is more accurate than the default HOG model, but it's slower
        # unless you have an nvidia GPU and dlib compiled with CUDA extensions. But if you do,
        # this will use GPU acceleration and perform well.
        # See also: find_faces_in_picture.py
        face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=NTU)  # , model="cnn")
        return {fono: locat for locat in face_locations for fono, locati in match_fono(locat, image).items()
                if fono}

    def download_photos(self):
        url = "https://activufrj.nce.ufrj.br/photo/"
        page = "/members/Fonoaudiologia?group=2017_2"
        mech = mechanize.Browser()
        mech.set_handle_robots(False)
        mech.open(self.plat)

        mech.select_form(nr=0)
        mech["user"] = "abrapacarla"
        mech["passwd"] = "vidanova"
        mech.submit().read()
        print("self.plat + page", self.plat + page)
        # mech.open(self.plat + page).read()
        bf = BeautifulSoup(mech.open(self.plat + page))
        # mech.select_form("updateparts")
        members = {login["href"].split("/")[-1]: login["title"]
                        for login in bf.findAll('a') if ("/user/" in login["href"]) and login.has_key("title")}
        self.members = [(login, name) for login, name in members.items() if login in self.logins]
        # self.members = [login for login in mech.links]
        # self.members = [(login.name, login.items) for login in mech.controls if login.name in self.logins]
        for member, member_name in self.members:
            photo_url = os.path.join(url, member)
            filename = os.path.join("fono17_2", "{}_{}_.png".format(member_name, member))
            print("member {}, member_name {}".format(member, filename))
            data = mech.open(photo_url).read()
            save = open(filename, 'wb')
            save.write(data)
            save.close()

    def scrap_from_page(self):
        # self.page='https://activufrj.nce.ufrj.br/evaluation/result/Neuro_UM_XII'
        mech = mechanize.Browser()
        mech.set_handle_robots(False)
        mech.open(self.plat)

        mech.select_form(nr=0)
        mech["user"] = "abrapacarla"
        mech["passwd"] = "vidanova"
        mech.submit().read()
        # soup(results)
        mech.open(self.plat + '/groups/Fonoaudiologia?group=2017_2/').read()
        form = mech.select_form("updateparts")
        self.members = [login for login in mech.controls]
        self.members = [login for login in self.members if login.name in self.logins]
        for member in mech.controls:
            if member.name in self.logins:
                member.selected = True
            else:
                member.selected = False

        for member in mech.controls:
            if member.type == "checkbox":
                try:

                    print(member.name, member.selected
                          )
                except:
                    pass

        reponse = mech.submit()
        print reponse.read()

        # self.members = [login for login in mech.find_control(type="checkbox").items]
        # self.logins = [mech.find_control(login) for login in self.logins]
        # print(self.members)

    def html_photo(self, photo_number=1):
        def parse(nome_):
            return nome_.split("_")[1].split("/")[-1], nome_.split("_")[-2]
        self.train_recgnizable_faces()
        photo, date, fonod = self.name_photos(PHOTOS[photo_number])
        mape = MAP.format("\n".join([AREA.format(nome=parse(nome)[0], l=t-200, t=l-30, b=200, r=200)
                                     for nome, (l, t, b, r) in fonod.items()]))
        lines = "\n".join(
            LINE.format(nome=parse(nome)[1], title=parse(nome)[0], src=nome+".png") for nome in fonod.keys())
        html = HTML.format(style=STYLE, photo=IMG.format(photo), mape=mape, lines=lines)
        print(html)
        filename= "/home/carlo/Documentos/dev/draft/src/activmech/fonolista.html"
        save = open(filename, 'wb')
        save.write(html)
        save.close()

    def main(self):
        self.html_photo(4)
        # self.download_photos()
        # self.scrap_from_page()

if __name__ == "__main__":
    Main().main()
