# CAAS - CV As A Service


## Structure

The schema (*where all the magic happens*) is in [cv/schema.py](./cv/schema.py).
> Look ma, a GraphQL integration with Django models in less than 150 LOC!


## Deploying locally

You can also have your own GraphQL cv example running on locally.
Just run the following commands and you'll be all set!

```bash
git clone git@github.com:zwant/caas.git
cd caas

# Make a virtualenv
virtualenv env
source env/bin/activate
# Install the requirements
pip install -r requirements_base.txt


# Setup the db and load the fixtures
python manage.py migrate
```

Once you have everything done, just run:

```bash
python manage.py runserver
```

Open your browser and visit [localhost:8080](http://localhost:8080/) et voilá!

**For querying the schema we recomend using [/graphiql](http://localhost:8080/graphiql)**
