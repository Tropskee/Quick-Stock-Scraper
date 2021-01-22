#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 11:11:16 2020

@author: andrewczeropski
"""

#This program will pull the last stock price from Market Watch

#This program will pull the last stock price from Market Watch

import bs4
import requests
from bs4 import BeautifulSoup
import time

stock_symbol = input('Enter the stock symbol you want to examine:')

def ParsePrice():
    stock_URL = "https://finance.yahoo.com/quote/" + stock_symbol
    response = requests.get(stock_URL)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    price = soup.find('div', {'class' : 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
    return price

while True:
    print('The current stock price for', stock_symbol, 'is:', str(ParsePrice()))
    time.sleep(1)