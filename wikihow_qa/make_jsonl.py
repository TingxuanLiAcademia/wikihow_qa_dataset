"""
convert json file into summary json
  summary json: including src and tgt key
"""

import json
import sys

import MeCab
def remecab(word):
    word = word.split(' ')
    mecab = MeCab.Tagger('-r /dev/null -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd -Owakati')
    # return mecab.parse(''.join(word)).strip('').split()
    return mecab.parse(''.join(word))

def normal(str):
    str = str.replace('\n', '')
    str = str.replace('How_to', '')
    return str

def load_data(file_path):
    with open(file_path, encoding='utf-8') as i_f:
        data = json.load(i_f)
    return data

def convert_summary(data, index_main_title):
    """
    crawlingされたjson fileにまとめたデータから，
    context
    summary
    title
    を抽出
    """
    output_data = list()
    num_part = data['num_part']
    main_title = data['original_title']
    contents = data['contents'] # list
    for idx, content in enumerate(contents):
        # temp_dict = {'src': '', 'tgt': '', 'title': title+'_{}'.format(idx)}
        # temp_dict = {'src': '', 'tgt': '', 'title': ''}
        temp_dict = {
            "qid":index_main_title + f'{str(idx).zfill(4)}',
            "question":"",
            "context":"",
            "answers":{"text":"", "answer_start":""},
            "is_impossible":"False"
        }
        part_contents = content['part_contents'] # summary
        sub_title = content['part_title']

        src_list = list()
        tgt_list = list()
        # title_list = list()
        # LEO 20220719
        title_q = main_title + '方法について，' + sub_title + '，どうすればいいですか？'
        for c in part_contents:
            # bold line が空の場合、対応する記事も空にする
            # 逆も然り
            article = c['article']
            bold_line = c['bold_line']
            if article != '' and bold_line != '':
                src_list.append(article)
                tgt_list.append(bold_line)
                # title_list.append(title_q)
        
        # 一つも入っていなかったらそもそもデータにならない
        if not src_list:
            continue
        src = ''.join(src_list)
        tgt_list = [t if t[-1] == '。' else t + '。' for t in tgt_list]
        tgt = ''.join(tgt_list)
        # tgt = '。'.join(tgt_list) + '。'
        # title = ''.join(title_list)

        src = normal(src)
        tgt = normal(tgt)
        title_q = normal(title_q)

        temp_dict['context'] = remecab(src)
        temp_dict['answers']['text'] = remecab(tgt)
        temp_dict['answers']['answer_start'] = 0
        temp_dict['question'] = remecab(title_q)

        output_data.append(temp_dict)
    
    return output_data

def convert_jsonl(output_data):
    output_strings = list()
    for part_dict in output_data:
        #output_json = json.dumps(part_dict, ensure_ascii=False, indent=None)
        #output_strings.append(output_json)
        output_strings.append(part_dict)
    return output_strings
    

def main():
    input_json = sys.argv[1]
    input_json = load_data(input_json)

    output_data = convert_summary(input_json) 
    for i in convert_jsonl(output_data):
        print(i)

if __name__ == '__main__':
    main()
