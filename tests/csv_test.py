"""Testing CSV Functions"""

import os.path
import pandas as pd
from csvmanager.write import Write
from csvmanager.read import Read


def test_write_csv():
    """testing that our calculator has a static method for addition"""
    # Arrange
    filename = 'csv_output.csv'
    path = 'tests/test_data'
    fullpath = path + '/' + filename
    name_dict = {
        'value1': ['1.0', '2.0', '3.0', '4.0'],
        'value2': ['1.0', '2.0', '3.0', '4.0'],
        'result': [2.0, 4.0, 6.0, 8.0]
    }
    os.remove(fullpath)
    df_data = pd.DataFrame(name_dict)
    # Act

    Write.dataframetocsvfile(fullpath, df_data)
    # Assert
    assert os.path.exists(fullpath)


# pylint: disable= C0123
def test_read_csv():
    """testing that our calculator has a static method for addition"""
    # Arrange
    filename = 'csv_output.csv'
    path = 'tests/test_data'
    fullpath = path + '/' + filename
    # Act
    df_data1 = Read.dataframefromcsvfile(fullpath)
    # Assert
    assert type(df_data1) is pd.DataFrame
