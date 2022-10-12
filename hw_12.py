# Lisa Chen
# BZC180000
# Homework 12

import string
import nltk
import sys
import pickle
import requests
import re
import urllib
import urllib.request

import stopwords as stopwords
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
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
                if link_string.startswith('http') and 'dragon' not in link_string and 'dndbeyond' not in link_string and 'frostmaiden' not in link_string and 'ddal' not in link_string and 'fiction' not in link_string and 'merchandise' not in link_string and 'miniatures' not in link_string and 'digital-games' not in link_string and 'board-games' not in link_string and 'where-to-start' not in link_string and 'tabletop-rpg' not in link_string and 'locator' not in link_string and 'support' not in link_string and 'discord' not in link_string and 'twitch' not in link_string and 'podcast' not in link_string and 'black-dice' not in link_string and "fancontentpolicy" not in link_string:
                    f.write(link_string + '\n') # writes websites to file
                    if counter > 11:
                        break
                    counter += 1
            elif 'dmsguild' in link_string:
                f.write(link_string + '\n') # writes other websites to file
        link_string = "https://wpn.wizards.com/en"
        f.write(link_string + '\n')  # writes other websites to file

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
    # opens the test file that has the urls, reads in each of the url and scrapes the text from each page
    with open('url_list.txt', 'r') as r: # opens text file that has the urls in it
        for (counter, line) in enumerate(r):
            with open('Scraper{0}.txt'.format(counter), 'w', encoding='utf-8') as f: # opens file for each url
                if counter == 4:
                    html = urllib.request.urlopen(line)
                    soup = BeautifulSoup(html)
                    for script in soup(["script", "style"]):
                        script.extract()
                    text = soup.get_text()
                    f.write(text) # writes text to file
                else:
                    html = urllib.request.urlopen(line)
                    soup = BeautifulSoup(html)
                    data = soup.findAll(text=True)
                    result = filter(visible, data)
                    info_list = list(result)
                    info_string = ' '.join(info_list)
                    f.write(info_string) # writes scraped text to file

# function to clean scraped text, extract sentences, and writes sentences to new file
def clean_text():
    # opens file
    with open('Cleaner0.txt', 'w', encoding='utf-8') as f:
        with open('Scraper0.txt', 'r', encoding='utf-8') as r:
            old_text0 = r.read() # reads in text
        clean_text0 = old_text0.replace('\n', '').replace("\t", "") # cleans file
        sents0 = sent_tokenize(clean_text0) # tokenizes text
        for sent in sents0:
            f.write(sent) # writes to file

    #opens file, cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner1.txt', 'w', encoding='utf-8') as f:
        with open('Scraper1.txt', 'r', encoding='utf-8') as r: # reads in scraped data file
            old_text1 = r.read()
        clean_text1 = old_text1.replace('\n', '').replace("\t", "") # cleans text
        sents1 = sent_tokenize(clean_text1) # tokenizes sentences
        for sent in sents1:
            f.write(sent) # writes to file
        
    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner2.txt', 'w', encoding='utf-8') as f:
        with open('Scraper2.txt', 'r', encoding='utf-8') as r: # reads in scraped data file
            old_text2 = r.read()
        clean_text2 = old_text2.replace('\n', '').replace("\t", "") # cleans file
        sents2 = sent_tokenize(clean_text2) # tokenizes sentences
        for sent in sents2:
            f.write(sent) # writes to file
        
    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner3.txt', 'w', encoding='utf-8') as f:
        with open('Scraper3.txt', 'r', encoding='utf-8') as r: # reads in scraped data file
            old_text3 = r.read()
        clean_text3 = old_text3.replace('\n', '').replace("\t", "") # cleans text
        sents3 = sent_tokenize(clean_text3) # tokenizes file
        for sent in sents3:
            f.write(sent) # writes to file
        
    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner4.txt', 'w', encoding='utf-8') as f:
        with open('Scraper4.txt', 'r', encoding='utf-8') as r: # reads in scraped data file
            old_text4 = r.read()
        # cleans text
        clean_text4 = old_text4.replace('\n', '').replace("\t", "").replace('','')
        sents4 = sent_tokenize(clean_text4) # tokenizes file
        for sent in sents4:
            f.write(sent) # writes to file

    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner5.txt', 'w', encoding='utf-8') as f:
        with open('Scraper5.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text5 = r.read()
        clean_text5 = old_text5.replace('\n', '').replace("\t", "") # cleans text
        sents5 = sent_tokenize(clean_text5) # tokenizes sentences
        for sent in sents5:
            f.write(sent) # writes to file
        
    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner6.txt', 'w', encoding='utf-8') as f:
        with open('Scraper6.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text6 = r.read()
        clean_text6 = old_text6.replace('\n', '').replace("\t", "")
        sents6 = sent_tokenize(clean_text6)
        for sent in sents6:
            f.write(sent) # writes to file
        
    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner7.txt', 'w', encoding='utf-8') as f:
        with open('Scraper7.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text7 = r.read()
        clean_text7 = old_text7.replace('\n', '').replace("\t", "")
        sents7 = sent_tokenize(clean_text7)
        for sent in sents7:
            f.write(sent) # writes to file
    
    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner8.txt', 'w', encoding='utf-8') as f:
        with open('Scraper8.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text8 = r.read()
        clean_text8 = old_text8.replace('\n', '').replace("\t", "")
        sents8 = sent_tokenize(clean_text8)
        for sent in sents8:
            f.write(sent) # writes to file
        
    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner9.txt', 'w', encoding='utf-8') as f:
        with open('Scraper9.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text9 = r.read()
        clean_text9 = old_text9.replace('\n', '').replace("\t", "")
        sents9 = sent_tokenize(clean_text9)
        for sent in sents9:
            f.write(sent) # writes to file
        
    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner10.txt', 'w', encoding='utf-8') as f:
        with open('Scraper10.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text10 = r.read()
        clean_text10 = old_text10.replace('\n', '').replace("\t", "")
        sents10 = sent_tokenize(clean_text10)
        for sent in sents10:
            f.write(sent) # writes to file
        
    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner11.txt', 'w', encoding='utf-8') as f:
        with open('Scraper11.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text11 = r.read()
        clean_text11 = old_text11.replace('\n', '').replace("\t", "")
        sents11 = sent_tokenize(clean_text11)
        for sent in sents11:
            f.write(sent) # writes to file
        
    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner12.txt', 'w', encoding='utf-8') as f:
        with open('Scraper12.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text12 = r.read()
        clean_text12 = old_text12.replace('\n', '').replace("\t", "")
        sents12 = sent_tokenize(clean_text12)
        for sent in sents12:
            f.write(sent) # writes to file
        
    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner13.txt', 'w', encoding='utf-8') as f:
        with open('Scraper13.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text13 = r.read()
        clean_text13 = old_text13.replace('\n', '').replace("\t", "")
        sents13 = sent_tokenize(clean_text13)
        for sent in sents13:
            f.write(sent) # writes to file
        
    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner14.txt', 'w', encoding='utf-8') as f:
        with open('Scraper14.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text14 = r.read()
        clean_text14 = old_text14.replace('\n', '').replace("\t", "")
        sents14 = sent_tokenize(clean_text14)
        for sent in sents14:
            f.write(sent) # writes to file

# function to extract at least 25 important terms from the pages and print them
def extract_terms():
    stopwords.words('english')

    # opens file
    with open('Cleaner0.txt', 'r', encoding='utf-8') as r:
        content0 = r.read()
    with open('Cleaner1.txt', 'r', encoding='utf-8') as r:
        content1 = r.read()
    with open('Cleaner2.txt', 'r', encoding='utf-8') as r:
        content2 = r.read()
    with open('Cleaner3.txt', 'r', encoding='utf-8') as r:
        content3 = r.read()
    with open('Cleaner4.txt', 'r', encoding='utf-8') as r:
        content4 = r.read()
    with open('Cleaner5.txt', 'r', encoding='utf-8') as r:
        content5 = r.read()
    with open('Cleaner6.txt', 'r', encoding='utf-8') as r:
        content6 = r.read()
    with open('Cleaner7.txt', 'r', encoding='utf-8') as r:
        content7 = r.read()
    with open('Cleaner8.txt', 'r', encoding='utf-8') as r:
        content8 = r.read()
    with open('Cleaner9.txt', 'r', encoding='utf-8') as r:
        content9 = r.read()
    with open('Cleaner10.txt', 'r', encoding='utf-8') as r:
        content10 = r.read()
    with open('Cleaner11.txt', 'r', encoding='utf-8') as r:
        content11 = r.read()
    with open('Cleaner12.txt', 'r', encoding='utf-8') as r:
        content12 = r.read()
    with open('Cleaner13.txt', 'r', encoding='utf-8') as r:
        content13 = r.read()
    with open('Cleaner14.txt', 'r', encoding='utf-8') as r:
        content14 = r.read()

    information = content0 + "" + content1 + "" + content2 + "" + content3 + "" + content4 + "" + content5 + "" + content6 + "" + content7 + "" + content8 + "" + content9 + "" + content10 + "" + content11 + "" + content12 + "" + content13 + "" + content14

    # lowercase text
    lowercase_info = [t.lower() for t in information]

    # remove stopwords, number, and punctuation
    stopwords_info = [t for t in lowercase_info if t.isalpha() and t not in stopwords.words('english')]
    
    # uses importance measure such as term frequency or tf-idf to extract the top 25-40 terms
    count = 0
    max_count = 0
    result = []
    for i in range(len(stopwords_info)):
        for j in range(len(stopwords_info)):
            if (stopwords_info[i] == stopwords_info[j]):  # finding word count
                count += 1
            else:
                count = count
            if (count == max_count):  # comparing with max count
                result.append(stopwords_info[i])
            elif (count > max_count):
                result.clear()
                result.append(stopwords_info[i])
                max_count = count
            else:
                result = result
            count = 0
        if count == 30:
            break
    print(result)

    sorted_counts_result = sorted(stopwords_info.items(), key=lambda x: x[1], reverse=True)
    print("30 most common words:")
    for y in range(30):
        print(sorted_counts_result[y])

# function to build knowledge base
def knowledge_base():
    # python dict of knowledge base that has facts
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

    # pickles python dict
    with open('my_pickle', 'wb') as handle:
        pickle.dump(knowledge_base_dict, handle)

if __name__ == '__main__':
    name =  "https://dnd.wizards.com/" # url variable
    web_crawler(name) # calls web_crawler function with url as argument
    scraper() # calls scraper function
    clean_text() # calls clean_text function
    extract_terms() # calls extract_terms function
    knowledge_base() # calls knowledge base function
   




