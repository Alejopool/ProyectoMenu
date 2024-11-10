
window.onload = function(){
    const boton_contar_vocales = document.getElementById("boton_contar_vocales")
    boton_contar_vocales.addEventListener('click',function(){
        var modal_contar_vocales = new bootstrap.Modal(document.getElementById("modal_contar_vocales"))
        modal_contar_vocales.show()    
    })

    const boton_sub_cadena = document.getElementById("boton_sub_cadena")
    boton_sub_cadena.addEventListener('click',function(){
        var modal_sub_cadena = new bootstrap.Modal(document.getElementById("modal_sub_cadena"))
        modal_sub_cadena.show()    
    })
    
    const boton_palindromas = document.getElementById("boton_palindromas")
    boton_palindromas.addEventListener('click',function(){
        var modal_palindromas = new bootstrap.Modal(document.getElementById("modal_palindromas"))
        modal_palindromas.show()    
    })

    const buton_primera_mayuscula = document.getElementById("buton_primera_mayuscula")
    buton_primera_mayuscula.addEventListener('click',function(){
        var moda_primera_mayuscula = new bootstrap.Modal(document.getElementById("moda_primera_mayuscula"))
        moda_primera_mayuscula.show()    
    })
}