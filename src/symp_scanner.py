import re


class SymptomLoader(object):
    def scanInput(input):

        if (re.search(r'b[oó]l.*gł', input)): return 'Ból głowy'
        if (re.search(r'wymio[tc]', input)): return 'Wymioty'
        if (re.search(r'b[oó]l.*kla.*', input)): return 'Ból klatki piersiowej'
        if (re.search(r'b[oó]l.*r[ęea]', input)): return 'Ból ręki'
        if (re.search(r'b[oó]l.*mi[eê]', input)): return 'Ból mięśni'
        if (re.search(r'b[oó]l.*staw', input)): return 'Ból stawów'
        if (re.search(r'b[oó]l.*brzu', input)): return 'Ból brzucha'
        if (re.search(r'.*puch.*r[ę]', input)): return 'Opuchlizna ręki'
        if (re.search(r'.*grubi.*r[ę]', input)): return 'Wygrubienie na ręce'
        if (re.search(r'.*staj.*koś', input)): return 'Wystająca kość'
        if (re.search(r'.*pobud', input)): return 'Zwiększona pobudliwość nerwowa'
        if (re.search(r'(.*sn(u|em))|(spa[nćc])', input)): return 'Zaburzenia snu'
        if (re.search(r'.*ko³.*serc', input)): return 'Kołatanie serca'
        if (re.search(r'.*zawr[oó]', input)): return 'Zawroty głowy'
        if (re.search(r'.*wyżzs].*ciśs]', input)): return 'Podwyższone ciśnienie'
        if (re.search(r'(.*pragnie)|((du|wi).*pi[jcæ])', input)): return 'Wzmożone pragnienie'
        if (re.search(r'.*czę.*mocz', input)): return 'Częste oddawanie moczu'
        if (re.search(r'.*((wzmoż)|(du|wi[eę]))?.*apetyt', input)): return 'Wzmożony apetyt'
        if (re.search(r'słab.*', input)): return 'Osłabienie'
        if (re.search(r'senn', input)): return 'Sennośc'
        if (re.search(r'(widz)?.*(podw[óo]).*(widz)?', input)): return 'Podwójne widzenie'
        if (re.search(r'tra[ct].*wa[gd]', input)): return 'Utrata wagi'
        if (re.search(r'dra[ż]', input)): return 'Drażliwość'
        if (re.search(r'apat(ia|ycz)', input)): return 'apatia'
        if (re.search(r'zm[ęe]cz', input)): return 'Zmęczenie'
        if (re.search(r'go[ji].*si[eê].*ran', input)): return 'Wolne gojenie się ran'
        if (re.search(r'dreszcz', input)): return 'Dreszcze'
        if (re.search(r'płlyt.*odd', input)): return 'Płytki oddech'
        if (re.search(r'[wz] p[ł]uc', input)): return 'Wydzielina z płuc'
        if (re.search(r'(such)?.*kasz(el|le)', input)): return 'Suchy kaszel'
        if (re.search(r'dusznośc]', input)): return 'Duszności'
        if (re.search(r'katar', input)): return 'Katar'
        if (re.search(r'[ł]zaw', input)): return 'Łzawienie'
        if (re.search(r'dusznośc]', input)): return 'Duszności'
        if (re.search(r'wysyp', input)): return 'Wysypka'
        if (re.search(r'nudnośs]', input)):return 'Nudności'
        if (re.search(r'biegun[kc]', input)):return 'Biegunka'
        if (re.search(r'gorączk', input)):return 'Gorączka'

        else:
            print("nie znaleziono objawu w bazie")
