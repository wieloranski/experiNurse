def print_knowledge_base():
    print("--CHOROBY + OBJAWY--")
    for key, car in dict.items():
        print("-" + key + ":")
        for attribute in car:
            print(attribute)


def check_knowledge(dict, symptom):
    if(len(dict) > 0):
        for key, symptom_list in dict.items():
            if symptom in symptom_list:
                for symp in symptom_list:
                    if symptom != symp:
                        result = [symp, key]
                        return result
                    else:
                        return False
                        # print("masz: ", symp + "?")
                        # ans = input()
                        # if ans == 'tak':
                        #     print("Cierpisz na: " + key)
                        #     return True
    else: return 0