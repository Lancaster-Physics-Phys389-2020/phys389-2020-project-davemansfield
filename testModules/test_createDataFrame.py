import createDataFrame

def test_createDataFrame():
    #this fucntion dosnt return a value so if all goes well it should return None
    #note the function must have a valid data file to read
    assert createDataFrame.createDataFrame()==None