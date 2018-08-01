python manage.py runserver # run application

python manage.py makemigrations # Make migration # To create SQL for migration
python manage.py migrate # To migrate models change
python manage.py sqlmigrate flights 0001 # See the actual SQL details
python manage.py shell # also you to interact in a shell mode

In apps.py isnert class FlightsConfig(AppConfig) name ='flights'
In settings.py, add "flights.apps.FlightConfig"