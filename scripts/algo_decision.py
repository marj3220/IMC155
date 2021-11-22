#from alert_sender import AlertSender

DATA = []

# ree=[
#     [1,0,0],
#     [0,0,1],
#     ]

# DATA.append(ree)
# DATA.append(ree)
# DATA.append(ree)
# DATA.append(ree)
#alerter = AlertSender()

last_T=[
    [5,5,5],
    [5,5,5]
    ]
T=[
    [3,5,5],
    [3,5,3],
    ]
nb_strip = len(T) # nombre de strip de capteur
nb_sensor = len(T[0]) # nombre de capteur par strip
T_seuil = 3 # Température de seuil (si plus bas = alerte)
# Flag sur les températures basses 
T_state = [[0 for i in range(nb_sensor)] for j in range(nb_strip)]
heat = [[0 for i in range(2*nb_sensor+1)] for j in range(3*nb_strip-1)]
for i in range(nb_strip):
    for j in range(nb_sensor):
        if T[i][j] <= T_seuil: # dans ce cas, valeur = 1 sinon reste 0
            #if last_T[i][j] > T_seuil: # notification par textos
                #alerter.sendAlert("Indice de gel au capteur " + str(j+1) + " de la rangée " + str(i+1))
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
            print(i,j,i_heat,j_heat)
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

DATA.append({"heat":heat, "T_state":T_state})

#display
print('Nombre de bandes : ',nb_strip)
print('Nombre de capteurs par bandes :',nb_sensor)
print('map = ',len(heat),'x',len(heat[0]))
print('Anciennes températures')
for i in range(len(last_T)):
    print(last_T[i])
print('Nouvelles températures :')
for i in range(nb_strip):
    print(T[i])
print('Seuil de température :',T_seuil,'Celsius')
print('États des capteurs de température :')
for i in range(nb_strip):
    print(T_state[i])
print('États des sources de chaleurs :')
for i in range(len(heat)):
    print(heat[i])
