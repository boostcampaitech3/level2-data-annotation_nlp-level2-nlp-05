import json
import pandas as pd
import os 


def json_to_csv(file_list):
    with open('annotations-legend.json', "r") as json_file:
        ann_list = json.load(json_file)

    for file in file_list:
        with open(os.path.join(f'./{file}.json'), "r") as ann_json:
            ann_json = json.load(ann_json)
        with open(os.path.join(f'./{file}.txt'), 'r') as text_file:
            texts = text_file.read()
        relations = ann_json['relations']

        sentences = []
        subjects = []
        se_context = []
        objects = []
        oe_context = []
        rels = []
        relation_list = []

        for relation in relations:
            classId = relation['classId']
            relation_type = ann_list[classId]
            rels.append(relation_type)

            entities = relation['entities']
            for entity in entities:
                _, entity_type, idx = entity.split('|')
                entity_type = ann_list[entity_type]
                start_idx, end_idx = map(int, idx.split(','))
                if entity_type.startswith('SUB'):
                    subjects.append({'start_idx':start_idx, 'end_idx':end_idx, 'context':texts[start_idx:end_idx+1], 'entity_type':entity_type})
                    se_context.append(texts[start_idx:end_idx+1])
                    relation_list.append('-'.join(entity_type.split('-')[1:]))
                if entity_type.startswith('OBJ'):
                    objects.append({'start_idx':start_idx, 'end_idx':end_idx, 'context':texts[start_idx:end_idx+1], 'entity_type':entity_type})
                    oe_context.append(texts[start_idx:end_idx+1])
            tok = start_idx
            sentence_end = texts.find('\n', tok)
            sentences.append(texts[:sentence_end].split('\n')[-1])
        
        output_df = pd.DataFrame(list(zip(sentences, subjects, se_context, objects, oe_context, relation_list, rels)), columns=['sentence_context','subject_entity', 'subject_entity_context', 'object_entity', 'object_entity_context', 'relation-ko', 'relation'])
        output_df.to_csv(f'{file}.csv', index=False)

if __name__ == '__main__':
    file_list = ['2022-C', 'Sports-C']

    json_to_csv(file_list)
