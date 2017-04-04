class Email:
    def __init__(self, ID_mail, text, date, expediteurs, destinataires, tokenise = None):
        self.ID_mail = ID_mail,
        self.text = text,
        self.date = date,
        self.destinataires = destinataires
        self.expediteurs = expediteurs
        self.tokenise = None