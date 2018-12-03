import xmlrpc.client
import random
import visualizer
import xml.etree.ElementTree as ET

# BEFORE YOU START
# 1) SET VIRTUAL ENVIRONMENT
# python3 -m venv spja
# . spja/bin/activate
# pip3 install pygame

class Agent:
    def __init__(self, filename):
        # TODO 1 1b - nacist data z configuracniho xml souboru (nazev v parametru
        # filename)
        # TODO 2 0.5b - vytvorit instancni promenne (login, data, gameserver)
        # login - nastavit dle hodnoty prectene z XML
        # data - prazdny list, kde budou ukladana data ze serveru
        # gameserver - pripojit se k XML-RPC serveru (url v XML souboru)
        self.visualizer = visualizer.Visualizer()
        # TODO 3 0.5p - na serveru zavolat metodu add_player s parametrem login (v instancni promenne login)

        file = open(filename, "r")
        feed = file.read()
        root = ET.fromstring(feed)
        self.login = root.find("login").text
        self.data = []
        self.visualizer = visualizer.Visualizer()
        self.gameserver= xmlrpc.client.ServerProxy(root.find("url").text)
        self.gameserver.add_player(self.login)

    def action(self):
        # TODO 4 0.5p - zavolat z xml-rpc serveru metodu make_action
        self.data= self.gameserver.make_action(self.login, "look", "")
        self.visualizer.visualize(self.data)
        # metoda ma 3 parametry (login, nazev_akce, parametry)
        # vsechny tri jsou retezce. Zavolejte "look" na rozhlizeni
        # kolem sebe bez parametru (prazdny retezec). Metoda make-action vraci pole
        # retezcu, kde kazdy radek reprezentuje jeden radek z okoli.
        # Tato data ulozte do instancni promenne data a vykreslete pomoci metody visualize z tridy Visualizer.
        # Kazdy retezec ma sirku 11 znaku a samotnych radku je 22. Prvnich
        # jedenact reprezentuje okoli agenta a dalsich jedenact, objekty v
        # jeho okoli (zatim pouze "p" - ostatni agenti). Hrac je v tomto
        # okoli na pozici [5][5] (paty radek, paty znak). Objekty na stejne
        # pozici neleznete na souradnicich [5+11][5].
        # "~" voda
        # " " trava
        # "*" cesta
        # "t" strom
        # "o" skala (zed)
        # "f" dlazdena podlaha
        # "p" hrac

          #self.gameserver.make_action(self.login, nazev_akce, parametry)


class AgentRandom(Agent):
    # TODO 5 1b - tento agent bude dedit z agenta predchoziho a
    # upravi funkci action tak, ze akci bude "move" a v parametru
    # preda jeden ze smeru "north", "west", "south", "east". Tyto
    # smery bude vybirat nahodne (najdete vhodnou metodu z balicku
    # random)
    def action (self):
        smer = random.choice(["north", "west", "south", "east"])
        self.data = self.gameserver.make_action(self.login, "move", smer)
        self.visualizer.visualize(self.data)


class AgentLeftRight(Agent):
    # TODO 6 1.5b - tento agent bude chodit stale doleva, dokud nenarazi na prekazku (co je a neni prekazka viz komentar v metode action, 
    # zajimaji vas pozice [5][4] a [5][6]).
    # V takovem pripade obrati svuj smer a pohybuje se stale doprava, nez take narazi na prekazku.
    def action(self):
        flag = 0
        if (not flag):
            smer = "east"
        else:
            smer = "west"
        self.data = self.gameserver.make_action(self.login, "move", smer)
        self.visualizer.visualize(self.data)




def main():
    agent = None
    try:
        agent = Agent("config.xml")
        agent = AgentRandom("config.xml")
        # agent = AgentLeftRight("config.xml")
        while agent.visualizer.running:
            agent.action()
        else:
            agent.gameserver.make_action(agent.login, "exit", "")
    except KeyboardInterrupt:
        agent.gameserver.make_action(agent.login, "exit", "")


if __name__ == "__main__":
    main()
