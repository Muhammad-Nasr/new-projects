import unittest
from life import CellList, Life

class TestCellList(unittest.TestCase):
    
    def test_empty(self):
        c = CellList()
        assert list(c) == []

    def test_set_true(self):
        c = CellList()
        c.set(1, 2, True)
        assert c.has(1, 2)
        assert list(c) == [(1, 2)]
        c.set(500, 600)
        assert c.has(1, 2) and c.has(500, 600)
        assert list(c) == [(1, 2), (500, 600)]
        c.set(1, 2, True)
        assert c.has(1, 2) and c.has(500, 600)
        assert list(c) == [(1, 2), (500, 600)]

    def test_set_false(self):
        c = CellList()
        c.set(1, 2, False)
        assert not c.has(1, 2)
        assert list(c) == []
        c.set(1, 2, True)
        c.set(1, 2, False)
        assert not c.has(1, 2)
        assert list(c) == []
        c.set(1, 2, True)
        c.set(3, 2, True)
        c.set(1, 2, False)
        assert not c.has(1, 2)
        assert c.has(3, 2)
        assert list(c) == [(3, 2)]

    def test_set_default(self):
        c = CellList()
        c.set(1, 2)
        assert c.has(1, 2)
        assert list(c) == [(1, 2)]
        c.set(1, 2)
        assert not c.has(1, 2)
        assert list(c) == []





class TestLife(unittest.TestCase):
    pass