# tour-tag
Embedded systems development Tour-Tag

## Setup
To run this project, clone the repository 

```
$ git clone https://github.com/ullallulla/tour-tag.git tourtag

```
activate your virtual environment

cd to tourtag that you just created

install requirements

```
$ pip install -r requirements.txt

```
create .env file to the root of tourtag directory

add a secret key to  .env

```
SECRET_KEY=your-secret-key

```

setup flask while being in the tourtag directory

linux
```
$ export FLASK_APP=tourtag

```
move one directory up

```
$ cd ..

```
run flask app

```
$ python3 -m flask run --host 0.0.0.0

```
