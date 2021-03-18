'''
Code entirely written by the authors of leNER-Br paper
'''

# This file was developed as part of the project reported in the paper below.
# We kindly request that users cite our paper in any publication that is 
# generated as a result of the use of our source code or our dataset.
# 
# Pedro H. Luz de Araujo, Teófilo E. de Campos, Renato R. R. de Oliveira, Matheus Stauffer, Samuel Couto and Paulo Bermejo.
# LeNER-Br: a Dataset for Named Entity Recognition in Brazilian Legal Text.
# International Conference on the Computational Processing of Portuguese (PROPOR),
# September 24-26, Canela, Brazil, 2018. 
#
#    @InProceedings{luz_etal_propor2018,
#          author = {Pedro H. {Luz de Araujo} and Te\'{o}filo E. {de Campos} and
#          Renato R. R. {de Oliveira} and Matheus Stauffer and
#          Samuel Couto and Paulo Bermejo},
#          title = {LeNER-Br: a Dataset for Named Entity Recognition in Brazilian Legal Text},
#          booktitle = {International Conference on the Computational Processing of Portuguese
#          ({PROPOR})},
#          year = {2018},
#          month = {September 24-26},
#          address = {Canela, RS, Brazil},
#          note = {Available from \url{https://cic.unb.br/~teodecampos/LeNER-Br/}}
#      }      

import pandas as pd
from model.ner_model import NERModel
from model.config import Config
from nltk import word_tokenize
from nltk.tokenize.punkt import PunktSentenceTokenizer
#import sys

# create instance of config
config = Config()

# build model
model = NERModel(config)
model.build()
model.restore_session(config.dir_model)

for i in range(0,99):
    filename = 'C:/Users/Pedro/Documents/Python Scripts/notas-trabalhistas/input_raw_docs/nov_to_fev%s.csv' % i #sys.argv[1]
    tokenizer = PunktSentenceTokenizer()
    
    with open(filename, 'r') as file:
        text = file.read()
    
    tokenizer.train(text)
    sentences = tokenizer.tokenize(text)
    
    ner = []
    ner2 = []
    
    for sentence in sentences:
        words = word_tokenize(sentence, language='portuguese')
        preds = model.predict(words)
        ner.append(words)
        ner2.append(preds)
        print(words, preds)
        print('\n')
    
    ner = pd.DataFrame(ner)
    ner2 = pd.DataFrame(ner2)
    ner.to_csv('C:/Users/Pedro/Documents/Python Scripts/notas-trabalhistas/output_raw_docs/words%s.csv' % i, encoding='cp1252')
    ner2.to_csv('C:/Users/Pedro/Documents/Python Scripts/notas-trabalhistas/output_raw_docs/preds%s.csv' % i, encoding='cp1252')     

    