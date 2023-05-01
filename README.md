# Recommendation-system

To run this project  you need to install first python and pip

```bash
  sudo apt install python3
  pip install --upgrade pip 
```

After install the requirements from requirements.txt by the following command
```bash
  pip install -r requirements.txt
```

Second option

Setup and run the application on a docker container

First you need to create the docker image

```bash
  docker build -t recommendation_system_flask .
```
Then create the docker container and run it 

```bash
  docker container run -d -p 8000:8000 recommendation_system_flask
```

The aplication runs on port 8000 , test by enter localhost:8000 on your browser
