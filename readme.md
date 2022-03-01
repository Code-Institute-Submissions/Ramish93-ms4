# Takhleeq Kada
This repo contains the code for Takhleeq Kada

## Branches
* Release branch is public facing. Any code pushed to this branch will immediately go live
* Master branch is pre-prod and is used for testing and code sharing between developers

## Contributing

#### Technology Stack
* Python 3.9+ - [Official Download Link](https://www.python.org/downloads/)
* Django 4.0.1 - [Official Link](https://www.djangoproject.com/)
* Postgres 11.3+ - [Official Download Link](https://www.postgresql.org/download/) (Provided by Heroku in our case)


#### Development Setup
##### Git & Clone Code
Download and
[add SSH key](https://docs.gitlab.com/ee/ssh/)
before cloning the project. To clone project run
```bash
git clone git@github.com:Ramish93/ms4.git
```

HTTPS clone can also be used
```bash
git clone https://github.com/Ramish93/ms4.git
```

##### Virtual Environment
Create and activate virtual environment and then install the requirements.
```bash
cd ms4
python -m venv .venv                     # First time

# windows
. ./.venv/Scripts/activate               # In every new terminal window
# Linux 
. venv/bin/activate                      # In every new terminal window

pip install -r requirements.txt          # First time, and if new package is added
python manage.py runserver               # Run localserver
python manage.py makemigration           # Run for making changes in DB
python manage.py migrate                 # Run for perfom chanegs in DB
python manage.py showmigrations          # Run for see the status of migrations
```

Access Website at: [localhost:8000](localhost:8000)

## Deploy
1. Install heroku CLI from the official link: [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)
2. Login into the CLI / Terminal
3. Make the changes
4. Add all the changes `git add --all`
5. Commit them `git commit -m "<Message to explain changes>"`
6. Push to github `git push origin master`
7. Deploy to heroku `git push herku master`
8. SOMETIMES: If you have the database migrations run additionally `heroku run python manage.py migrate`
9. SOMETIMES: If you have the changes in static files (logo etc) `heroku run python manage.py collectstatic`


### Accessing Deployed Applications
[https://ms4-takhleeq-kada.herokuapp.com/](https://ms4-takhleeq-kada.herokuapp.com/)
