import sys
from pyke import krb_traceback
from symp_scanner import SymptomLoader
from knowledge_base.driver import *

class Diagnosis(object):


    def find_common_part_of_diagnosis(diag1, diag2):
        list1 = list(diag1)
        list2 = list(diag2)
        final_diagnosis = list(set(list1).intersection(list2))
        return final_diagnosis

    '''dla maks. 2 wyników diagnozy (dwóch chorób)'''


    def perform_diagnosis(name, symptoms_list):


        for symptom in symptoms_list:

            engine.reset()


            engine.add_universal_fact('patient', 'feels', (name, symptom))


            try:

                engine.activate('diagnose')
                with engine.prove_goal('patient.suffers_from($patient, $diseases)') \
                    as gen:
                    #probes - liczba prób diagnozy w pliku patient.kfb
                    probes = 0
                    diagnosis_list = []

                    for vars, plan in gen:

                        probes = probes + 1
                        diagnosis_list.append(vars['diseases'])
                        #print("%s cierpi na %s" % (vars['patient'], vars['diseases']))

                        if (probes > 1):
                            result = Diagnosis.find_common_part_of_diagnosis(diagnosis_list[0], diagnosis_list[1])
                            if((len(result) > 0) & (len(result) < 2)):
                                print("%s cierpi na: %s" % (vars['patient'], result[0]))
                                return 0

                    diseases_list = vars['diseases']


            except:
                krb_traceback.print_exc()
                sys.exit(1)


            if (len(diseases_list) == 1):
                print("%s cierpi na: %s" % (vars['patient'], diseases_list[0]))
                return 0
            if (len(diseases_list) == 0):
                print("nie znaleziono choroby")
            # else:
            #     print('możliwe choroby to: ', [disease for disease in diseases_list])
