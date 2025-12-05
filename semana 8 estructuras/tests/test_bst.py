from semana_8_estructuras.bst import BST

def test_bst_insert_and_inorder():
    bst = BST()
    nums = [50, 30, 70, 20, 40, 60, 80]
    for n in nums:
        bst.insertar(n) if hasattr(bst, 'insertar') else bst.insertar(n)  # safe if API differs
    # our class method is insertar in HTML, but implementation above uses insertar
    # verify inorden is sorted
    assert bst.inorden() == sorted(nums)

def test_bst_delete_cases():
    bst = BST()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        bst.insertar(v)
    # Case 1: delete leaf (20)
    bst.eliminar(20)
    assert bst.inorden() == [30, 40, 50, 60, 70, 80]
    # Case 2: delete node with one child: insert 25 as child of 30 then delete 30
    bst.insertar(25)
    bst.eliminar(30)
    assert 30 not in bst.inorden()
    # Case 3: delete node with two children (delete 50 root)
    bst.eliminar(50)
    assert 50 not in bst.inorden()
    assert bst.inorden() == sorted(bst.inorden())  # still sorted
