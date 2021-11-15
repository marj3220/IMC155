#Matrice n x m test chaque ligne (vecteur) est une bande de n capteurs
from alert_sender import AlertSender

DATA: list = []

alerter = AlertSender()
T=[
    [5,5,5,5],
    [5,2,2,5],
    [5,2,2,5],
    [5,5,5,5]
    ]
nb_strip = len(T) # nombre de strip de capteur
nb_sensor = len(T[0]) # nombre de capteur par strip
T_seuil = 3 # Température de seuil (si plus bas = alerte)
# Flag sur les températures basses 
flag_T = [[0 for i in range(nb_sensor)] for j in range(nb_strip)]
for i in range(len(T)):
    for j in range(len(T[1])):
        if T[i][j] <= T_seuil:
            flag_T[i][j] = 1 # Si température plus petite ou égal au seuil, valeur devient 1 sinon reste 0
            alerter.sendAlert("Indice de gel au capteur " + str(j+1) + " de la rangée " + str(i+1))
            DATA.append("Indice de gel au capteur " + str(j+1) + " de la rangée " + str(i+1))
#display
print('\n')
print('T = ',T)
print('Nombre de bandes : ',nb_strip)
print('Nombre de capteurs par bandes :',nb_sensor)
print('État a chaque capteurs :\n',flag_T)
print('\n')    
