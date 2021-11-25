from alert_sender import AlertSender

class DecisionTaker():
    def __init__(self) -> None:
        self.alreadySent = [    [False, False, False],
                                [False, False, False] ]
        self.alerter = AlertSender()

    def compute_data(self, temp_matrix):
        T = temp_matrix
        nb_strip = len(T) # nombre de strip de capteur
        nb_sensor = len(T[0]) # nombre de capteur par strip
        T_seuil = 24 # Température de seuil (si plus bas = alerte)
        
        # Flag sur les températures basses 
        T_state = [[0 for i in range(nb_sensor)] for j in range(nb_strip)]
        heat = [[0 for i in range(2*nb_sensor+1)] for j in range(3*nb_strip-1)]
        for i in range(nb_strip):
            for j in range(nb_sensor):
                if T[i][j] <= T_seuil: # dans ce cas, valeur = 1 sinon reste 0
                    if self.alreadySent[i][j] == False: # notification par textos
                        self.alreadySent[i][j] = True
                        #self.alerter.sendAlert("Indice de gel au capteur " + str(j+1) + " de la rangée " + str(i+1))
                    if i == 0 and j == 0:
                        i_heat = i
                        j_heat = j + 1
                    elif i == 0:
                        i_heat = i
                        j_heat = 2 ** j + 1
                    elif j == 0:
                        j_heat = j + 1
                        i_heat = 3 * i
                    else:
                        i_heat = 3 * i
                        j_heat = 2 ** j + 1
                    T_state[i][j] = 1
                    heat[i_heat][j_heat] = 1
                    for n in range(i_heat,i_heat+2): # sources de chaleur
                        for m in range(j_heat-1,j_heat+2):
                            if n == i_heat and m == j_heat:
                                pass
                            else:
                                heat[n][m] = 1
                    if i != nb_strip - 1 and T[i+1][j] <= T_seuil: # chauffage du centre 
                        i_hc = i_heat + 2
                        for c in range(j_heat-1,j_heat+2):
                            heat[i_hc][c] = 1 
                else:
                    self.alreadySent[i][j] = False
        return {"heat":heat, "T_state":T_state, "T":T}