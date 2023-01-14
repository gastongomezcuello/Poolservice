# Poolservice

Se necesita install de : pandas, sqlalchemy, django, openpyxl (mas que nada por el add_data.py para pro-
ductos que es para agregar datos desde un archivo excel)



Este proyecto pretende ser una pagina de administración y ventas online de un negocio de articulos 
para piscinas.
De momento están definidas vistas para crear: productos, clientes y pedidos. 
Para la creación de pedidos se hace referencia tanto a productos como a clientes.
Hay un add_data.py para productos que genera errores. NO USARLO. Hasta que lo arregle al menos ;)

En la pagina de inicio no hay nada mas que texto. Para probar los formularios hay que entrar a products
en la nav. Ahi se verá de manera muy fea el listado de productos y 3 links: NuevoProducto, NuevoCliente, 
NuevoPedido, clickear en cualquiera de los 3. 
Al agregar producto se pide codigo(tiene que ser unico, aunque no esté hecha esa validacion aun), descrip-
cion, precio, TC2 (si es tipo de cambio 2 o no, deberia ser boolean pero de momento es charfield) y si hay
o no stock de ese producto. Cada formulario se valida antes de agregar la data a la DB
Sigo trabajando en los estilos, y la creacion de paginas para completar. Los forms son tipo forms.Form
pero probaré con forms.ModelForm.

Los campos Tipo de cliente, TC2 en productos, y Forma de pago en orders son importantes a la hora de cal-
cular el precio final de los productos (revendedores tienen descuentos que los clientes normales no, tipo
de cambio hace referencia al dolar que rige para cada producto, y dependiendo la forma de pago hay 
descuentos o recargos) ESTO AUN NO ESTÁ plasmado en codigo pero es lo que se pretende

Al final solo se va a mostrar la pagina de prductos con un listado, precios, opciones de pago, etc. ;
informacion sobre el negocio, sucursales, videos del funcionamiento de los productos, informacion de al-
gunos empleados a cualquiera que entre al sitio
y paneles de administracion, edicion, etc para personas registradas


