"""
divide jsonl files into train/dev/test files
  based on a tsv file.
"""

import sys
import os
import json

import make_jsonl_new

def load_tsv(file_path):
    """
    return --> list(tuple1, tuple2, ...)
    """
    data = list()
    with open(file_path) as i_f:
        for idx, line in enumerate(i_f):
            if idx == 0:
                continue
            name, size, data_type = line.strip().split()
            idx = str(idx).zfill(4)
            data.append((idx, name, data_type))
    
    return data

'''
def save_jsonl(data, file_path):
    with open(file_path, 'w') as o_f:
        for j in data:
            o_f.write(j+'\n')
'''
# LEO 20220719
def save_json(data, file_path):
    dataset = {'dataset':'','data':''}
    dataset['dataset'] = os.path.splitext(file_path)[0]
    dataset['data'] = data
    with open(file_path, 'w', encoding='utf-8') as fp:
        json.dump(dataset, fp, ensure_ascii=False, indent=None)

def main():
    json_dir = sys.argv[1]
    output_dir = sys.argv[2]
    divided_tsv = sys.argv[3]

    divided_tsv = load_tsv(divided_tsv)

    train_data = list()
    dev_data = list()
    test_data = list()
    for idx, name, data_type in divided_tsv:
        file_path = os.path.join(json_dir, name)
        data = make_jsonl_new.load_data(file_path)
        output_data = make_jsonl_new.convert_summary(data, idx)
        output_data = make_jsonl_new.convert_jsonl(output_data)

        if data_type == 'train':
            train_data.extend(output_data)
        elif data_type == 'dev':
            dev_data.extend(output_data)
        elif data_type == 'test':
            test_data.extend(output_data)
        else:
            raise ValueError()

    # print(test_data)
    save_json(train_data, os.path.join(output_dir, 'train.json'))
    save_json(dev_data, os.path.join(output_dir, 'dev.json'))
    save_json(test_data, os.path.join(output_dir, 'test.json'))

if __name__ == '__main__':
    main()
