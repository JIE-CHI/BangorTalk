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