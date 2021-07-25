import unittest
from .analyzeweb import *

class TestAnalyseWeb(unittest.TestCase):
    def test_most_words(self):
        result=(AnalyzeWeb.most_words([1,1,1,2,3,3]),1)
        
        
if __name__=='__main__':
    unittest.main