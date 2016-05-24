from pyke import knowledge_engine
from db.API import read_choroby_objawy_objaw, read_objawy_id
from itertools import chain


engine = knowledge_engine.engine(__file__)


def get_symptoms_disease_relation_from_rows():

    symptoms_list = []

    for i in range(1, 39):
        symptoms_list.append(list(chain(read_objawy_id(i)))[0])

    print('POBRANO OBJAWY:', symptoms_list)


    for symptom in symptoms_list:
        choroby = read_choroby_objawy_objaw(symptom)
        for choroba in choroby:
            engine.add_universal_fact('choroby', 'symptom_of',
                                      (symptom, choroba))



