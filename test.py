from main import *



def test_noot_found():
    patterns = ['zzz']
    s = "abcba"
    root = aho_create_statemachine(patterns)
    ans = aho_find_all(s, root)
    pos = ans.get('zzz', None)
    assert pos == None

def test_found(): 

    patterns = ['a', 'ab', 'abc', 'bc', 'c', 'cba', 'zzz', 'abcbad'] 

    s = "abcba" 

    root = aho_create_statemachine(patterns) 

    ans = aho_find_all(s, root) 

    assert ans['a'] == [0, 4] 

