import time
import os

print(f"{' ANALYSE PASSWORD ':-^35}\n")

user = input("User : ")

def check_length(password):

    if len(str(password)) > 8:
        return True

def check_uppercase(password):

    for caractére in password:

        if caractére.isupper():
            return True

    return False 
    
def check_digit(password):

    for caractére in password:

        if caractére.isdigit():
            return True

    return False

def check_special_char(password):
    
    speciaux = "!@#$%^&*"

    for caractére in password:

        if caractére in speciaux:
            return True

    return False 

def check_espace(password):

    if password.spilt(' '):
        return True

def evaluate_password(password):

    counter = 0

    if check_length(password) == True:
        counter += 1

    if check_uppercase(password) == True:
        counter += 1

    if check_digit(password) == True:
        counter += 1

    if check_special_char(password) == True:
        counter += 1

    if counter == 1:
        print(f"{user} your password is Faible\n")

    if counter == 2:
        print(f"{user} your password is Faible\n")

    if counter == 3:
        print(f"{user} your password is Moyen\n")
    
    if counter == 4:
        print(f"{user} your password is Fort\n")

def evaluate_password_premium(password):

    counter = 0

    print("\nVerification en cours...\n")
    time.sleep(1)
    
    if check_length(password) == True:
        counter += 1

    if check_uppercase(password) == True:
        counter += 1

    if check_digit(password) == True:
        counter += 1

    if check_special_char(password) == True:
        counter += 1
    
    if check_espace(password) == True:
        counter += 1

    courente_password = ["123456", "password", "azerty"]

    if password in courente_password:
        if counter == 0:
            pass
        else:
            counter -= 1

    if counter == 1:
        for i in range(0,11):
            c = int(i)
            print(f"\rChargement du resultat : [{'█' * c}]\n", end="", flush=True)
            time.sleep(0.9)
            os.system('clear')
            
        print(f"{user} your password is Faible")

    if counter == 2:
        for i in range(0,11):
            c = int(i)
            print(f"\rChargement du resultat : [{'█' * c}]\n", end="", flush=True)
            time.sleep(0.9)
            os.system('clear')

        print(f"{user} your password is Faible")

    if counter == 3:
        for i in range(0,11):
            c = int(i)
            print(f"\rChargement du resultat : [{'█' * c}]\n", end="", flush=True)
            time.sleep(0.9)
            os.system('clear')

        print(f"{user} your password is Moyen")
    
    if counter == 4 or counter == 5:
        for i in range(0,11):
            c = int(i)
            print(f"\rChargement du resultat : [{'█' * c}]\n", end="", flush=True)
            time.sleep(0.9)
            os.system('clear')

        print(f"\n{user} your password is Fort")

    print("Fin de L'analyse !\n")

systeme_actif = True

while systeme_actif:
    
    choix = input("Entrez un mot de passe (ou 'quitter') : ")

    if choix == "quitter":
        systeme_actif = False
        print(f"{' Arrêt du système '.upper():-^35}")
    elif choix == 'bacprociel Okai5@':
        print("\nLancement de l'analyse premium")
        password = input('Password : ')
        evaluate_password_premium(password)
    else:
        print("\nAnalyse en cours...\n")
        evaluate_password(choix)
