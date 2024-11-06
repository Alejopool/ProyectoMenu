from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'  # esto solo es una linea necesaria para usar flash

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

@app.route('/Home')  # se mueve a la plantilla de Home
def home():
    return render_template('Home.html')



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
