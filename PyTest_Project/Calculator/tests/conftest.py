import pytest
import pandas as pd


@pytest.fixture
def numbers():
    a=9
    b=3
    print("Herllo")
    return a,b






@pytest.fixture(scope='module')
def numbers_csv():
    print("\n=============SETUP==============")
    data=pd.read_csv('numbers.csv')
    print( "Initialization Size",data.size)
    print("Initialization Shape",data.shape)
    yield data
    print("\n============TEAR DOWN==============")
    data = pd.DataFrame()
    print("Teardown Size",data.size)
    print("Teardown Shape",data.shape)


