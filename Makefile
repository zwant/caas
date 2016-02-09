
env: env/bin/activate

env/bin/activate:
	  test -d env || virtualenv env
	  env/bin/pip install -Ur requirements_base.txt
	  touch env/bin/activate

serve: env
	(\
		source env/bin/activate; \
		python manage.py runserver; \
	)

resetdb: env
	rm db.sqlite3
	make migrate

migrate: env
	(\
		source env/bin/activate; \
		python manage.py migrate; \
	)
