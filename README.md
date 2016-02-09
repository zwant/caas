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

# running the serve which will make all deps
make serve
```

Other make targets that you can run. First is the migration. This will simple
running the migration the current database state
```bash
make migrate
```

If you for some reason want to resetdb. This will remove your current database
and create a new one
```bash
make resetdb
```

Open your browser and visit [localhost:8000](http://localhost:8000/) et voilá!

To try submitting data, go to [localhost:8000/cv](http://localhost:8000/cv) .
Here's some example JSON you can use:
```
{
    "introduction": "hello",
    "name": "kalle",
    "work_experience": [
        {"from_date": "2015-12-12",
            "to_date": "2016-02-01",
            "role": "developer",
            "company": "Acme Inc",
            "location": "Göteborg",
            "description": "I did the doings"
        },
        {"from_date": "2015-12-12",
            "to_date": "2016-02-01",
            "role": "developer",
            "company": "Acme Inc",
            "location": "Göteborg",
            "description": "I did the doings"
        }
    ],
    "languages": [{
        "language": "swedish",
        "level": "basic"
    }]
}
```

**For querying the schema we recomend using [/graphiql](http://localhost:8080/graphiql)**
