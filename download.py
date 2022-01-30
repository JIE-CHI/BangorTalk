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
import multiprocessing

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


def worker(bash_file):
    os.system(f"bash {bash_file}")  
      

    
def prepare (corpora, data_dir):

    base_dir = data_dir
    wavscp = open(base_dir+'/wav.scp','w')
    fout = open(base_dir+'/trans','w')
    utt2spk = open(base_dir + '/utt2spk', 'w')
    bash_files = []

    for corpus in corpora:
        corpus_dir = pathlib.Path(os.path.join(base_dir, corpus))
        for audio in corpus_dir.iterdir():
            bash_file = 'trim' + '_' + corpus +'_' + audio.name + '.sh'
            bash_files.append(bash_file)
            bash = open(bash_file,'w')
            bash.writelines("#!/bin/bash\n")
            p = audio / 'split'
            p.mkdir(parents=True, exist_ok=True)
            chat_file = os.path.join(str(audio) , audio.name +'.cha')
            count = 0
            with open(chat_file, 'r') as f:
                for line in f:
                    if '\x15' in line and line[0] == '*':
                        count += 1
                        line = line.replace('\x15', '')
#                        print(line)
                        start, end = (line.split()[-1]).split('_')
                        speaker = line.split(':')[0][1::]
                        text = ' '.join((line.split(':')[1]).split()[0:-1])
                        
#                       print(speaker, text)
                        utterid = speaker + '-' + audio.name + f'-{count:04}'
#                        print(start, end)
                        fout.writelines(f"utterid\t{' '.join(text)}\n")
                        wavscp.writelines(f"utterid\t{os.path.join(str(p), utterid)}.wav\n")
                        utt2spk.writelines(f"{speaker}-{audio.name}\t{utterid}\t")
                        #f"{5:04}"
                        cmd = f"ffmpeg -y -i {os.path.join(str(audio), audio.name + '.mp3')} -ss {int(start)/1000} -to {int(end)/1000} -ar 16000 {os.path.join(str(p), utterid)}.wav"
#                        print(cmd)
                        bash.writelines(cmd + "\n")

    
    jobs = []
    for i in bash_files:
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
    os.system("rm trim*.sh") 

def clean (corpus, data_dir):
    pass

def data_split(corpus, data_dir, file_list):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download corpus from http://www.bangortalk.org.uk/.",
                                     usage="python download.py --data_dir ./ --corpora siarad miami")
    parser.add_argument("-d", "--data_dir", type=str, nargs="?", default='/home/jiechi/ssd_home/data/codeswitch', 
                        help='dir to save the data')
    parser.add_argument("-c", "--corpora", nargs="+", default=['siarad', 'patagonia', 'miami'], 
                        help='a list of corpora to be downloaded')
    parser.add_argument("-fs", "--first_step", type=str, nargs="?", default='1',
                        help='1:download data 2:preprocess')
    parser.add_argument("-sr", "--split_ref", type=str, nargs="?", default='None', 
                        help='split data into train, dev, test based on this file, if None then split it randomly 8:1:1 ')

    value = parser.parse_args()
    data_dir = value.data_dir
    corpora = value.corpora
    fs = int(value.first_step)
    file_list = value.split_ref
    print(data_dir)
    print(corpora)
    if fs <= 1:
        p = pathlib.Path(os.path.join(data_dir, 'bangortalk'))
        p.mkdir(parents=True, exist_ok=True)
    
        #corpus name
        #corpora = ['siarad', 'patagonia', 'miami']
        for i in corpora:
            p = pathlib.Path(os.path.join(data_dir, 'bangortalk', i))
            p.mkdir(parents=True, exist_ok=True)
            html_parse(i, os.path.join(data_dir, 'bangortalk', i))
    if fs <= 2:
        prepare(corpora, os.path.join(data_dir, 'bangortalk'))
        
    if fs <= 3:
        clean(corpora, data_dir)
    
    if fs <= 4:
        data_split(corpora, data_dir, file_list=None)
    
        

