
# Notes


## Creating a local environment:

````
py -3 -m venv venv
venv\Scripts\activate.bat 
venv\Scripts\deactivate.bat 
````

## Starting the web server

````
uvicorn app.main:app --reload
````


### Change Windows Envronment Variable

* rundll32 sysdm.cpl,EditEnvironmentVariables


````
pip install alembic

````



* /verions/ tabellen (columns) upgraden/ downgraden zu bestimmten Zeitpunkten



````
venv\Scripts\activate.bat
git add --all
git commit -m "fehlerbehebung"
git push origin main
heroku login
git push heroku main 
heroku ps:restart 
heroku run "alembic upgrade head"
````
