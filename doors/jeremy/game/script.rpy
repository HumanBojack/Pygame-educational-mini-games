# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.




define m = Character('Moi', color="#c8ffc8")
define j = Character('Jérémy', color="#c8ffc8")


# Le jeu commence ici
label start:


    # play music "rock.opus"
    show screen test

    scene tableau

    m "Bonjour, je souhaiterai devenir développeur en intelligence articielle..."

    show jeremy at right
    with dissolve
    
    j "Voici des questions sur les bases de données"
    

    menu:
        j "Question 1: Reqûete SQL "
        "Réponse A : La réponse A":
            jump r1a
        "Réponse B : La réponse B":
            jump r1b

label r1a:
    j "Bonne réponse !"

    call screen livre

    scene black
    with dissolve
    return

label r1b:
    j "Mauvaise réponse !"

    scene black
    with dissolve
    return
