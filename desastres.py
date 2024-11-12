def main():
    desastre1=desastres(3160000,7.3,"Haiti","terremoto")
    desastre2=desastres(8,5,"Texas","ciclone")
    desastre3=desastres(20000,7,"Japão","tsunami")
    desastre4=desastres(0,4.5,"California","terremoto")
    # ------------------------------------------#
    desastre1.mostrar_info()
    desastre1.media_por_escala()
    desastre2.mostrar_info()
    desastre2.media_por_escala()
    desastre3.mostrar_info()
    desastre3.media_por_escala()
class desastres:
    ''' __init__()
        mostrar_info()
        media_por_escala()
        main()'''      
    def __init__(self,mortes,escala,local,desastre):
        self.mortes=mortes
        self.escala=escala
        self.local=local
        self.desastre=desastre

    def mostrar_info(self):
        print(f"{25*"=-"}\ndesastre:{self.desastre}|escala:{self.escala}|mortes:{self.mortes}|local:{self.local}\n{25*"=-"}")

    def media_por_escala(self):
        media=self.mortes/self.escala
        print(f"Média de mortes do {self.desastre}:{round(media,2)}")
# ---------------------------------------------------------------#


if __name__=="__main__":
    main()
