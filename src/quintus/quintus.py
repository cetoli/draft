# from math import pi
pi = 3.1416


class Ball:
    Q = None

    def __init__(self):
        pass
        self.ball = None
        self.q = Ball.Q

    def draw(self, ctx):
        ctx.fillStyle = "black"
        ctx.beginPath()
        ctx.arc(-self.p.cx,
                -self.p.cy,
                self.p.w / 2, 0, pi * 2)
        ctx.fill()

    def main(self):
        self.ball = self.q.Ball(dict(w=20, h=20,
                                x=30, y=300,
                                vx=30, vy=-100,
                                ax=0, ay=30))

        self.q.gameLoop(self.loop)

    def loop(self, dt):
        self.q.clear()
        self.ball.update(dt)
        self.ball.render(self.q.ctx)


def main(window):
    Ball.Q = window.Quintus().include("Sprites").setup(dict(width=400, height=400))
    Ball.Q.MovingSprite.extend("Ball", Ball)
    Ball().main()
