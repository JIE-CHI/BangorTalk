#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 19:27:03 2022

@author: jiechi
"""
import os 
import pathlib
import multiprocessing
import re

corpora = ['siarad', 'patagonia', 'miami']
base_dir = '/home/jiechi/ssd_home/data/codeswitch/bangortalk'


bash_files = []
# not_permitted = ['[/.]+<']
for corpus in corpora:
    corpus_dir = pathlib.Path(os.path.join(base_dir, corpus))
    wavscp = open(base_dir+'/' +corpus + 'wav.scp','w')
    fout = open(base_dir+'/' +corpus + 'trans','w')
    utt2spk = open(base_dir + '/' +corpus + 'utt2spk', 'w')
    for audio in corpus_dir.iterdir():
        # bash_file = 'trim' + '_' + corpus +'_' + audio.name + '.sh'
        # bash_files.append(bash_file)
        # bash = open(bash_file,'w')
        # bash.writelines("#!/bin/bash\n")
        p = audio / 'split'
        p.mkdir(parents=True, exist_ok=True)
        
        chat_file = os.path.join(str(audio) , audio.name +'.cha')
        count = 0
        with open(chat_file, 'r') as f:
            for line in f:
                if 'Language markers:' in line:
                    # print(line)
                    m = re.search('(?<=Untagged words are )(\w+)', line).group(1)
                   
                    if m == 'Spanish':
                        marker = 's'
                    elif m == 'English':
                        marker = 'e'
                        
                    elif m == 'Welsh':
                        marker = 'w'
                if '\x15' in line and line[0] == '*':
                    if '[- spa]' in line:
                        m = 's'
                        line = line.replace('[- spa]', '')
                    elif '[- cym]' in line:
                        m = 'w'
                        line = line.replace('[- cym]', '')
                    elif '[- eng]' in line:
                        m = 'e'
                        line = line.replace('[- eng]', '')
                    else:
                        m = marker
                    count += 1
                    line = line.replace('\x15', '')
                    # print(marker)
                    # print(line)
                    start, end = (line.split()[-1]).split('_')
                    speaker = line.split(':')[0][1::]
                    words = (line.split("\t")[1]).split()[0:-1]
                    #text = ' '.join((line.split(':')[1]).split()[0:-1])
                    text = []
                    for word in words[0:-1]:
                        
                        if '@s:eng&spa' in word:
                            word = word.replace('@s:eng&spa', '')
                            word = 'esu_' + word
                            
                        elif '@s:spa+cym' in word:
                            word = word.replace('@s:spa+cym', '')
                            word = 'sw_' + word

                        elif '@s:eng+spa' in word:
                            word = word.replace('@s:eng+spa', '')
                            word = 'es_' + word
                        elif '@s:spa+eng' in word:
                            word = word.replace('@s:spa+eng', '')
                            word = 'se_' + word
                        elif '@s:cym+spa' in word:
                            word = word.replace('@s:cym+spa', '')
                            word = 'ws_' + word
                        elif '@s:cym&spa' in word:
                            word = word.replace('@s:cym&spa', '')
                            word = 'wsu_' + word
                        elif '@s:cym&eng' in word:
                            word = word.replace('@s:cym&eng', '')
                            word = 'weu_' + word
                        elif '@s:spa' in word:
                            word = word.replace('@s:spa', '')
                            word = 's_' + word
                        elif '@s:eng' in word:
                            word = word.replace('@s:eng', '')
                            word = 'e_' + word
                        elif '@s:cym' in word:
                            word = word.replace('@s:cym', '')
                            word = 'w_' + word
                        else:
                            word = m + '_' + word
                        text.append(word)
                                    
                        
                        
                    
                    utterid = speaker + '-' + audio.name + f'-{count:04}'
                    # print(utterid, ' '.join(text))
                    # break
                    fout.writelines(f"{utterid}\t{' '.join(text)}\n")
                    wavscp.writelines(f"{utterid}\t{os.path.join(str(p), utterid)}.wav\n")
                    utt2spk.writelines(f"{utterid}\t{speaker}-{audio.name}\n")
                    #f"{5:04}"
                    # cmd = f"ffmpeg -y -i {os.path.join(str(audio), audio.name + '.mp3')} -ss {int(start)/1000} -to {int(end)/1000} -ar 16000 {os.path.join(str(p), utterid)}.wav"
                    # print(cmd)
                    # bash.writelines(cmd + "\n")
# def worker(bash_file):
#     os.system(f"bash {bash_file}")  
      
# jobs = []
# for i in bash_files:
#     p = multiprocessing.Process(target=worker, args=(i,))
#     jobs.append(p)
#     p.start()
# os.system("rm trim*.sh")


# test_dir = '/home/jiechi/ssd_home/data/codeswitch/bangortalk/patagonia/patagonia1'
# file_name = 'patagonia1'
# chat_file = os.path.join(test_dir, file_name + '.cha')
# p = pathlib.Path(os.path.join(test_dir , 'split'))
# p.mkdir(parents=True, exist_ok=True)
# lines = open(chat_file,'r').read().split("\n")
# fout = open(os.path.join(str(p), 'trans'),'w')

# for line in lines:
#     if '\x15' in line:
#         line = line.replace('\x15', '')
#         start, end = (line.split()[-1]).split('_')
#         speaker = line.split(':')[0][1::]
#         text = ' '.join((line.split(':')[1]).split()[0:-1])
#         print(line)
#         print(speaker, text)
#         utterid = file_name + f'-{5:04}'
#         print(start, end)
#         #f"{5:04}"
#         cmd = f"ffmpeg -i {os.path.join(test_dir, file_name + '.mp3')} -ss {int(start)/1000} -to {int(end)/1000} -ar 16000 {os.path.join(str(p), utterid)}.wav"
#         print(cmd)
#         bash.writelines(cmd + "\n")
#         break
# os.system(f"bash {bash_file}")
        