import xml.etree.ElementTree as ET

class Poslanec(object):
    def __init__(self, jmeno, hlasy):
        self.jmeno = jmeno
        self.hlasy = float(hlasy)

    def get_jmeno(self):
        return self.jmeno

    def get_hlasy(self):
        return self.hlasy

    #TODO 1
    def __repr__(self):
        return '{} ({})' .format(self.jmeno, self.hlasy)


class Strana(object):
    def __init__(self, nazev, procenta):
        self.nazev = nazev
        self.procenta = float(procenta)
        self.poslanci = []

    def get_nazev(self):
        return self.nazev

    def pridej_poslance(self, posl):
        self.poslanci.append(posl)

    def get_poslanci(self):
        return self.poslanci

    def get_procenta(self):
        return self.procenta
    
    #TODO 1
    def __repr__(self):
        # lst=None
        # for i in self.poslanci:
        #     lst += '\t' +i + '\n'
        return '{} ({})' .format(self.nazev, self. procenta)



class Volby(object):
    def __init__(self, xml_file):
        self.xml_file = xml_file
        self.strany = self.parsuj_strany()
    def get_strany(self):
        return self.strany
        
    #TODO 2
    def parsuj_strany(self):
        root=ET.parse(self.xml_file)
        strana=root.findall()
        print(strana)
        return []
    
    #TODO 3
    def vrat_strany(self):
        return []

    #TODO 4
    def vrat_poslance(self):
        return []
            

def main():
    volby = Volby("vysledky.xml")
    strany = volby.vrat_strany()
    print("SEZNAM STRAN:")
    for s in strany:
        print(s)
        
    print("\nSEZNAM POSLANCU:")
    poslanci = volby.vrat_poslance()
    for p in poslanci:
        print(p)

if __name__=="__main__":
    main()
