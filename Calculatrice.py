#Projet Calculatrice Borda Elorien - Briffaut Milan

git remote add origin https://github.com/bordaelorien/calculette-tp.git
git branch -M main
git push -u origin main

class calculatrice:

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
        while i<b:
            resu+=a
            i+=1
        if signe:
            return -resu
        else:
            return resu

    def division(self,a:int,b:int,precision:int):
        if b==0:
            raise ValueError("Impossible de diviser par 0")
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
            while temps<precision:
                tmp+=reste
                temps+=1
            reste=tmp
            chiffre=0
            while reste>=b:
                reste-=b
                chiffre+=1
            decimales+=str(chiffre)
            nombre_decimales+=1
        if quotient!=0:
            if signe:
                resu=f"-{quotient}.{decimales}"
            else:
                resu=f"{quotient}.{decimales}"
        return resu

    def exponentielle(self,base:int,exp:int,precision:int):
        if exp==0:
            return 1
        if exp>0:
            resu=1
            i=0
            while i<exp:
                resu=self.multiplication(resu,base)
                i+=1
            return resu
        position_exp=-exp
        puissance=1
        i=0
        while i<position_exp:
            puissance=self.multiplication(puissance,base)
            i+=1
        return self.division(1,puissance,precision=precision)

    def fibonnaci(self,n:int):
        if n<0:
            raise ValueError("n doit être positif ou nul")
        if n==0:
            return 0
        if n==1:
            return 1
        F_0=0
        F_1=1
        i=2
        while i<=n:
            F_i=F_0+F_1
            F_0=F_1
            F_1=F_i
            i+=1
        return F_1

#Tests

calc = Calculatrice()

print(calc.addition(7, 5))  # 12
print(calc.soustraction(7, 5))  # 2
print(calc.multiplication(7, -3))  # -21
print(calc.division(22, 7, precision=6))  # ~3.142857
print(calc.exponentielle(2, 10))  # 1024
print(calc.exponentielle(2, -3, precision=8))  # ~0.12500000
print(calc.fibonacci(10))  # 55



