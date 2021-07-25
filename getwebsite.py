import requests
from bs4 import BeautifulSoup
from common import common_words
import nltk
import re


class GetWebsiteText:   
    '''Class taking the text, convert it to list, then remove the common words from the website'''
    def __init__(self,url):
        self.url=url
    
    def get_website(self):
        '''Functions that get the website and remove all the html tags and convert to texts.'''
        res=requests.get(self.url)
        soup= BeautifulSoup(res.text,'html.parser')
        raw_text=soup.get_text()
        return raw_text
            
            
                
    def get_text_list(self):
        '''Funcions that convert raw text into a list'''
        tokenizer = nltk.tokenize.RegexpTokenizer('[a-zA-z]+')
        tokens = tokenizer.tokenize(self.get_website())
        return tokens
    
    def lower_case_all(self):
        '''This function convert all the text to lower case'''
        words=[]
        for word in self.get_text_list():
            words.append(word.lower())
        return words
    
    def remove_common_words(self):
        '''this function remove the common words like is,the,my etc'''
        new_words=[]
        for element in self.lower_case_all():
            if element not in common_words and len(element) >=3:
                 new_words.append(element)
        return new_words
    