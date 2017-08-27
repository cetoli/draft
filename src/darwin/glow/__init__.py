from browser import document, window
from javascript import JSObject, JSConstructor

from .utils import create_script_tag
from .primitive import box, arrow, cone, curve, pyramid, helix, cylinder, sphere, attach_trail, compound

from .vector import vec

version = "1.0"
#
# create_script_tag('../../labase/glow/jslibs/jquery-1.6.2.min.js')
# create_script_tag('../../labase/glow/jslibs/glow.1.0.min.js')
_glowscript = JSObject(window.glowscript)
'''
#find a better way to do this..
while 1:
  _glowscript = window.glowscript  # JSObject(glowscript)

  try:
    if _glowscript.version == version:
       break
  except TypeError:
    pass
'''
#or we could make this some type of function instead of a class
class glow:
  def __init__(self, container):
      self._id=document.get(id=container)[0]
      setattr(self._id, 'id', '')

      setattr(window, '__context', {})
      setattr(getattr(window, '__context'), 'glowscript_container', 
              self._id.elt)
  
#todo, make canvas its own class    
def canvas():
    return _glowscript.canvas()

def rate(t, func):
    _glowscript.rate(t, func)

color = _glowscript.color
