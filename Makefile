
env: env/bin/activate

env/bin/activate: requirements_base.txt
	  test -d env || virtualenv env
	  env/bin/pip install -Ur requirements_base.txt
	  touch env/bin/activate

serve: env db.sqlite3
	(\
		source env/bin/activate; \
		python manage.py runserver; \
	)

resetdb: env
	rm db.sqlite3
	make db.sqlite3

db.sqlite3:
	make migrate
	touch db.sqlite3

migrate: env
	(\
		source env/bin/activate; \
		python manage.py migrate; \
	)
