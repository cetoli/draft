import unittest
from server.views.rtcgame import Base, Item


class TestCaseRtc(unittest.TestCase):
    def setUp(self):
        Item.send = lambda _, data=0: self._send(data)

    def _send(self, data):
        self.data = data

    def test_create_base(self):
        tester = Base(0, "NOD%02d")
        # response = tester.get('/')
        props = [tester.parent, tester.node_id, tester.rgb, tester.size]
        cprops = [Item.prefix, Item.item]
        csets = ['NOD%02d', {(): tester, (0,): tester}]
        sets = [tester, (0,), (50, 50, 50), (404, 788)]
        assert Item.conn is not None
        assert tester.container == [], tester.container
        assert props == sets, props
        assert cprops == csets, cprops

    def test_create_item(self):
        itemer = Base(0, "NOD%02d")
        tester = itemer.create((9, 8, 7))
        # response = tester.get('/')
        props = [tester.parent, tester.node_id, tester.rgb, tester.size]
        cprops = [Item.prefix, Item.item]
        csets = ['NOD%02d', {(0, 0): tester, (): itemer, (0,): itemer}]
        sets = [itemer, (0, 0), (9, 8, 7), (50, 50)]
        assert Item.conn is not None
        assert itemer.container == [tester], itemer.container
        assert tester.container == [], tester.container
        assert props == sets, props
        assert cprops == csets, cprops

if __name__ == '__main__':
    unittest.main()
