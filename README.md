# TestCoil

All of these codebase used as technical test with `Coil`.  I'm using my own's skeleton
python rest api app, listed [here](https://github.com/hiraq/base-sanic).  This REST api engine
using MongoDB as main database, you can use docker or install mongo in your host OS.

API endpoints :

**News**

- `/v1/news` [POST] - For create new news content
- `/v1/news` [GET] - For getting all saved content news
- `/v1/news/<id>` [GET] - Get single news
- `/v1/news/<id>` [PUT] - Update single news
- `/v1/news/<id>` [DELETE] - Delete single news

**Topics**

- `/v1/topics` [POST] - For create new news content
- `/v1/topics` [GET] - For getting all saved content news
- `/v1/topics/<id>` [GET] - Get single news
- `/v1/topics/<id>` [PUT] - Update single news
- `/v1/topics/<id>` [DELETE] - Delete single news

## Stacks

- Main programming language: `Python3`
- Framework: [Sanic](https://github.com/channelcat/sanic)
- Configuration: [Python Dotenv](https://github.com/theskumar/python-dotenv)

Dependencies:

- Sanic (of course)
- Python dotenv: Manage environment variable for configurations
- aiohttp: Async http client/server library (actually you should got this lib from sanic itself, i just need to make sure about it)
- Fabric3: Manage automated tasks

---

## Getting Started

Install dependencies :

```
pip install -r requirements.txt
```

Start sanic:

```
python main.py
```

Start with debug:

```
python main.py --debug
```

Enable access logs:

```
python main.py --access
```

Read more about command line options:

```
python main.py -h
```

Dockerized:

build:

```
docker build -t testcoil:0.1 .
```

run:

```
docker run --name testcoil -e MONGO_HOST=<mongo_host> -p 8080:8080 -d testcoil:0.1
```

---

## Structures

`apps` 

Put all of your apps here.  I'm just following Django modular apps here.

`core`

This place used to put all core library (not business logic) like for helpers
and also for sanic's extensions like custom exception handler or custom middlewares.

`main`

You need to install all of your apps or extentions by registering their `blueprint`,
for more detail, you can see the code inside `main.py`.

---

## Settings

We are using `python-dotenv` to manage all of your configurations.  There is file named
with `env.default` , put all of your config keys here (do not put your sensitive values, like
your api key).  You need to copy and rename the file to `.env` (this file listed at `.gitignore`),
and configure your configuration key and values in this file (`.env`).

You need to add all of those configurations to `settings.py`, then all your configurations will
be loaded inside sanic's lifecycle, you can access these configurations from your blueprint's apps, using
`request.app.config`.

---

## Automate Tests & Tasks

I'm also a fan of automated tests.  This skeleton also provide a basic structures that _maybe_ you 
will need it to manage all of your tests.

For all tests it will separated by their modules, examples:

- tests/apps
- tests/core

It will help you to select your context when running test. 

Besides of automated tests, this skeleton also provide basic automated tasks using [Fabric3](https://github.com/mathiasertl/fabric/).

You can setup your tasks in `fabfile.py`.  An example to run your tests:

```
fab test:apps
```

Test news app:

```
fab test:apps/news
```

Test topics app:

```
fab test:apps/topics
```
