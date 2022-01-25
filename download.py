#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 16:00:15 2022

@author: jiechi
"""
import urllib.request
import pathlib
import os 
import argparse
from bs4 import BeautifulSoup


def html_parse (corpus, data_dir):
    base_url = 'http://www.bangortalk.org.uk/'
    url = base_url + 'speakers.php?c=' + corpus
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    for tr in soup.findAll('tr'):
        if len(tr.findAll('td')) == 1:
            file_name = tr.find('td').text
    #wav url: http://bangortalk.bangor.ac.uk/davies1.mp3 
    #chat url: http://www.bangortalk.org.uk/chats/siarad/davies1.cha
            wav_url = 'http://bangortalk.bangor.ac.uk/' + file_name + '.mp3'
            
            chat_url = base_url + 'chats/' + corpus + '/' + file_name + '.cha'
            p = pathlib.Path(os.path.join(data_dir, file_name))
            p.mkdir(parents=True, exist_ok=True)
            print(wav_url)
            urllib.request.urlretrieve(wav_url, os.path.join(data_dir, file_name, file_name+".mp3"))
            print(chat_url)
            urllib.request.urlretrieve(chat_url, os.path.join(data_dir, file_name, file_name+".cha"))
            
            fout = open(os.path.join(data_dir, file_name, file_name+".txt"), 'w')
            fout.writelines("{0:<10}{1:<10}{2:<10}\n".format('speaker', 'age', 'sex'))
        else:
            tags = tr.findAll('td')[1:4]
            fout.writelines("{0:<10}{1:<10}{2:<10}\n".format(tags[0].text, tags[1].text, tags[2].text))
            
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download corpus from http://www.bangortalk.org.uk/.",
                                     usage="python download.py --data_dir ./ --corpora siarad miami")
    parser.add_argument("-d", "--data_dir", type=str, nargs="?", default='/home/jiechi/ssd_home/data/codeswitch', help='dir to save the data')
    parser.add_argument("-c", "--corpora", nargs="+", default=['siarad', 'patagonia', 'miami'], help='a list of corpora to be downloaded')
    
    value = parser.parse_args()
    data_dir = value.data_dir
    corpora = value.corpora
    print(data_dir)
    print(corpora)
    p = pathlib.Path(os.path.join(data_dir, 'bangortalk'))
    p.mkdir(parents=True, exist_ok=True)
    
    #corpus name
    #corpora = ['siarad', 'patagonia', 'miami']
    for i in corpora:
        p = pathlib.Path(os.path.join(data_dir, 'bangortalk', i))
        p.mkdir(parents=True, exist_ok=True)
        html_parse(i, os.path.join(data_dir, 'bangortalk', i))

