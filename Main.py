a = 2
b = 3
c = 4
d = 5

def  exercice1(): 
    print("Exercice 1 : Bonjour le monde !") 
    print("Hello World !") 
    
def excercice2():
    print ("Hello world !")


def exercice3():
     prenom = (input("quel est ton prénom ? "))

def exercice4():
    prenom = (input("quel est ton prénom ? "))
    print ("Bonjour " + prenom)
    print ("Bienvenue dans le monde de la programmation")
    print ("bon courage pour les études")

def exercice5():
    année_naissance = int(input("En quelle année est tu né(e) ?"))
    année_actuelle = 2025
    age = année_actuelle - année_naissance
    print ("tu as " +  str(age)+ "ans")
    
def exercice6():
    a = 2
    b = 3
    print(a+b)
    
def exercice7():
    a = 2
    b = 3
    print(a-b)
    
def exercice8():
    print(a*b)
    
def main(): 
    # Demande à l'utilisateur quel exercice exécuter 
    choix = input("Entrez le numéro de l'exercice à exécuter : ") 
    if choix == "1": 
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
    else: 
        print("Exercice non reconnu.") 
if __name__ == "__main__": 
    main()