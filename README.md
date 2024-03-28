# ProyectoFinal_Rega

El objetivo del proyecto es generar una página web que permita el ingreso de solicitudes de dosificaciones de fármacos para que el laboratorio del hospital pueda procesarlas. 
En el modelo Farmaco el usuario administrador puede agregar los fármacos que se encuentran en su cartera y que tipo de muestra se requiere para el análisis.
En los modelos Medico y Paciente se solicitan los datos necesarios para la trazabilidad de las muestras, para saber a quien y donde comunicar los resultados obtenidos, y a quien corresponden las muestras recibidas. 
En el modelo Solicitud, se cruzan los datos del médico tratante, paciente, fármaco a dosifcar y la fecha de realización de la solicitud.
Es necesario ingresar al Paciente y al Médico previo al ingreso de la Solicitud, ya que el modelo Solicitud se alimenta de los datos ya registrados, para asegurar que se cuenta con toda la información necesaria antes de ingresar la solicitud.
Es necesario estar logueado para realizar el ingreso y modificación de los datos, y solamente el administrador podrá modificar los datos de Fármacos.

## Modificar directorio
1. Asegurarse de encontrarse en el directorio que contiene al archivo manage.py
2. De no ser así cambiar a ese archivo ingresando en el terminal el comando:
`cd "nombre del nuevo directorio"`

3. Hacer la migración del proyecto ingresando los comandos
`python manage.py makemigrations`
`python manage.py migrate`

4. Para ejercutar el servidor ejecutar en el terminal el comando:
`python runserver`

5. Ingresar al link proporcionado en el terminal agregando "/AppCoder" al final

## Usuario administrador

El usuario administrador para la aplicación es el siguiente:
user: admin
password: coderhouse




