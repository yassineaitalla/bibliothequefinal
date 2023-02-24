from ast import excepthandler
from cProfile import label
from distutils.cmd import Command
from email.mime import image
from logging import root
import operator 
from re import L      
from tkinter import * # pour importer la bibliotheque tkinter
from subprocess import call #permet dimporter le call pour ouvrir les fenetre
from tkinter import ttk, messagebox #importer des messages box  
from turtle import bgcolor, title #
 #permetre de gerer les selcetions et les message derrueeur  afficher ou de securite
import pymysql #pour récuperer la bibliotheque de la base de donnée
  
                    
class gestionlivres:  #classe formulaire
    def __init__(self,root):                   
        self.Pagegestionlivres = root  
        self.Pagegestionlivres.title("Gestionlivres")#Titre de l'application gestion livres
        self.Pagegestionlivres.geometry("1040x560+400+200")#Taille de notre Application    

        self.Pagegestionlivres.resizable(width=False, height=False) #eviter d'agrandir la fenetre  
        self.Pagegestionlivres.iconbitmap("Images/bib.ico") #Icone de l'application 


        #Déclarer des variables pour ensuite les récuperer
        self.id = StringVar()
        self.titre = StringVar()
        self.auteurs = StringVar()
        self.collections = StringVar()
        self.Etat = StringVar()
        self.recherche_par= StringVar()
        self.recherche = StringVar()



        self.Paneauvertdegestionlivres = Frame(self.Pagegestionlivres, bg="#bedb0d") 
        self.Paneauvertdegestionlivres.place(x=190, y=0, width=1100, height=1000)

        self.Paneauorangedegestionlivres = Frame(self.Pagegestionlivres, bg="#ff7f00")
        self.Paneauorangedegestionlivres.place(x=0, y=0, width=190, height=1000)

        self.ImageGestionLivresDeLaPageGestionlivres = PhotoImage(file="Images/Gestionlivre.png")
        self.BoutonGestionLivresDeLaPageGestionlivres = Button(self.Pagegestionlivres, text="",compound=LEFT,image=self.ImageGestionLivresDeLaPageGestionlivres, width=184,height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonGestionLivresDeLaPageGestionlivres.place(x=0 , y=0) 
        # Si vous souhaitez que l’étique affiche à la fois un texte et un graphique (soit un bitmap, soit une image),
        # cette option sert à préciser l’orientation relative de l’image par rapport au texte. Les valeur peuvent-être 'left', 'right', 'center', 'bottom' ou 'top'.

        self.ImageAdherentDeLaPageGestionlivres = PhotoImage(file="Images/Adherents.png")
        self.BoutonGestionLivresDeLaPageGestionlivres = Button(self.Pagegestionlivres,command=self.VersPageAdherents, text="",compound=LEFT,image=self.ImageAdherentDeLaPageGestionlivres, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonGestionLivresDeLaPageGestionlivres.place(x=0 , y=140) 

        self.ImageGestionDesPretsDeLaPageGestionlivres = PhotoImage(file="Images/Emprunter.png")
        self.BoutonGestionDesPretsDeLaPageGestionlivres = Button(self.Pagegestionlivres,command=self.VersPageGestionDesPrets, text="",compound=LEFT,image=self.ImageGestionDesPretsDeLaPageGestionlivres, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonGestionDesPretsDeLaPageGestionlivres.place(x=0 , y=280) 

        self.ImageSeDeconnecterDeLaPageGestionlivres = PhotoImage(file="Images/Sedeconnecter.png")
        self.BoutonSeDeconnecterDeLaPageGestionlivres = Button(self.Pagegestionlivres, text="",command=self.BoutonDeconnexion,compound=LEFT,image=self.ImageSeDeconnecterDeLaPageGestionlivres, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonSeDeconnecterDeLaPageGestionlivres.place(x=0 , y=420) 
        
        
        titreGestionlivre = Label(self.Pagegestionlivres, text=" Gestion des livres ",font =("algarian", 20,"bold"), bg="#bedb0d", fg="black")
        titreGestionlivre.place(x=350, y=20,width=500)
        
        
        titreGestionlivres = Label(self.Pagegestionlivres, text="Livres", font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreGestionlivres.place(x=0, y=100,width=190)

        titreAdherents = Label(self.Pagegestionlivres, text=" Adhérents ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreAdherents.place(x=0, y=240,width=190)
        
        titreGestionprets = Label(self.Pagegestionlivres, text=" Prêts", font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreGestionprets.place(x=0, y=380,width=190)

        titreSedeconnecter = Label(self.Pagegestionlivres, text=" Se déconnecter",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreSedeconnecter.place(x=0, y=520,width=190)
        
        

        titreGestionprets = Label(self.Pagegestionlivres, text="Rechercher les livres disponible par:",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        titreGestionprets.place(x=210, y=90,width=300)

        self.rechercherlivres= Entry(self.Pagegestionlivres,textvariable=self.recherche, font= (5), bg="white")
        self.rechercherlivres.place(x=640, y=90,width=150)

        BoutonRechercherUnLivre = Button(self.Pagegestionlivres,command=self.ClickBoutonRechercher ,text=" Rechercher ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonRechercherUnLivre.place(x=830, y=90)

        BoutonActualiser = Button(self.Pagegestionlivres,command=self.actualiser, text=" Actualiser ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonActualiser.place(x=920, y=90)

        BoutonAjouterlivre = Button(self.Pagegestionlivres,command=self.BoutonAjouterUnlivre, text=" Cliquer Pour Ajouter un livre ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonAjouterlivre.place(x=215, y=500)
        
        BoutonSupprimerUnlivre = Button(self.Pagegestionlivres, command=self.SupprimerDesLivres, text=" Supprimer livre ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonSupprimerUnlivre.place(x=910, y=500)
        #cursor="hand2" pour mettre en mode cliquer sur un lien   
        

        Listepourcherchercherunlivre = ttk.Combobox(self.Pagegestionlivres,textvariable=self.recherche_par, font=("times new roman", 15), state="readonly")
        Listepourcherchercherunlivre["values"]=("titreLivre", "idAuteur", "idCollection") 
        Listepourcherchercherunlivre.place(x=510, y=90, width=110)
        Listepourcherchercherunlivre.current(0)
        #liste titres auteurs collections

        

        
       
    
        #affichage

        CadrePourTbaleauGestionlivres = Frame(self.Pagegestionlivres, bd=5,relief=GROOVE,bg="green")
        CadrePourTbaleauGestionlivres.place(x=215, y=130,width=800, height=350) 

        
        barrededefilementX= Scrollbar(CadrePourTbaleauGestionlivres,orient=HORIZONTAL)
        barrededefilemenY = Scrollbar(CadrePourTbaleauGestionlivres, orient=VERTICAL) 
        
        self.TableauGestionlivres = ttk.Treeview(CadrePourTbaleauGestionlivres,columns=("id","titre", "auteur", "collection","etat"), xscrollcommand=barrededefilementX.set, yscrollcommand=barrededefilemenY.set)
        barrededefilementX.pack(side=BOTTOM, fill=X)
        barrededefilemenY.pack(side=RIGHT, fill=Y) 
        
        self.TableauGestionlivres.heading("id", text="idLivre")
        self.TableauGestionlivres.heading("titre", text="titreLivre")
        self.TableauGestionlivres.heading("auteur", text="idAuteur")
        self.TableauGestionlivres.heading("collection", text="idCollection")

        self.TableauGestionlivres.heading("etat", text="etatLivre")

        self.TableauGestionlivres["show"]="headings"

        self.TableauGestionlivres.column("id", width=80)
        self.TableauGestionlivres.column("titre",width=80)
        self.TableauGestionlivres.column("auteur",width=80)
        self.TableauGestionlivres.column("collection",width=80)
      
        self.TableauGestionlivres.column("etat", width=80)

        self.TableauGestionlivres.pack(side=TOP, fill=X)
        self.TableauGestionlivres.pack(fill=BOTH, expand=1) #pour agrandir le tableau
        
        
        self.TableauGestionlivres.bind("<ButtonRelease-1>",self.RecupereInformation)
        self.actualiser()# Pour actualiser   
    
    
    def ClickBoutonRechercher(self):
        con= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes") # connexion a la base de donnes
        cur=con.cursor()        
        cur.execute("select * from livre where "+str(self.recherche_par.get())+" LIKE '%"+str(self.recherche.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
           self.TableauGestionlivres.delete(*self.TableauGestionlivres.get_children())
           for row in rows:
            self.TableauGestionlivres.insert('', END, values=row)
        con.commit()
        con.close()


    def VersPageAdherents(self):
        self.Pagegestionlivres.destroy()
        call(["python", "Adherents.py"]) 

    def VersPageGestionDesPrets(self):
        self.Pagegestionlivres.destroy()
        call(["python", "Gestiondesprets.py"]) 

    def BoutonAjouterUnlivre(self):
        self.Pagegestionlivres.destroy()
        call(["python", "Ajouterdeslivres.py"]) 
    
    def BoutonDeconnexion(self): #fonction deconexion pour pouvoir se deconecter qui prend pour parametre self
        lemessagebox = messagebox.askyesno("Déconnexion","Voulez-vous vous déconnecter", parent=self.Pagegestionlivres) #message box pour pouvoir se deconnecter
        if lemessagebox == YES: #si le la colonne yes a était selectionner  
         self.Pagegestionlivres.destroy() # fermer la fenetre                             
         call(["python", "Connexion.py"]) #appeler la page connexion 
         


    def actualiser(self):
        con= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes") #
        cur=con.cursor()
        cur.execute(" select * from livre ") #ligne sql pour récuperer la table ajoutlivres
        rows= cur.fetchall()
        if len(rows)!=0: 
            self.TableauGestionlivres.delete(*self.TableauGestionlivres.get_children())
            for row in rows:
                self.TableauGestionlivres.insert("", END, values=row)
        con.commit()
        con.close()

    
    def RecupereInformation(self,ev): #fonction information pour récuperer les lignes  
        cursor_row = self.TableauGestionlivres.focus()
        contents = self.TableauGestionlivres.item(cursor_row)
        row = contents["values"]
        self.id.set(row[0]),
        self.titre.set(row[1]),
        self.auteurs.set(row[2]),
        self.collections.set(row[3]),
        self.Etat.set(row[4]),

    
    def SupprimerDesLivres(self): #fonction supprimer pour supprimer des livres   
                con= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes")
                cur=con.cursor()
                cur.execute("delete from livre where titreLivre = %s", self.titre.get()) #commande delete pour supprimer une table dans la base données, self.titre.get pour récuperer le titre 
                con.commit()
                self.actualiser()
                con.close()
    

root =Tk()
obj = gestionlivres(root)
root.mainloop()

