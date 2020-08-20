
import apoor

def test_make_scale():
    assert apoor.make_scale(0,1,0,10)(0.1) == 1
    assert apoor.make_scale(10,0,0,1)(9) == 0.1
    assert apoor.make_scale(0,1,0,1,True)(-1) == 0
    assert apoor.make_scale(0,1,0,10,True)(11) == 10

