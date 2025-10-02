

def  exercice0(): 
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
                     
    else: 
        print("Exercice non reconnu.") 
if __name__ == "__main__": 
    main()