# Lisa Chen
# BZC180000
# Homework 12

import os
import pathlib
import string
import nltk
import sys
import pickle
import requests
import re
import urllib.request
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup
from urllib import request

# web crawler function that takes the starter site url and outputs a list of at least 15 relevant urls
def web_crawler(name):
    r = requests.get(name)  # request to get url
    info = r.text # sets variable for url data
    soup = BeautifulSoup(info) # sets info from beautiful soup library
    counter = 0 # counter variable

    # writes list of urls to a file
    with open('url_list.txt', 'w') as f:
        for link in soup.find_all('a'):
            link_string = str(link.get('href'))
            # filters out unwanted urls
            if 'wizards' in link_string or 'dnd' in link_string:
                if link_string.startswith('/url?q='):
                    link_string = link_string[7:]
                    print('MOD:', link_string)
                if '&' in link_string:
                    i = link_string.find('&')
                    link_string = link_string[:i]
                if link_string.startswith('http') and 'witchlight' not in link_string and 'ddal' not in link_string and 'dragonmag' not in link_string and 'dragon' not in link_string and 'fiction' not in link_string and 'merchandise' not in link_string and 'miniatures' not in link_string and 'digital-games' not in link_string and 'board-games' not in link_string and 'where-to-start' not in link_string and 'tabletop-rpg' not in link_string and 'locator' not in link_string and 'support' not in link_string and 'discord' not in link_string and 'twitch' not in link_string and 'podcast' not in link_string and 'black-dice' not in link_string and "fancontentpolicy" not in link_string:
                    f.write(link_string + '\n') # writes websites to file
                    if counter > 12:
                        break
                    counter += 1
            elif 'dmsguild' in link_string:
                f.write(link_string + '\n') # writes other websites to file

    # displays list of urls
    with open('url_list.txt', 'r') as r:
        urls = r.read().splitlines()
    for u in urls:
        print(u)

#checks if there a element in url
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True

# function to loop through list of urls and scrape text from each page and stores each pages text in own file
def scraper():
    # opens the test file that has the urls
    with open('url_list.txt', 'r') as r:
        urls = r.read().splitlines()
    counter = 0
    # reads in each of the url and scrapes the text from each page
    for u in urls:
        html = urllib.request.urlopen(u)
        soup = BeautifulSoup(html)
        data = soup.findAll(text=True)
        result = filter(visible, data)
        info_list = list(result)
        info_string = ' '.join(info_list)
        # takes text from each page and saves it in a file
        for (counter, line) in enumerate(u):
            with open('Scraper{0}.txt'.format(counter), 'w', encoding='utf-8') as f:
                f.write(info_string)
        counter += 1

# function to clean scraped text, extract sentences, and writes sentences to new file
def clean_text():
    counter = 0
    # opens file
    with open('Scraper0.txt', 'r') as r:
        old_text = r.read()
    with open('Scraper1.txt', 'r') as r:
        old_text1 = r.read()
    with open('Scraper2.txt', 'r') as r:
        old_text2 = r.read()
    with open('Scraper3.txt', 'r') as r:
        old_text3 = r.read()
    with open('Scraper4.txt', 'r') as r:
        old_text4 = r.read()
    with open('Scraper5.txt', 'r') as r:
        old_text5 = r.read()
    with open('Scraper6.txt', 'r') as r:
        old_text6 = r.read()
    with open('Scraper7.txt', 'r') as r:
        old_text7 = r.read()
    with open('Scraper8.txt', 'r') as r:
        old_text8 = r.read()
    with open('Scraper9.txt', 'r') as r:
        old_text9 = r.read()
    with open('Scraper10.txt', 'r') as r:
        old_text10 = r.read()
    with open('Scraper11.txt', 'r') as r:
        old_text11 = r.read()
    with open('Scraper12.txt', 'r') as r:
        old_text12 = r.read()
    with open('Scraper13.txt', 'r') as r:
        old_text13 = r.read()
    with open('Scraper14.txt', 'r') as r:
        old_text14 = r.read()

    # cleans up text
    clean_text = old_text('\n', '')
    clean_text1 = old_text1.replace('\n', '').replace("\t", "")
    clean_text2 = old_text2.replace('\n', '').replace("\t", "")
    clean_text3 = old_text3.replace('\n', '').replace("\t", "")
    clean_text4 = old_text4.replace('\n', '').replace("\t", "")
    clean_text5 = old_text5.replace('\n', '').replace("\t", "")
    clean_text6 = old_text6.replace('\n', '').replace("\t", "")
    clean_text7 = old_text7.replace('\n', '').replace("\t", "")
    clean_text8 = old_text8.replace('\n', '').replace("\t", "")
    clean_text9 = old_text9.replace('\n', '').replace("\t", "")
    clean_text10 = old_text10.replace('\n', '').replace("\t", "")
    clean_text11 = old_text11.replace('\n', '').replace("\t", "")
    clean_text12 = old_text12.replace('\n', '').replace("\t", "")
    clean_text13 = old_text13.replace('\n', '').replace("\t", "")
    clean_text14 = old_text14.replace('\n', '').replace("\t", "")

    # extracts sentences with nltk's sentence tokenizer
    sents = sent_tokenize(clean_text)
    sents1 = sent_tokenize(clean_text1)
    sents2 = sent_tokenize(clean_text2)
    sents3 = sent_tokenize(clean_text3)
    sents4 = sent_tokenize(clean_text4)
    sents5 = sent_tokenize(clean_text5)
    sents6 = sent_tokenize(clean_text6)
    sents7 = sent_tokenize(clean_text7)
    sents8 = sent_tokenize(clean_text8)
    sents9 = sent_tokenize(clean_text9)
    sents10 = sent_tokenize(clean_text10)
    sents11 = sent_tokenize(clean_text11)
    sents12 = sent_tokenize(clean_text12)
    sents13 = sent_tokenize(clean_text13)
    sents14 = sent_tokenize(clean_text14)

    # writes sentences for each file to a new file
    with open('Cleaner.txt', 'w', encoding='utf-8') as f:
        f.write(sents)
    with open('Cleaner1.txt', 'w', encoding='utf-8') as f:
        f.write(sents1)
    with open('Cleaner2.txt', 'w', encoding='utf-8') as f:
        f.write(sents2)
    with open('Cleaner3.txt', 'w', encoding='utf-8') as f:
        f.write(sents3)
    with open('Cleaner4.txt', 'w', encoding='utf-8') as f:
        f.write(sents4)
    with open('Cleaner5.txt', 'w', encoding='utf-8') as f:
        f.write(sents5)
    with open('Cleaner6.txt', 'w', encoding='utf-8') as f:
        f.write(sents6)
    with open('Cleaner7.txt', 'w', encoding='utf-8') as f:
        f.write(sents7)
    with open('Cleaner8.txt', 'w', encoding='utf-8') as f:
        f.write(sents8)
    with open('Cleaner9.txt', 'w', encoding='utf-8') as f:
        f.write(sents9)
    with open('Cleaner10.txt', 'w', encoding='utf-8') as f:
        f.write(sents10)
    with open('Cleaner11.txt', 'w', encoding='utf-8') as f:
        f.write(sents11)
    with open('Cleaner12.txt', 'w', encoding='utf-8') as f:
        f.write(sents12)
    with open('Cleaner13.txt', 'w', encoding='utf-8') as f:
        f.write(sents13)
    with open('Cleaner14.txt', 'w', encoding='utf-8') as f:
        f.write(sents14)

# function to extract at least 25 important terms from the pages
def extract_terms():
    # uses importance measure such as term frequency or tf-idf to extract at least 25 important terms
    with open('Cleaner.txt', 'r') as r:
        content = r.read()
    with open('Cleaner1.txt', 'r') as r:
        content1 = r.read()
    with open('Cleaner2.txt', 'r') as r:
        content2 = r.read()
    with open('Cleaner3.txt', 'r') as r:
        content3 = r.read()
    with open('Cleaner4.txt', 'r') as r:
        content4 = r.read()
    with open('Cleaner5.txt', 'r') as r:
        content5 = r.read()
    with open('Cleaner6.txt', 'r') as r:
        content6 = r.read()
    with open('Cleaner7.txt', 'r') as r:
        content7 = r.read()
    with open('Cleaner8.txt', 'r') as r:
        content8 = r.read()
    with open('Cleaner9.txt', 'r') as r:
        content9 = r.read()
    with open('Cleaner10.txt', 'r') as r:
        content10 = r.read()
    with open('Cleaner11.txt', 'r') as r:
        content11 = r.read()
    with open('Cleaner12.txt', 'r') as r:
        content12 = r.read()
    with open('Cleaner13.txt', 'r') as r:
        content13 = r.read()
    with open('Cleaner14.txt', 'r') as r:
        content14 = r.read()
    information = content + content1 + content2 + content3 + content4 + content5 + content6 + content7 + content8 + content9 + content10 + content11 + content12 + content13 + content14
    count = 0
    max_count = 0
    result = []
    # prints top 25-40 words
    for i in range(len(information)):
        for j in range(len(information)):
            if (information[i] == information[j]):  # finding word count
                count += 1
            else:
                count = count
            if (count == max_count):  # comparing with max count
                result.append(information[i])
            elif (count > max_count):
                result.clear()
                result.append(information[i])
                max_count = count
            else:
                result = result
            count = 0
    print(result)

# function to build knowledge base
def knowledge_base():
    # python dict of knowledge base
    knowledge_base_dict = {"dnd": "Go to dndbeyond",
                           "players": "Find more in the player's handbook and at D&D beyond",
                           "magic": "cast spells of explosive fire, arcing lightning, subtle deception, and brute-force mind control.",
                           "fight": "share an unparalleled mastery with weapons and armor, and a thorough knowledge of the skills of combat.",
                           "D&D": "create a character in minutes and jump into action with your digital character sheet. ",
                           "game": "gaming table primarily intended for pen-and-paper style narrative roleplaying games",
                           "party": "You can play D&D solo or with one friend (a duet) to satisfy that urge to roll your d20s",
                           "DM": "tell fantastic stories with your friends ",
                           "skill": "Even if the group doesn’t complete the adventure successfully, the good time and memories make everyone a winne",
                           "Dungeon": " create an exciting story where their bold adventurers confront deadly perils."}

if __name__ == '__main__':
    name =  "https://dnd.wizards.com/" # url variable
    web_crawler(name) # calls web_crawler function with url as argument

    scraper() # calls scraper function
    clean_text() # calls clean_text function
    extract_terms() # calls extract_terms function
    knowledge_base() # calls knowledge base function
   




