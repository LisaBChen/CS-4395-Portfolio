import string
import nltk
import sys
import pickle
import requests
import re
import urllib
import urllib.request
import collections

import stopwords as stopwords
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import random
from nltk.tokenize import word_tokenize
from collections import Counter
from urllib import request



# web crawler function that takes the starter site url and outputs a list of at least 15 relevant urls
def web_crawler(name):
    r = requests.get(name)  # request to get url
    info = r.text  # sets variable for url data
    soup = BeautifulSoup(info)  # sets info from beautiful soup library
    counter = 0  # counter variable

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
                if link_string.startswith(
                        'http') and 'dragon' not in link_string and 'dndbeyond' not in link_string and 'frostmaiden' not in link_string and 'ddal' not in link_string and 'fiction' not in link_string and 'merchandise' not in link_string and 'miniatures' not in link_string and 'digital-games' not in link_string and 'board-games' not in link_string and 'where-to-start' not in link_string and 'tabletop-rpg' not in link_string and 'locator' not in link_string and 'support' not in link_string and 'discord' not in link_string and 'twitch' not in link_string and 'podcast' not in link_string and 'black-dice' not in link_string and "fancontentpolicy" not in link_string:
                    f.write(link_string + '\n')  # writes websites to file
                    if counter > 11:
                        break
                    counter += 1
            elif 'dmsguild' in link_string:
                f.write(link_string + '\n')  # writes other websites to file
        link_string = "https://wpn.wizards.com/en"
        f.write(link_string + '\n')  # writes other websites to file


# checks if there a element in url
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True


# function to loop through list of urls and scrape text from each page and stores each pages text in own file
def scraper():
    # opens the test file that has the urls, reads in each of the url and scrapes the text from each page
    with open('url_list.txt', 'r') as r:  # opens text file that has the urls in it
        for (counter, line) in enumerate(r):
            with open('Scraper{0}.txt'.format(counter), 'w', encoding='utf-8') as f:  # opens file for each url
                if counter == 4:
                    html = urllib.request.urlopen(line)
                    soup = BeautifulSoup(html)
                    for script in soup(["script", "style"]):
                        script.extract()
                    text = soup.get_text()
                    f.write(text)  # writes text to file
                else:
                    html = urllib.request.urlopen(line)
                    soup = BeautifulSoup(html)
                    data = soup.findAll(text=True)
                    result = filter(visible, data)
                    info_list = list(result)
                    info_string = ' '.join(info_list)
                    f.write(info_string)  # writes scraped text to file

"""
one of the functions to clean and process scraped text, extract sentences, writes sentences 
to new file, using information extraction and retrieval, Tokenization, Text normalization,  
by using multiple NLP techniques learned in class 
"""
def clean_text():
    # opens file
    with open('Cleaner0.txt', 'w', encoding='utf-8') as f:
        with open('Scraper0.txt', 'r', encoding='utf-8') as r:
            old_text0 = r.read()  # reads in text
        clean_text0 = old_text0.replace('\n', '').replace("\t", "")  # cleans file
        sents0 = sent_tokenize(clean_text0)  # tokenizes text
        for sent in sents0:
            f.write(sent)  # writes to file

    # opens file, cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner1.txt', 'w', encoding='utf-8') as f:
        with open('Scraper1.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text1 = r.read()
        clean_text1 = old_text1.replace('\n', '').replace("\t", "")  # cleans text
        sents1 = sent_tokenize(clean_text1)  # tokenizes sentences
        for sent in sents1:
            f.write(sent)  # writes to file

    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner2.txt', 'w', encoding='utf-8') as f:
        with open('Scraper2.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text2 = r.read()
        clean_text2 = old_text2.replace('\n', '').replace("\t", "")  # cleans file
        sents2 = sent_tokenize(clean_text2)  # tokenizes sentences
        for sent in sents2:
            f.write(sent)  # writes to file

    with open('Clean2.txt', 'w', encoding='utf-8') as f:
        with open('Scraper2.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            older_text2 = r.read()
        cleaner_text2 = older_text2.replace("\t", "")  # cleans file
        senten2 = sent_tokenize(cleaner_text2)  # tokenizes sentences
        for sent in senten2:
            f.write(sent)  # writes to file

    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner3.txt', 'w', encoding='utf-8') as f:
        with open('Scraper3.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text3 = r.read()
        clean_text3 = old_text3.replace('\n', '').replace("\t", "")  # cleans text
        sents3 = sent_tokenize(clean_text3)  # tokenizes file
        for sent in sents3:
            f.write(sent)  # writes to file

    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner4.txt', 'w', encoding='utf-8') as f:
        with open('Scraper4.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text4 = r.read()
        # cleans text
        clean_text4 = old_text4.replace('\n', '').replace("\t", "").replace('', '')
        sents4 = sent_tokenize(clean_text4)  # tokenizes file
        for sent in sents4:
            f.write(sent)  # writes to file

    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner5.txt', 'w', encoding='utf-8') as f:
        with open('Scraper5.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text5 = r.read()
        clean_text5 = old_text5.replace('\n', '').replace("\t", "")  # cleans text
        sents5 = sent_tokenize(clean_text5)  # tokenizes sentences
        for sent in sents5:
            f.write(sent)  # writes to file

    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner6.txt', 'w', encoding='utf-8') as f:
        with open('Scraper6.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text6 = r.read()
        clean_text6 = old_text6.replace('\n', '').replace("\t", "")
        sents6 = sent_tokenize(clean_text6)
        for sent in sents6:
            f.write(sent)  # writes to file

    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner7.txt', 'w', encoding='utf-8') as f:
        with open('Scraper7.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text7 = r.read()
        clean_text7 = old_text7.replace('\n', '').replace("\t", "")
        sents7 = sent_tokenize(clean_text7)
        for sent in sents7:
            f.write(sent)  # writes to file

    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner8.txt', 'w', encoding='utf-8') as f:
        with open('Scraper8.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text8 = r.read()
        clean_text8 = old_text8.replace('\n', '').replace("\t", "")
        sents8 = sent_tokenize(clean_text8)
        for sent in sents8:
            f.write(sent)  # writes to file

    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner9.txt', 'w', encoding='utf-8') as f:
        with open('Scraper9.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text9 = r.read()
        clean_text9 = old_text9.replace('\n', '').replace("\t", "")
        sents9 = sent_tokenize(clean_text9)
        for sent in sents9:
            f.write(sent)  # writes to file

    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner10.txt', 'w', encoding='utf-8') as f:
        with open('Scraper10.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text10 = r.read()
        clean_text10 = old_text10.replace('\n', '').replace("\t", "")
        sents10 = sent_tokenize(clean_text10)
        for sent in sents10:
            f.write(sent)  # writes to file

    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner11.txt', 'w', encoding='utf-8') as f:
        with open('Scraper11.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text11 = r.read()
        clean_text11 = old_text11.replace('\n', '').replace("\t", "")
        sents11 = sent_tokenize(clean_text11)
        for sent in sents11:
            f.write(sent)  # writes to file

    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner12.txt', 'w', encoding='utf-8') as f:
        with open('Scraper12.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text12 = r.read()
        clean_text12 = old_text12.replace('\n', '').replace("\t", "")
        sents12 = sent_tokenize(clean_text12)
        for sent in sents12:
            f.write(sent)  # writes to file

    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner13.txt', 'w', encoding='utf-8') as f:
        with open('Scraper13.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text13 = r.read()
        clean_text13 = old_text13.replace('\n', '').replace("\t", "")
        sents13 = sent_tokenize(clean_text13)
        for sent in sents13:
            f.write(sent)  # writes to file

    # cleans up text, tokenize sentences, and writes them to a file
    with open('Cleaner14.txt', 'w', encoding='utf-8') as f:
        with open('Scraper14.txt', 'r', encoding='utf-8') as r:  # reads in scraped data file
            old_text14 = r.read()
        clean_text14 = old_text14.replace('\n', '').replace("\t", "")
        sents14 = sent_tokenize(clean_text14)
        for sent in sents14:
            f.write(sent)  # writes to file


"""
Extracts important terms from the pages and handles term extraction, information extraction, 
information retrieval and Text normalization, 
"""
def extract_terms():
    stopwords.words('english')
    info = []

    # opens file
    with open('Cleaner0.txt', 'r', encoding='utf-8') as r:
        for line in r:
            for word in line.split():
                info.append(word)
    with open('Cleaner1.txt', 'r', encoding='utf-8') as r:
        for line in r:
            for word in line.split():
                info.append(word)
    with open('Cleaner2.txt', 'r', encoding='utf-8') as r:
        for line in r:
            for word in line.split():
                info.append(word)
    with open('Cleaner3.txt', 'r', encoding='utf-8') as r:
        for line in r:
            for word in line.split():
                info.append(word)
    with open('Cleaner4.txt', 'r', encoding='utf-8') as r:
        for line in r:
            for word in line.split():
                info.append(word)
    with open('Cleaner5.txt', 'r', encoding='utf-8') as r:
        for line in r:
            for word in line.split():
                info.append(word)
    with open('Cleaner6.txt', 'r', encoding='utf-8') as r:
        for line in r:
            for word in line.split():
                info.append(word)
    with open('Cleaner7.txt', 'r', encoding='utf-8') as r:
        for line in r:
            for word in line.split():
                info.append(word)
    with open('Cleaner8.txt', 'r', encoding='utf-8') as r:
        for line in r:
            for word in line.split():
                info.append(word)
    with open('Cleaner9.txt', 'r', encoding='utf-8') as r:
        for line in r:
            for word in line.split():
                info.append(word)
    with open('Cleaner10.txt', 'r', encoding='utf-8') as r:
        for line in r:
            for word in line.split():
                info.append(word)
    with open('Cleaner11.txt', 'r', encoding='utf-8') as r:
        for line in r:
            for word in line.split():
                info.append(word)
    with open('Cleaner12.txt', 'r', encoding='utf-8') as r:
        for line in r:
            for word in line.split():
                info.append(word)
    with open('Cleaner13.txt', 'r', encoding='utf-8') as r:
        for line in r:
            for word in line.split():
                info.append(word)
    with open('Cleaner14.txt', 'r', encoding='utf-8') as r:
        for line in r:
            for word in line.split():
                info.append(word)

    # lowercase text, and removes numbers and punctuation
    for i in range(len(info)):
        info[i] = re.sub(r'[.?!,:;()\-\n\d]', ' ', info[i].lower())

    # remove stopwords
    stopwords_info = [t for t in info if t not in stopwords.words('english')]

    # uses importance measure, term frequency, tf-idf, information retrieval technique, information extraction to extract the top terms
    count = 0
    max_count = 0
    result = []

    for corpus in stopwords_info:
        find_result = {}
        for common_words in corpus.split():
            if common_words in find_result:
                find_result[common_words] += 1
            else:
                find_result[common_words] = 1
        for common_words, freq in find_result.items():
            print(common_words, freq)
            find_result[common_words] = freq / len(corpus.split())
        result.append(find_result)

# Handles additional dialog using knowledge base and collected added information and/or knowledge etc
def dialog(user_input, file_name):
    general_input = ["That's an oof","Gee, thanks", "Not a problem", "What's that?",
                     "Just why?", "You're going to need to provide more context", "Chill out",
                     "I'm fine. How are you?", "What's up?", "If you say so and/or what you think",
                     "What about you?", "I'm so tired of this", "I'm chill with whatever",
                     "Why do you say these things?", "I can't believe I woke up for this."]
    general_input.append(user_input)

    f = open("Clean2.txt", "r")
    new_text = f.read()
    info = new_text.split("\n")
    f.close()

    list_count = len(general_input)

    if "dnd" or "d&d" or "Dnd" or "dungeon" or "dragon" or "player" or "game" or "dm" or "play" in user_input:
        user_input = random.choice(info)
    elif user_input == "":
        user_input = "Why so quiet?"
    else:
        response = random.randrange(list_count)
        user_input = general_input[response]

    return user_input

# makes different user profiles and adds and stores users data including their name, likes, dislikes etc
def user_model(user_prof):
    bot_name = "Axford: "
    UserOne = "UserOne"
    UserTwo = "UserTwo"
    UserThree = "UserThree"
    person = "User"

    if user_prof == UserOne:
        print(bot_name + "Hi " + user_prof + "! " + "What’s your name?")
        print(person, end=":")
        get_name = input()
        f = open('userOne.txt', 'w')
        file_name = "userOne.txt"
        f.write(get_name + "\n")
        print(bot_name + "That’s a cool name! What are your likes and dislikes?")
        print(person, end=":")
        user_input = input()
        if user_input == "bye" or user_input == "Bye":
            quit()
        f.write(user_input + "\n")
        print(bot_name + "I’m going to take a note of that. Btw, If you saw anything weird earlier that’s just us adding or storing some data. Just ignore it ok?")
        while True:
            print(person, end=":")
            user_input = input()
            if user_input == "bye" or user_input == "Bye":
                sys.exit("Look over there! *Runs away* I gotta go, bye!")
            f.write(user_input + "\n")
            bot_response = dialog(user_input, file_name)
            print(bot_name + bot_response)
        f.close()
    elif user_prof == UserTwo:
        print(bot_name + "Hi " + user_prof + "! " + "What’s your name?")
        print(person, end=":")
        get_name = input()
        f = open('userTwo.txt', 'w')
        file_name = "userTwo.txt"
        f.write(get_name + "\n")
        print(bot_name + "That’s a cool name! What are your likes and dislikes?")
        print(person, end=":")
        user_input = input()
        if user_input == "bye" or user_input == "Bye":
            quit()
        f.write(user_input + "\n")
        print(bot_name + "I’m going to take a note of that. Btw, If you saw anything weird earlier that’s just us adding or storing some data. Just ignore it ok?")
        while True:
            print(person, end=":")
            user_input = input()
            if user_input == "bye" or user_input == "Bye":
                sys.exit("Look over there! *Runs away* I gotta go, bye!")
            f.write(user_input + "\n")
            bot_response = dialog(user_input, file_name)
            print(bot_name + bot_response)
        f.close()
    elif user_prof == UserThree:
        print(bot_name + "Hi " + user_prof + "! " + "What’s your name?")
        print(person, end=":")
        get_name = input()
        f = open('userThree.txt', 'w')
        file_name = "userThree.txt"
        f.write(get_name + "\n")
        print(bot_name + "That’s a cool name! What are your likes and dislikes?")
        print(person, end=":")
        user_input = input()
        if user_input == "bye" or user_input == "Bye":
            quit()
        f.write(user_input + "\n")
        print(bot_name + "I’m going to take a note of that. Btw, If you saw anything weird earlier that’s just us adding or storing some data. Just ignore it ok?")
        while True:
            print(person, end=":")
            user_input = input()
            if user_input == "bye" or user_input == "Bye":
                sys.exit("Look over there! *Runs away* I gotta go, bye!")
            f.write(user_input + "\n")
            bot_response = dialog(user_input, file_name)
            print(bot_name + bot_response)
        f.close()
    else:
        user_prof = "user"
        print(bot_name + "Hi " + user_prof + "! " + "What’s your name?")
        print(person, end=":")
        get_name = input()
        f = open('userPlus.txt', 'w')
        file_name = "userPlus.txt"
        f.write(get_name + "\n")
        print(bot_name + "That’s a cool name! What are your likes and dislikes?")
        print(person, end=":")
        user_input = input()
        if user_input == "bye" or user_input == "Bye":
            quit()
        f.write(user_input + "\n")
        print(bot_name + "I’m going to take a note of that. Btw, If you saw anything weird earlier that’s just us adding or storing some data. Just ignore it ok?")
        while True:
            print(person, end=":")
            user_input = input()
            if user_input == "bye" or user_input == "Bye":
                sys.exit("Look over there! *Runs away* I gotta go, bye!")
            f.write(user_input + "\n")
            bot_response = dialog(user_input, file_name)
            print(bot_name + bot_response)
        f.close()

if __name__ == '__main__':
    name = "https://dnd.wizards.com/"  # url variable
    # code that demonstrates multiple NLP techniques learned in class and external knowledge
    web_crawler(name)  # calls web_crawler function with url as argument
    scraper()  # calls scraper function
    clean_text()  # calls clean_text function
    extract_terms()  # calls extract_terms function

    bot_name = "Axford: "
    UserOne = "UserOne"
    UserTwo = "UserTwo"
    UserThree = "UserThree"
    User = "User"
    intro = "Hi, I’m Axford, a chaotic chatbot that has an interest in DnD. "
    user_prof_select = "Please enter one of the following choices: UserOne, UserTwo, UserThree"
    print(bot_name + intro + user_prof_select)
    user_input = input("User: ")
    # creates different user model saved for each user
    user_model(user_input)
