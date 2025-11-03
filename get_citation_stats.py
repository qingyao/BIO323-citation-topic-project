import requests as rq
import time

pmids = []
with open('paxdb_citation_pmids.txt') as f:
    for l in f:
        pmids.append(l.strip().strip('"'))

checked = {}
log = open('citation_fetch.log', 'w')
with open('citation_info.tsv', 'w') as wf:
    for pmid in pmids:
        if pmid in checked:
        #     print(checked[pmid],file = wf)
            continue

        try:
            with rq.get(f'https://metrics-api.dimensions.ai/pmid/{pmid}') as response:
                data = response.json()
        except Exception as e:
            print(pmid, e, file = log)
            break
            data = {'times_cited':'', 'recent_citations':'', 'field_citation_ratio':'', 'relative_citation_ratio': ''}

        to_print = ''
        for citation_info in ['times_cited', 'recent_citations', 'field_citation_ratio', 'relative_citation_ratio']:
            to_print += str(data[citation_info]) + '\t'
        checked[pmid] = to_print
        print(pmid, to_print, sep = '\t', file = wf)
        time.sleep(0.05)
log.close()