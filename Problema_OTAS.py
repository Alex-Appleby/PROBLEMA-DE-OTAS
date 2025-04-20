
def Problema_OTAS(Open_Travel_Areas, Intersecciones):
    #Variable de resultados
    Resultados = {}
    
    for Interseccion, Coordenadas in Intersecciones.items():
        
        OTAS_y_TIPOS = {}
        
        for OTA, Medidas in Open_Travel_Areas.items():
            
            Tipo = ""
            
            #Verificar si la intersección está dentro de la OTA
            if (Coordenadas[0] > Medidas[0] and Coordenadas[0] < Medidas[1]) and (Coordenadas[1] > Medidas[2] and Coordenadas[1] < Medidas[3]):
                Tipo = "Dentro"
            else:
                #Verificar si la intersección está en un borde de la OTA
                bordes_verticales = False
                bordes_horizontales = False
                
                if (Coordenadas[0] == Medidas[0] or Coordenadas[0] == Medidas[1]) and (Coordenadas[1] >=  Medidas[2] and Coordenadas[1] <= Medidas[3]):
                    bordes_verticales = True
                if (Coordenadas[1] == Medidas[2] or Coordenadas[1] == Medidas[3]) and (Coordenadas[0] >= Medidas[0] and Coordenadas[0] <= Medidas[1]):
                    bordes_horizontales = True
                
                if bordes_verticales or bordes_horizontales:
                    Tipo = "Borde"
                else: #Se encuentra fuera de la OTA
                    Tipo = "Fuera"
            
            OTAS_y_TIPOS[OTA] = Tipo
        
        Resultados[Interseccion] = OTAS_y_TIPOS
        
    return Resultados

#Variables de Datos
Open_Travel_Areas = {"OTA_RCBGEN": [10000, 24360, 10000, 12540], "OTA_CRCBGE": [10000, 42030, 12540, 12930], "OTA_PCKIZQ": [10000, 11930, 12930, 20170], "OTA_EMP1": [10000, 32550, 20170, 21520], "OTA_EMP2": [32550, 36280, 20470, 21520], "OTA_MANT": [36280, 45729, 20170, 21520], "OTA_EMPFR1": [10000, 11030, 21520, 23180], "OTA_EMPFR2": [26570, 27720, 21520, 23180], "OTA_EMPFR3": [42010, 42280, 21520, 23180], "OTA_EMBE": [10000, 42280, 23180, 24120], "TIENDA_1": [11930, 21530, 16750, 17010], "OTA_TARDIR": [21530, 22990, 12930, 20170], "OTA_TRASB": [22990, 24360, 12930, 20170], "OTA_RCB": [24360, 30140, 10000, 12540], "OTA_RCBCLS": [24360, 26560, 12930, 13930], "OTA_TARCYT": [28190, 29860, 12930, 20170], "OTA_RCBSTK": [30140, 42030, 10000, 12540], "OTA_STOCK1": [29860, 37590, 16560, 16940], "OTA_STOCK2": [35210, 37010, 12930, 16560], "OTA_STOCK3": [37690, 44790, 16560, 16940], "OTA_TRAC": [44650, 44790, 12930, 16560], "OTA_RCBAC": [42130, 45759, 11000, 12930]}
Intersecciones = {"I_PICKA1": [14550,12929], "I_PICKA2": [14550,16751], "I_PICKB1": [14550,17009], "I_PICKB2": [14550,20171], "I_PICKC1": [16130,17009], "I_PICKC2": [16130,20171], "I_PICKD1": [16130,12929], "I_PICKD2": [16130,16751], "I_PICKG1": [17540,17009], "I_PICKG2": [17540,20171], "I_PICKH1": [17540,12929], "I_PICKH2": [17540,16751], "I_PICKDC1": [29860,12929], "I_PICKDC2": [29860,16751], "I_PICKDC3": [29860,17009], "I_PICKDC4": [29860,20171], "I_FR1": [11029,21700], "I_FR2": [26571,21700], "I_FR3": [27719,21700], "I_FR4": [42011,21700], "I_STOCK2_1": [30140,12929], "I_STOCK2_2": [30140,16561], "I_STOCK2_3": [30140,16939], "I_STOCK2_4": [30140,20171], "I_STOCK4_1": [31270,12929], "I_STOCK4_2": [31270,16561], "I_STOCK4_3": [31270,16939], "I_STOCK4_4": [31270,20171], "I_STOCK6_1": [31810,12929], "I_STOCK6_2": [31810,16561], "I_STOCK6_3": [31810,16939], "I_STOCK6_4": [31810,20171], "I_STOCK8_1": [32400,12929], "I_STOCK8_2": [32400,16561], "I_STOCK8_3": [32400,16939], "I_STOCK8_4": [32400,20171], "I_STCK10_1": [32970,12929], "I_STCK10_2": [32970,16561], "I_STCK10_3": [32970,16939], "I_STCK10_4": [32970,20471], "I_STCK12_1": [33540,12929], "I_STCK12_2": [33540,16561], "I_STCK12_3": [33540,16939], "I_STCK12_4": [33540,20471], "I_STCK50_1": [34060,12929], "I_STCK50_2": [34060,16561], "I_STCK50_3": [34060,16939], "I_STCK50_4": [34060,20471], "I_STCK14_1": [34640,12929], "I_STCK14_2": [34640,16561], "I_STCK14_3": [34640,16939], "I_STCK14_4": [34640,20171], "I_STCK16_1": [35210,12929], "I_STCK16_2": [35210,16561], "I_STCK16_3": [35210,16939], "I_STCK16_4": [35210,20171], "I_STCK18_3": [35700,16939], "I_STCK18_4": [35700,20171], "I_STCK20_3": [36280,16939], "I_STCK20_4": [36280,20171], "I_STCK22_3": [36860,16939], "I_STCK22_4": [36860,20171], "I_STCK24_3": [37440,16939], "I_STCK24_4": [37440,20171], "I_STCK28_1": [37950,12929], "I_STCK28_2": [37950,16561], "I_STCK28_3": [37950,16939], "I_STCK28_4": [37950,20171], "I_STCK30_1": [38550,12932], "I_STCK30_2": [38550,16561], "I_STCK30_3": [38550,16939], "I_STCK30_4": [38550,20171], "I_STCK32_1": [39100,12932], "I_STCK32_2": [39100,16561], "I_STCK32_3": [39100,16939], "I_STCK32_4": [39100,20171], "I_STCK34_1": [39660,12932], "I_STCK34_2": [39660,16561], "I_STCK34_3": [39660,16939], "I_STCK36_4": [39660,20171], "I_STCK36_1": [40240,12932], "I_STCK36_2": [40240,16561], "I_STCK36_3": [40240,16939], "I_STCK34_4": [40240,20171], "I_PICKAV_1": [43540,12929], "I_PICKAV_2": [43540,16561], "I_PICKCV_1": [42950,12929], "I_PICKCV_2": [42950,16561], "I_PICKEV_1": [42430,12929], "I_PICKEV_2": [42430,16561], "I_PICKGV_1": [41880,12929], "I_PICKGV_2": [41880,16561], "I_PICKIV_1": [41340,12932], "I_PICKIV_2": [41340,16561]}

Resultados = Problema_OTAS(Open_Travel_Areas, Intersecciones)

'''
Resultados_Limpios = {}

#Limpiar Resultados
for Interseccion, Valor in Resultados.items():
    
    OTAS_Y_TIPOS = {}
    
    for OTA, Tipo in Valor.items():
        if Tipo == "Dentro" or Tipo == "Borde":
            OTAS_Y_TIPOS[OTA] = Tipo
            
    Resultados_Limpios[Interseccion] = OTAS_Y_TIPOS

print(Resultados_Limpios)
'''


#Crear CSV de salida
print("------------------------------------")
print("Intersection,Intersection Type,Open Travel Area 1,Open Travel Area 2")
for Interseccion, Valor in Resultados.items():
    
    contador_dentro = 0
    contador_bordes = 0
    
    for OTA, Tipo in Valor.items():
        #Cuando el tipo es #Dentro"
        if Tipo == "Dentro":
            print(Interseccion,",","3",",", OTA,",",",")
            contador_dentro += 1
        
        #Cuando el tipo es "Borde"
        if Tipo == "Borde":
            print(Interseccion,",","1",",", OTA,",",",")
            contador_bordes += 1
        
    
    #Intersección de tipo 0
    if not contador_dentro and not contador_bordes:
        print(Interseccion,",","0",",",",",",")
        
    
print("------------------------------------")