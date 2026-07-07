import time
import os
    
print(f"\n{' ANALYSE PASSWORD ':-^35}\n")

user = input("User : ")

def check_length(password):

    if len(password) >= 8:
        return True
    
    return False

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

    if ' ' in password:
        return True
    return False

def evaluate_password(password):

    counter = 0

    if counter == 0:
        print(f"{user} your password is Very Weak")
        print("Fin de l'analyse !\n")
        return

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

def chargement():
    for i in range(0,11):
            i
            print(f"\rChargement du resultat : [{'█' * c}]\n", end="", flush=True)
            time.sleep(0.5)
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")

def evaluate_password_premium(password):

    counter = 0

    print("\nVerification en cours...\n")
    time.sleep(1)
    
    if check_length(password):
        counter += 1

    if check_uppercase(password) == True:
        counter += 1

    if check_digit(password) == True:
        counter += 1

    if check_special_char(password) == True:
        counter += 1
    
    if check_espace(password) == True:
        counter += 1

    courente_password = [
        
        "123456", "password", "123456789", 
        "12345678", "12345", "qwerty", 
        "abc123", "111111", "123123", 
        "admin", "welcome", "letmein", 
        "iloveyou", "monkey", "dragon", 
        "000000", "654321", "qwerty123", 
        "1234", "passw0rd"
                         
    ]

    if password in courente_password:
        if counter == 0:
            pass
        else:
            counter -= 1

    if counter == 0:
        chargement()
        print(f"{user} your password is Very Weak")
        print("Fin de l'analyse !\n")
        return
    
    if counter == 1:
        chargement()
        print(f"{user} your password is Faible")

    if counter == 2:
        chargement()
        print(f"{user} your password is Faible")

    if counter == 3:
        chargement()
        print(f"{user} your password is Moyen")
    
    if counter >= 4:
        chargement()
        print(f"\n{user} your password is Fort")

    print("Fin de L'analyse !\n")

systeme_actif = True

if __name__ == '__main__':

    mdp = 'bacprociel Okai5@'
    
    while systeme_actif:
        choix = input("Entrez un mot de passe (ou 'quitter') : ")

        if choix == "quitter":
            systeme_actif = False
            print(f"\n{' Arrêt du système '.upper():-^35}")
        elif choix == mdp:
            print("\nLancement de l'analyse premium")
            password = input('Password : ')
            try:
                evaluate_password_premium(password)
            except KeyboardInterrupt:
                print('Interruption Analyse !')
        else:
            print("\nAnalyse en cours...\n")
            evaluate_password(choix)
