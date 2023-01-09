# Proyecto final de coderhouse de Tomas Capdevila
# "Music Blog"

## Acerca de Music Blog:
<p>
Music blog es el nombre de la pagina web que se hizo como proyecto final para el curso de Python en Coderhouse. Esta pagina es un blog sobre musica.
</p>

<p>
Para la creacion de esta pagina, se utilizo el framework de python Django junto con algunas herramientas de html, css y javascript.<br>
Ademas, se utilizaron plantillas html que se descargaron de la pagina "Themeslab" y se modificaron para adaptarlas a las necesidades de la web.
</p>

<p>
Los posteos del blog fueron redactados mediante la inteligencia artificial "ChatGPT" a modo de prueba para generar contenido en la pagina.
</p>

<p>
Asimismo, para realizar pruebas, se puede usar el usuario 'admin' cuya contraseña es igual al usuario para entrar al panel de administracion de django y crear o modificar objetos en la base de datos.
</p>

## Funcionamiento:

<p>
Al ejecutar el comando <strong>manage.py runserver</strong> se inicia el servidor en el localhost de la pc, en el puerto 8000 por defecto. <br>
Una vez que el servidor esta corriendo, la pagina nos redigira a la URL '/' que es el inicio, en donde se puede observar la pagina de inicio de la web.
</p>
<p>
Para movernos entre las diferentes vistas de la pagina, se puede usar la barra de navegacion situada en la parte superior de la web, teniendo en cuenta que para muchas de las vistas hace falta estar logueado. <br>
Se puede usar a modo de prueba el usuario <strong>tomycapde</strong> cuya contraseña es <strong>#Coderhouse2022</strong><br>
De ser necesario, se puede crear un nuevo usuario desde la opcion en la barra de navegacion llamada "register" que solo sera visible si no se esta logueado.
</p>
<p>
La pagina en si esta compuesta de tres aplicaciones:
<li>En la app de "Posts" se pueden ver, crear y editar posteos para el blog. Para ver los posteos solo hace falta dirigirse a la opcion "Ver posteos" en la barra de navegacion. Para editar un posteo, es necesario ser el creador de este y si esto sucede, en la parte inferior del posteo se vera la opcion de editar el posteo. Por ultimo, para crear un nuevo posteo, solo hace falta dirigirse a la URL /blog/create_post.
<li>En la app de "Users" se configura todo lo relativo a los usuarios. Para ver el perfil de un usuario solo hace falta hacer click en el nombre de usuario en la barra de herramientas. Una vez hecho el paso anterior, se puede observar informacion acerca de el usuario y al final de la pagina dos botones: Uno para editar lo referido al perfil (biografia, avatar, sitio web) y el otro para editar lo referido al usuario (nombre de usuario, mail y contraseña).
<li>En la app de "Messages" se pueden enviar y recibir mensajes como un cliente de correo habitual. Solo hace falta dirigirse al apartado de mensajes desde la barra de navegacion y hacer click para dirigirnos a la bandeja de mensajes. Desde este punto se pueden leer mensajes enviados o recibidos e incluso redactar un nuevo mensaje. Hay que tener en cuenta que al redactar un nuevo mensaje, se necesita introducir un nombre de usuario valido para que el mismo sea enviado.
</p>

## Requerimientos:

Para instalar los requerimientos necesarios hay que ejecutar el comando `pip install -r requirements.txt`

Cabe destacar que el proyecto se realizo usando linux y algunos requerimientos son propios de este sistema operativo.