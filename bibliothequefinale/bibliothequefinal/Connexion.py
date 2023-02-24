from distutils.cmd import Command              # c'est des bibliotheque qu'on a importer pour pouvoir bosser avec 
                                               #pour pouvoir importer ces bibiotheques on utilise pip install dns l'invite de commande
from logging import root 
from tkinter import *    #pour importer la bibliotheque tkinter
  
from tkinter import ttk, messagebox #pour les messages derreur
import pymysql #c'est une bibliothèque python qui permet d'interagir avec une base de données
from subprocess import call #bibliotheque pour changer de page
import hashlib # Pour faire le hashage de mot de passe 

class PagedeConnexion:  #classe formulaire 
    def __init__(self,root): #self représente l'instance de la classe. En utilisant le mot clé " self " nous pouvons accéder aux attributs et méthodes de la classe en python. 
        self.PagedeConnexion = root  
        self.PagedeConnexion.title("Connexion") #titre en haut de la page
        self.PagedeConnexion.geometry("1040x560+400+200")  #taille de page
        
        self.PagedeConnexion.resizable(width=False, height=False) #pour que le bouton agrandir ne puisse pas marcher
        self.PagedeConnexion.iconbitmap("Images/bib.ico")  #a modifier importer l'icone de l'application
        
         
        #champs du formulaire
        PaneauOrangeDuHaut = Frame(self.PagedeConnexion, bg="#ff7f00") #Frame est un conteneur qui permets de gérer des widgets paneau orange du haut 
        PaneauOrangeDuHaut.place(x=0, y=-30, width=1100, height=150) #largeur longeur taille du panneau

        self.ImageDelaPageConnexion = PhotoImage(file="Images/bibliotheque.png") # logo a gauche des livres 
        self.BoutonPourRecupererLimage = Label(root, text="",compound=LEFT,image=self.ImageDelaPageConnexion, width=500, height=320, font="arial 12 bold") 
        #Compound si on souhaite que l’étiquette affiche à la fois un texte et un graphique (soit un bitmap, soit une image) 
        self.BoutonPourRecupererLimage.place(x=0,y=119) #Pour gerer l'emplacement du logo

       

        PanneauGrisDuMilieu = Frame(self.PagedeConnexion, bg="#ff7f00") #Frame est Un cadre est simplement un conteneur pour d’autre widgets.
        PanneauGrisDuMilieu.place(x=650, y=160, width=350, height=240) 

        PaneauOrangeDuBas = Frame(self.PagedeConnexion, bg="#ff7f00") #Frame est Un cadre est simplement un conteneur pour d’autre widgets.
        PaneauOrangeDuBas.place(x=0, y=435, width=1100, height=190) 

       


        #les titres
        titrepourBibYasoPourLesLecteurs = Label(PaneauOrangeDuHaut, text=" BibYaso Pour Les Lecteurs !", font =("algarian", 30,"bold"), bg="#ff7f00", fg="black")
        titrepourBibYasoPourLesLecteurs.place(x=260, y=60) 

        titrepourByYassineSofiane = Label(PaneauOrangeDuBas, text="By Yassine Sofiane ", font =("Times New Roman", 15,"italic"), bg="#ff7f00", fg="black")
        titrepourByYassineSofiane.place(x=460, y=45)
  
        titreSidentifier =  Label(PanneauGrisDuMilieu, text="S'identifier", font =("Times New Roman", 15,"bold"), bg="#ff7f00", fg="black")
        titreSidentifier.place(x=148, y=16)

        titreEmail = Label(PanneauGrisDuMilieu, text="E-mail:", font =("Times New Roman", 12,"bold",), bg="#ff7f00", fg="black")
        titreEmail.place(x=10, y=80)
        
        titreMotdepasse = Label(PanneauGrisDuMilieu, text="Mot de passe:", font =("Times New Roman", 12,"bold"), bg="#ff7f00", fg="black")
        titreMotdepasse.place(x=10, y=120)
        
        
        #Entry c'est un champs de saisie en français
        self.emailDeLaPageConnexion= Entry(PanneauGrisDuMilieu, font= (5), bg="white") 
        self.emailDeLaPageConnexion.place(x=150, y=80,width=150)


        self.motdepasseDeLaPageConnexion= Entry(PanneauGrisDuMilieu, show="*",font= (5), bg="white")  # show="*" pour cacher le mot de passe
        self.motdepasseDeLaPageConnexion.place(x=150, y=120,width=150) # Pour gerer l'emplacement du champs de saisie mot de passe
       

        

        #Bouton Cree un compte
        BoutonCreeuncompte = Button(PaneauOrangeDuHaut, text="Créer un compte",command=self.PageCreationDeCompte, cursor="hand2", font=("times new roman",12,"bold"), bd=0,bg="#474338",fg="white")
        BoutonCreeuncompte.place(x=880, y=100) 
        #command=self.creeuncompte est utilisé pour récuperer la fonction creeuncompte qu'on a declarer en bas 

        #Bouton mot de passe 
        BoutonMotdepasseoublie = Button(PanneauGrisDuMilieu, text=" Vous avez oublié votre mot de passe ?", command=self.CliquerMotdepasseOublie, cursor="hand2", font=("times new roman",11), bd=0,bg="#ff7f00",fg="black")
        BoutonMotdepasseoublie.place(x=9, y=170)
        #command=self.motdepasseoublie est utilisé pour recuperer la fonction mot de passe oublie qu'on a declarer en bas

        
        #bouton connexion
        BoutonConnexion = Button(PanneauGrisDuMilieu, text="Se connecter",command=self.CliquerBoutonConnexion, cursor="hand2", font=("times new roman",12,"bold"), bd=0,bg="#474338",fg="white")
        BoutonConnexion.place(x=250, y=170) 
        #command=self.connexion est utilisé pour recuperer la fonction pour recuperer le self.connexion qu'on a declarer en bas
    
    """
    def effacerchampssaisieconnexion(self): #on declare une fonction pour effacer champs de saisie apres une connexion
        self.txt_email.delete(0, END) #efface le champs de saisie email
        self.txt_motdepasse.delete(0, END) #efface le champs de saisie mot de passe
    """
    
    def CliquerBoutonConnexion(self): #fonction Connexion qui prendra pour parametre self
        if self.emailDeLaPageConnexion.get()=="" or self.emailDeLaPageConnexion.get()=="":  #si le champs de saisie mail est égal à null et si le champ de saisie mot de passe est égal à null  
           messagebox.showerror("Erreur", "Veuillez saisir un email et un mot de passe", parent=self.PagedeConnexion) # si les champs ne sont pas rempli alors affiche une message pour dire "Veuillez Saisir Email Mot depasse"
        else: #sinon
           try:
                con = pymysql.connect(host="localhost", user="root",password="", database="bddcomptes")
                cur = con.cursor()
                cur.execute("select * from utilisateur where emailUtilisateur=%s and motdepasseUtilisateur=%s", (self.emailDeLaPageConnexion.get(), self.motdepasseDeLaPageConnexion.get()))  #.get recuperer les informations saisie
                row = cur.fetchone()
                if row == None:
                   messagebox.showerror("Erreur", "Votre e-mail ou le mot de passe est incorrect ", parent=self.PagedeConnexion)
                   #self.effacerchampssaisieconnexion()
                else: #alors 
                   messagebox.showinfo("Succes", "Bienvenue") #affiche un message box Bienvenue
                   #self.effacerchampssaisieconnexion() #Appel la fonction effacerchampssaisieconnexion pour supprimer les champs de saisie 
                   self.OuvrirLaPageGestionLivres()
                   con.close()
                
           except Exception as ex:
               messagebox.showerror("Erreur", f"erreur de connexion{str(ex)}", parent=self.PagedeConnexion)
    
    
    def CliquerMotdepasseOublie(self): #fonction mot de passe oublié
        if self.emailDeLaPageConnexion.get()=="": #si le champs email est null alors
            messagebox.showerror("erreur", "Veuillez donner un e-mail et un mot de passe valide", parent=self.PagedeConnexion)#on affiche un message d'erreur pour donner un mail valide
        else:
            try:
                con = pymysql.connect(host="localhost", user="root",password="", database="bddcomptes") #connexion à la base de donnes 
                cur = con.cursor()
                cur.execute("select * from utilisateur where emailUtilisateur=%s ", self.emailDeLaPageConnexion.get()) #.get recuperer les informations saisie
                row = cur.fetchone()
                if row == None: #si les champs ne corresponde pas a ceux dans la base de données alors 
                    messagebox.showerror("Erreur", "Votre e-mail ou mot de passe est incorrecte ", parent=self.PagedeConnexion) # Alors affiche un messagebox pour dire que le message et le password sont invalide   
                else:
                    con.close() 


                    #Page Mot de passe Oublié
                    self.PageDeMotdepasseOublie= Toplevel() #Fenetre Mere
                    self.PageDeMotdepasseOublie.title("Mot de passe oublie") #titre de mot de passe oublie
                    self.PageDeMotdepasseOublie.config(bg="#ff6600") #couleur du background 
                    self.PageDeMotdepasseOublie.geometry("350x350+800+300") #taille de l'application
                    self.PageDeMotdepasseOublie.grab_set() #eviter de toucher au autre page 
                    self.PageDeMotdepasseOublie.resizable(width=False, height=False) #Eviter d'aggrandir la PageDeMotdepasseOublie
                    self.PageDeMotdepasseOublie.iconbitmap("Images/bib.ico") 

                    #titres
                    titreMotdepasseOublieDelaPageMotdepasseOublie = Label(self.PageDeMotdepasseOublie, text= "Rénitialisez votre mot de passe", font =("Arial", 12,"bold"), fg="black")
                    titreMotdepasseOublieDelaPageMotdepasseOublie.place(x=93, y=20) 
                    

                    titreSelectionnezunequestionDelaPageMotdepasseOublie = Label(self.PageDeMotdepasseOublie, text="Séléctionnez une question", font =("Arial", 10,"bold"), fg="black")
                    titreSelectionnezunequestionDelaPageMotdepasseOublie.place(x=10, y =70)

                    #liste questions
                    self.questionDeLaPageMotDepasseOublie = ttk.Combobox(self.PageDeMotdepasseOublie, font=("times new roman", 15), state="readonly")
                    self.questionDeLaPageMotDepasseOublie["values"]=("Select", "Prénom", "Lieu de naissance", "Meilleur ami", "Film préféré") 
                    self.questionDeLaPageMotDepasseOublie.place(x=10, y=100, width=110)
                    self.questionDeLaPageMotDepasseOublie.current(0)# combox pour récuperer les champs prenom lieu de naissance   

                    repondreDelaPageMotdepasseOublie = Label(self.PageDeMotdepasseOublie, text="Répondre", font =("Arial", 10,"bold"), fg="black")
                    repondreDelaPageMotdepasseOublie.place(x=10, y =150)

                     # Label mot de passe
                    nouveaumotdepasseDelaPageMotdepasseOublie = Label(self.PageDeMotdepasseOublie, text="Nouveau Mot de passe", font =("Arial", 10,"bold"), fg="black")
                    nouveaumotdepasseDelaPageMotdepasseOublie.place(x=10, y =230)

                    
                    self.nouveaumotdepasseDelaPageMotdepasseOublie = Entry(self.PageDeMotdepasseOublie,show="*", font=(5), bg="white")
                    self.nouveaumotdepasseDelaPageMotdepasseOublie.place(x=10, y =270)
                    #show="*" permet de rendre le mot de passe invisible 

                    self.titreRepondreDelaPageMotdepasseOublie = Entry(self.PageDeMotdepasseOublie, font= (5), bg="white")
                    self.titreRepondreDelaPageMotdepasseOublie.place(x=10, y =190)
                    #label pour répondre     
                    
                    
                    #bouton pour modifier mot de passe
                    BoutonMotdePasseOublieDeLaPageMotDepasseOublie = Button(self.PageDeMotdepasseOublie, text="Modifier",command=self.MotdePasseOublie,cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
                    BoutonMotdePasseOublieDeLaPageMotDepasseOublie.place(x=150, y=320)

                    #self.password_oublie pour récuperer la variable qu'on a creer en haut 
                    
            except Exception as ex:
                 messagebox.showerror("Erreur", f"erreur de connexion{str(ex)}", parent=self.CliquerBoutonCreeuncompte)


    
    
    #Fonction de mot de passe oublié
    def MotdePasseOublie(self):
        if self.questionUtilisateur.get()=="" or self.questionDeLaPageMotDepasseOublie.get()=="" or self.nouveaumotdepasseDelaPageMotdepasseOublie()=="": #si les champs ne sont pas rempli
            messagebox.showerror("Erreur","Veuillez remplir tous les champs",parent=self.PageDeMotdepasseOublie) #alors affiche un message box pour dire remplir tout les champs
        else:
            try:
                con = pymysql.connect(host="localhost", user="root",password="", database="bddcomptes")
                cur = con.cursor()
                cur.execute("select * from utilisateur where emailUtilisateur=%s and questionUtilisateur=%s and reponseUtilisateur=%s",( self.emailDeLaPageConnexion.get(), self.questionDeLaPageMotDepasseOublie.get(), self.repondreunequestion_entry.get()))
                row= cur.fetchone()

                if row == None: #si cest faux alors affiche message box  
                   messagebox.showerror("Erreur", "Vous n'avez pas bien répondu a la question séléctionnez",parent= self.PageDeMotdepasseOublie)
                
                else:  # si cest correct alors
                    cur.execute("update utilisateur set motdepasseUtilisateur=%s where emailUtilisateur=%s",(self.nouveaumotdepasseDelaPageMotdepasseOublie.get(),self.emailDeLaPageConnexion.get()))
                    con.commit()
                    con.close() # pour fermer la base de donnes
                    
                    messagebox.showinfo("Success","Vous avez modifier votre mot de passe", parent=self.PageDeMotdepasseOublie)
                    self.effacerchampssaisie() #pour affacer les champs de saisie
            
            except Exception as es :
                messagebox.showerror("erreur",f"Erreur de connexion{str(es)}", parent=self.PageDeMotdepasseOublie)#    
            #On utilise Except pour eviter les erreurs
    
    
    #Fonction de la page de de création de compte
    def PageCreationDeCompte(self): 
                
                    self.PageCreationDeCompte= Toplevel() #Page mere,  Toplevel()-----> fenetre fille 
                    self.PageCreationDeCompte.title("Crée un compte") #Titre de la page
                    self.PageCreationDeCompte.config(bg="#ff7f00") #Couleur de la page 
                    self.PageCreationDeCompte.geometry("400x500+750+200") #taille de la page 
                    self.PageCreationDeCompte.resizable(width=False, height=False) #pour que le bouton agrandir ne puisse pas marcher  
                    self.PageCreationDeCompte.grab_set() #Grab_set our eviter de cliquer sur d'autre page tout en ettant sur la principal
                    self.PageCreationDeCompte.iconbitmap("Images/bib.ico") 
                    

                    #Titres
                    titreDeLaPageCreeunCompte = Label(self.PageCreationDeCompte, text="Créer votre compte BibYaso", font =("Arial", 12,"bold"), fg="black")
                    titreDeLaPageCreeunCompte.place(x=100, y=20)

                    titreNom = Label(self.PageCreationDeCompte, text=" Nom : ", font =("algarian", 11,), bg="#ff7f00", fg="black")
                    titreNom.place(x=10, y=80)
                    
                    titrePrenom = Label(self.PageCreationDeCompte, text=" Prénom : ", font =("algarian", 11,), bg="#ff7f00", fg="black")
                    titrePrenom.place(x=10, y=120)

                    titreEmail = Label(self.PageCreationDeCompte, text=" Email : ", font =("algarian", 11,), bg="#ff7f00", fg="black")
                    titreEmail.place(x=10, y=160)

                    titreTelephone = Label(self.PageCreationDeCompte, text=" Téléphone : ", font =("algarian", 11,), bg="#ff7f00", fg="black")
                    titreTelephone.place(x=10, y=200)
                    
                    titreSelectionnezUnequestion = Label(self.PageCreationDeCompte, text=" Séléctionnez une question : ", font =("algarian", 11,), bg="#ff7f00", fg="black")
                    titreSelectionnezUnequestion.place(x=10, y=240)

                    titreRepondre = Label(self.PageCreationDeCompte, text=" Répondre : ", font =("algarian", 11,), bg="#ff7f00", fg="black")
                    titreRepondre.place(x=10, y=280)
                    
                    TitreMotdepasse = Label(self.PageCreationDeCompte, text=" Mot de passe : ", font =("algarian", 11,), bg="#ff7f00", fg="black")
                    TitreMotdepasse.place(x=10, y=320)

                    titreConfirmeeMotdepasse = Label(self.PageCreationDeCompte, text=" Confirmée mot de passe : ", font =("algarian", 11,), bg="#ff7f00", fg="black")
                    titreConfirmeeMotdepasse.place(x=10, y=360)

                    
                    
                    
                    #Champs de saisie
                    self.nomUtilisateur= Entry(self.PageCreationDeCompte, font= (5), bg="white")
                    self.nomUtilisateur.place(x=190, y=80,width=150)

                    self.prenomUtilisateur= Entry(self.PageCreationDeCompte, font= (5), bg="white")
                    self.prenomUtilisateur.place(x=190, y=120,width=150)

                    self.emailUtilisateur= Entry(self.PageCreationDeCompte, font= (5), bg="white")
                    self.emailUtilisateur.place(x=190, y=160,width=150)
                    
                    self.telephoneUtilisateur= Entry(self.PageCreationDeCompte, font= (5), bg="white")
                    self.telephoneUtilisateur.place(x=190, y=200,width=150)

                    
                    self.reponseUtilisateur= Entry(self.PageCreationDeCompte, font= (5), bg="white")
                    self.reponseUtilisateur.place(x=190, y=280,width=150)

                    self.motdepasseUtilisateur= Entry(self.PageCreationDeCompte, show="*",font= (5), bg="white")
                    self.motdepasseUtilisateur.place(x=190, y=320,width=150)

                    self.confirmemotdepasseUtilisateur= Entry(self.PageCreationDeCompte, show="*",font= (5), bg="white")
                    self.confirmemotdepasseUtilisateur.place(x=190, y=360,width=150)


                    #Liste combobox
                    self.questionUtilisateur = ttk.Combobox(self.PageCreationDeCompte, font=("times new roman", 15), state="readonly")
                    self.questionUtilisateur["values"]=("Prénom", "Lieu de naissance", "Meilleur ami", "Film préféré") 
                    self.questionUtilisateur.place(x=190, y=240,width=150)
                    self.questionUtilisateur.current(0)

                    

                    self.BoutonBoutonPourAccepterLesConditions = IntVar() #On déclare la variable BoutonBoutonPourAccepterLesConditions pour ensuite la récuperer en bas
                     
                    BoutonPourAccepterLesConditions = Checkbutton(self.PageCreationDeCompte, variable=self.BoutonBoutonPourAccepterLesConditions, onvalue=1, offvalue=0 , text="J'accepte les conditions et les termes", font=("times new roman",12), bg="white").place(x=10, y=400)
                    #On Recupere la varibale BoutonBoutonPourAccepterLesConditions
                    
                    BoutonSuivant = Button(self.PageCreationDeCompte, text="Suivant",command=self.CliquerBoutonCreeuncompte,cursor="hand2", font=("times new roman",12,"bold"), bd=0,bg="#474338",fg="white")
                    BoutonSuivant.place(x=270, y=440)
                    #Bouton creation de compte qui prend comme parametre command de la fonction self.CliquerBoutonCreeuncompte qu'on à declarer juste en bas 
       
                  
    
    #Fonction pour cree un compte
    def CliquerBoutonCreeuncompte(self):  
        if self.nomUtilisateur.get()=="" or self.prenomUtilisateur.get()=="" or self.emailUtilisateur.get()=="" or self.telephoneUtilisateur.get()=="" or self.questionUtilisateur.get()=="" or self.reponseUtilisateur.get()=="" or  self.telephoneUtilisateur.get()=="" or self.motdepasseUtilisateur.get()=="" or self.confirmemotdepasseUtilisateur.get()=="":
         messagebox.showerror("Erreur", "Veuillez remplir tous les champs", parent=self.PageCreationDeCompte) #si tout les champs ne sont pas rempli alors affiche un message box pour dire que les champs ne sont pas rempli 
        elif self.motdepasseUtilisateur.get()!= self.confirmemotdepasseUtilisateur.get():#si les mots de passe ne sont pas pareils
         messagebox.showerror("Erreur", "les mots de passe ne sont pas conforme", parent=self.PageCreationDeCompte) #alors affiche un message box en disant que ses mots de passe ne sont pas pareils
        elif self.BoutonBoutonPourAccepterLesConditions.get()==0: #si le champ conditions n'est pas rempli 
         messagebox.showerror("Erreur","Veuillez accepter les conditions", parent=self.PageCreationDeCompte)#alors affiche un message box pour accepter les conditions

        else:
            try:
                con= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes") #pour faire la connexion à la base de données
                cur=con.cursor()
                cur.execute("select * from utilisateur where emailUtilisateur=%s",self.emailUtilisateur.get()) # récuperer la table mail dans la base de données
                row= cur.fetchone()  #La méthode fetchone() récupère ensuite la première ligne de ce résultat.

                if row != None: #si se qu'on a rentrer se trouve  dans la base de données alors 
                    messagebox.showerror("Erreur", "Ce mail existe déja", parent=self.PageCreationDeCompte) #alors affiche un message box pour dire que ce mail existe déja dans la base de donnés
                else:
                   cur.execute("insert into utilisateur (nomUtilisateur, prenomUtilisateur, emailUtilisateur, telephoneUtilisateur, questionUtilisateur,reponseUtilisateur,motdepasseUtilisateur,confirmemotdepasseUtilisateur) values (%s,%s,%s,%s,%s,%s,%s,%s)",#on insere dans la base de donnes les champs prenom, email,telephone, question,reponse,password
                   (
                       self.nomUtilisateur.get(),
                       self.prenomUtilisateur.get(),
                       self.emailUtilisateur.get(),
                       self.telephoneUtilisateur.get(),
                       self.questionUtilisateur.get(),
                       self.reponseUtilisateur.get(),
                       self.motdepasseUtilisateur.get(),
                       self.confirmemotdepasseUtilisateur.get(),
                    ))

                   messagebox.showinfo("Succes","Votre compte a été créé avec succès", parent=self.PageCreationDeCompte) #On affiche un message box pour dire que le compte à bien été crée
                   self.EffacerChampsdeSaisiedelaPageCreationdecompte()#Fonction pour effacer les champs de saisie apres avoir creer un compte  
                
                con.commit()
                con.close

            except Exception as es :
                messagebox.showerror("erreur",f"Erreur de connexion{str(es)}",parent=self.PageCreationDeCompte) 
    
    
    #Fonction pour effacer les champs de saisie apres la création de compte

    def EffacerChampsdeSaisiedelaPageCreationdecompte(self): #Fonction pour effacer les champs de saisie de la page creation de compte
        self.nomUtilisateur.delete(0, END) #efface le champs de saisie creeuncompte
        self.prenomUtilisateur.delete(0, END) #efface le champs de saisie prenom
        self.emailUtilisateur.delete(0, END) #efface le champs de saisie email
        self.telephoneUtilisateur.delete(0, END) #efface le champs de saisie telephone
        self.questionUtilisateur.delete(0, END) #efface le champs de saisie question
        self.reponseUtilisateur.delete(0, END) #efface le champs de saisie repondre a une question
        self.motdepasseUtilisateur.delete(0, END) #efface le champs de saisie mot de passe
        self.confirmemotdepasseUtilisateur.delete(0, END) #efface le champs de saisie confirmee mot de passe
        

    #Fonction pour ouvrir la page Gestionlivres    
    def OuvrirLaPageGestionLivres(self): #On declare une fonction pour ouvrir la page gestion livres
        self.PagedeConnexion.destroy() #Pour fermer la page dans la quelle on se trouve 
        call(["python", "gestionlivres.py"])# et avec le call on ouvre la page dans la quelle on souhaite aller
        
root =Tk() 
obj = PagedeConnexion(root) 
root.mainloop() #est une méthode sur la fenêtre principale que nous exécutons lorsque nous voulons exécuter notre application 