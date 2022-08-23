# wikihow_qa_japanese
- A generative question answering dataset collected from wikihow_japanese

## Structure of the directory
'''
.
|-- README.md
|-- wikihow_qa
|   |-- create_qa_dataset.sh
|   |-- data
|   |   `-- output
|   |-- make_data.py
|   |-- make_jsonl.py
|   `-- make_jsonl_new.py
`-- wikihow_summarization
    |-- crawl_article.sh
    |-- data
    |   |-- divided_data.tsv
    |   |-- html
    |   |-- json
    |   |-- output
    |   `-- urls
    |-- get.sh
    |-- requirements.txt
    |-- scrape2jsonl.sh
    `-- script
        |-- __pycache__
        |-- crawl_article.py
        |-- make_data.py
        |-- make_jsonl.py
        `-- scrape4json.py

11 directories, 14 files
'''

## Web scraping
- The scraping script is reference to [wikihow_japanese](https://github.com/Katsumata420/wikihow_japanese)

## Converted the Summarization Dataset to a Generative Question Answering Dataset
- 使い方: `sh create_qa_dataset.sh`