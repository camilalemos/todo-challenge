#install with: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt 
#run with: python manage.py runserver

#Para correr el log se deberá crear el archivo ToDo_Log.log en la ruta /var/log/ y darle permisos de r/w/x:
- sudo touch /var/log/ToDo_Log.log 
- sudo chmod 777 /var/log/ToDo_Log.log