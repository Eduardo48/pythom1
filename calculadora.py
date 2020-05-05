def sumar(a,b):
    c=a+b
    return c

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def div_entera(a,b):
    if b==0:
        print("Error division sobre 0")
        return 
    return a//b

def div_real(a,b):
    if b==0:
        print("Error division sobre 0")
        return 
    return a/b

def modulo(a,b):
    if b==0:
        print("Error division sobre 0")
        return 
    return a%b
  
def potencia(a,b):
    return a**b

def main():
    c=1

    while (c==1):
         print("ingresa dos valores")
         x=int(input())
         y=int(input())
         print("1 sumar\n 2 restar\n 3 division entera\n 4 division\n 5 modulo\n 6 potencia\n 7 muiltiplicar\n 8 salir ")
         op=int(input())

         if op==1:
           print(sumar(x, y))
        
         elif op==2:#como else
           print(restar(x,y))
        
         elif op==3:
          print(div_entera(x,y))
        
         elif op==4:
          print(div_real(x,y))
        
         elif op==5:
           print(modulo(x,y))
         
         elif op==6:
          print(potencia(x,y))
        
         elif op==7:
            print(multiplicar(x,y))
        
         elif op==8:
             c=5
            
             
             
         else:#else por que no hay otra opcion
           print("opcion no valida")
        
   
    print("Usted ha salido del menu")
        
    
        
if  __name__=="__main__":#importa archivos "main"
    main()
    
    
        
        
