class Email:
    def __init__(self, ID_mail, text, date, expediteurs, destinataires, tokenise = None):
        self.ID_mail = ID_mail,
        self.text = text,
        self.date = date,
        self.destinataires = destinataires
        self.expediteurs = expediteurs
        self.tokenise = None
    def print(self):
        print("ID: " + str(*self.ID_mail) + "################################")
        print(str(self.date))
        print("_____________________________")
        print(str(self.destinataires))
        print("_____________________________")
        print(str(self.expediteurs))
        print("_____________________________")
        print(str(self.text))
        print("_____________________________")
        print(str(self.tokenise))
        print("\n")