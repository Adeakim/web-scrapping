from getwebsite import *
from collections import Counter

class AnalyzeWeb(GetWebsiteText):
    '''This is a class that inheit infor mation from GetWebsiteText and count the number time
        each word occur in the website
    '''
    def countwords(self):
        '''this method returns the 7 most common words from the website'''
        count=Counter(self.remove_common_words()).most_common(7)
        return count
        
    def most_words(self):
        '''this method returns the most used words from the website.'''
        most_count=Counter(self.remove_common_words()).most_common(1)
        first_count=[value[0]for value in most_count]
        return f'The top word is {first_count[0]}'