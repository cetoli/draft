#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Calculo das notas para plotagem
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: $Date: 2012/03/24  $
:Status: This is a "work in progress"
:Revision: $Revision: 0.01 $
:Home: `Labase <http://labase.nce.ufrj.br/>`__
:Copyright: ©2010, `GPL <http://is.gd/3Udt>__.
"""
import mechanize
# from BeautifulSoup import BeautifulSoup as soup
from colors import COLOR as K
import ssl
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
# ssl_version corrections are done


COLORS = [K.red, K.green, K.blue, K.fuchsia, K.teal, K.navy, K.maroon, K.yellow,
          K.purple, K.darkgoldenrod, K.lime, K.aqua, K.tomato, K.olivedrab, K.dodgerblue,
          K.lightpink, K.lightgreen, K.black, K.gray, K.silver]
__author__ = "Carlo E. T. Oliveira (cetoli@yahoo.com.br) $Author: cetoli $"
__version__ = "1.0 $Revision$"[10:-1]
__date__ = "2012/03/24 $Date$"
NL = []


class Main:
    def __init__(self, page, owners, avals, nopeers, degrade, pub_dir,
                 grades, averages, evs=NL, peers=NL, plat=None, no_last=0):
        self.owners, self.avals, self.nopeers = owners, avals, nopeers
        self.degrade, self.pub_dir, self.peers = degrade, pub_dir, peers
        self.grades_file, self.averages_file = grades, averages
        self.page, self.evs, self.no_last = page, evs, no_last
        self.plat = plat or 'https://activufrj.nce.ufrj.br'
        self.events = self.norms = self.grades = self.titles = self.range = self.speers = None

    def plot_results(self, outfile='test_grades.png'):
        tcks = ['%s%s:%d' % (lab[0:3], lab[-2:], ind) for ind, lab in enumerate(self.events)]
        # plotter = ['.', ',', ':','-','--' ,'-.',':','-','--' ]*6# 	,':','.','<','>', '+', 'v', '^']
        plotter = []
        color = COLORS * 4
        [plotter.extend([tk] * 16) for tk in ['-', '--', '-.', ':']]  # ,':','.','<','>', '+', 'v', '^']
        plt.xticks(range(len(tcks)), tcks)
        plt.figure()
        top = .9 - (len(set(self.peers) - set(self.nopeers)) / 3.0) * 0.05
        plt.subplots_adjust(bottom=0.08, left=.05, right=.96, top=top, hspace=.35)
        for peer, plot, color in zip(self.speers, plotter, color):
            if peer in self.nopeers or "_" in peer:
                continue
            plt.plot(self.grades[peer], plot, color=color, label=peer[:15], linewidth=2.0)
            plt.legend(bbox_to_anchor=(0, 1, 1, 3), loc=3, borderaxespad=1., ncol=3,
                       mode="expand", )  # loc='upper right')
            # plt.margins(10,10)
            plt.savefig(self.pub_dir + outfile, pad_inches=2)
            # plt.label(peer)
        plt.show()

    def normalize_grade_grid(self):
        grades = [self.grades[peer] for peer in self.speers]
        self.norms = [max(ev) > 0 and max(ev) or 9 for ev in zip(*grades)]
        # self.norms = [(max(ev)> 0 and max(ev) or 9,
        #    min(ev)>max(ev)/3.0 and min(ev) or max(ev)/3.0)  for ev in zip(*grades)]
        for peer in self.grades:
            if peer in self.nopeers:
                continue
            self.grades[peer] = [g * 100 / (n + 2) + 1 for g, n in zip(self.grades[peer], self.norms)]  # [:-1])]

    def average_grade_grid(self):
        def min_for_max(ingrades):
            ingrades[ingrades.index(min(ingrades))] = max(ingrades)
            if len(ingrades) > 6:
                ingrades[ingrades.index(min(ingrades))] = max(ingrades)
            return ingrades

        for peer in self.grades:
            if peer in self.nopeers:
                continue
            grades = [0] + self.grades[peer]
            grades = min_for_max(min_for_max(grades))
            self.grades[peer] = [sum(grades[0:i + 1]) / (i + 1) for i, grade in enumerate(grades) if 0 < i]  # <9]

    def create_grade_grid(self):
        self.grades = dict((peer, [0] * len(self.events)) for peer in self.speers)

    def remove_page(self, entry):
        pg = self.page + '/'
        if pg in entry:
            return entry.replace(pg, '')
        else:
            return entry

    def assess_a_vote_session(self, session_no, event):
        session = self.avals[event]
        for vote in session.itervalues():
            self.assess_a_user_vote(vote, session_no)

    def assess_a_user_vote(self, vote, session):
        vote = isinstance(vote, dict) and vote.values()[0] or vote
        print(vote)
        degrade = self.range[session] + 2
        votes = [(voted, rank) for voted, rank
                 in zip(vote, self.degrade[:-degrade])]
        for voted in votes:
            peer_name, rank = voted
            peer_name = self.remove_page(peer_name) if peer_name else 0
            if peer_name in self.nopeers:
                continue
            for vote in self.owners[peer_name]:
                assert self.grades[vote][session] >= -100, 'v:%s,p:%s,s:%s' % (vote, peer_name, session)
                self.grades[vote][session] += rank

    def calculate(self):
        # global self.owners, self.speers, AVALS
        self.avals.update(self.scrap_from_page())
        # return
        if self.owners is None:
            first_event = self.events[0]
            self.owners = {name: [name] for name in self.avals[first_event]}
            for i, v in self.owners.iteritems():
                print('    %s = %s,' % (i, str(v)))
        self.events = self.evs + self.events
        [self.events.pop() for _ in range(self.no_last)]
        avals = self.avals
        # print("avals", avals)
        print("ownwer", self.owners)
        self.peers = {peer for votes in avals.itervalues()
                      for vote in votes.itervalues() for peer in vote
                      if not ({0, '/'} & set(list(peer == 0 and [0] or peer)))}
        self.speers = sorted(self.peers)
        # self.owners = {peer:[peer] for peer in self.peers}
        self.owners.setdefault(0, [])
        self.create_grade_grid()
        for session, event in enumerate(self.events):
            self.assess_a_vote_session(session, event)
        print('grades before normalize:\n', self.grades)
        self.normalize_grade_grid()
        self.plot_results(self.grades_file)
        print('grades  normalizers:\n', self.norms)
        self.average_grade_grid()

        print('grades average after normalize:\n', self.grades)
        self.plot_results(self.averages_file)

    def scrap_from_page(self):
        # self.page='https://activufrj.nce.ufrj.br/evaluation/result/Neuro_UM_XII'
        mech = mechanize.Browser()
        mech.set_handle_robots(False)
        mech.open(self.plat)

        mech.select_form(nr=0)
        mech["user"] = "carlo"
        mech["passwd"] = "labase4ct1v"
        mech.submit().read()
        # soup(results)
        mech.open(self.plat + '/evaluation/' + self.page).read()
        self.events = [link.url.split('/')[-1] for link in mech.links()
                       if '/evaluation/edit/' in link.url]
        print(self.events)

        events = self.events
        avs = mech.open(self.plat + '/rest/evaluation/result/' + self.page).read()
        avs = json.loads(avs)["result"]
        # doc = soup(avs)
        # lns = doc.findAll('a')
        print(avs)

        def get_range(event):
            rngpg = mech.open(event).read()
            return len(rngpg.split('para os votados')[1].split('Data')[0].split()[4:-4])

        self.range = [get_range(self.plat+"/evaluation/edit/%s/%s" % (self.page, link)) for link in events]
        print('self.range %s' % self.range)

        return {l: avs[self.page+"/"+l] for l in self.events}

    def main(self):
        self.calculate()
