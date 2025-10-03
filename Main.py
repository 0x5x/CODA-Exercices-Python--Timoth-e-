def exercice0(): 
    print("Exercice 1 : Bonjour le monde !") 
    print("Hello World !") 
    
def excercice1():
    print ("Hello world !")

def exercice2():
    prenom = str (input("quel est ton prénom ? "))
    print ("Bonjour " + prenom) 
        
def exercice3():
    prenom = str (input("quel est ton prénom ? "))
    print ("Bonjour " + prenom)
    print ("Bienvenue dans le monde de la programmation")
    print ("bon courage pour les études")

def exercice4():
    année_naissance = int(input("En quelle année est tu né(e) ?"))
    année_actuelle = 2025
    age = année_actuelle - année_naissance
    print ("tu as " +  str(age)+ "ans")
    
def exercice5():
    a = int (input("Entrez un premier nombre : "))
    b = int (input("Entrez un deuxième nombre : "))
    print(addition(a, b))
    
def soustraction(a, b):
        return a - b    
def exercice6():
    a = int (input("Entrez un premier nombre : "))
    b = int (input("Entrez un deuxième nombre : "))
    print(soustraction(a,b))
    
def multiplication (a,b):
    return a * b    
def exercice7():
    a =int (input ("Entrez un nombre "))
    b =int (input ("Entrez un autre nombre"))
    print(multiplication(a,b))

def division (a,b):
    return a / b
def exercice8():
    a = int (input ("Entrez un nombre ")) 
    b = int (input ("Entrez un autre nombre "))           
    print(division(b/a))

def carre (a):
    return a**2
def exercice9():
    a = int (input ("Entrez un nombre "))
    print(a**2)
    
def double (a):
    return a*2
def exercice10():
    a = int (input ("Entrez un nombre "))
    print(a*2)

def nombre_diviser (a):
    return a/2
def exercice11():
    a = int (input ("entez un nombre"))
    print(a/2)
    
def afficher_5fois (prenom):
    for i in range (1,5):
        print(prenom)
        
def exercice12():
        prenom = str (input ("entrez un mot"))
        afficher_5fois(prenom)
        
def compter():
    return list (range(1,6))
def exercice13():
    print(compter())
    
def table_de_multiplication(n):
    for i in range (1,11):
        print (f"{n} x {i} = {n*i}")
def exercice14():
    n = int (input ("entrez un nombre"))
    print(table_de_multiplication(n))
    
def aire_carre (cote):
    return cote * cote   
def perimetre_carre (cote):
    return cote * 4
def exercice15():
    cote = float (input ("entrez la longueur d'un coter du carré"))
    print("le périmètre du carré est de " + str(perimetre_carre(cote)))
    print("l'aire du carré est de " + str(aire_carre(cote)))
    
def convertir_euros_en_dollars(euros):
    taux_de_change = 1.1
    return euros * taux_de_change
def exercice17():
    euros = float (input ("Entrez un montantn en euros"))
    print("le montant en dollars est de " + str(convertir_euros_en_dollars(euros)))
    
def convertir_minutes_en_heures(minutes):
    heure = minutes // 60 
    minute = minutes % 60
    return heure, minute
def exercice18():
    minutes = int (input ("entez un nombre de minutes"))
    heure , minute = convertir_minutes_en_heures(minutes)
    print(f"{minutes} minutes = {heure} heures et {minutes} minutes")

def calculer_ttc(prix_ht, taux_tva):
    return prix_ht * (1 + taux_tva / 100)
def exercice19():
    prix_ht = float (input ("entrez un prix hors taxe"))
    taux_tva = float (input ("entez le taux de tva en pourcentage"))
    print("le prix ttc est de " + str(calculer_ttc(prix_ht, taux_tva)))

def demander_nom_et_age():
    nom = (input ("Entez votre nom"))
    age = int (input ("entrez votre âge"))
    return (nom, age)
    print("tu t'appelles  " + demander_nom_et_age()) ("et tu as" + age + "ans")
def exercice20():
       nom, age = demander_nom_et_age()
       print("tu t'appelles " + nom + " et tu as " + str(age) + " ans")     
       
def nombre_positif_ou_negatif(n):
    if n > 0:
        return "positif"
    elif n < 0:
        return "négatif"
    else :
        return "zéro"
def exercice21():
    n = int (input ("entrez un nombre"))
    print(nombre_positif_ou_negatif(n))
    
def majeur_ou_mineur(age):
    if age >= 18:
        return "majeur"
    elif age < 18:
        return "mineur"
def exercice22():
    age = int (input ("entrez votre âge"))
    print(majeur_ou_mineur(age))
    
def note_validee(note):
    if note >= 12:
       return "validée"
    elif note < 12:
       return "non validée"
def exercice23():
    note = float(input("entrez votre note"))
    print(note_validee(note))
    
def comparer_nombres(a,b):
    if a > b:
        return f"{a} est plus grand que {b}"
    elif a < b: 
        return f"{a} est plus petit que {b}"
def exercice24():
    a = int (input ("entrez un nombre"))
    b = int (input ("entrez un autre nombre")) 
    print(comparer_nombres(a,b))
    
def nombre_croissant (a,b):
    if a < b :
        return True
    elif a > b :
        return False 
def exercice25():
    a = int (input ("entrez un nombre"))
    b = int (input ("entrez un autre nombre"))
    print(nombre_croissant(a,b))
    
def savoir_si_divisible_par_5(n):
    if n % 5 == 0:
        return True
    elif n % 5 != 0: 
        return False
def exercice26():
    n = int (input (" entrez un nombre"))
    print(savoir_si_divisible_par_5(n))
    
def classer_selon_age(age):
    if age <12:
        return "enfant"
    elif 12 <= age < 18:
        return "adolescent"
    elif age >= 18:
        return "adulte"
def exercice27():
    age = int(input ("entrez votre âge "))
    print(classer_selon_age(age)) 

def température_solide_liquide_gazeux(eau):
    if eau <= 0:
        return "glace"
    elif 0 < eau < 100:
        return "liquide"
    elif eau >= 100:
        return "vapeur"
def exercice28():
    eau = float (input ("entrez la temperature de l'eau en degre celsius pas farenheit hein"))
    print(température_solide_liquide_gazeux(eau))
    
def attribuer_mention_selon_note(note):
    if note < 10:
        return "Recalé"
    elif note >= 11 and note < 14:
        return "Passable"
    elif note >= 14:
        return "Bien"
    elif note >= 17: 
        return "Très bien"
def exercice29():
    note = float (input ("entez un nombre"))
    print(attribuer_mention_selon_note(note))
    
def compter_1_jusqua_n(n):
    for i in range (1,n+1):
        print(i)
def exercice30():
    n = int (input ("entrez un nombre"))
    compter_1_jusqua_n(n)
    
def compte_a_rebours(n):
    for i in range (n,0,-1):
        print(i)
def exercice31():
    n = int (input ("entrez un nombre"))
    print(compte_a_rebours(n))
              
def somme_jusqua_n(n):
    somme = 0 
    for i in range (1,n+1):
        somme += i
    return somme
def exercice32():
    n = int (input ("entrez un nombre"))
    print(somme_jusqua_n(n))

def table_de_multiplication_de_1_a_10():
    for i in range (1,11):
        print(f"Table de multiplication de {i}")
        for j in range (1,11):
            print(f"{i} x {j} = {i*j}")
            
def exercice33():
    i = int (input ("entrez un nombre")) 
    print(table_de_multiplication_de_1_a_10)

def nombre_pair_0_à_n(n):
    for i in range (0,n+1,2):
        print(i)
def exercice34():
    n = int (input ("entrez un nombre"))
    print(nombre_pair_0_à_n(n))
        
def carré_parfait_n(n):
    for i in range (1,n+1):
        print(i**2)
def exercice35():
    n = int (input ("entrez un nombre"))
    print(carré_parfait_n(n))
    
def repeter_mot_n_fois(mot,n):
    for i in range (n):
        print (mot)           
def exercice36():
    mot = str (input ("entrez un mot"))
    n = int (input ("entrez un nombre"))
    print(repeter_mot_n_fois(mot,n))
    
def pyramide_étoiles(n):
    for i in range (1,n+1):
        print('*' * i)
def exercice37():
    n = int (input ("entrez un nombre"))
    print(pyramide_étoiles(n))            
    
def calculatrice_simple():
    a = float (input ("entrez un nombre"))
    b = float (input ("entrez un autre nombre"))
    operateur = input ("entrez un opérateur (+,-,*,/)")
    if operateur == "+":
        return addition (a,b)
    elif operateur == "-":
        return soustraction (a,b)
    elif operateur == "*":
        return multiplication (a,b)
    elif operateur =="/":
        return division (a,b)
     
def exercice38():
    print(calculatrice_simple())
 
def deviner_pair_ou_impair():
    nombre = int (input ("entrez un nombre"))
    if nombre % 2 == 0:
        return "pair"
    else :
        return "impair"
def exercice39():
    print(deviner_pair_ou_impair())
    
def verifier_mot_de_passe_6caracteres(mot_de_passe):
     if len(mot_de_passe) >= 6:
          return True
     else:
          return False
def exercice40():
     mot_de_passe = input ("entrez un mot de passe")
     if verifier_mot_de_passe_6caracteres(mot_de_passe):
         print("mot de passe valide")
     else :
         print("mot de passe invalide , il doit contenir au moin 6 caractères")
         
    
def main(): 
    # Demande à l'utilisateur quel exercice exécuter 
    choix = input("Entrez le numéro de l'exercice à exécuter : ") 
    if choix == "0": 
        exercice0() 
    elif choix == "1": 
        exercice1()
    elif choix == "2": 
        exercice2()
    elif choix == "3":
        exercice3()
    elif choix == "4":
        exercice4()
    elif choix == "5":
        exercice5()
    elif choix == "6":
        exercice6()
    elif choix == "7":
        exercice7()
    elif choix == "8":
        exercice8()
    elif choix == "9":
        exercice9()
    elif choix == "10":
        exercice10()
    elif choix == "11":
        exercice11()    
    elif choix == "12":
        exercice12()
    elif choix == "13":
        exercice13()      
    elif choix == "14":
        exercice14()
    elif choix == "15":
        exercice15()
    elif choix == "17":
        exercice17()
    elif choix =="18":
        exercice18()
    elif choix =="19":
        exercice19()    
    elif choix =="20":
        exercice20()
    elif choix =="21":
        exercice21()
    elif choix =="22":
        exercice22()        
    elif choix =="23":
        exercice23()
    elif choix =="24":
        exercice24()    
    elif choix =="25":
        exercice25()  
    elif choix =="26":
        exercice26()
    elif choix =="27":
        exercice27()  
    elif choix == "28":
        exercice28()   
    elif choix == "28":
        exercice28()   
    elif choix == "29":
        exercice29()
    elif choix == "30":
        exercice30()
    elif choix == "31":
        exercice31()    
    elif choix == "32":
        exercice32()  
    elif choix == "33":
        exercice33()
    elif choix == "34":
        exercice34()   
    elif choix == "35":
        exercice35() 
    elif choix == "36":
        exercice36()        
    elif choix == "37":
        exercice37()
    elif choix == "38":
        exercice38()
    elif choix == "39":
        exercice39()
    elif choix == "40":
        exercice40()
    else: 
        print("Exercice non reconnu.") 
if __name__ == "__main__": 
    main()