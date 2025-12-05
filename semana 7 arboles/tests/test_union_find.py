from semana_7_arboles.union_find import UnionFind

def test_union_find_basic():
    uf = UnionFind(5)
    assert uf.find(0) == 0
    assert uf.union(0, 1) is True
    assert uf.find(0) == uf.find(1)

def test_union_find_double_union():
    uf = UnionFind(3)
    assert uf.union(0, 1)
    assert uf.union(1, 2)
    assert not uf.union(0, 2)

def test_union_find_path_compression():
    uf = UnionFind(4)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(2, 3)
    root = uf.find(3)
    assert root == uf.find(0)
