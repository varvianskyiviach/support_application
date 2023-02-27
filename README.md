# Project support application

## Start
...
## <span style='color:red'>Installing</span>

### <span style='color:yellow'>Instal Deps</span>
```bash
# install pipenv
pip install pipenv

# activate virtual env
pipenv shell

# install deps
pipenv sync --dev
```
### <span style='color:yellow'>Collecting static files</span>
```bash
# copy all static files to the directory "staticfiles" 
python src\manage.py collectstatic
```
### Additional

```bash
# regenerate Pipfile.lock file
pipenv lock

# pipenv lock & pipenv sync
pipenv update
```
\
## Usage code quality tools
The pre-commit hook will be automatically run

You can use the code quality checkers on GitHub CI

\
## <span style='color:red'>Run using Docker Compose</span>
```bash
docker-compose up -d
```
### Usefull commands

```bash
# Build images
docker-compose build

# Stop containers
docker-compose down

# Restart containers
docker-compose restart

# Check containers status
docker-compose ps
```

### Logs
```bash
# get all logs
docker-compose logs

# get specific logs
docker-compose logs app

# get limited logs
docker-compose logs --tail 10 app

# get flowed logs
docker-compose logs -f app
```