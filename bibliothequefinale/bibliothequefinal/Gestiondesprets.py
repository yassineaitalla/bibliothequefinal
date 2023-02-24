from tkinter import * #importer la bibliotheque tkinter
import tkinter as tk  #
from tkinter import ttk, messagebox #bibliotheque pour afficher nos message d'erreur dans l'application
from turtle import bgcolor, title #permetre de gerer les selections et les message derreur  afficher ou de securite
from tkcalendar import * #Bibliothéque pour importer les calendrier 
import pymysql #bibliotheque pour interagir avec la base de données
#import os #faire des actions diretement au niveau du systeme  
from subprocess import call   #bibliotheque pour pouvoir changer de page  


                    
class gestionprets:  # classe formulaire:
    def __init__(self,root):                   
        self.PageGestiondesprets = root #changer
        self.PageGestiondesprets.title("Gestionprets") #titre de la fenetre 
        self.PageGestiondesprets.geometry("1040x560+400+200")#pour gerer la taille de l'application
        
        self.PageGestiondesprets.resizable(width=False, height=False)#Pour eviter d'agrandir notre application
        self.PageGestiondesprets.iconbitmap("Images/bib.ico")  #pour gerer l'icone de notre application
       
        
        
        self.var_dateemprunt = StringVar()  # on declare des variables pour ensuite les recuperer
        self.var_nomdelhadherent = StringVar()  # Mémorise une chaîne de caractères; sa valeur par défaut est ''
        self.var_livre = StringVar()
        self.var_dateretour = StringVar()
        self.recherche_par = StringVar()
        self.recherche = StringVar()
        self.nomdelhadherent_list=[]
        self.livre=[]
        self.Recuperelenomdeladhereneetletitredulivre()

        
        


        self.Paneauvertdegestionlivres = Frame(self.PageGestiondesprets, bg="#bedb0d")
        self.Paneauvertdegestionlivres.place(x=190, y=0, width=1100, height=1000)

        Paneauorangedegestionlivres = Frame(self.PageGestiondesprets, bg="#ff7f00")
        Paneauorangedegestionlivres.place(x=0, y=0, width=190, height=1000)

        self.ImageGestionlivres = PhotoImage(file="Images/Gestionlivre.png")
        self.BoutonPourAllerVersGestionLivres = Button(self.PageGestiondesprets,command=self.VersGestionLivres, text="",compound=LEFT,image=self.ImageGestionlivres, width=184,height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonPourAllerVersGestionLivres.place(x=0 , y=0) 
        
        self.ImageAdherents = PhotoImage(file="Images/Adherents.png")
        self.BoutonPourAllerVersAdherents = Button(self.PageGestiondesprets,command=self.VersAdherents, text="",compound=LEFT,image=self.ImageAdherents, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonPourAllerVersAdherents.place(x=0 , y=140) 

        self.ImageGestionDesprets = PhotoImage(file="Images/Emprunter.png")
        self.BoutonPourAllerVersGestionDesprets = Button(self.PageGestiondesprets, text="",compound=LEFT,image=self.ImageGestionDesprets, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonPourAllerVersGestionDesprets.place(x=0 , y=280) 

        
        self.ImageSedeconnecter = PhotoImage(file="Images/Sedeconnecter.png")
        self.BoutonPourSedeconnecter = Button(self.PageGestiondesprets, text="",command=self.PourSeDeConnecter,compound=LEFT,image=self.ImageSedeconnecter, width=184, height=90, bg="#ff7f00",font="arial 12 bold")
        self.BoutonPourSedeconnecter.place(x=0 , y=420) 

        #Labels

        #Grandtitre
        titreGestionprets = Label(self.PageGestiondesprets, text=" Gestion Prêts ",font =("algarian", 20,"bold"), bg="#bedb0d", fg="black")
        titreGestionprets.place(x=350, y=20,width=500)
        
        titreGestionlivres = Label(self.PageGestiondesprets, text=" Livres ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreGestionlivres.place(x=0, y=100,width=190)

        titreAdherents = Label(self.PageGestiondesprets, text=" Adhérents ",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreAdherents.place(x=0, y=240,width=190)

        titreGestiondesprets = Label(self.PageGestiondesprets, text=" Prêts",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreGestiondesprets.place(x=0, y=380,width=190)

        titreSedeconnecter = Label(self.PageGestiondesprets, text=" Se déconnecter",font =("algarian", 15,"bold"), bg="#ff7f00", fg="black")
        titreSedeconnecter.place(x=0, y=520,width=190)


        titreRechercherlesemprunts= Label(self.PageGestiondesprets, text=" Rechercher les emprunts par :",font =("algarian", 12,"bold"), bg="#bedb0d", fg="black")
        
        titreRechercherlesemprunts.place(x=210, y=90,width=250)

        

        Question = ttk.Combobox(self.PageGestiondesprets,textvariable=self.recherche_par, font=("times new roman", 15), state="readonly")
        Question["values"]=("idEmprunt", "numAdherent") # on recupere le soit l'idEmprunt ou soit le numAdheren
        Question.place(x=455, y=87, width=110) #.place pour la position du ttk.combobox 
        Question.current(0)


        


        self.ChampsDesaisiePourRechercherDeslivres= Entry(self.PageGestiondesprets,textvariable=self.recherche ,font= (5), bg="white")
        self.ChampsDesaisiePourRechercherDeslivres.place(x=570, y=90,width=150)

        BoutonPourRechercherUnEmprunt = Button(self.PageGestiondesprets,command=self.ClickBoutonRechercher, text="Rechercher  ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonPourRechercherUnEmprunt.place(x=730, y=90) # command est attribuer a un bouton pour pouvoir l'executer  

        BoutonActualiser = Button(self.PageGestiondesprets,command=self.ClickBoutonActualiser, text="Actualiser ",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonActualiser.place(x=820, y=90) # command est attribuer a un bouton pour pouvoir l'executer  

        BoutonPourAjouterUnlivre = Button(self.PageGestiondesprets,command=self.PageEmprunt, text="Cliquer pour emprunter un livre",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black", )
        BoutonPourAjouterUnlivre.place(x=215, y=500)

        
        

        BoutonRetournerUnLivre = Button(self.PageGestiondesprets,command=self.RetournerUnlivre, text="Retourner un livre",cursor="hand2", font=("times new roman",11), bd=0,bg="white",fg="black")
        BoutonRetournerUnLivre.place(x=890, y=500) 
        # cursor pour mettre la main quand on clique sur le bouton 
       

       
        

        CadreDuTableauGestiondesprets = Frame(self.PageGestiondesprets, bd=5,relief=GROOVE,bg="green") #self.root pour mettre le table sur cette frame la 
        CadreDuTableauGestiondesprets.place(x=215, y=130,width=800, height=350)

        scroll_x = Scrollbar(CadreDuTableauGestiondesprets,orient=HORIZONTAL)
        scroll_y = Scrollbar(CadreDuTableauGestiondesprets, orient=VERTICAL)
        
        self.tableauGestiondesprets = ttk.Treeview(CadreDuTableauGestiondesprets,columns=("idemprunt", "numadherent", "numlivre","dateemprunt","dateretour"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y) 

        self.tableauGestiondesprets.heading("idemprunt", text="idEmprunt")
        self.tableauGestiondesprets.heading("numadherent", text="numAdherent")
        self.tableauGestiondesprets.heading("numlivre", text="numLivre")
     
        self.tableauGestiondesprets.heading("dateemprunt", text="dateEmprunt")
        self.tableauGestiondesprets.heading("dateretour", text="dateRetour")



        

        self.tableauGestiondesprets["show"]="headings"

        self.tableauGestiondesprets.column("idemprunt",  width=80)
        self.tableauGestiondesprets.column("numadherent", width=80)
        self.tableauGestiondesprets.column("numlivre", width=80)
       
        self.tableauGestiondesprets.column("dateemprunt", width=80)
        self.tableauGestiondesprets.column("dateretour", width=80)


        self.tableauGestiondesprets.pack(fill=BOTH, expand=1)
        self.tableauGestiondesprets.bind("<ButtonRelease-1>",self.information)
        self.ClickActualiser()

    def ClickBoutonActualiser(self):
        con= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes")
        cur=con.cursor()
        cur.execute("select * from emprunter ")
        rows= cur.fetchall()
        if len(rows)!=0:
            self.tableauGestiondesprets.delete(*self.tableauGestiondesprets.get_children())
            for row in rows:
                self.tableauGestiondesprets.insert("", END, values=row)
    


    
    def ClickBoutonRechercher(self):
        con= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes") # connexion a la base de donnes
        cur=con.cursor()        
        cur.execute("select * from emprunter where "+str(self.recherche_par.get())+" LIKE '%"+str(self.recherche.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!=0:
           self.tableauGestiondesprets.delete(*self.tableauGestiondesprets.get_children())
           for row in rows:
            self.tableauGestiondesprets.insert('', END, values=row)
        con.commit()
        con.close()




    def RetournerUnlivre(self): # fonction supprimerlivre qui prendra pour parametre self
                
        con= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes") # connexion a la base de donnes 
        cur=con.cursor()
        cur.execute("delete from adherent where nomAdherent = %s", self.var_nomdelhadherent.get()) #supprimer la ligne 
        cur.execute(" update livre set etatLivre = 'Disponible' where titreLivre=%s",self.var_livre.get()),
        con.commit()
        messagebox.showinfo("Succes", "Le livre à bien été rendu, Merci", parent=self.PageGestiondesprets)  
        self.ClickActualiser ()
        con.close()




    def information(self,ev):  # on recupere les informations pour ensuite les modifier ou supprimer
        cursor_row = self.tableauGestiondesprets.focus()
        contents = self.tableauGestiondesprets.item(cursor_row)
        row = contents["values"]
        
        self.var_nomdelhadherent.set(row[1]),
        
        self.var_livre.set(row[2]),
        self.var_dateemprunt.set(row[3])
        self.var_dateretour.set(row[4]),
        

    def PourSeDeConnecter(self):
        lemessagebox = messagebox.askyesno("Déconnexion","Voulez-vous vous déconnecter", parent=self.PageGestiondesprets)
        if lemessagebox == YES:
         self.PageGestiondesprets.destroy()
         call(["python", "Connexion.py"])

         
    def VersGestionLivres(self):
        self.PageGestiondesprets.destroy()
        call(["python", "Gestionlivres.py"]) 
        
    def VersAdherents(self):
        self.PageGestiondesprets.destroy()
        call(["python", "Adherents.py"])
       

   


    
    def Recuperelenomdeladhereneetletitredulivre(self):  #recuperer les nom et livres dispo dans la base de donnes 
            self.nomdelhadherent_list.append("Vide")
            self.livre.append("Vide")
            con= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes")
            cur=con.cursor()
            try:
                cur.execute("select nomAdherent from adherent")
                nomdelhadherent=cur.fetchall()
                if len(nomdelhadherent)>0:
                    del self.nomdelhadherent_list[:]
                    self.nomdelhadherent_list.append("Selectionnez un adhérent")
                    for i in nomdelhadherent:
                        self.nomdelhadherent_list.append(i[0])

                cur.execute("select titreLivre from livre")
                four=cur.fetchall()
                if len(four)>0:
                    del self.livre[:]
                    self.livre.append("Selectionnez un livre")
                    for i in four:
                        self.livre.append(i[0])
                
            except Exception as ex:
                messagebox.showerror("Erreur", f"Erreur de connexion {str(ex)}")

    def ClickActualiser(self):
        con= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes") #
        cur=con.cursor()
        cur.execute("select  * from emprunter ") #ligne sql pour récuperer la table ajoutlivres
        rows= cur.fetchall()
        if len(rows)!=0:
            self.tableauGestiondesprets.delete(*self.tableauGestiondesprets.get_children())
            for row in rows:
                self.tableauGestiondesprets.insert("", END, values=row)
        con.commit()
        con.close()



    def PageEmprunt(self):          
        self.PageEmprunt= Toplevel() # top level fenetre fille a la fenetre mere 
        self.PageEmprunt.title("Emprunter un livre") # titre de la frame
        self.PageEmprunt.config(bg="#ff6600")  # background de la frame 
        self.PageEmprunt.geometry("1056x560+400+200") # la taille de la frame
        #self.PageEmprunt.focus_force()  
        self.PageEmprunt.grab_set() # si on lance une fenetre on poura pas cliquer ailleurs 
        self.PageEmprunt.resizable(width=False, height=False)
        self.PageEmprunt.iconbitmap("Images/bib.ico") 

        #self.root.withdraw()
        

        nom = Label(self.PageEmprunt, text=" Nom ",font =("algarian", 15,"bold"), bg="#ff6600", fg="black")
        nom.place(x=10, y=50)

        ComboboxAdherent = ttk.Combobox(self.PageEmprunt,values=self.nomdelhadherent_list,   textvariable=self.var_nomdelhadherent,font=("goudy old style",20), state="readonly", justify=CENTER)
        ComboboxAdherent.place(x=200, y=50, width=300)
        ComboboxAdherent.current(0)

        livre = Label(self.PageEmprunt, text="Livre ",font =("algarian", 15,"bold"), bg="#ff6600", fg="black")
        livre.place(x=10, y=100)

        ComboboxLivre = ttk.Combobox(self.PageEmprunt,values= self.livre, textvariable=self.var_livre,font=("goudy old style",20), state="readonly", justify=CENTER)
        ComboboxLivre.place(x=200, y=100, width=270)
        ComboboxLivre.current(0)

        

        self.date_emprunte = Label(self.PageEmprunt, text="Date Emprunter ",font =("algarian", 15,"bold"), bg="#ff6600", fg="black")
        self.date_emprunte.place(x=10, y=200)

        date_retour = Label(self.PageEmprunt, text="Date Retour ",font =("algarian", 15,"bold"), bg="#ff6600", fg="black")
        date_retour.place(x=10, y=250)
        ############################################# 

        #Dates
        self.txt_date_emprunte=DateEntry(self.PageEmprunt,font=("time new roman",15),bg="lightgray",textvariable=self.var_dateemprunt, date_pattern="dd/mm/yy")
        self.txt_date_emprunte.place(x=200, y=200, width=140)

        self.txt_date_retour=DateEntry(self.PageEmprunt,font=("time new roman",15),bg="lightgray", textvariable=self.var_dateretour,date_pattern="dd/mm/yy")
        self.txt_date_retour.place(x=200, y=250, width=140)

        BoutonSuivant = Button(self.PageEmprunt, command=self.ClickBoutonEmprunter, text="Suivant",font=("times new roman", 20),cursor="hand2", bg="white").place(x=10, y=300, height=60, width=150)
        #modif_btn = Button(self.PageEmprunt,text="Modifier", font=("times new roman", 20),cursor="hand2", bg="yellow").place(x=170, y=300, height=60, width=150)
        #supp_btn = Button(self.PageEmprunt,text="Supprimer",font=("times new roman", 20),cursor="hand2", bg="red").place(x=10, y=400, height=60, width=150)
        #reini_btn = Button(self.PageEmprunt,text="Réinitialiser",command=self.reni, font=("times new roman", 20),cursor="hand2", bg="gray").place(x=170, y=400, height=60, width=150)
        
        #command=lambda c'est pour passer deux commandes en meme temps

      
        
   
    


    
    def ClickBoutonEmprunter(self):
        try:
                con= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes")

                cur=con.cursor()
                cur.execute("select * from adherent where nomAdherent=%s",self.var_nomdelhadherent.get())
                row= cur.fetchone()

                if row!= None:

                   messagebox.showerror("Erreur", "Cet adhérent à déja emprunter un livre", parent=self.PageEmprunt)

                elif cur.execute("select * from livre where titreLivre=%s",self.var_livre.get()):

                  messagebox.showerror("Erreur", "livre deja emprunter", parent=self.PageEmprunt)
                
                else:
                
                 cur.execute("insert into emprunter (numAdherent,numLivre,dateEmprunt,dateRetour) values (%s,%s,%s,%s)",
                   
                   (
                       
                       self.var_nomdelhadherent.get(),
                       self.var_livre.get(),
                      
                       self.var_dateemprunt.get(),
                       self.var_dateretour.get(),
                       
                    ))

                 cur.execute(" update livre set Etat = 'Emprunter' where titreLivre=%s",self.var_livre.get()),

                 messagebox.showinfo("Succes", "Votre livre à bien été emprunter", parent= self.PageEmprunt)
                   
                 con.commit()
                 con.close
        except Exception as es :
                messagebox.showerror("erreur",f"Erreur de connexionnnn{str(es)}",parent=self.PageEmprunt)

    def reni(self):
        try:
                con= pymysql.connect(host="localhost", user="root", password="", database="bddcomptes")
                cur=con.cursor()
                messagebox.showinfo("Succes"," Votre livre à été gérée", parent= self.PageEmprunt)
                   
                con.commit()
                con.close
        except Exception as es :
                messagebox.showerror("erreur",f"Erreur de connexionnnn{str(es)}",parent=self.PageEmprunt) 

root =Tk()
obj = gestionprets(root)
root.mainloop() #executer tkinter