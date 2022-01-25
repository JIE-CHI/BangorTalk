# BangorTalk
A repo holds my scripts for bangortalk corpora.

## download data

	python download.py -h
	usage: python download.py --data_dir ./ --corpora siarad miami
	
	Download corpus from http://www.bangortalk.org.uk/.
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -d [DATA_DIR], --data_dir [DATA_DIR]
	                        dir to save the data
	  -c CORPORA [CORPORA ...], --corpora CORPORA [CORPORA ...]
		                        a list of corpora to be downloaded
		                        
The data structure look like:
>📦bangortalk
> ┣ 📂miami
> ┃ ┣ 📂herring1
> ┃ ┃ ┣ 📜herring1.cha
> ┃ ┃ ┣ 📜herring1.mp3
> ┃ ┃ ┗ 📜herring1.txt
> ┣ 📂patagonia
> ┃ ┣ 📂patagonia1
> ┃ ┃ ┣ 📜patagonia1.cha
> ┃ ┃ ┣ 📜patagonia1.mp3
> ┃ ┃ ┗ 📜patagonia1.txt
> ┗ 📂siarad
> ┃ ┣ 📂davies1
> ┃ ┃ ┣ 📜davies1.cha
> ┃ ┃ ┣ 📜davies1.mp3
> ┃ ┃ ┗ 📜davies1.txt