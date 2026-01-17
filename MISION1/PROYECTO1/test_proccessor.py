from proccessor import clean_id
def test_clean_id():
    assert clean_id("cc-24.879.987")=="24879987"
    
from proccessor import merge_name
def test_merge_name():
    assert merge_name("Isabel", "Alzate")=="Isabel Alzate"
    