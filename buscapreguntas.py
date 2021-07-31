# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 20:43:45 2021

@author: ldiaz
"""

#import urllib.request

#datos= urllib.request.urlopen('https://www.lider.cl/supermercado/category/Despensa').read().decode()


from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


class Pregunta(Item) :
    
    pregunta = Field()
    titulo= Field()
    id = Field()

class stackoverflowspider(Spider) :
    name = "miprimerspider"
    start_urls= ['https://stackoverflow.com/questions']
    def parse(self, response):  
        sel = Selector(response)
        preguntas = sel.xpath('//div[@id="questions"]/div[contains(@class, "question-summary")]')
        
 #iterar sobre todas las preguntas
        for i, elem in enumerate(preguntas):
            item = ItemLoader(Pregunta(), elem)
            item.add_xpath('pregunta', './/div[contains(@class, "excerpt")]/text()')
            item.add_xpath('titulo', './/h3/a/text()') 
            item.add_value('id', i)
            yield item.load_item()
            
 #scrapy runspider buscapreguntas.py -o preguntas.csv -t csv
  #      id= "questions"
   #     class= "question-summary"
    #    class "question-hyperlink"
     #   class "excerpt"
     
    