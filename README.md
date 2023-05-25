## Activate the vertual env
```
 source venv/bin/activate
```
## launch the project


```
 
 python3 manage.py  runserver

```
## Create a buckup to migrate the DB to Supabase:
```
  pg_dump --host=localhost --username=pgadmin -d nourportfolio -f backup.sql

```

