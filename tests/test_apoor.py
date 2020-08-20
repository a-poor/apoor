
import apoor

def test_make_scale():
    assert apoor.make_scale(0,1,0,10)(0.1) == 1
    assert apoor.make_scale(10,0,0,1)(9) == 0.1
    assert apoor.make_scale(0,1,0,1,True)(-1) == 0
    assert apoor.make_scale(0,1,0,10,True)(11) == 10

def test_set_seed():
    np = apoor.np
    n = 0
    apoor.set_seed(n)
    a = np.random.random()
    assert a != np.random.random() or a != np.random.random()
    apoor.set_seed(n)
    b = np.random.random()
    assert a == b


def test_train_test_split():
    # Getting started
    np = apoor.np
    x = np.arange(10)
    y = x[::-1]
    z = np.arange(0,20,2)
    ### Test 1 ###
    x_train = np.array([2,8,4,9,1,6,7,3,0])
    x_test  = np.array([5])
    apoor.set_seed(0)
    assert apoor.train_test_split(x) == (x_train,x_test)
    ### Test 2 ###
    y_train = np.array([7,1,5,0,8,3,2,6,9])
    y_test  = np.array([4])
    apoor.set_seed(0)
    assert apoor.train_test_split(x,y) == (x_train,x_test,y_train,y_test)
    ### Test 3 ###
    z_train = np.array([4,16,8,18,2,12,14,6,0])
    z_test  = np.array([10])
    apoor.set_seed(0)
    assert apoor.train_test_split(x,y,z) == (x_train,x_test,y_train,y_test,z_train,z_test)