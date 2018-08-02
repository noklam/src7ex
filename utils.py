python manage.py runserver # run application

python manage.py makemigrations # Make migration # To create SQL for migration
python manage.py migrate # To migrate models change
python manage.py sqlmigrate flights 0001 # See the actual SQL details
python manage.py shell # also you to interact in a shell mode

from  flights.models import Flight
f = Flight(origin="New York", destination="London", duration=420)
f.save()
Flight.objects.all()

from flights.models import Airport, Flight
jfk = Airport(code="JFK", city="NY City")
lhr = Airport(code="LHR", city="London")
jfk.save()
lhr.save()
f = Flight(origin=jfk, destination=lhr, duration=415)
f.save()

In apps.py isnert class FlightsConfig(AppConfig) name ='flights'
In settings.py, add "flights.apps.FlightConfig"

python manage.py createsuperuser