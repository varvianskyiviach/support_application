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
python src/manage.py collectstatic
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

## Deployment Process (for example DigitalOcean)

## Steps
- ### Install and prepare Droplet
1. Sign up for a DigitalOcean account and create a new Droplet (a virtual machine running Linux). Instruction [DigitalOcean](https://docs.digitalocean.com/products/droplets/how-to/create/).
2. SSH connect into your Droplet.
3. Install Docker and Docker compose in your server
    - Option 1 from - [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)

    - Option 2 from - [Docker](https://docs.docker.com/engine/install/ubuntu/)

4. Intro your Droplet Generate and add to Git hub SSH key [tap](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

  
- ### Deployment project
1. Clone your project
2. Create production ".env" file based on ".env.default"'

    ```bash
    # copy file
    cp .env.default .env,
    ```
    - set up
    DJANGO_ALLOWED_HOSTS=*,

3. docker-compose.yaml
    - delete string ports
    'ports: 5432:5432'

4. Start the project
    ``` bash
    # run project from docker
    docker compose up -d   

    # make migrations
    docker compose exec app python src/manage.py migrate

    # create superuser
    docker ompose exec app python src/manage.py createsuperuser 
    ```