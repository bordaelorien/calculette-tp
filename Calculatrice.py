#Projet Calculatrice Borda Elorien - Briffaut Milan
#https://github.com/bordaelorien/calculette-tp.git

class Calculatrice:

    def addition(self,a:int,b:int):
        return a+b

    def soustraction(self,a:int,b:int):
        return a-b

    def multiplication(self,a:int,b:int):
        if a==0 or b==0:
            return 0
        #Détermination du signe du résultat
        signe=False
        if a<0:
            a=-a
            signe=not signe
        if b<0:
            b=-b
            signe=not signe
        resu=0
        i=0
        #Additions répétées
        while i<b:
            resu+=a
            i+=1
        #Prise en compte du signe du résultat
        if signe:
            return -resu
        else:
            return resu

    def division(self,a:int,b:int,precision=5):
        #Vérification de non division par 0
        if b==0:
            raise ZeroDivisionError
        #Détermination du signe du résultat
        signe=False
        if a<0:
            a=-a
            signe=not signe
        if b<0:
            b=-b
            signe=not signe
        #Calcul de la partie entière du résultat
        quotient=0
        reste=a
        while reste>=b:
            reste-=b
            quotient+=1
        #Calcul des décimales du résultat
        decimales=''
        nombre_decimales=0
        while nombre_decimales<precision:
            tmp=0
            temps=0
            #Multiplication du reste par 10
            while temps<10:
                tmp+=reste
                temps+=1
            reste=tmp
            #Recherche du chiffre décimal suivant
            chiffre=0
            while reste>=b:
                reste-=b
                chiffre+=1
            #Ajout de chaque chiffre décimal à la chaîne des décimales
            decimales+=str(chiffre)
            nombre_decimales+=1
        #Prise en compte du signe du résultat
        if signe:
            resu=f"-{quotient}.{decimales}"
        else:
            resu=f"{quotient}.{decimales}"
        #Conversion du résultat
        return float(resu)

    #Fonction utile à l'exponentielle
    def puissance(self,base:int,exp:int,precision:int):
        #Fin si l'exposant est nul
        if exp==0:
            return 1
        #Cas où l'exposant est positif
        if exp>0:
            resu=1
            i=0
            #Multiplication de la base par exp
            while i<exp:
                resu=self.multiplication(resu,base)
                i+=1
            return resu
        #Cas où l'exposant est négatif
        #Prenons la valeur absolue de l'exposant
        position_exp=-exp
        #Calcul de la puissance positive
        puissance=1
        i=0
        while i<position_exp:
            puissance=self.multiplication(puissance,base)
            i+=1
        #Renvoie de l'inverse avec la division
        return self.division(1,puissance,precision=precision)

    #Fonction utile à  l'exponentielle
    def factorielle(self,n:int):
        if n<0:
            raise ValueError("n doit être positif ou nul")
        resu=1
        for i in range(1,n+1):
            resu*=i
        return resu

    def exponentielle(self,a:int,precision:int):
        #Utilisation du développement limité de l'exponentielle à l'odre precision
        resu=0
        i=0
        while i <= precision:
            #Calcul de a**i
            numerateur=self.puissance(a,i,precision)
            #Calcul de i!
            denominateur=self.factorielle(i)
            #Calcul de a**i/i!
            terme=self.division(numerateur,denominateur,precision)
            #Ajout du terme au résultat
            resu+=terme
            i+=1
        return resu

    def fibonacci(self,n:int):
        #Vérification du domaine de définition de la fonction
        if n<0:
            raise ValueError("n doit être positif ou nul")
        #Cas d'initialisation
        if n==0:
            return 0
        if n==1:
            return 1
        #Initialisation des deux premiers termes
        F_0=0
        F_1=1
        i=2
        #Calcul du n-ième terme
        while i<=n:
            #F(i)=F(i-1)+F(i-2)
            F_i=F_0+F_1
            #Mise à jour de F(i-2) et de F(i-1)
            F_0=F_1
            F_1=F_i
            i+=1
        #F_1 correspond alors à F(n)
        return F_1


if __name__ == "__main__":
    #Tests

    calculette=Calculatrice()

    print(calculette.addition(7,5))
    print(calculette.soustraction(7,5))
    print(calculette.multiplication(7,-3))
    print(calculette.division(22,7,precision=6))
    print(calculette.exponentielle(2,precision=3))
    print(calculette.exponentielle(0,precision=1))
    print(calculette.fibonacci(10))

    #12
    #2
    #-21
    #3.142857
    #6.333
    #1.0
    #55
