# Design of the app

<img src="design.jpg">

## Project check-list
- [x] Create basic structure
- [x] Docker setup (v20.10.2)
- [x] Flask app (default Flask app, requirements)
- [x] Some generic content (Added default structure from documentation)
- [x] Add Blueprints (Model-Template-View)
- [x] Add Jinja2 templates (+ Bootstrap's Font Awesome, generic CSS)
- [x] Added some default content (FAQ's, ToS, Policy Page)  
- [x] Testing (pytest, pytest-cov, flake8)
- [x] Added CLI (Click, added testing commands)
- [x] Flask extension (added debug toolbar)
- [x] Form creation (Celery, WTForms, auto-email setup)
- [ ] Admin Dashboard 
- [ ] Logging and error handling
- [ ] CLI additions
- [ ] Add some functionality
- [ ] Payments + Micro-transactions
- [ ] DB migration

## Run the code:

- Setup Oracle VirtualBox v6.1
- Start Docker Container [Docker: 20.10.2, Docker-compose: 1.27.4]
- Go to the project directory
- Type in terminal:
  
        docker-compose up --build

- My filepath for the app.py folder is based on Windows filesystem

    For Linux:

    Make Changes in docker-compose.yml --> volumes - '.:/snakeeyes' for gunicorn and celery

- For tests: Start another terminal (Docker)
    
        docker-compose exec website snakeeyes test
        docker-compose exec website snakeeyes cov

- The website will be on 'localhost:8000'
- Stop the containers:

        docker-compose stop

- Cleanup the dangling/stopped containers

        docker-compose rm if
        docker rmi -f $(docker images -qf dangling=true)