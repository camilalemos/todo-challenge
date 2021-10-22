> Lemos Camila Soledad 

# Invera ToDo-List Challenge (Python/Django Jr-SSr)

## Ejecución del repo
Seguir instrucciones del archivo INSTALL.md para correr el proyecto

## Endpoints
Se utiliza en el módulo URL Conf. Para probarlo:
- Crear una tarea: http://127.0.0.1:8000/create/*descripcion donde *descripcion es el detalle de la tarea que desea crear. Devuelve el id de la tarea.
- Eliminar una tarea: http://127.0.0.1:8000/delete/*id *id es el id de la tarea que se desea borrar.
- Marcar tareas como completadas: http://127.0.0.1:8000/complete/*id *id es el id de la tarea que se desea marcar como completada.
- Poder ver una lista de todas las tareas existentes: http://127.0.0.1:8000/get/
- Filtrar/buscar tareas por fecha de creación: Existen dos maneras de buscar por fecha de creación. La primera busca las tareas de la fecha indicada exactamente. Y la segunda, busca las tareas más recientes apartir de la fecha indicada. *Date es de tipo string y se espera un formato YYYYMMDD (ej. 20211019) 
	- http://127.0.0.1:8000/filter_date_eq/*date
	- http://127.0.0.1:8000/filter_date_gt/*date
- Filtrar/buscar tareas por el contenido de la misma: http://127.0.0.1:8000/filter_content/*contenido *contenido es la cadena de texto por la que se desea filtrar.
