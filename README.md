# BIO323 Project
Our project looks at how researchers around the world are using PaxDb.
We do this by tracking the papers that cite the database and then using topic modeling to see what those papers are about. This lets us find out, for example, whether the data is being used more in medical research, in ecology, or maybe in new computational methods — and how those trends have changed over the years.
By looking at these patterns, we get a clearer picture of the database’s real-world impact. But more importantly, it helps us understand what the community needs and direct our future updates to support that field.

## Starting material
 - Citation information files downloaded from PubMed (citing three PaxDb publications)
   - csv-*.csv: pmid, title, journal, year
   - abstract-*.txt: title, author list, abstract and other information in free text form
 - citation_info.tsv
   - the quality metrics of these articles provided by metrics-api.dimensions.ai

## First exercises
 - merge the files to get pmid, title, abstract which will become input to the BERTopic
 - run the topic clustering with BERTopic with Jupyter notebook for quick start in BERTopic (start_with_topic_modeling.ipynb)
   - try different parameters
   - try different embedding models
   - try different stop words (what are they?)

Reference:
1. [What is topic modeling?](https://www.ibm.com/think/topics/topic-modeling)
2. [BERTopic: python library](https://maartengr.github.io/BERTopic/index.html)
3. [past_curation.tsv](past_curation.tsv) contains 79 citations I analyzed in 2021.
