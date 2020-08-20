
from apoor import data


def test_list_data():
    d = data.list_data()
    assert "iris" in d
    assert "boston" in d

def test_load_iris():
    df = data.load_iris()
    iris_shape = (150, 5)
    assert df.shape == iris_shape
    iris_cols = [
        'sepal_length','sepal_width', 
        'petal_length','petal_width', 
        'target']
    assert df.columns.to_list() == iris_cols
    
def test_load_boston():
    df = data.load_boston()
    boston_shape = (506, 14)
    assert df.shape == boston_shape
    boston_cols = [
        'CRIM','ZN','INDUS',
        'CHAS','NOX','RM',
        'AGE','DIS','RAD','TAX',
        'PTRATIO','B','LSTAT',
        'MEDV']
    assert df.columns.to_list() == boston_cols

