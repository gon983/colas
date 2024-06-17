La funcion simulacion.fila() instancia todos los valores de la simulacion en su valor actual. 

con esta funcion, teniendo el objeto simulacion en memoria quedaria una funcion que sea simulacion.correr() que retorne una tabla.

Esta tabla se haria con 1 una funcion que busque la llegada, fin , mas proximo
                        2 una funcion que si esta es llegada setee determinados valores y si es fin setee otros con la logica puesta en el excel que se llama proto que esta en el grupo de wpp
                        3 la funcion simular fila, que iria instanciando cada iteracion entre 1 y 2 dejando un registro en la tabla

estaria bueno agregar una scrollbar horizontal

y despues despues hay q hacer esas consignas q estan tapadas

# COSAS QUE FALTAN
* Ver si se agrega una nueva columna "cliente" por cada cliente que llega 
* Que la simulacion se haga por tiempo, y que se pueda elegir desde que linea hasta que linea mostrar 
    * me imagino que una manera de solucionar esto es que por cada evento se sume 1 a un iterador
    cuando el iterador llegue a la linea_Desde que selecciono el ususario, empiece a generar la tabla. Se van a cargar filas a la tabla hasta alcanzar con el iterador hasta la linea_hasta
    * es decir, sacaria el "cant_lineas_a_mostrar" y pondria un "linea_Desde" y "linea_hasta"
* Hacer las consignas :(