import re


class SymptomLoader(object):


    def scanInput(input):

            symptom_list = []

            if (re.search(r'b[oó]l.*gł', input)): symptom_list.append('Ból głowy')
            if (re.search(r'wymio[tc]', input)): symptom_list.append('Wymioty')
            if (re.search(r'b[oó]l.*kla.*', input)): symptom_list.append('Ból klatki piersiowej')
            if (re.search(r'b[oó]l.*r[ęea]', input)): symptom_list.append('Ból ręki')
            if (re.search(r'b[oó]l.*mi[eê]', input)): symptom_list.append('Ból mięśni')
            if (re.search(r'b[oó]l.*staw', input)): symptom_list.append('Ból stawów')
            if (re.search(r'b[oó]l.*brzu', input)): symptom_list.append('Ból brzucha')
            if (re.search(r'.*puch.*r[ę]', input)): symptom_list.append('Opuchlizna ręki')
            if (re.search(r'.*grubi.*r[ę]', input)): symptom_list.append('Wygrubienie na ręce')
            if (re.search(r'.*staj.*koś', input)): symptom_list.append('Wystająca kość')
            if (re.search(r'.*pobud', input)): symptom_list.append('Zwiększona pobudliwość nerwowa')
            if (re.search(r'(.*sn(u|em))|(spa[nćc])', input)): symptom_list.append('Zaburzenia snu')
            if (re.search(r'.*ko³.*serc', input)): symptom_list.append('Kołatanie serca')
            if (re.search(r'.*zawr[oó]', input)): symptom_list.append('Zawroty głowy')
            if (re.search(r'.*wyżzs].*ciśs]', input)): symptom_list.append('Podwyższone ciśnienie')
            if (re.search(r'(.*pragnie)|((du|wi).*pi[jcæ])', input)): symptom_list.append('Wzmożone pragnienie')
            if (re.search(r'.*czę.*mocz', input)): symptom_list.append('Częste oddawanie moczu')
            if (re.search(r'.*((wzmoż)|(du|wi[eę]))?.*apetyt', input)): symptom_list.append('Wzmożony apetyt')
            if (re.search(r'słab.*', input)): symptom_list.append('Osłabienie')
            if (re.search(r'senn', input)): symptom_list.append('Sennośc')
            if (re.search(r'(widz)?.*(podw[óo]).*(widz)?', input)): symptom_list.append('Podwójne widzenie')
            if (re.search(r'tra[ct].*wa[gd]', input)): symptom_list.append('Utrata wagi')
            if (re.search(r'dra[ż]', input)): symptom_list.append('Drażliwość')
            if (re.search(r'apat(ia|ycz)', input)): symptom_list.append('apatia')
            if (re.search(r'zm[ęe]cz', input)): symptom_list.append('Zmęczenie')
            if (re.search(r'go[ji].*si[eê].*ran', input)): symptom_list.append('Wolne gojenie się ran')
            if (re.search(r'dreszcz', input)): symptom_list.append('Dreszcze')
            if (re.search(r'płlyt.*odd', input)): symptom_list.append('Płytki oddech')
            if (re.search(r'[wz] p[ł]uc', input)): symptom_list.append('Wydzielina z płuc')
            if (re.search(r'(such)?.*kasz(el|le)', input)): symptom_list.append('Suchy kaszel')
            if (re.search(r'dusznośc]', input)): symptom_list.append('Duszności')
            if (re.search(r'katar', input)): symptom_list.append('Katar')
            if (re.search(r'[ł]zaw', input)): symptom_list.append('Łzawienie')
            if (re.search(r'dusznośc]', input)): symptom_list.append('Duszności')
            if (re.search(r'wysyp', input)): symptom_list.append('Wysypka')
            if (re.search(r'nudnośs]', input)):symptom_list.append('Nudności')
            if (re.search(r'biegun[kc]', input)):symptom_list.append('Biegunka')
            if (re.search(r'gorączk', input)):symptom_list.append('Gorączka')

            if len(symptom_list) is not 0:
                return symptom_list
            else:
                print("nie znaleziono objawu w bazie")
                return 0