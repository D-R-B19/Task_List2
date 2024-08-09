# To-Do-List Application in Python using Flask

## Setting Up the Application

### Step 1: Create a Virtual Environment

```bash
 python3 -m venv venv
 source venv/bin/activate
 ```

### Step 3: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 4: Run App and Tests

```bash
python3 main.py --> for running the App

```
### Step 5: Dockerization

```bash
Docker installation
Dockerfile creation 
.dockerignore creation 
docker build -t firstimage .
docker run -it -p5000:5000 firstimage  
----------------
Docker hub || push from local to hub registery
docker login
docker tag loca_repo_name username/dockerhub_reponame:tag
docker push username/dockerhub_reponame:tag
----------------
Docker hub || pull from docker hub registery to docker client(local)
docker pull (containeror image name)
docker run (containeror image name)