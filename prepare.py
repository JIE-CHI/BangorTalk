#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 19:27:03 2022

@author: jiechi
"""
import os 
import pathlib


corpora = ['siarad', 'patagonia', 'miami']
base_dir = '/home/jiechi/ssd_home/data/codeswitch/bangortalk'
bash_file = 'trim.sh'
bash = open(bash_file,'w')
bash.writelines("#!/bin/bash\n")
wavscp = open(base_dir+'/wav.scp','w')
fout = open(base_dir+'/trans','w')
utt2spk = open(base_dir + '/utt2spk', 'w')
for corpus in corpora:
    corpus_dir = pathlib.Path(os.path.join(base_dir, corpus))
    
    for audio in corpus_dir.iterdir():
        
        p = audio / 'split'
        p.mkdir(parents=True, exist_ok=True)
        
        chat_file = os.path.join(str(audio) , audio.name +'.cha')
        count = 0
        with open(chat_file, 'r') as f:
            for line in f:
                if '\x15' in line and line[0] == '*':
                    count += 1
                    line = line.replace('\x15', '')
                    print(line)
                    start, end = (line.split()[-1]).split('_')
                    speaker = line.split(':')[0][1::]
                    text = ' '.join((line.split(':')[1]).split()[0:-1])
                    
                    print(speaker, text)
                    utterid = speaker + '-' + audio.name + f'-{count:04}'
                    print(start, end)
                    fout.writelines(f"utterid\t{' '.join(text)}\n")
                    wavscp.writelines(f"utterid\t{os.path.join(str(p), utterid)}.wav\n")
                    utt2spk.writelines(f"{speaker}-{audio.name}\t{utterid}\t")
                    #f"{5:04}"
                    cmd = f"ffmpeg -i {os.path.join(str(audio), audio.name + '.mp3')} -ss {int(start)/1000} -to {int(end)/1000} -ar 16000 {os.path.join(str(p), utterid)}.wav"
                    print(cmd)
                    bash.writelines(cmd + "\n")

os.system(f"bash {bash_file}")                
            
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
        