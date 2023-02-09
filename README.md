# Poolservice

Proyecto de Gastón Gómez Cuello DNI: 40522131

link de drive con el video: https://drive.google.com/file/d/1u0er8XskfU_6LKGpepwSK2--BIOEzbzF/view?usp=sharing

Primero que nada, anoche 8/2/23 cuando estaba haciendo el video de la entrega me di con un error, por la falta de tiempo, no lo revise. Esta
mañana 9/2/23 me di cuenta que era una tontera y me tome el atrevimiento de corregirlo (no habia puesto un return antes del redirect..). 
No se modificó nada mas del proyecto, hay otras cosas que quedaron obsoletas y siguen estando. Ej: link "nuevo cliente" en pestaña clientes.



Se necesita install de : PYTHON(preferentemente 3.11 ya que fue la versión que se usó), pandas, sqlalchemy, django, openpyxl 
(mas que nada por el add_data.py para productos que es para agregar datos desde un archivo excel), se necesita tambien install de Pillow para
trabajar con ImageField (de todas formas no aparece en el formulario de completar perfil, pero ahi DEBERIA ESTAR)



Este proyecto pretende ser una pagina de administración y ventas online de un negocio de articulos 
para piscinas.
De momento están definidas vistas para crear: productos, clientes, usuarios y pedidos; modificar: precios, descripción, stock. 
Para la creación de pedidos se hace referencia tanto a productos como a clientes.
Hay un add_data.py para productos de un provedor. YA FUNCIONA ;)

En la pagina de inicio no hay nada mas que texto, se pretende mostrar algunas imagenes, enlaces y algunas funciones menores.
Para probar los formularios (ademas del de creacion de usuario) hay que crear un superusuario. Luego aparecerán en la nav enlaces para ir a clientes
, pedidos. Luego tendran un enlace de "nuevo cliente" o "nuevo pedido".
Se puede acceder a productos sin estar registrado pero solo para ver los productos, no se podran actualizar ni crear nuevos productos. 
Al agregar producto se pide codigo(tiene que ser unico), descripcion, precio, tc (tipo de cambio charfield con opciones de cada provedor) y si hay
o no stock de ese producto. Cada formulario se valida antes de agregar la data a la DB
Sigo trabajando en los estilos, y la creacion de paginas para completar. Los forms YA SON de tipo forms.ModelForm.

Los campos Tipo de cliente, tipo de cambio en productos, y Forma de pago en orders son importantes a la hora de cal-
cular el precio final de los productos (revendedores tienen descuentos que los clientes normales no, tipo
de cambio hace referencia al dolar que rige para cada producto, y dependiendo la forma de pago hay 
descuentos o recargos) ESTO AUN NO ESTÁ plasmado en codigo pero es lo que se pretende. Ojala tuviera mas tiempo para trabajar en mi código.
EL LINK DE NUEVO CLIENTE NO SE DEBE UTILIZAR. Ahora el perfil de cliente se crea tanto al registrarse en la pagina como al clickear en el usuario
una vez logueado (esto sirve si el usuario se crea desde consola con createsuperuser, etc.). Se completa el perfil de cliente con los campos del
modelo con el mismo nombre, asociado one to one con el usuario.

POR SUPUESTO que las personas registradas como clientes no deberian poder modificar ni crear ningun objeto, pero a fines del trabajo, para que sea mas
facil probar todas las funciones quedará sin modificar por el momento. 

Lo mas interesante esta en el contact us, se envia una consulta que ademas de guardarse en base de datos, queda en el mail de la empresa, a la vez que
se envia un mail automatico al mail del que realiza la consulta.

Al final solo se va a mostrar la pagina de prductos con un listado, precios,  etc. ;
informacion sobre el negocio, contacto, preguntas frecuentes (desde la pagina de contacto) a cualquiera que entre
al sitio y:  paginas de creacion de clientes, productos, pedidos,  para personas registradas


