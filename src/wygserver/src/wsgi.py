#! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa Marayho
# Copyright 2014-2017 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://j.mp/GNU_GPL3>`__.
#
# Marayho é um software livre; você pode redistribuí-lo e/ou
# modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF); na versão 2 da
# Licença.
#
# Este programa é distribuído na esperança de que possa ser útil,
# mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
# a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para maiores detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa, se não, veja em <http://www.gnu.org/licenses/>

"""Start wsgi server with bottle.

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
from server.control.control import main, application
import server.control.control as sv_ctl
import server

_ = application
sv_ctl.SRC_DIR = server.CLIENT

if __name__ == "__main__":
    main(server.CLIENT)