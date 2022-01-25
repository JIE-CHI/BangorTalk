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
📦bangortalk
 ┣ 📂miami
 ┃ ┣ 📂herring1
 ┃ ┃ ┣ 📜herring1.cha
 ┃ ┃ ┣ 📜herring1.mp3
 ┃ ┃ ┗ 📜herring1.txt
 ┃ ┣ 📂herring10
 ┃ ┃ ┣ 📜herring10.cha
 ┃ ┃ ┣ 📜herring10.mp3
 ┃ ┃ ┗ 📜herring10.txt
 ┃ ┣ 📂herring11
 ┃ ┃ ┣ 📜herring11.cha
 ┃ ┃ ┣ 📜herring11.mp3
 ┃ ┃ ┗ 📜herring11.txt
 ┃ ┣ 📂herring12
 ┃ ┃ ┣ 📜herring12.cha
 ┃ ┃ ┣ 📜herring12.mp3
 ┃ ┃ ┗ 📜herring12.txt
 ┃ ┣ 📂herring13
 ┃ ┃ ┣ 📜herring13.cha
 ┃ ┃ ┣ 📜herring13.mp3
 ┃ ┃ ┗ 📜herring13.txt
 ┃ ┣ 📂herring14
 ┃ ┃ ┣ 📜herring14.cha
 ┃ ┃ ┣ 📜herring14.mp3
 ┃ ┃ ┗ 📜herring14.txt
 ┃ ┣ 📂herring15
 ┃ ┃ ┣ 📜herring15.cha
 ┃ ┃ ┣ 📜herring15.mp3
 ┃ ┃ ┗ 📜herring15.txt
 ┃ ┣ 📂herring16
 ┃ ┃ ┣ 📜herring16.cha
 ┃ ┃ ┣ 📜herring16.mp3
 ┃ ┃ ┗ 📜herring16.txt
 ┃ ┣ 📂herring17
 ┃ ┃ ┣ 📜herring17.cha
 ┃ ┃ ┣ 📜herring17.mp3
 ┃ ┃ ┗ 📜herring17.txt
 ┃ ┣ 📂herring2
 ┃ ┃ ┣ 📜herring2.cha
 ┃ ┃ ┣ 📜herring2.mp3
 ┃ ┃ ┗ 📜herring2.txt
 ┃ ┣ 📂herring3
 ┃ ┃ ┣ 📜herring3.cha
 ┃ ┃ ┣ 📜herring3.mp3
 ┃ ┃ ┗ 📜herring3.txt
 ┃ ┣ 📂herring5
 ┃ ┃ ┣ 📜herring5.cha
 ┃ ┃ ┣ 📜herring5.mp3
 ┃ ┃ ┗ 📜herring5.txt
 ┃ ┣ 📂herring6
 ┃ ┃ ┣ 📜herring6.cha
 ┃ ┃ ┣ 📜herring6.mp3
 ┃ ┃ ┗ 📜herring6.txt
 ┃ ┣ 📂herring7
 ┃ ┃ ┣ 📜herring7.cha
 ┃ ┃ ┣ 📜herring7.mp3
 ┃ ┃ ┗ 📜herring7.txt
 ┃ ┣ 📂herring8
 ┃ ┃ ┣ 📜herring8.cha
 ┃ ┃ ┣ 📜herring8.mp3
 ┃ ┃ ┗ 📜herring8.txt
 ┃ ┣ 📂herring9
 ┃ ┃ ┣ 📜herring9.cha
 ┃ ┃ ┣ 📜herring9.mp3
 ┃ ┃ ┗ 📜herring9.txt
 ┃ ┣ 📂maria1
 ┃ ┃ ┣ 📜maria1.cha
 ┃ ┃ ┣ 📜maria1.mp3
 ┃ ┃ ┗ 📜maria1.txt
 ┃ ┣ 📂maria10
 ┃ ┃ ┣ 📜maria10.cha
 ┃ ┃ ┣ 📜maria10.mp3
 ┃ ┃ ┗ 📜maria10.txt
 ┃ ┣ 📂maria16
 ┃ ┃ ┣ 📜maria16.cha
 ┃ ┃ ┣ 📜maria16.mp3
 ┃ ┃ ┗ 📜maria16.txt
 ┃ ┣ 📂maria18
 ┃ ┃ ┣ 📜maria18.cha
 ┃ ┃ ┣ 📜maria18.mp3
 ┃ ┃ ┗ 📜maria18.txt
 ┃ ┣ 📂maria19
 ┃ ┃ ┣ 📜maria19.cha
 ┃ ┃ ┣ 📜maria19.mp3
 ┃ ┃ ┗ 📜maria19.txt
 ┃ ┣ 📂maria2
 ┃ ┃ ┣ 📜maria2.cha
 ┃ ┃ ┣ 📜maria2.mp3
 ┃ ┃ ┗ 📜maria2.txt
 ┃ ┣ 📂maria20
 ┃ ┃ ┣ 📜maria20.cha
 ┃ ┃ ┣ 📜maria20.mp3
 ┃ ┃ ┗ 📜maria20.txt
 ┃ ┣ 📂maria21
 ┃ ┃ ┣ 📜maria21.cha
 ┃ ┃ ┣ 📜maria21.mp3
 ┃ ┃ ┗ 📜maria21.txt
 ┃ ┣ 📂maria24
 ┃ ┃ ┣ 📜maria24.cha
 ┃ ┃ ┣ 📜maria24.mp3
 ┃ ┃ ┗ 📜maria24.txt
 ┃ ┣ 📂maria27
 ┃ ┃ ┣ 📜maria27.cha
 ┃ ┃ ┣ 📜maria27.mp3
 ┃ ┃ ┗ 📜maria27.txt
 ┃ ┣ 📂maria30
 ┃ ┃ ┣ 📜maria30.cha
 ┃ ┃ ┣ 📜maria30.mp3
 ┃ ┃ ┗ 📜maria30.txt
 ┃ ┣ 📂maria31
 ┃ ┃ ┣ 📜maria31.cha
 ┃ ┃ ┣ 📜maria31.mp3
 ┃ ┃ ┗ 📜maria31.txt
 ┃ ┣ 📂maria4
 ┃ ┃ ┣ 📜maria4.cha
 ┃ ┃ ┣ 📜maria4.mp3
 ┃ ┃ ┗ 📜maria4.txt
 ┃ ┣ 📂maria40
 ┃ ┃ ┣ 📜maria40.cha
 ┃ ┃ ┣ 📜maria40.mp3
 ┃ ┃ ┗ 📜maria40.txt
 ┃ ┣ 📂maria7
 ┃ ┃ ┣ 📜maria7.cha
 ┃ ┃ ┣ 📜maria7.mp3
 ┃ ┃ ┗ 📜maria7.txt
 ┃ ┣ 📂sastre1
 ┃ ┃ ┣ 📜sastre1.cha
 ┃ ┃ ┣ 📜sastre1.mp3
 ┃ ┃ ┗ 📜sastre1.txt
 ┃ ┣ 📂sastre10
 ┃ ┃ ┣ 📜sastre10.cha
 ┃ ┃ ┣ 📜sastre10.mp3
 ┃ ┃ ┗ 📜sastre10.txt
 ┃ ┣ 📂sastre11
 ┃ ┃ ┣ 📜sastre11.cha
 ┃ ┃ ┣ 📜sastre11.mp3
 ┃ ┃ ┗ 📜sastre11.txt
 ┃ ┣ 📂sastre12
 ┃ ┃ ┣ 📜sastre12.cha
 ┃ ┃ ┣ 📜sastre12.mp3
 ┃ ┃ ┗ 📜sastre12.txt
 ┃ ┣ 📂sastre13
 ┃ ┃ ┣ 📜sastre13.cha
 ┃ ┃ ┣ 📜sastre13.mp3
 ┃ ┃ ┗ 📜sastre13.txt
 ┃ ┣ 📂sastre2
 ┃ ┃ ┣ 📜sastre2.cha
 ┃ ┃ ┣ 📜sastre2.mp3
 ┃ ┃ ┗ 📜sastre2.txt
 ┃ ┣ 📂sastre3
 ┃ ┃ ┣ 📜sastre3.cha
 ┃ ┃ ┣ 📜sastre3.mp3
 ┃ ┃ ┗ 📜sastre3.txt
 ┃ ┣ 📂sastre4
 ┃ ┃ ┣ 📜sastre4.cha
 ┃ ┃ ┣ 📜sastre4.mp3
 ┃ ┃ ┗ 📜sastre4.txt
 ┃ ┣ 📂sastre5
 ┃ ┃ ┣ 📜sastre5.cha
 ┃ ┃ ┣ 📜sastre5.mp3
 ┃ ┃ ┗ 📜sastre5.txt
 ┃ ┣ 📂sastre6
 ┃ ┃ ┣ 📜sastre6.cha
 ┃ ┃ ┣ 📜sastre6.mp3
 ┃ ┃ ┗ 📜sastre6.txt
 ┃ ┣ 📂sastre7
 ┃ ┃ ┣ 📜sastre7.cha
 ┃ ┃ ┣ 📜sastre7.mp3
 ┃ ┃ ┗ 📜sastre7.txt
 ┃ ┣ 📂sastre8
 ┃ ┃ ┣ 📜sastre8.cha
 ┃ ┃ ┣ 📜sastre8.mp3
 ┃ ┃ ┗ 📜sastre8.txt
 ┃ ┣ 📂sastre9
 ┃ ┃ ┣ 📜sastre9.cha
 ┃ ┃ ┣ 📜sastre9.mp3
 ┃ ┃ ┗ 📜sastre9.txt
 ┃ ┣ 📂zeledon1
 ┃ ┃ ┣ 📜zeledon1.cha
 ┃ ┃ ┣ 📜zeledon1.mp3
 ┃ ┃ ┗ 📜zeledon1.txt
 ┃ ┣ 📂zeledon11
 ┃ ┃ ┣ 📜zeledon11.cha
 ┃ ┃ ┣ 📜zeledon11.mp3
 ┃ ┃ ┗ 📜zeledon11.txt
 ┃ ┣ 📂zeledon13
 ┃ ┃ ┣ 📜zeledon13.cha
 ┃ ┃ ┣ 📜zeledon13.mp3
 ┃ ┃ ┗ 📜zeledon13.txt
 ┃ ┣ 📂zeledon14
 ┃ ┃ ┣ 📜zeledon14.cha
 ┃ ┃ ┣ 📜zeledon14.mp3
 ┃ ┃ ┗ 📜zeledon14.txt
 ┃ ┣ 📂zeledon2
 ┃ ┃ ┣ 📜zeledon2.cha
 ┃ ┃ ┣ 📜zeledon2.mp3
 ┃ ┃ ┗ 📜zeledon2.txt
 ┃ ┣ 📂zeledon3
 ┃ ┃ ┣ 📜zeledon3.cha
 ┃ ┃ ┣ 📜zeledon3.mp3
 ┃ ┃ ┗ 📜zeledon3.txt
 ┃ ┣ 📂zeledon4
 ┃ ┃ ┣ 📜zeledon4.cha
 ┃ ┃ ┣ 📜zeledon4.mp3
 ┃ ┃ ┗ 📜zeledon4.txt
 ┃ ┣ 📂zeledon5
 ┃ ┃ ┣ 📜zeledon5.cha
 ┃ ┃ ┣ 📜zeledon5.mp3
 ┃ ┃ ┗ 📜zeledon5.txt
 ┃ ┣ 📂zeledon6
 ┃ ┃ ┣ 📜zeledon6.cha
 ┃ ┃ ┣ 📜zeledon6.mp3
 ┃ ┃ ┗ 📜zeledon6.txt
 ┃ ┣ 📂zeledon7
 ┃ ┃ ┣ 📜zeledon7.cha
 ┃ ┃ ┣ 📜zeledon7.mp3
 ┃ ┃ ┗ 📜zeledon7.txt
 ┃ ┣ 📂zeledon8
 ┃ ┃ ┣ 📜zeledon8.cha
 ┃ ┃ ┣ 📜zeledon8.mp3
 ┃ ┃ ┗ 📜zeledon8.txt
 ┃ ┗ 📂zeledon9
 ┃ ┃ ┣ 📜zeledon9.cha
 ┃ ┃ ┣ 📜zeledon9.mp3
 ┃ ┃ ┗ 📜zeledon9.txt
 ┣ 📂patagonia
 ┃ ┣ 📂patagonia1
 ┃ ┃ ┣ 📜patagonia1.cha
 ┃ ┃ ┣ 📜patagonia1.mp3
 ┃ ┃ ┗ 📜patagonia1.txt
 ┃ ┣ 📂patagonia10
 ┃ ┃ ┣ 📜patagonia10.cha
 ┃ ┃ ┣ 📜patagonia10.mp3
 ┃ ┃ ┗ 📜patagonia10.txt
 ┃ ┣ 📂patagonia11
 ┃ ┃ ┣ 📜patagonia11.cha
 ┃ ┃ ┣ 📜patagonia11.mp3
 ┃ ┃ ┗ 📜patagonia11.txt
 ┃ ┣ 📂patagonia12
 ┃ ┃ ┣ 📜patagonia12.cha
 ┃ ┃ ┣ 📜patagonia12.mp3
 ┃ ┃ ┗ 📜patagonia12.txt
 ┃ ┣ 📂patagonia13
 ┃ ┃ ┣ 📜patagonia13.cha
 ┃ ┃ ┣ 📜patagonia13.mp3
 ┃ ┃ ┗ 📜patagonia13.txt
 ┃ ┣ 📂patagonia14
 ┃ ┃ ┣ 📜patagonia14.cha
 ┃ ┃ ┣ 📜patagonia14.mp3
 ┃ ┃ ┗ 📜patagonia14.txt
 ┃ ┣ 📂patagonia15
 ┃ ┃ ┣ 📜patagonia15.cha
 ┃ ┃ ┣ 📜patagonia15.mp3
 ┃ ┃ ┗ 📜patagonia15.txt
 ┃ ┣ 📂patagonia16
 ┃ ┃ ┣ 📜patagonia16.cha
 ┃ ┃ ┣ 📜patagonia16.mp3
 ┃ ┃ ┗ 📜patagonia16.txt
 ┃ ┣ 📂patagonia17
 ┃ ┃ ┣ 📜patagonia17.cha
 ┃ ┃ ┣ 📜patagonia17.mp3
 ┃ ┃ ┗ 📜patagonia17.txt
 ┃ ┣ 📂patagonia18
 ┃ ┃ ┣ 📜patagonia18.cha
 ┃ ┃ ┣ 📜patagonia18.mp3
 ┃ ┃ ┗ 📜patagonia18.txt
 ┃ ┣ 📂patagonia19
 ┃ ┃ ┣ 📜patagonia19.cha
 ┃ ┃ ┣ 📜patagonia19.mp3
 ┃ ┃ ┗ 📜patagonia19.txt
 ┃ ┣ 📂patagonia2
 ┃ ┃ ┣ 📜patagonia2.cha
 ┃ ┃ ┣ 📜patagonia2.mp3
 ┃ ┃ ┗ 📜patagonia2.txt
 ┃ ┣ 📂patagonia20
 ┃ ┃ ┣ 📜patagonia20.cha
 ┃ ┃ ┣ 📜patagonia20.mp3
 ┃ ┃ ┗ 📜patagonia20.txt
 ┃ ┣ 📂patagonia21
 ┃ ┃ ┣ 📜patagonia21.cha
 ┃ ┃ ┣ 📜patagonia21.mp3
 ┃ ┃ ┗ 📜patagonia21.txt
 ┃ ┣ 📂patagonia22
 ┃ ┃ ┣ 📜patagonia22.cha
 ┃ ┃ ┣ 📜patagonia22.mp3
 ┃ ┃ ┗ 📜patagonia22.txt
 ┃ ┣ 📂patagonia23
 ┃ ┃ ┣ 📜patagonia23.cha
 ┃ ┃ ┣ 📜patagonia23.mp3
 ┃ ┃ ┗ 📜patagonia23.txt
 ┃ ┣ 📂patagonia24
 ┃ ┃ ┣ 📜patagonia24.cha
 ┃ ┃ ┣ 📜patagonia24.mp3
 ┃ ┃ ┗ 📜patagonia24.txt
 ┃ ┣ 📂patagonia25
 ┃ ┃ ┣ 📜patagonia25.cha
 ┃ ┃ ┣ 📜patagonia25.mp3
 ┃ ┃ ┗ 📜patagonia25.txt
 ┃ ┣ 📂patagonia26
 ┃ ┃ ┣ 📜patagonia26.cha
 ┃ ┃ ┣ 📜patagonia26.mp3
 ┃ ┃ ┗ 📜patagonia26.txt
 ┃ ┣ 📂patagonia27
 ┃ ┃ ┣ 📜patagonia27.cha
 ┃ ┃ ┣ 📜patagonia27.mp3
 ┃ ┃ ┗ 📜patagonia27.txt
 ┃ ┣ 📂patagonia28
 ┃ ┃ ┣ 📜patagonia28.cha
 ┃ ┃ ┣ 📜patagonia28.mp3
 ┃ ┃ ┗ 📜patagonia28.txt
 ┃ ┣ 📂patagonia29
 ┃ ┃ ┣ 📜patagonia29.cha
 ┃ ┃ ┣ 📜patagonia29.mp3
 ┃ ┃ ┗ 📜patagonia29.txt
 ┃ ┣ 📂patagonia3
 ┃ ┃ ┣ 📜patagonia3.cha
 ┃ ┃ ┣ 📜patagonia3.mp3
 ┃ ┃ ┗ 📜patagonia3.txt
 ┃ ┣ 📂patagonia30
 ┃ ┃ ┣ 📜patagonia30.cha
 ┃ ┃ ┣ 📜patagonia30.mp3
 ┃ ┃ ┗ 📜patagonia30.txt
 ┃ ┣ 📂patagonia31
 ┃ ┃ ┣ 📜patagonia31.cha
 ┃ ┃ ┣ 📜patagonia31.mp3
 ┃ ┃ ┗ 📜patagonia31.txt
 ┃ ┣ 📂patagonia32
 ┃ ┃ ┣ 📜patagonia32.cha
 ┃ ┃ ┣ 📜patagonia32.mp3
 ┃ ┃ ┗ 📜patagonia32.txt
 ┃ ┣ 📂patagonia33
 ┃ ┃ ┣ 📜patagonia33.cha
 ┃ ┃ ┣ 📜patagonia33.mp3
 ┃ ┃ ┗ 📜patagonia33.txt
 ┃ ┣ 📂patagonia34
 ┃ ┃ ┣ 📜patagonia34.cha
 ┃ ┃ ┣ 📜patagonia34.mp3
 ┃ ┃ ┗ 📜patagonia34.txt
 ┃ ┣ 📂patagonia35
 ┃ ┃ ┣ 📜patagonia35.cha
 ┃ ┃ ┣ 📜patagonia35.mp3
 ┃ ┃ ┗ 📜patagonia35.txt
 ┃ ┣ 📂patagonia36
 ┃ ┃ ┣ 📜patagonia36.cha
 ┃ ┃ ┣ 📜patagonia36.mp3
 ┃ ┃ ┗ 📜patagonia36.txt
 ┃ ┣ 📂patagonia37
 ┃ ┃ ┣ 📜patagonia37.cha
 ┃ ┃ ┣ 📜patagonia37.mp3
 ┃ ┃ ┗ 📜patagonia37.txt
 ┃ ┣ 📂patagonia38
 ┃ ┃ ┣ 📜patagonia38.cha
 ┃ ┃ ┣ 📜patagonia38.mp3
 ┃ ┃ ┗ 📜patagonia38.txt
 ┃ ┣ 📂patagonia39
 ┃ ┃ ┣ 📜patagonia39.cha
 ┃ ┃ ┣ 📜patagonia39.mp3
 ┃ ┃ ┗ 📜patagonia39.txt
 ┃ ┣ 📂patagonia4
 ┃ ┃ ┣ 📜patagonia4.cha
 ┃ ┃ ┣ 📜patagonia4.mp3
 ┃ ┃ ┗ 📜patagonia4.txt
 ┃ ┣ 📂patagonia40
 ┃ ┃ ┣ 📜patagonia40.cha
 ┃ ┃ ┣ 📜patagonia40.mp3
 ┃ ┃ ┗ 📜patagonia40.txt
 ┃ ┣ 📂patagonia41
 ┃ ┃ ┣ 📜patagonia41.cha
 ┃ ┃ ┣ 📜patagonia41.mp3
 ┃ ┃ ┗ 📜patagonia41.txt
 ┃ ┣ 📂patagonia42
 ┃ ┃ ┣ 📜patagonia42.cha
 ┃ ┃ ┣ 📜patagonia42.mp3
 ┃ ┃ ┗ 📜patagonia42.txt
 ┃ ┣ 📂patagonia43
 ┃ ┃ ┣ 📜patagonia43.cha
 ┃ ┃ ┣ 📜patagonia43.mp3
 ┃ ┃ ┗ 📜patagonia43.txt
 ┃ ┣ 📂patagonia5
 ┃ ┃ ┣ 📜patagonia5.cha
 ┃ ┃ ┣ 📜patagonia5.mp3
 ┃ ┃ ┗ 📜patagonia5.txt
 ┃ ┣ 📂patagonia6
 ┃ ┃ ┣ 📜patagonia6.cha
 ┃ ┃ ┣ 📜patagonia6.mp3
 ┃ ┃ ┗ 📜patagonia6.txt
 ┃ ┣ 📂patagonia7
 ┃ ┃ ┣ 📜patagonia7.cha
 ┃ ┃ ┣ 📜patagonia7.mp3
 ┃ ┃ ┗ 📜patagonia7.txt
 ┃ ┣ 📂patagonia8
 ┃ ┃ ┣ 📜patagonia8.cha
 ┃ ┃ ┣ 📜patagonia8.mp3
 ┃ ┃ ┗ 📜patagonia8.txt
 ┃ ┗ 📂patagonia9
 ┃ ┃ ┣ 📜patagonia9.cha
 ┃ ┃ ┣ 📜patagonia9.mp3
 ┃ ┃ ┗ 📜patagonia9.txt
 ┗ 📂siarad
 ┃ ┣ 📂davies1
 ┃ ┃ ┣ 📜davies1.cha
 ┃ ┃ ┣ 📜davies1.mp3
 ┃ ┃ ┗ 📜davies1.txt
 ┃ ┣ 📂davies10
 ┃ ┃ ┣ 📜davies10.cha
 ┃ ┃ ┣ 📜davies10.mp3
 ┃ ┃ ┗ 📜davies10.txt
 ┃ ┣ 📂davies11
 ┃ ┃ ┣ 📜davies11.cha
 ┃ ┃ ┣ 📜davies11.mp3
 ┃ ┃ ┗ 📜davies11.txt
 ┃ ┣ 📂davies12
 ┃ ┃ ┣ 📜davies12.cha
 ┃ ┃ ┣ 📜davies12.mp3
 ┃ ┃ ┗ 📜davies12.txt
 ┃ ┣ 📂davies13
 ┃ ┃ ┣ 📜davies13.cha
 ┃ ┃ ┣ 📜davies13.mp3
 ┃ ┃ ┗ 📜davies13.txt
 ┃ ┣ 📂davies14
 ┃ ┃ ┣ 📜davies14.cha
 ┃ ┃ ┣ 📜davies14.mp3
 ┃ ┃ ┗ 📜davies14.txt
 ┃ ┣ 📂davies15
 ┃ ┃ ┣ 📜davies15.cha
 ┃ ┃ ┣ 📜davies15.mp3
 ┃ ┃ ┗ 📜davies15.txt
 ┃ ┣ 📂davies16
 ┃ ┃ ┣ 📜davies16.cha
 ┃ ┃ ┣ 📜davies16.mp3
 ┃ ┃ ┗ 📜davies16.txt
 ┃ ┣ 📂davies17
 ┃ ┃ ┣ 📜davies17.cha
 ┃ ┃ ┣ 📜davies17.mp3
 ┃ ┃ ┗ 📜davies17.txt
 ┃ ┣ 📂davies2
 ┃ ┃ ┣ 📜davies2.cha
 ┃ ┃ ┣ 📜davies2.mp3
 ┃ ┃ ┗ 📜davies2.txt
 ┃ ┣ 📂davies3
 ┃ ┃ ┣ 📜davies3.cha
 ┃ ┃ ┣ 📜davies3.mp3
 ┃ ┃ ┗ 📜davies3.txt
 ┃ ┣ 📂davies4
 ┃ ┃ ┣ 📜davies4.cha
 ┃ ┃ ┣ 📜davies4.mp3
 ┃ ┃ ┗ 📜davies4.txt
 ┃ ┣ 📂davies5
 ┃ ┃ ┣ 📜davies5.cha
 ┃ ┃ ┣ 📜davies5.mp3
 ┃ ┃ ┗ 📜davies5.txt
 ┃ ┣ 📂davies6
 ┃ ┃ ┣ 📜davies6.cha
 ┃ ┃ ┣ 📜davies6.mp3
 ┃ ┃ ┗ 📜davies6.txt
 ┃ ┣ 📂davies7
 ┃ ┃ ┣ 📜davies7.cha
 ┃ ┃ ┣ 📜davies7.mp3
 ┃ ┃ ┗ 📜davies7.txt
 ┃ ┣ 📂davies9
 ┃ ┃ ┣ 📜davies9.cha
 ┃ ┃ ┣ 📜davies9.mp3
 ┃ ┃ ┗ 📜davies9.txt
 ┃ ┣ 📂deuchar1
 ┃ ┃ ┣ 📜deuchar1.cha
 ┃ ┃ ┣ 📜deuchar1.mp3
 ┃ ┃ ┗ 📜deuchar1.txt
 ┃ ┣ 📂fusser10
 ┃ ┃ ┣ 📜fusser10.cha
 ┃ ┃ ┣ 📜fusser10.mp3
 ┃ ┃ ┗ 📜fusser10.txt
 ┃ ┣ 📂fusser11
 ┃ ┃ ┣ 📜fusser11.cha
 ┃ ┃ ┣ 📜fusser11.mp3
 ┃ ┃ ┗ 📜fusser11.txt
 ┃ ┣ 📂fusser12
 ┃ ┃ ┣ 📜fusser12.cha
 ┃ ┃ ┣ 📜fusser12.mp3
 ┃ ┃ ┗ 📜fusser12.txt
 ┃ ┣ 📂fusser13
 ┃ ┃ ┣ 📜fusser13.cha
 ┃ ┃ ┣ 📜fusser13.mp3
 ┃ ┃ ┗ 📜fusser13.txt
 ┃ ┣ 📂fusser14
 ┃ ┃ ┣ 📜fusser14.cha
 ┃ ┃ ┣ 📜fusser14.mp3
 ┃ ┃ ┗ 📜fusser14.txt
 ┃ ┣ 📂fusser15
 ┃ ┃ ┣ 📜fusser15.cha
 ┃ ┃ ┣ 📜fusser15.mp3
 ┃ ┃ ┗ 📜fusser15.txt
 ┃ ┣ 📂fusser16
 ┃ ┃ ┣ 📜fusser16.cha
 ┃ ┃ ┣ 📜fusser16.mp3
 ┃ ┃ ┗ 📜fusser16.txt
 ┃ ┣ 📂fusser17
 ┃ ┃ ┣ 📜fusser17.cha
 ┃ ┃ ┣ 📜fusser17.mp3
 ┃ ┃ ┗ 📜fusser17.txt
 ┃ ┣ 📂fusser18
 ┃ ┃ ┣ 📜fusser18.cha
 ┃ ┃ ┣ 📜fusser18.mp3
 ┃ ┃ ┗ 📜fusser18.txt
 ┃ ┣ 📂fusser19
 ┃ ┃ ┣ 📜fusser19.cha
 ┃ ┃ ┣ 📜fusser19.mp3
 ┃ ┃ ┗ 📜fusser19.txt
 ┃ ┣ 📂fusser21
 ┃ ┃ ┣ 📜fusser21.cha
 ┃ ┃ ┣ 📜fusser21.mp3
 ┃ ┃ ┗ 📜fusser21.txt
 ┃ ┣ 📂fusser22
 ┃ ┃ ┣ 📜fusser22.cha
 ┃ ┃ ┣ 📜fusser22.mp3
 ┃ ┃ ┗ 📜fusser22.txt
 ┃ ┣ 📂fusser23
 ┃ ┃ ┣ 📜fusser23.cha
 ┃ ┃ ┣ 📜fusser23.mp3
 ┃ ┃ ┗ 📜fusser23.txt
 ┃ ┣ 📂fusser25
 ┃ ┃ ┣ 📜fusser25.cha
 ┃ ┃ ┣ 📜fusser25.mp3
 ┃ ┃ ┗ 📜fusser25.txt
 ┃ ┣ 📂fusser26
 ┃ ┃ ┣ 📜fusser26.cha
 ┃ ┃ ┣ 📜fusser26.mp3
 ┃ ┃ ┗ 📜fusser26.txt
 ┃ ┣ 📂fusser27
 ┃ ┃ ┣ 📜fusser27.cha
 ┃ ┃ ┣ 📜fusser27.mp3
 ┃ ┃ ┗ 📜fusser27.txt
 ┃ ┣ 📂fusser28
 ┃ ┃ ┣ 📜fusser28.cha
 ┃ ┃ ┣ 📜fusser28.mp3
 ┃ ┃ ┗ 📜fusser28.txt
 ┃ ┣ 📂fusser29
 ┃ ┃ ┣ 📜fusser29.cha
 ┃ ┃ ┣ 📜fusser29.mp3
 ┃ ┃ ┗ 📜fusser29.txt
 ┃ ┣ 📂fusser3
 ┃ ┃ ┣ 📜fusser3.cha
 ┃ ┃ ┣ 📜fusser3.mp3
 ┃ ┃ ┗ 📜fusser3.txt
 ┃ ┣ 📂fusser30
 ┃ ┃ ┣ 📜fusser30.cha
 ┃ ┃ ┣ 📜fusser30.mp3
 ┃ ┃ ┗ 📜fusser30.txt
 ┃ ┣ 📂fusser31
 ┃ ┃ ┣ 📜fusser31.cha
 ┃ ┃ ┣ 📜fusser31.mp3
 ┃ ┃ ┗ 📜fusser31.txt
 ┃ ┣ 📂fusser32
 ┃ ┃ ┣ 📜fusser32.cha
 ┃ ┃ ┣ 📜fusser32.mp3
 ┃ ┃ ┗ 📜fusser32.txt
 ┃ ┣ 📂fusser4
 ┃ ┃ ┣ 📜fusser4.cha
 ┃ ┃ ┣ 📜fusser4.mp3
 ┃ ┃ ┗ 📜fusser4.txt
 ┃ ┣ 📂fusser5
 ┃ ┃ ┣ 📜fusser5.cha
 ┃ ┃ ┣ 📜fusser5.mp3
 ┃ ┃ ┗ 📜fusser5.txt
 ┃ ┣ 📂fusser6
 ┃ ┃ ┣ 📜fusser6.cha
 ┃ ┃ ┣ 📜fusser6.mp3
 ┃ ┃ ┗ 📜fusser6.txt
 ┃ ┣ 📂fusser7
 ┃ ┃ ┣ 📜fusser7.cha
 ┃ ┃ ┣ 📜fusser7.mp3
 ┃ ┃ ┗ 📜fusser7.txt
 ┃ ┣ 📂fusser8
 ┃ ┃ ┣ 📜fusser8.cha
 ┃ ┃ ┣ 📜fusser8.mp3
 ┃ ┃ ┗ 📜fusser8.txt
 ┃ ┣ 📂fusser9
 ┃ ┃ ┣ 📜fusser9.cha
 ┃ ┃ ┣ 📜fusser9.mp3
 ┃ ┃ ┗ 📜fusser9.txt
 ┃ ┣ 📂lloyd1
 ┃ ┃ ┣ 📜lloyd1.cha
 ┃ ┃ ┣ 📜lloyd1.mp3
 ┃ ┃ ┗ 📜lloyd1.txt
 ┃ ┣ 📂robert1
 ┃ ┃ ┣ 📜robert1.cha
 ┃ ┃ ┣ 📜robert1.mp3
 ┃ ┃ ┗ 📜robert1.txt
 ┃ ┣ 📂robert2
 ┃ ┃ ┣ 📜robert2.cha
 ┃ ┃ ┣ 📜robert2.mp3
 ┃ ┃ ┗ 📜robert2.txt
 ┃ ┣ 📂robert3
 ┃ ┃ ┣ 📜robert3.cha
 ┃ ┃ ┣ 📜robert3.mp3
 ┃ ┃ ┗ 📜robert3.txt
 ┃ ┣ 📂robert4
 ┃ ┃ ┣ 📜robert4.cha
 ┃ ┃ ┣ 📜robert4.mp3
 ┃ ┃ ┗ 📜robert4.txt
 ┃ ┣ 📂robert5
 ┃ ┃ ┣ 📜robert5.cha
 ┃ ┃ ┣ 📜robert5.mp3
 ┃ ┃ ┗ 📜robert5.txt
 ┃ ┣ 📂robert6
 ┃ ┃ ┣ 📜robert6.cha
 ┃ ┃ ┣ 📜robert6.mp3
 ┃ ┃ ┗ 📜robert6.txt
 ┃ ┣ 📂robert7
 ┃ ┃ ┣ 📜robert7.cha
 ┃ ┃ ┣ 📜robert7.mp3
 ┃ ┃ ┗ 📜robert7.txt
 ┃ ┣ 📂robert8
 ┃ ┃ ┣ 📜robert8.cha
 ┃ ┃ ┣ 📜robert8.mp3
 ┃ ┃ ┗ 📜robert8.txt
 ┃ ┣ 📂robert9
 ┃ ┃ ┣ 📜robert9.cha
 ┃ ┃ ┣ 📜robert9.mp3
 ┃ ┃ ┗ 📜robert9.txt
 ┃ ┣ 📂roberts1
 ┃ ┃ ┣ 📜roberts1.cha
 ┃ ┃ ┣ 📜roberts1.mp3
 ┃ ┃ ┗ 📜roberts1.txt
 ┃ ┣ 📂roberts2
 ┃ ┃ ┣ 📜roberts2.cha
 ┃ ┃ ┣ 📜roberts2.mp3
 ┃ ┃ ┗ 📜roberts2.txt
 ┃ ┣ 📂roberts3
 ┃ ┃ ┣ 📜roberts3.cha
 ┃ ┃ ┣ 📜roberts3.mp3
 ┃ ┃ ┗ 📜roberts3.txt
 ┃ ┣ 📂roberts4
 ┃ ┃ ┣ 📜roberts4.cha
 ┃ ┃ ┣ 📜roberts4.mp3
 ┃ ┃ ┗ 📜roberts4.txt
 ┃ ┣ 📂smith1
 ┃ ┃ ┣ 📜smith1.cha
 ┃ ┃ ┣ 📜smith1.mp3
 ┃ ┃ ┗ 📜smith1.txt
 ┃ ┣ 📂stammers1
 ┃ ┃ ┣ 📜stammers1.cha
 ┃ ┃ ┣ 📜stammers1.mp3
 ┃ ┃ ┗ 📜stammers1.txt
 ┃ ┣ 📂stammers2
 ┃ ┃ ┣ 📜stammers2.cha
 ┃ ┃ ┣ 📜stammers2.mp3
 ┃ ┃ ┗ 📜stammers2.txt
 ┃ ┣ 📂stammers3
 ┃ ┃ ┣ 📜stammers3.cha
 ┃ ┃ ┣ 📜stammers3.mp3
 ┃ ┃ ┗ 📜stammers3.txt
 ┃ ┣ 📂stammers4
 ┃ ┃ ┣ 📜stammers4.cha
 ┃ ┃ ┣ 📜stammers4.mp3
 ┃ ┃ ┗ 📜stammers4.txt
 ┃ ┣ 📂stammers5
 ┃ ┃ ┣ 📜stammers5.cha
 ┃ ┃ ┣ 📜stammers5.mp3
 ┃ ┃ ┗ 📜stammers5.txt
 ┃ ┣ 📂stammers6
 ┃ ┃ ┣ 📜stammers6.cha
 ┃ ┃ ┣ 📜stammers6.mp3
 ┃ ┃ ┗ 📜stammers6.txt
 ┃ ┣ 📂stammers7
 ┃ ┃ ┣ 📜stammers7.cha
 ┃ ┃ ┣ 📜stammers7.mp3
 ┃ ┃ ┗ 📜stammers7.txt
 ┃ ┣ 📂stammers8
 ┃ ┃ ┣ 📜stammers8.cha
 ┃ ┃ ┣ 📜stammers8.mp3
 ┃ ┃ ┗ 📜stammers8.txt
 ┃ ┗ 📂stammers9
 ┃ ┃ ┣ 📜stammers9.cha
 ┃ ┃ ┣ 📜stammers9.mp3
 ┃ ┃ ┗ 📜stammers9.txt