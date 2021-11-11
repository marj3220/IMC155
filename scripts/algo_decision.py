#Matrice n x m test chaque ligne (vecteur) est une bande de n capteurs
T=[
    [1,2,4],
    [3,4,2],
    [2,3,3],
    [4,4,3]
    ]
nb_strip = len(T) # nombre de strip de capteur
nb_sensor = len(T[0]) # nombre de capteur par strip
d_capt = 1 # Distance entre les capteurs sur une même bande
d_strip = 1 # Distance entre les bandes
T_seuil = 3 # Température de seuil (si plus bas = alerte)
# algo de décision
flag_T = [[0 for i in range(nb_sensor)] for j in range(nb_strip)]
for i in range(len(T)):
    for j in range(len(T[1])):
        if T[i][j] <= T_seuil:
            flag_T[i][j] = 'We good'
        else:
            flag_T[i][j] = "Get u're ass outside!"
#display
print('\n')
print('T = ',T)
print('Nombre de bandes : ',nb_strip)
print('Nombre de capteurs par bandes :',nb_sensor)
print('État a chaque capteurs :\n',flag_T)
print('\n')    
