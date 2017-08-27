# This file contains the WSGI configuration required to serve up your
# web application.
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Bottle project
import bottle
import os
import sys
from bottle import default_app, route, view, get, post, static_file, request, redirect, run, TEMPLATE_PATH
here = os.path.dirname(__file__)
# add your project directory to the sys.path
project_home = here  # os.path.join(here, "src/")
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# make sure the default templates directory is known to Bottle
templates_dir = os.path.join(project_home, 'views/')
if templates_dir not in TEMPLATE_PATH:
    TEMPLATE_PATH.insert(0, templates_dir)

LAST = 0


@get('/')
@view('game')
def register_user():
    global LAST
    LAST += 1
    gid = ":".join(["N_O_D_E", "%02d" % LAST])
    print('game register', gid)
    return dict(nodekey=gid, lastid=LAST)

application = default_app()


if __name__ == "__main__":
    run(host='localhost', port=8080)
