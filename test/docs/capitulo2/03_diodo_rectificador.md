# Diodo rectificador

El diodo rectificador es una aplicación del diodo genérico, a lo que hace referencia que el diodo rectifique, en concreto, es que recorta una señal alterna, solo dejando pasar una parte de ella, ya sea positiva o negativa, depende como se haya conectado.

## Rectificador de Media Onda

Esta aplicación la podríamos decir que es la “conversión de corriente alterna a directa”, desde el punto de vista del contexto que queremos pasar la corriente que tenemos en un contacto convencional de 127VAC para obtener en general una “corriente Directa o Continua”. 
La conversión más básica se llama **Rectificación de Media Onda**, como se muestra en la siguiente imagen:

![circuito media onda]()

Aquí tenemos que observar como está conectado el diodo, pero al mismo tiempo debemos poner mucha atención en el tipo de voltaje al que lo tenemos conectado, es Voltaje Alterno, ya sabemos que este tipo de voltaje no tiene polaridad concreta, es decir, su polaridad cambia constantemente, no tiene una polaridad constante; ahora que tenemos esas consideraciones aplicadas hacia el diodo, nos damos cuenta de que en un momento el diodo está conectado de forma directa y al siguiente instante de forma inversa, este efecto lo que logra es que a la salida del diodo está recortando o eliminando una parte del voltaje de entrada. En este caso por la forma en que está conectado, se elimina la parte negativa de la onda, y al solo quedar una parte de la onda, se le llama **“Rectificador de Media Onda”**. *Con esto logramos que la corriente se convierta en directa, al solo tener una parte positiva*.

Para evitar perder tanto voltaje, se puede aplicar con 2 diodos como se muestra:

![circuito rectificador media onda]()
<figcaption>Aquí estamos recuperando la parte positiva del otro semi ciclo.</figcaption>

## Rectificador de Onda Completa (Puente rectificador)

La siguiente esta es tener un rectificador de onda completa, la cual se tienen que aplicar 4 diodos en configuración puente, a este arreglo de diodos se llama **Puente Rectificador** o **Rectificador de Onda completa**.

Se ilustra a continuación:

![puente rectificador]()

Con esta configuración se tiene el total de la conversión de la corriente alterna a directa.

En la figura se muestra:

![funcionamiento del rectificador]()

El símbolo que se puede encontrar para un puente rectificador:

|Representación 1|Representación 2|
|-|-|
||

Aplicación más clásica de un puente rectificador es una fuente de alimentación lineal, como se muestra en la imagen.

![circuito con puente rectificador de una fuente de 5V]()

[Simulador](https://www.falstad.com/circuit/circuitjs.html)

