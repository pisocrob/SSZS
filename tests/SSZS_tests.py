from nose.tools import *
from SSZS.writer import XMLWriter

#fix this

def test_generateXML():
    generation = XMLWriter()
    generation.generateXML('captn', '250', '77')
    assert_equal(generation.vname, 'captn')
    assert_equal(generation.vyears, '250')
    assert_equal(generation.vechoes, '77')