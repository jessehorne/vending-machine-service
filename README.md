vending-machine-service
=======================

A API written in Python that uses Flask, and is an implementation of the vending machine specified [here](https://github.com/PillarTechnology/kata-vending-machine). This is the minimum acceptable implementation of this project, so please see the [TODO](##TODO) section at the bottom of this README.

---

## Setup for Ubuntu

Please follow the steps in this order. For any assistance, contact me directly.

#### Install pip
```
wget https://bootstrap.pypa.io/get-pip.py

python get-pip.py
```

#### Install virtualenvwrapper and create virtual environment
```
pip install virtualenvwrapper

mkvirtualenv vending-machine-service
```

#### Clone repo and install requirements for project
```
git clone git@bleh.com/vending-machine-service.git

cd vending-machine-service

pip install -r requirements.txt
```
---

## Run the service

```
python vending_machine_service/vending_machine_service.py
```

---

## Run tests
```
pytest test/
```

---

## TODO

more coming soon...
