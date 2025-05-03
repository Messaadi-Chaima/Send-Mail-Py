# coding: utf-8
import yagmail

# Adresse email et mot de passe d'application
email_user = "messaadichaimamanel@gmail.com"
app_password = "xtfm gmhx ghug ggyh"  # Remplace avec ton vrai mot de passe d'application (sans espaces)

try:
    # Créer un objet SMTP avec mot de passe direct
    yag = yagmail.SMTP(user=email_user, password=app_password)

    # Informations du mail
    destinataire = "messaadichaima21@gmail.com"
    sujet = "Le sujet de mon mail"
    message = "Bonjour ! Ceci est un test envoyé avec yagmail sans keyring."

    # Envoi
    yag.send(to=destinataire, subject=sujet, contents=message)
    print("Email envoyé avec succès !")

except Exception as e:
    print("Erreur lors de l'envoi de l'e-mail :", e)
