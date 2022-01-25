# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.




define m = Character('Moi', color="#c8ffc8")
define s = Character('Safia', color="#c8ffc8")


# Le jeu commence ici
label start:


    # play music "rock.opus"
    show screen test

    scene simplon

    m "Bonjour, je souhaiterai devenir développeur en intelligence articielle..."

    show safia at right
    with dissolve
    
    s "Bonjour, tu es au bon endroit ! Bienvenue dans le campus Simplon !"
    s "Je suis Safia et je suis en charge de trouver de nouveaux apprenants en dév IA"
    s "Je serai en charge de ton accompagnement professionnel"
    s "Mais avant cela, il me faut savoir si tu es capable de répondre à ces quelques questions..."

    menu:
        s "Question 1: Qu'est-ce qu'un développeur en intelligence articielle ?"
        "Réponse A : La réponse A":
            jump r1a
        "Réponse B : La réponse B":
            jump r1b

label r1a:
    s "Bonne réponse !"

    call screen livre

    scene black
    with dissolve
    return

label r1b:
    s "Mauvaise réponse !"

    scene black
    with dissolve
    return
