""" Just a purple sphere """

from vapory import *


class Torus(POVRayElement):
    """"""
    pass


class ClippedBy(POVRayElement):
    """"""
    pass
C1, C2, C3, C4 = [0.8, 0.4, 0.1], [0.6, 0.3, 0.09], [0.08, 0.05, 0.04], [0.5, 0.05, 0.06]

W1 = dict(scale=0.2, octaves=5)
W3 = dict(scale=0.08, octaves=5, turbulence=0.12, c1=[0.45, 0.25, 0.1], c2=[0.25, 0.12, 0.05])
W4 = dict(scale=0.06, octaves=8, c1=[0.3, 0.2, 0.2], c2=[0.25, 0.15, 0.15])
W5 = dict(scale=0.01, octaves=3, c1=[0.7, 0.6, 0.5], c2=[0.4, 0.35, 0.25])
W2 = dict(scale=0.15, lambdah=0.4, octaves=9, c1=[0.25, 0.02, 0.03], c2=[0.16, 0.02, 0.03])
WD = [{}, W1, W2, W3, W4, W5]
CP = 5
PAWN = "pawn%d.png" % CP


def Wood(c1=C1, c2=C2, scale=0.035, turbulence=0.09, lambdah=0.6, octaves=3, omega=1.2, phase=2.0):
        return Texture(
            Pigment('wood', 'scale', scale, "turbulence", turbulence,
                    "lambda", lambdah, "octaves", octaves, "omega", omega, "phase", phase,
                    ColorMap([0.0, "rgb", c1],
                             [0.3, "rgb", c2],
                             [1.0, "rgb", c1]
                             )
                    ),
            Normal('wood', 0.75, 'scale', 0.35),
            Finish('phong', 0.06)

        )
H0 = 0.009

# C3 = C4
STP = 6.0
XYL = 1.2


def Hashure():
    xy = {True: 1, False: 0.1}
    hasher = [Cylinder([-1, 0.35, y/STP],  [1, 0.35, y/STP], H0, Pigment("color", "rgb", C3))
              for y in range(-10, 10)] + [
        Cylinder([y/STP, 0.35, -XYL],  [y/STP, 0.35, XYL], H0, Pigment("color", "rgb", C3)) for y in range(-10, 10)] + [
        Cylinder([-XYL, 0.35, -XYL+y/STP],  [XYL, 0.35, XYL+y/STP], H0, Pigment("color", "rgb", C3)) for y in range(-20, 20)]+ [
        Cylinder([-XYL, 0.35, XYL+y/STP],  [XYL, 0.35, -XYL+y/STP], H0, Pigment("color", "rgb", C3)) for y in range(-20, 20)]
    return Union(
        *hasher
    )


def Pawn():
    return Union(
        Torus(1, 0.35), Torus(0.6, 0.35),
        Cylinder([0, 0, 0],  [0, 0.35, 0], 1, ClippedBy(Cylinder([0, -0.2, 0.0],  [0.0, 0.4, 0.0], 0.6, "inverse"))),
        Wood(**WD[CP]),
        )

objects = [

    # SUN
    LightSource([1500, 2500, -2500], 'color', 1),

    # SKY
    Sphere([0, 0, 0], 1, 'hollow',
           Texture(
               Pigment('gradient', [0, 1, 0],
                       'color_map{[0 color White] [1 color Blue  ]}'
                       'quick_color', 'White'
                       ),
               Finish('ambient', 1, 'diffuse', 0)
           ),

           'scale', 10000
           ),

    # GROUND
    # PAWN
    # Union(Sphere([0, 1, 0], 0.35),
    #
    Difference(Pawn(), Hashure())
    #        Cone([0, 0, 0], 0.5, [0, 1, 0], 0.0),
    # Pawn()
]

scene = Scene(Camera('ultra_wide_angle',
                     'angle', 89,
                     'location', [0.0, 3.0, -0.3],
                     'look_at', [0.0, 0.0, 0.0]
                     ),

              objects=objects,
              included=['colors.inc', 'textures.inc']
              )

scene.render(PAWN, remove_temp=False)
