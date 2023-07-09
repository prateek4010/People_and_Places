# PEOPLE AND PLACES

A python app for processing data from csv. Also includes inserting and fetching data from MYSQL.

### App directory 
To run the process, move to the app directory.
Run the following command:
```bash
cd people_and_places
```

### Build containers
The docker-compose file describes a local setup consisting of MySql and App containers.
To create the containers, run the following command:
```bash
make build
```

### Getting the containers up
To start the all containers, run the following commands.
```bash
make run
```

If you want to restart the app container only:
```bash
make run-app
```

### Stop Services
To stop the services, run the following command:
```bash
make stop-services
```