

class Main:
    def __init__(self, go, gb, gg):
        config = {
            "undoManager.isEnabled": True
        }
        mydiagram = mk(go.Diagram, "myDiagramDiv", config)
        mydiagram.nodeTemplate = mk(
            go.Node, "Auto", 
            mk(go.Shape, "RoundedRectangle", gb("fill", "color")),
            mk(go.TextBlock, {"margin": 3}, gb("text", "key"))
        )

        mydiagram.model = gg(
            [
                {"key": "Alpha", "color": "lightblue"},
                {"key": "Beta", "color": "orange"},
                {"key": "Gamma", "color": "lightgreen"},
                {"key": "Delta", "color": "pink"}
            ],
            [
                {"from": "Alpha", "to": "Beta"},
                {"from": "Alpha", "to": "Gamma"},
                {"from": "Beta", "to": "Beta"},
                {"from": "Gamma", "to": "Delta"},
                {"from": "Delta", "to": "Alpha"}
            ])

mk = lambda *_: []


def main(make, go, gb, gg):
    global mk
    mk = make

    Main(go, gb, gg)





