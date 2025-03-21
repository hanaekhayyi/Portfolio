import smtplib
from flask import Flask, request, render_template

app = Flask(__name__)

# Configuration du serveur SMTP
GMAIL_USER = 'hanaekhayyi7@gmail.com'  # Remplace par ton adresse Gmail
GMAIL_PASSWORD = 'H@n@E2020'  # Utilise un mot de passe d'application si 2FA est activé

@app.route('/')
def home():
    return render_template('index.html')  # Assure-toi que ce fichier existe bien

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    subject = request.form['subject']
    message = request.form['message']

    # Création du message à envoyer
    subject = f"New Contact Request: {subject}"
    body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

    # Connexion au serveur Gmail
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Démarrer la connexion sécurisée
        server.login(GMAIL_USER, GMAIL_PASSWORD)

        # Envoi de l'email
        server.sendmail(email, 'hanaekhayyi7@gmail.com', f"Subject: {subject}\n\n{body}")
        server.quit()  # Fermeture de la connexion
        return "Message sent successfully!"
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
