from knowledge_base.driver import *
from symp_scanner import SymptomLoader
from diag import Diagnosis
from check import *

'''example of created fact in patient.fbc file: feels(Tadeusz, headache)'''


get_symptoms_disease_relation_from_rows()


'''
perform diagnosis
EXAMPLE
'''


dict = {}
while(True):

    diseases_list = []
    symptom_list = []
    print("--Proszę podać imię:")
    name = input()
    while(True):

        print("--Proszę podać objaw:")
        ailment = input();
        symptom = SymptomLoader.scanInput(ailment)
        if(symptom): symptom_list.append(symptom)

        if(check_knowledge(dict, symptom)): break

        diseases_list = Diagnosis.perform_diagnosis(name , symptom)

        if(len(diseases_list) == 1):
            break
    if(diseases_list):
        print(name + " cierpi na: ", diseases_list[0])
        key = str(diseases_list[0])

        dict.setdefault(key, [])
        dict.update({key :symptom_list})
    #print_knowledge_base()






'''
example of asserted fact into patient.fbc file: suffers_from('Tadeusz', 'Wymioty')
'''
