#from alert_sender import AlertSender

DATA: list = []

#alerter = AlertSender()

last_T=[
    [2,5,5,5],
    [5,5,3,5],
    [5,4,5,5],
    [5,5,5,5]
    ]
T=[
    [2,5,5,5],
    [5,5,2,5],
    [5,3,5,5],
    [5,5,5,5]
    ]
nb_strip = len(T) # nombre de strip de capteur
nb_sensor = len(T[0]) # nombre de capteur par strip
T_seuil = 3 # Température de seuil (si plus bas = alerte)
# Flag sur les températures basses 
map = [[0 for i in range(2*nb_sensor+1)] for j in range(2*nb_strip+1)]
for i in range(nb_strip):
    for j in range(nb_sensor):
        if T[i][j] <= T_seuil: # dans ce cas, valeur dans flag = 1 sinon reste 0
            #if last_T[i][j] > T_seuil: # notification par textos
                #alerter.sendAlert("Indice de gel au capteur " + str(j+1) + " de la rangée " + str(i+1))
            if i == 0 and j == 0:
                i_map = i + 1
                j_map = i_map
            elif i == 0:
                i_map = i + 1
                if j == nb_sensor - 1:
                    j_map = 2 ** j - 1
                else:
                    j_map = 2 ** j +1
            elif j == 0: # pense pas j == 0 nécessaire....
                j_map = j + 1
                if i == nb_strip - 1:
                    i_map = 2 ** i -1
                else:
                    i_map = 2 ** i + 1
            elif i == nb_strip - 1 and j == nb_sensor - 1:
                i_map = 2 ** i - 1
                j_map = 2 ** j - 1
            elif j == nb_sensor - 1:
                i_map = 2 ** i + 1
                j_map = 2 ** j - 1
            elif i == nb_strip - 1:
                i_map = 2 ** i - 1
                j_map = 2 ** j + 1
            else:
                i_map = 2 ** i + 1
                j_map = 2 ** j + 1
            map[i_map][j_map] = 1
            for n in range(i_map-1,i_map+2): # sources de chaleur
                for m in range(j_map-1,j_map+2):
                    if n == i_map and m == j_map:
                        pass
                    else:
                        map[n][m] = 2
            DATA.append(map)
            DATA.append(map)
#display
print('\n')
print('Nombre de bandes : ',nb_strip)
print('Nombre de capteurs par bandes :',nb_sensor)
print('map = ',len(map),'x',len(map[0]))
print('Anciennes températures')
for i in range(len(last_T)):
    print(last_T[i])
print('Nouvelles températures :')
for i in range(nb_strip):
    print(T[i])
print('Mapping du vignoble :')
for i in range(len(map)):
    print(map[i])
print('\n')    
