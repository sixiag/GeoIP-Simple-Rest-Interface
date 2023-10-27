# GeoIP-Simple-Rest-Interface
A command line interface (CLI) tool that queries the IPStack API and obtains the latitude and longitude of an IP address.

#### Tested with Python 3.8

### Features
* Accept a command line parameter of an IP address and a valid API key.
* Check if an IP address is valid.
* Query the IPStack API for a result over the network.
* Retrieve the latitude and longitude data for any IP address.
* Run the tool directly from the Unix environment or in a docker container.

---

### Command Line Usage
```bash
$ geoip -h
usage: geoip [-h] -i IP -k KEY

optional arguments:
  -h, --help         show this help message and exit
  -i IP, --ip IP     IP address to query.
  -k KEY, --key KEY  Your API key.
```

#### Example
```bash
$ geoip -i 134.201.250.155 -k [your_api_key]
{
  "latitude": 34.0655517578125,
  "longitude": -118.24053955078125
}
```

### Build and Install Tool in Virtual Environment
You can always directly install the tool in your system, but I would recommend creating a virtual environment and installing it there.
```bash
# Create a venv folder
$ virtualenv -p /usr/bin/python3 venv

# Activate the virtualenv settings
$ source venv/bin/activate

# Change to folder Geo-Simple-Rest-Interface folder and install the tool
$ pip install .

# Run the command
$ geoip -i [ip] -k [api_key]
```

### Build and Start a docker container
```bash
# Change to folder Geo-Simple-Rest-Interface folder
# Build the docker image (with name geoip_app)
$ docker build -t geoip_app .

# Start a docker container
$ docker run -ti -d geoip_app

# Check the running containers
$ docker ps

# Access the command line of the container
$ docker exec -ti [container_id] bash

# Run the command in 
root@[container_id]:/run# geoip -i [ip] -k [api_key]
```
