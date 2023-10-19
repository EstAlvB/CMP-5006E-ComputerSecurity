## Ejercicio 1

**Supongamos que se elige una contraseña como concatenación de siete palabras del diccionario en minúsculas. Cada palabra se selecciona uniformemente al azar de un diccionario de 50.000 palabras. Un ejemplo de contraseña es ``"mothercathousefivenextcrossroom"``. ¿Cuántos bits de entropía tiene?**

Una forma común de calcular la entropía es mediante la fórmula de Shannon, que se basa en la probabilidad de que cada símbolo, carácter o *palabra* aparezca en la información. La fórmula es la siguiente:

$H=−\sum_{i=1}^np_i\times log_2(p_i)$

La fórmula que se utiliza para calcular la entropía de una contraseña es similar a la de Shannon, pero con algunas diferencias:

$H=L\times log_2(​N)$

Donde $H$ es la entropía, $L$ es la longitud de la contraseña, $N$ es el número de caracteres posibles que se pueden usar para formar la contraseña y $log_2$​ es el logaritmo en base 2. La diferencia entre las dos fórmulas es que la de Shannon asume que cada símbolo o carácter tiene una probabilidad conocida y fija de aparecer, mientras que la de la contraseña asume que cada símbolo o carácter tiene una probabilidad uniforme e igual de aparecer. Además, la de Shannon suma las entropías individuales de cada símbolo o carácter, mientras que la de la contraseña multiplica la longitud de la contraseña por el logaritmo del número de caracteres posibles.

Para este caso no nos basaremos en los caracteres, sino en las palabras. Por ende, en términos de palabras, la longitud de la contraseña es: $L=7$. Dado que tenemos un diccionario de 50,000 palabras, entonces $N=50000$. Reemplazando esto en la última fórmula, obtenemos:

$H=7\times log_2(​50000)=109.26$ 

	Solución: 109.27 bits de entropía

**Considere un esquema alternativo en el que la contraseña se elige como una secuencia de 10 caracteres alfanuméricos aleatorios (incluyendo letras mayúsculas y minúsculas). Un ejemplo es ``"dA3mG67Rrs"``. ¿Cuántos bits de entropía tiene?**

Los caracteres alfanuméricos comprenden números del ``0-9`` (10) y letras de la ``A-Z``(26). Las letras del alfabeto pueden ser también en minúsculas, así que a esta lista se agregarían las letras de la ``a-z`` (26) en minúsculas. Es decir que el número de caracteres posibles para elegir es $N=10+26+26=62$. Si sabemos que la longitud de la contraseña es $L=10$, entonces:

$H=L\times log_2(​N)=10\times log_2(​62)=59.54$ 

	Solución: 59.54 bits de entropía

**¿Qué contraseña es mejor, la de 1 o la de 2?**

Las claves criptográficas con altos niveles de entropía son más difíciles de predecir o descifrar, lo que hace que el algoritmo criptográfico asociado sea más seguro. Por ende, la contraseña número 1 es la mejor, pues tiene la entropía más alta.

## Ejercicio 2

**Diseñe un sistema de verificación de datos utilizando funciones hash. Explica los pasos del proceso.**

- Antes de la transmisión de datos, estos se pasaran a través de una función hash segura como SHA-256; obteniendo así un valor hash o *digest* de los datos.
- El valor hash se compartirá con el receptor a través de un canal de comunicación seguro.
- Se realiza la transmisión de los datos hacia el receptor.
- El receptor recibe los datos, los cuales pasarán a través de la misma función hash que utilizó el emisor, obteniendo otro valor hash para los datos recibidos.
- Si el nuevo valor hash coincide con el valor hash compartido por el emisor, entonces los datos no han sido modificados ni alterados. Si no coinciden, entonces implica que se vulneró la integridad de los datos durante la transmisión.

**Discutir las ventajas e inconvenientes de utilizar funciones hash para la verificación de datos**

<table>
	<tr>
		<th> Ventajas</th>
		<th> Desventajas </th>
	</tr>
	<tr>
		<td>
		Es muy difícil descubrir el mensaje original a través del valor hash
		</td>
		<td>
		Si un atacante consigue acceder al valor hash del mensaje original, podría intentar generar el mismo valor hash pero con otros datos.
		</td>
	</tr>
	<tr>
		<td>
		Es computacionalmente económico calcular el valor hash de los datos
		</td>
		<td>
		Si la función hash es vulnerable a ataques de extensión de longitud, un atacante podría añadir comandos maliciosos a un mensaje válido y generar un hash válido para el mensaje modificado
		</td>
	</tr>
</table>

**Proporcione un ejemplo de una aplicación real en la que se utilice un sistema de verificación de datos mediante funciones hash.**

Las funciones de hash son ampliamente utilizadas en la gestión de contraseñas. En lugar de almacenar las contraseñas en texto plano, los sistemas utilizan funciones de hash para convertir las contraseñas en valores irreversibles. Esto significa que incluso si alguien accede a la base de datos de contraseñas, no podrá obtener las contraseñas reales. Además, cuando un usuario intenta iniciar sesión, la función de hash se utiliza para verificar si la contraseña ingresada coincide con el valor hash almacenado, sin revelar la contraseña real.

## Ejercicio 3

**Defina qué es un código de autenticación de mensajes (MAC) y cómo se utiliza en criptografía.**

El *código de autenticación de mensajes (MAC)* es un bloque de datos que se envía junto a un mensaje encriptado con el fin de que el receptor pueda confirmar la autenticidad del origen de la información. Los códigos MAC son muy similares a las funciones hash, pero, a diferencia de estas, cuentan con una clave secreta que garantiza la integridad del mensaje.

Si el valor MAC enviado coincide con el valor que el destinatario calcula, este puede garantizar que:

-   El mensaje no fue alterado
-   El mensaje proviene del remitente indicado en el mensaje
-   Si el mensaje incluye un número de secuencia, que el mensaje sigue la secuencia correcta

Las MAC se suelen usar para autenticación (de ahí su nombre). El que se quiere autenticar y el verificador comparten la clave de la función MAC y la mantienen en secreto. De esta forma cuando el verificador recibe el valor MAC puede verificar si ese valor MAC se corresponde con el que se tiene que generar a partir de un mensaje dado.

**Explique el proceso de generación y verificación de una MAC**

Los valores MAC se calculan mediante la aplicación de una función hash criptográfica con clave secreta _K_, que solo conocen el remitente y destinatario, pero no los atacantes. Matemáticamente la función hash criptográfica toma dos argumentos: una clave _K_ de tamaño fijo y un mensaje _M_ de longitud arbitraria. El resultado es un código MAC de longitud fija:

$MAC=C_k(M)$

Donde:

- $M$ es un mensaje de longitud arbitraria
- $C_K$ es la función que transforma el mensaje en un valor _MAC_ y que utiliza una clave secreta $K$ como parámetro
- $MAC$ es el valor MAC calculado.

Para verificar si el código MAC es correcto, se necesita conocer la clave secreta que se usó para generar el código MAC. Luego, se aplica la misma función hash criptográfica al mensaje recibido y se compara el resultado con el código MAC enviado. Si son iguales, significa que el mensaje no fue alterado y que proviene del remitente auténtico. Si son diferentes, significa que el mensaje fue manipulado o que el remitente no es quien dice ser.

## Ejercicio 4

**Dados los valores de $p = 17$ y $q = 23$, genera un par de claves para RSA.**

1. Calculamos $n$ mediante la siguiente ecuación:

	$n = p\times q=17\times 23=391$ (9 bits)

2. RSA utiliza la función $\phi$ de Euler de $n$ para calcular la clave secreta. Ésta se define como $\phi(n) = (p - 1) × (q - 1)$ . El requisito previo es que $p$ y $q$ sean diferentes. De lo contrario, la función $\phi$ se calcularía de forma diferente.

	$\phi(n)=(p - 1) × (q - 1)=(17-1)\times(23-1)=16\times 22=352$ <br>

4. La clave pública está formada por el módulo $n$ y un exponente $e$. Seleccionamos el número entero $e$ tal que: $1 < e < \phi(n)$ y $gcd(e, \phi(n)) = 1$ (co-primos).

	$e = 3$
	
	Para comprobar que $e$ sea co-primo con $\phi(n)$ aplicaremos el algoritmo de Euclides para calcular el $GCD$ entre $e$ y $\phi(n)$:
	
	$a=352$, $b=e=3$
	$q=a/b=352/3=117$ → cociente
	$r=a-b\times(a/b)=352-3\times(117)=1$ → residuo
	
	Dado que $r\neq0$, tenemos que continuar con el algoritmo hasta que $r=0$:
	
	$a=b=3$, $b=r=1$
	$q=a/b=3/1=3$ → cociente
	$r=a-b\times(a/b)=3-1\times(3)=0$ → residuo
	
	Obtenemos $r=0$, por lo tanto el valor de $b$ actual es el valor de GCD buscado:
	
	$gcd(3, 352) = b = 1$
	
	Concluimos entonces que $e$ y $\phi(n)$ son co-primos. <br>

5. La clave secreta también consiste en un $d$ (el inverso multiplicativo de $e\ mod(\phi(n))$) con la propiedad de que $d\times e = 1\ mod(\phi(n))$. Para hallar $d$ podemos usar el algoritmo de Euclides extendido, que nos permite encontrar el máximo común divisor de dos números y también sus coeficientes de *Bezout*, que son los números que satisfacen la ecuación: $a\times x + b\times y = gcd(a, b)$. Para hallar los coeficientes de *Bezout*, debemos ir sustituyendo los restos anteriores en las ecuaciones de las divisiones euclidianas, empezando por la última:

	$352-3\times(117)=1=gcd(3, 352)$
	
	Los coeficientes de Bezout que satisfacen esta ecuación $a\times x + b\times y = 1 = gcd(a, b)$ son:
	
	$352\times 1 + 3\times (-117) = 1$
	
	Por lo tanto, $x=1$ y $y=-117$. El valor de $d$ es el coeficiente que multiplica a $e$ en la ecuación, que es $-117$. Sin embargo, para simplificar el cálculo y la seguridad de la clave privada, se suele elegir un valor de $d$ que sea menor que $\phi(n)$ y positivo, lo cual se logra aplicando: 
	
	$d = d\ mod(\phi(n))=-117\ mod(352)=235$

Finalmente, hemos obtenido la clave privada y pública:

	Public Key: (n, e) = (391, 3)
	Private Key: (n, d) = (391, 235)

## Ejercicio 5

**Diseñe un sistema de infraestructura de clave pública (PKI). Explicar los componentes y sus funciones en el sistema.**

- El componente principal de una PKI es la *autoridad de certificación (CA)*. CA se encargará de emitir certificados, renovarlos, revocarlos y gestionarlos. Al emitir un certificado, CA firmará los certificados digitales con su clave privada para garantizar su validez y confianza. Además, publicará su clave pública y el certificado en un lugar accesible para los usuarios.
- Ese lugar accesible es el *repositorio de certificados*. Este servicio permite a los usuarios consultar y descargar los certificados.
- También se necesita la *autoridad de registro (RA)*. RA actúa como intermediario entre una entidad y CA. Cuando una entidad solicita un certificado, RA se encargará de revisar la solicitud, y, si se aprueba, se envía a CA. Luego RA entregará los certificados emitidos por la CA a la entidad solicitante.
- Si, por ejemplo, se sospecha que la clave privada asociada a un certificado ha sido comprometida o si la entidad deja de cumplir los requisitos para tener el certificado, se debe revocar el certificado. Aquí es donde la CA utiliza la llamada *lista de revocación de certificados (CRL)*, la cual contiene los números de serie de los certificados revocados, en un repositorio accesible para los usuarios. CRL permite a los usuarios comprobar el estado de validez de los certificados digitales que reciben o utilizan.

**Analice las ventajas y los retos de la implantación de un sistema PKI.**

<table>
	<tr>
		<th>Ventajas</th>
		<th>Retos</th>
	</tr>
	<tr>
		<td>
		Permite distribuir información de forma segura y confiable.
		</td>
		<td>
		Implementar esta infraestructura puede ser muy costoso
		</td>
	</tr>
	<tr>
		<td>
		Protege una amplia gama de comunicaciones y transacciones
		</td>
		<td>
		Esta infraestructura es vulnerable a ataques de phishing y "man in the middle"
		si no se configura correctamente
		</td>
	</tr>
</table>

**Proporcione un ejemplo de una aplicación real en la que se utilice un sistema PKI.**

En muchas empresas, el correo electrónico es el talón de Aquiles de la seguridad. Como ocurre con los sitios web y las transacciones bancarias, también hay que proteger los datos de los correos electrónicos mientras se transmiten del emisor al destinatario. Los certificados PKI constituyen una solución de cifrado y autenticación de eficacia demostrada que, además de proteger el contenido del mensaje de correo electrónico, también confirma la identidad del emisor.

La empresa DigiCert® creó una solución para ello llamada [DigiCert® Trust Lifecycle Manager](https://www.digicert.com/es/trust-lifecycle-manager), el cual nos permite controlar y administrar todos los certificados de correo electrónico desde un solo lugar. Con un solo inicio de sesión, se puede integrar servicios de correo electrónico empresarial, autenticar usuarios, retirar el acceso a quien ya no trabaja en la empresa y recuperar correos electrónicos seguros. La PKI de DigiCert® protege del phishing, el spearhead phishing, la suplantación de identidad y otros tipos de fraude por correo electrónico. Mediante los certificados S/MIME, la PKI cifra los mensajes que se transmiten al tiempo que vincula la identidad verificada del emisor con el mensaje propiamente dicho.

## Ejercicio 6

**Diseñe un sistema de firma digital basado en criptografía de clave pública. Explique las etapas del proceso y la función de cada componente.**

El esquema de firma digital se basa en la criptografía de clave pública. El modelo de esquema de firma digital se muestra en la siguiente ilustración:

![[digital_sign_model.png]]

- Cada persona tiene un par de claves pública-privada.
- Generalmente, los pares de claves utilizados para el cifrado / descifrado y la firma / verificación son diferentes. La clave privada que se usa para firmar se conoce como clave de firma y la clave pública como clave de verificación.
- El firmante alimenta datos a la función hash y genera hash de datos. La función hash es un algoritmo matemático que transforma cualquier dato en un valor fijo y único. Este valor se utiliza para verificar la integridad del mensaje cuando llega al receptor.
- El valor hash y la clave de firma se alimentan luego al algoritmo de firma que produce la firma digital en un hash dado. Un algoritmo de firma es un algoritmo criptográfico que utiliza la clave privada del remitente para generar una firma digital a partir de un hash dado. La firma se agrega a los datos y luego ambos se envían al verificador.
- El verificador introduce la firma digital y la clave de verificación en el algoritmo de verificación. El algoritmo de verificación es un algoritmo criptográfico que utiliza la clave pública del remitente para comprobar si una firma digital es válida para un hash dado.
- El verificador también ejecuta la misma función hash en los datos recibidos para generar valor hash.
- Para la verificación, se comparan este valor hash y la salida del algoritmo de verificación. Según el resultado de la comparación, el verificador decide si la firma digital es válida.
- Dado que la firma digital se crea con la clave "privada" del firmante y nadie más puede tener esta clave; el firmante no puede rechazar la firma de los datos en el futuro.
