import requests
import json
import time

# pmcid = 'PMC7961048'
## merge csv by skipping 2 rows, header and PaxDb paper itself
# for i in csv-*-set.csv;do tail -n +3 $i >> merged_csv.csv;done

pmid_texts = {}
logfile = open('pmc_ft_extract.log', 'w')
with open('merged_csv.csv') as f:
    
    for l in f:
        
        pmcid = l.split(',')[-3].strip('"')
        pmid = l.split(',')[0].strip('"')
        if not pmcid or pmid in pmid_texts:
            continue
        print(pmcid)
        r = requests.get(f'https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/{pmcid}/unicode')
        if r.status_code != 200:
            print(pmcid, r.status, r.text, sep = '\t', file = logfile)
            continue
        try:
            data = r.json()
        except Exception as e:
            print(pmcid, e, sep = '\t', file = logfile)
            continue
    # with open('test.json', 'w') as f:
    #     json.dump(data, indent=4, fp = f)
        relevant_sentences = ''
        for passage in data[0]['documents'][0]['passages']:
            ## exclude REF section
            if passage['infons']['section_type'] == 'REF':
                continue
            
            if 'paxdb' in passage['text'].lower() or 'pax-db' in passage['text'].lower():
                hit_sentence_id = []
                
                sentences = passage['text'].split('.')
                for i, sentence in enumerate(sentences):
                    if 'paxdb' in sentence.lower() or 'pax-db' in sentence.lower():
                        ## take the sentence and one sentence before
                        if i != 0:
                            hit_sentence_id += [i-1, i, None]
                        else:
                            hit_sentence_id += [i, None]
                for i in hit_sentence_id:
                    if i != None:
                        relevant_sentences += sentences[i] + '.'
                    else:
                        relevant_sentences += '\n'
        pmid_texts[pmid] = relevant_sentences
        time.sleep(1)
    
with open('pmid_texts.json', 'w') as f:
        json.dump(pmid_texts, indent=4, fp = f) 
logfile.close()