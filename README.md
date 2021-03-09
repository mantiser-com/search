# Mantiser Search


Mantiser search find pages and url based on a search word.
The url are then added to a nats que ore printed into stout in json 


In the docker compose we also include a nats image to test the nats output.


The search prash is added by env settings 

      SEARCH: "mattias"
      
      

# Config
All config is done my env settings

- NATS: nats
Tells whats nats server to use


- SEARCH: "mattias"
Search word to search for




# Install

Create folder fins (Ore what you want)

```
git@github.com:mantiser-com/search.git
```


# Setup Docker Compose

Copy the docker-compose.yaml fil from the cp folder to the *fins folder* (In the fins-manager repo) (ORe what you called it)


# Buld and run
In the fins folder (ORe what you called it)



Build
```
docker-compose build
```

Run
```
docker-compose up
```

When you devlope you can set so the docker only trace fstab and you can exec into the contaner and start the service from inside the docker. 
This is good when you develope.

1. Set docker-comopse to use fstab

```
command: tail -f /etc/fstab
```
2. Start up with docker compose

```
docker-compose up
```

3. Exec into the continer

find the container
```
docker ps
```
Exec into
```
docker exec -it "ID OF CONTANER" sh 
```

4. Start the service

```
python3 run.py
```



