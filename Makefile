migrations:
	./manage.py makemigrations && ./manage migrate && heroku run python manage.py migrate --app stonkstracker