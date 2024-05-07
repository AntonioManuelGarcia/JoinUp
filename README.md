# JoinUp

Prueba técnica sobre sync/async y optimización de consultas a la base de datos.

## Principales endpoints

Hay 2 endpoint principales, tal como pide el enunciado, un endpoint de registro y un
endpoint de perfil, además hay otros endpoints
secundarios como el del panel de administración o el de la documentación.

### Perfil:

GET `/api/1.0.0/profile/{id}/` con el parametro id del perfil, devuelve el perfil del usuario
con los datos del registro más dos campos extras boleanos para informar si el email y el número
de telefono han sido validados o no.

`````json
{
  "id": 73,
  "first_name": "aa",
  "last_name": "aa",
  "email": "wiladrow@gmail.com",
  "email_validated": false,
  "phone_number": "+34628461778",
  "phone_number_validated": true,
  "hobbies": "afsdfsafdfasdasfd"
}
`````

### Registro:

POST `/api/1.0.0/signup/` con los parametros requeridos `email` y `phone_number`, y los opcionales 
`first_name`,`last_name` y`hobbies`. Devuelve los datos del perfil creado

````json
{
  "id": 73,
  "first_name": "antonio",
  "last_name": "manuel",
  "email": "mail@gmail.com",
  "phone_number": "+34647234567",
  "hobbies": "jugar skyrim"
}

````

### Login:

POST `/api/users/auth/login/` con `username` y `password` como parámetros, 
devuelve el token jwt.

### Registro:

POST `/api/users/auth/register/` con `username`, `password`, `password2`
 y `email` como parametros, devuelve el username y el email si el registro 
se produce.

### Documentación:

GET `api/documentation/` nos permite acceder al swagger con la documentación del 
proyecto.

## Como desplegar el docker

Para poner en marcha el docker del proyecto simplemente hay que ejecutar 
los siguientes comandos.

```
docker-compose up -d --build
```

## Test y cobertura

Para lanzar los test basta con lanzarlos con el comando test de django, y si queremos 
acelerar la ejecución podemos usar la opcion de --parallel para ejecutarlos en paralelo.

```
python manage.py test --parallel --settings=djangoProject.settings.local
```

Para comprobar la cobertura usamos la herramienta coverage para obtener el informe 
de cobertura.

```
coverage erase
coverage run .\manage.py test
coverage report
```
Opcionalmente, podemos guardar el informe en un fichero con el siguiente comando.
```
coverage report > coverage.txt
```

### informe de cobertura actual
```
Name                                 Stmts   Miss  Cover
--------------------------------------------------------
Profile\__init__.py                      0      0   100%
Profile\admin.py                         8      0   100%
Profile\apps.py                          4      0   100%
Profile\migrations\0001_initial.py       6      0   100%
Profile\migrations\__init__.py           0      0   100%
Profile\models.py                       17      1    94%
Profile\serializers.py                  17      0   100%
Profile\tests.py                        52      0   100%
Profile\urls.py                          4      0   100%
Profile\views.py                        11      0   100%
commons\renderers.py                    13      3    77%
commons\views.py                        24      5    79%
djangoProject\__init__.py                0      0   100%
djangoProject\settings.py               28      0   100%
djangoProject\urls.py                   14      0   100%
manage.py                               12      2    83%
--------------------------------------------------------
TOTAL                                  210     11    95%

```
## Número de consultas a la base de datos en los test

Para controlar el número de peticiones a la base de datos se han usado dos paquetes, 
uno de ellos es django-debug-toolbar que permite ver en el propio navegador el número
de peticiones que se hacen en vivo cuando se lanza una petición, mientras que el otro 
django-query-counter que al lanzar los test permite sacar un informe en pantalla del 
número de peticiones en cada uno de los tests. Como cada test consulta un único endpoint
nos es fácil saber cuantas consultas a la base de datos se realizan en cada uno.

Los test los ejecutamos con el mismo comando para lanzarlos en paralelo.
```
python .\manage.py test --parallel
```
### Consultas en los test en la version Sync v1.0.0
```

testing test_create_new_profile
+--------+--------+--------+--------+------------+-------+----------+
| Select | Insert | Update | Delete | Duplicates | Total | Duration |
+--------+--------+--------+--------+------------+-------+----------+
|   2    |   1    |   0    |   0    |     0      |   3   |   0.01   |
+--------+--------+--------+--------+------------+-------+----------+
Target: /api/1.0.0/signup/ Profile.views.CreateProfileView
.
testing test_create_new_profile_with_same_email
+--------+--------+--------+--------+------------+-------+----------+
| Select | Insert | Update | Delete | Duplicates | Total | Duration |
+--------+--------+--------+--------+------------+-------+----------+
|   2    |   0    |   0    |   0    |     0      |   2   |   0.00   |
+--------+--------+--------+--------+------------+-------+----------+
Target: /api/1.0.0/signup/ Profile.views.CreateProfileView
.
testing test_create_new_profile_with_same_phone
+--------+--------+--------+--------+------------+-------+----------+
| Select | Insert | Update | Delete | Duplicates | Total | Duration |
+--------+--------+--------+--------+------------+-------+----------+
|   2    |   0    |   0    |   0    |     0      |   2   |   0.00   |
+--------+--------+--------+--------+------------+-------+----------+
Target: /api/1.0.0/signup/ Profile.views.CreateProfileView
.
testing test_create_new_profile_with_wrong_format_phone_number
+--------+--------+--------+--------+------------+-------+----------+
| Select | Insert | Update | Delete | Duplicates | Total | Duration |
+--------+--------+--------+--------+------------+-------+----------+
|   1    |   0    |   0    |   0    |     0      |   1   |   0.00   |
+--------+--------+--------+--------+------------+-------+----------+
Target: /api/1.0.0/signup/ Profile.views.CreateProfileView
.
testing test_create_new_profile_without_email
+--------+--------+--------+--------+------------+-------+----------+
| Select | Insert | Update | Delete | Duplicates | Total | Duration |
+--------+--------+--------+--------+------------+-------+----------+
|   1    |   0    |   0    |   0    |     0      |   1   |   0.00   |
+--------+--------+--------+--------+------------+-------+----------+
Target: /api/1.0.0/signup/ Profile.views.CreateProfileView
.
testing test_create_new_profile_without_phone_number
+--------+--------+--------+--------+------------+-------+----------+
| Select | Insert | Update | Delete | Duplicates | Total | Duration |
+--------+--------+--------+--------+------------+-------+----------+
|   1    |   0    |   0    |   0    |     0      |   1   |   0.00   |
+--------+--------+--------+--------+------------+-------+----------+
Target: /api/1.0.0/signup/ Profile.views.CreateProfileView
.
testing test_get_non_existing_profile
+--------+--------+--------+--------+------------+-------+----------+
| Select | Insert | Update | Delete | Duplicates | Total | Duration |
+--------+--------+--------+--------+------------+-------+----------+
|   1    |   0    |   0    |   0    |     0      |   1   |   0.00   |
+--------+--------+--------+--------+------------+-------+----------+
Target: /api/1.0.0/profile/99/ Profile.views.ProfileDetailView
.
testing test_get_profile
| Select | Insert | Update | Delete | Duplicates | Total | Duration |
+--------+--------+--------+--------+------------+-------+----------+
|   1    |   0    |   0    |   0    |     0      |   1   |   0.00   |
+--------+--------+--------+--------+------------+-------+----------+
Target: /api/1.0.0/profile/1/ Profile.views.ProfileDetailView
.
----------------------------------------------------------------------
Ran 8 tests in 0.095s

```
### Consultas en los test en la version Async v1.1.0
```

 testing test_create_new_profile
+--------+--------+--------+--------+------------+-------+----------+
| Select | Insert | Update | Delete | Duplicates | Total | Duration |
+--------+--------+--------+--------+------------+-------+----------+
|   2    |   1    |   0    |   0    |     0      |   3   |   0.06   |
+--------+--------+--------+--------+------------+-------+----------+
Target: /api/1.0.0/signup/ Profile.views.CreateProfileView
.
 testing test_create_new_profile_with_same_email
+--------+--------+--------+--------+------------+-------+----------+
| Select | Insert | Update | Delete | Duplicates | Total | Duration |
+--------+--------+--------+--------+------------+-------+----------+
|   2    |   0    |   0    |   0    |     0      |   2   |   0.00   |
+--------+--------+--------+--------+------------+-------+----------+
Target: /api/1.0.0/signup/ Profile.views.CreateProfileView
.
 testing test_create_new_profile_with_same_phone
+--------+--------+--------+--------+------------+-------+----------+
| Select | Insert | Update | Delete | Duplicates | Total | Duration |
+--------+--------+--------+--------+------------+-------+----------+
|   2    |   0    |   0    |   0    |     0      |   2   |   0.00   |
+--------+--------+--------+--------+------------+-------+----------+
Target: /api/1.0.0/signup/ Profile.views.CreateProfileView
.
 testing test_create_new_profile_with_wrong_format_phone_number
+--------+--------+--------+--------+------------+-------+----------+
| Select | Insert | Update | Delete | Duplicates | Total | Duration |
+--------+--------+--------+--------+------------+-------+----------+
|   1    |   0    |   0    |   0    |     0      |   1   |   0.00   |
+--------+--------+--------+--------+------------+-------+----------+
Target: /api/1.0.0/signup/ Profile.views.CreateProfileView
.
 testing test_create_new_profile_without_email
+--------+--------+--------+--------+------------+-------+----------+
| Select | Insert | Update | Delete | Duplicates | Total | Duration |
+--------+--------+--------+--------+------------+-------+----------+
|   1    |   0    |   0    |   0    |     0      |   1   |   0.00   |
+--------+--------+--------+--------+------------+-------+----------+
Target: /api/1.0.0/signup/ Profile.views.CreateProfileView
.
 testing test_create_new_profile_without_phone_number
+--------+--------+--------+--------+------------+-------+----------+
| Select | Insert | Update | Delete | Duplicates | Total | Duration |
+--------+--------+--------+--------+------------+-------+----------+
|   1    |   0    |   0    |   0    |     0      |   1   |   0.00   |
+--------+--------+--------+--------+------------+-------+----------+
Target: /api/1.0.0/signup/ Profile.views.CreateProfileView
.
 testing test_get_non_existing_profile
+--------+--------+--------+--------+------------+-------+----------+
| Select | Insert | Update | Delete | Duplicates | Total | Duration |
+--------+--------+--------+--------+------------+-------+----------+
|   1    |   0    |   0    |   0    |     0      |   1   |   0.00   |
+--------+--------+--------+--------+------------+-------+----------+
Target: /api/1.0.0/profile/99/ Profile.views.ProfileDetailView
.
 testing test_get_profile
+--------+--------+--------+--------+------------+-------+----------+
| Select | Insert | Update | Delete | Duplicates | Total | Duration |
+--------+--------+--------+--------+------------+-------+----------+
|   1    |   0    |   0    |   0    |     0      |   1   |   0.00   |
+--------+--------+--------+--------+------------+-------+----------+
Target: /api/1.0.0/profile/1/ Profile.views.ProfileDetailView
.
----------------------------------------------------------------------
Ran 8 tests in 0.115s

```

## Questionario

- ¿Cuántas consultas hace cada endpoint a la BD?
> Pues el endpoint de signup hace dos selects y un insert, el insert solo si los campos obligatorios son correctos.
> Mientras que el endpoint del profile hace una única consulta de select.
- ¿Cuántas consultas hace la parte asíncrona?
> La parte asincrona a la hora de crear un perfil tiene el mismo comportamiento, hace una consulta de insert y 
> dos selects también. 
- ¿Puedes poner un ejemplo de petición (tipo curl) por cada endpoint?
> Se puede consultar en el endpoint de documentación con swagger, pero serían tal que asi para 
> el endpoint de profile y signup respectivamente:
>> curl -X 'GET' \
  'http://localhost:8000/api/1.0.0/profile/1/' \
  -H 'accept: application/json'
> 
>> curl -X 'POST' \
  'http://localhost:8000/api/1.0.0/signup/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "antonio",
  "last_name": "manuel",
  "email": "mail@gmail.com",
  "phone_number": "647234567",
  "hobbies": "jugar skyrim"
}'

## Otras Preguntas
- ¿Qué te ha parecido la prueba? ¿Te ha gustado? ¿Te ha parecido sencilla, media,
compleja?
> La prueba me ha parecido bien, simple, dificultad media, más que nada por la 
> cantidad de cosas que puedes meter y optimizar si no es bastante sencilla, me ha 
> gustado que me ha permitido practicar cosas que normalmente en empresas grandes 
> con proyectos ya creados no tienes oportunidad.
- ¿Hay algún punto que te haya parecido confuso de la prueba?
> Hay cosas que no están especificadas en el enunciado, como si se necesita login, si 
> el mail y el teléfono se consideran validados cuando se envian ó
> el dejar a nuestro criterio hasta qué punto se necesita mockear el envio de email 
> y sms, pero entiendo que es parte de la evaluación del candidato
- ¿Has aprendido algo con esta prueba?
> Pues en este caso el envio de sms que no había tenido que trabajar con ello antes y
> el uso de las nuevas versiones de algunos de los paquetes con django5, que queria 
> probarlo, ya que aún no había tenido ocasión. También sobre los paquetes para controlar
> el número de consultas, muy utiles. 
- ¿Cuánto tiempo has tardado en hacer la prueba?
> Unas seis horas además de la puesta en marcha del proyecto, he dedicado la mayoria a
> investigar las nuevas versiones de los paquetes para la última version de django y su
> uso, algunos dan problemas de incompatibilidad con python 3.12 por ejemplo y se optó 
> por la versión 3.10 en su lugar.
- ¿Qué es lo más divertido que has desarrollado? ¿Qué es lo que más te gusta
desarrollar?
> Lo más divertido que he desarrollado ha sido en programación competitiva, algoritmos de lógica
> computacional y aprendizaje para plman, un clon del clasico pacman.
> Lo que más me gusta desarrollar son cosas que me supongan un reto y me permitan aprender cosas
> nuevas, no tiene que ser algo en concreto. 
- ¿Qué es lo que más odias desarrollar?
> Proyectos legacy con versiones muy antiguas.  
- ¿Tienes manías desarrollando? ¿Cuáles son?
> Tengo siempre una libreta al lado mientras desarrollo para apuntar temas que encuentro
interesante y quiero mirar con más detenimiento. 
- ¿Te gustaría comentar algo extra? ¿Te habría gustado que te hiciéramos alguna
pregunta?
> No se me ocurre nada ahora mismo.
- Después de hacer la prueba, ¿tienes algunas dudas extras sobre cómo trabajamos?
> Por ahora no.
- ¿Cambiarías algo de la prueba para completarla con algo que consideres
importante?
> Pues añadiría un poco de complejidad al tema de optimización de las consultas de la
> base de datos, pondría alguna relación con el modelo para ver si el candidato puede
> mejorar la consulta pertinente usando índices en la clave ajena o el select_related, 
> cosas no muy complejas para no aumentar mucho el tiempo de la prueba, pero que permite
> ver si se conoce un poco más sobre la optimización de consultas. 
