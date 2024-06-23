import pytest
import openpyxl
from python_pytest.func.operation import my_add

def get_excel():
    book = openpyxl.load_workbook('../data/工作簿1.xlsx')
    sheet = book.active
    cells = sheet['A1':'C3']
    values = []
    for row in cells:
        line = []
        for cell in row:
            line.append(cell.value)
        values.append(line)
    return values

def get_csv():
    with open('../data/data.csv', 'r') as f:
        lines = f.readlines()
        values = []
        for line in lines:
            # print(line.strip())
            values.append(line.strip().split(','))
        return values
class TestWithEXCEL:
    @pytest.mark.parametrize('x,y,expected',get_excel())
    def test_add(self, x, y, expected):
        assert my_add(int(x),int(y)) == int(expected)