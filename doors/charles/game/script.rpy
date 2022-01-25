# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.




define m = Character('Moi', color="#c8ffc8")
define c = Character('Charles', color="#c8ffc8")


# Le jeu commence ici
label start:


    # play music "rock.opus"
    show screen test

    scene computers

    m "Bonjour, je souhaiterai devenir développeur en intelligence articielle..."

    show charles at right
    with dissolve
    
    c "Voici des questions sur python"
    

    menu:
        c "Question 1: Qu'est-ce qu'une variable ?"
        "Réponse A : La réponse A":
            jump r1a
        "Réponse B : La réponse B":
            jump r1b

label r1a:
    c "Bonne réponse !"

    call screen livre

    scene black
    with dissolve
    return

label r1b:
    c "Mauvaise réponse !"

    scene black
    with dissolve
    return
