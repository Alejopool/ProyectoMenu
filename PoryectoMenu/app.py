from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'  # esto solo es una linea necesaria para usar flash

#--------------------------Modulo  contar vocales-----------------------------------
def contar_cadena(Cadena1, Cadena2): # funcion que almacena el resultado para devolver al html

    resultados = {}
    if Cadena1.isdigit() or Cadena2.isdigit():
        return "No puedo contar numero alguna de las 2 cadenas tiene numeros",resultados
    
    cantDigitos1 = len(Cadena1)
    cantDigitos2 = len(Cadena2)

    if cantDigitos1 == cantDigitos2 :
        
        resultados['cadena1'] = contar_vocales(Cadena1)
        resultados['cadena2'] = contar_vocales(Cadena2) #Estoy almacenando el resultado en una lista
    else :
        return "Las cadenas no tienen la misma cantidad de caracteres", resultados
    
    return None,resultados 
#--------------------------Modulo  contar vocales-----------------------------------
def contar_vocales(cadena):  # funcion para contar las vocales

    cadena = cadena.lower() #coloca toda la cadena en minusculas
    vocales = 'aieou'
    contador = {vocal:0 for vocal in vocales}  # que vocales(i)  recorra a vocales, este el que cuenta cuantas vocales hay

    for char in cadena:
        if char in vocales:
            contador[char] += 1   #[]  si se pone en parentesis ya no es una lista,
                                  #y necesitamos listarlo para hacer una respuesta en lista

    return {vocal:contador[vocal] for vocal in vocales if contador[vocal] > 0}
#-------------------------------------------------------------------------------------------
#------------------------------------------Funciones para comparar cadenas------------------
class CadenaVerificadora:
    def verificar_subcadena(self, cadena1, cadena2):
        
        if len(cadena1) >= len(cadena2):
            largo = cadena1
            corto = cadena2
        else:
            largo = cadena2
            corto = cadena1
        
        if corto in largo:
            return f"{corto} es subcadena de {largo}"
        else:
            return f"{corto} No es subcadena {largo}"
#-------------------------------------------------------------------------------------------
#------------------------------------------Buscar Palindromas ------------------------------
def FuncionPalindrioma(Parrafo):
    CantidadEspacios = Parrafo.count(' ')
    Palabra = Parrafo.split()

    Palindroma = []
    cobtador = 0
    while cobtador < len(Palabra):
        if Palabra[cobtador].lower() == Palabra[cobtador][::-1].lower():
            Palindroma.append(Palabra[cobtador])
        cobtador += 1
    
    CantPalabraspalindromas = len(Palindroma)

    resultado = f"Numero de espacios en el parrafo: {CantidadEspacios} <br>"
    resultado += f"Hay {CantPalabraspalindromas} palabras palindromas en el texto digitado. <br>"

    if Palindroma:
        resultado += "Palabras palindromas encontradas <br>"
        for palabra in Palindroma:
            resultado += f'<p class="text-dark">{palabra}</p><br>'
    else:
        resultado += "No se encontaron palabras palindromas . <br>"

    return resultado

#-------------------------------------------------------------------------------------------
#------------------------------------------Letra en mayusculas------------------------------
def  titulo(cadena):
    if cadena.isdigit():
        return "Lo que acaba de digitar son numeros "
    else:
        Palabras = cadena.split()
        resultado =""
        i = 0

        while i < len(Palabras):
            PalabrasConPrimeraLetraMayuscula = Palabras[i].capitalize()

            if resultado:
                resultado += " "
            
            resultado += PalabrasConPrimeraLetraMayuscula
            i +=1
        
        return resultado


#-------------------------------------------------------------------------------------------


@app.route('/')  # Inicializa el proyecto en la ruta Raiz 
def llevar_Login(): 
    return render_template('Login.html')

@app.route('/Login', methods=['POST'])  # extrae la informacion que viene desde el Login para vaidar y poder enviar al home
def llevar_Home(): 
    UsuarioLogin = request.form.get('UsuarioLogin')
    ContrasenaLogin = request.form.get('ContrasenaLogin')

   
    if UsuarioLogin == 'Prueba' and ContrasenaLogin == 'Prueba':    
        return redirect(url_for('home'))  # dirige al home
    else:
        flash('Usuario o Contraseña Incorrecta', 'danger')
        return redirect(url_for('llevar_Login')) # dirige al login en caso de que las credenciales sean incorrectas

@app.route('/Home', methods=['POST', 'GET'])  # se mueve a la plantilla de Home
def home():
    resultados = {}
    mensaje_error = None
    Resultado = None

    verificador = CadenaVerificadora()

    if request.method == "POST":
        cadena1 = request.form.get("Cadena1") # Extrae los valores que vienen desde HTML
        cadena2 = request.form.get("Cadena2")
        Texto1 = request.form.get("Texto1")
        Texto2 = request.form.get("Texto2")
        Palindromas = request.form.get("Palindromas")
        Titulo = request.form.get("Titulo")

        if cadena1 and cadena2:
            mensaje_error, resultados = contar_cadena(cadena1, cadena2)


        if Texto1 and Texto2:
            Resultado = verificador.verificar_subcadena(Texto1, Texto2)

        if Palindromas:
            Resultado = FuncionPalindrioma(Palindromas)


        if Titulo:
            Mayusculas = titulo(Titulo)
            Resultado = f"Título recibido: {Mayusculas}"  

    return render_template('Home.html', resultados=resultados, mensaje_error=mensaje_error, Resultado=Resultado)# Renderiza la plantilla con los resultados procesados





@app.route('/seleccionar', methods=['POST'])  # Enviar a ruta de selección
def seleccionar(): 
    opcion = request.form.get('opcion')
    if opcion == 'sustentacion':
        return render_template('sustentacion.html') 
    elif opcion == 'manual_usuario':
        return render_template('manual_usuario.html')
    else:
        return render_template('Home.html')

if __name__ == '__main__':
    app.run(debug=True)
