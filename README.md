# Poolservice

Proyecto de Gastón Gómez Cuello

Se necesita install de : pandas, sqlalchemy, django, openpyxl (mas que nada por el add_data.py para pro-
ductos que es para agregar datos desde un archivo excel)



Este proyecto pretende ser una pagina de administración y ventas online de un negocio de articulos 
para piscinas.
De momento están definidas vistas para crear: productos, clientes, usuarios y pedidos; modificar: precios, descripción, stock. 
Para la creación de pedidos se hace referencia tanto a productos como a clientes.
Hay un add_data.py para productos de un provedor. YA FUNCIONA ;)

En la pagina de inicio no hay nada mas que texto, se pretende mostrar algunas imagenes, enlaces y algunas funciones menores.
Para probar los formularios (ademas del de creacion de usuario) hay que registrarse en la pagina. Luego aparecerán en la nav enlaces para ir a clientes
, pedidos. Luego tendran un enlace de "nuevo cliente" o "nuevo pedido".
Se puede acceder a productos sin estar registrado pero solo para ver los productos, no se podran actualizar ni crear nuevos productos. 
Al agregar producto se pide codigo(tiene que ser unico), descripcion, precio, tc (tipo de cambio charfield con opciones de cada provedor) y si hay
o no stock de ese producto. Cada formulario se valida antes de agregar la data a la DB
Sigo trabajando en los estilos, y la creacion de paginas para completar. Los forms YA SON de tipo forms.ModelForm.

Los campos Tipo de cliente, tipo de cambio en productos, y Forma de pago en orders son importantes a la hora de cal-
cular el precio final de los productos (revendedores tienen descuentos que los clientes normales no, tipo
de cambio hace referencia al dolar que rige para cada producto, y dependiendo la forma de pago hay 
descuentos o recargos) ESTO AUN NO ESTÁ plasmado en codigo pero es lo que se pretende. Ojala tuviera mas tiempo para trabajar en mi código.
De todas formas no es muy distinto a lo que ya está en código, simplemente hay que crear un perfil de usuario que reemplace la tabla "cliente" y
asociarlo a cada usuario, o asociar la tabla cliente 1 a 1 con cada usuario y asi completar el registro.
POR SUPUESTO que las personas registradas como clientes no deberian poder modificar ni crear ningun objeto, pero a fines del trabajo, para que sea mas
facil probar todas las funciones quedará sin modificar por el momento.

Al final solo se va a mostrar la pagina de prductos con un listado, precios,  etc. ;
informacion sobre el negocio, contacto, preguntas frecuentes (desde la pagina de contacto) a cualquiera que entre
al sitio y:  paginas de creacion de clientes, productos, pedidos,  para personas registradas


