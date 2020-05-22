
#liste=['name','total_cases','active_cases','recovered_cases','total-deaths']

def tri_selection(liste,croi_decroi,tri_par):
    """(liste=liste that you wish to sort , croi_decroi = 1 si croissant 0 sinon  , tri_par= ('d' for death_rate)('t' for total cases)('a' for active cases)('r' for recovered cases)('n' for name)""" 
    try:
        if tri_par=="n" :
            tri_suivant_indice=0
        elif tri_par=="t" :
            tri_suivant_indice=1
        elif tri_par=="a" :
            tri_suivant_indice=2
        elif tri_par=="r":
            tri_suivant_indice=3
        elif tri_par=="d" :
            tri_suivant_indice=4
        else :
            raise TypeError("tri_par should take one of the following values ('d' for death_rate)('t' for total cases)('a' for active cases)('r' for recovered cases)('n' for name)")
    except TypeError as e:
        print(str(e))


    # if sorting by name (string)
    if tri_par=="n":
        try:
            if croi_decroi==1:
                i=0
                while i < len(liste):
                    j=i+1
                    indice=i
                    while j < len(liste):  
                        if str(liste[j][tri_suivant_indice]) < str(liste[indice][tri_suivant_indice]):
                            indice=j
                        j+=1
                    liste[i],liste[indice]=liste[indice],liste[i]
                    i+=1
                return liste
            elif croi_decroi==0 :
                i=0
                while i < len(liste):
                    j=i+1
                    indice=i
                    while j < len(liste):  
                        if str(liste[j][tri_suivant_indice]) > str(liste[indice][tri_suivant_indice]):
                            indice=j
                        j+=1
                    liste[i],liste[indice]=liste[indice],liste[i]
                    i+=1
                return liste
            else:
                raise TypeError("croi_decroi doit etre booléen")
        except TypeError as e:
            print('inserer 0 pour decroissant ou 1 pour croissant //'+str(e))
    
    
    #if sorting by numbers (int) 
    else:
        try:
            if croi_decroi==1:
                i=0
                while i < len(liste):
                    j=i+1
                    indice=i
                    while j < len(liste):  
                        if int(liste[j][tri_suivant_indice]) < int(liste[indice][tri_suivant_indice]):
                            indice=j
                        j+=1
                    liste[i],liste[indice]=liste[indice],liste[i]
                    i+=1
                return liste
            elif croi_decroi==0 :
                i=0
                while i < len(liste):
                    j=i+1
                    indice=i
                    while j < len(liste):  
                        if int(liste[j][tri_suivant_indice]) > int(liste[indice][tri_suivant_indice]):
                            indice=j
                        j+=1
                    liste[i],liste[indice]=liste[indice],liste[i]
                    i+=1
                return liste
            else:
                raise TypeError("croi_decroi doit etre booléen")
        except TypeError as e:
            print('inserer 0 pour decroissant ou 1 pour croissant //'+str(e))
        