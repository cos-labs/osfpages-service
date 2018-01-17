# <img src="https://cdn.cos.io/media/images/cos_center_logo_small.original.png" alt="alt text" width="22px" height="22px">  OSFPages (service)

OSF Pages is an Open Science Framework (OSF) addon and website builder that helps OSF users build beautiful websites very quickly using their existing project details. OSF Pages doesn't need additional hosting or management and it's free and open source.

## Prerequisites

You will need the following things properly installed on your computer.

* [Git](http://git-scm.com/)
* [Python3](http://python.org/)
* [Postgresql](http://postgresql.org/)

## Installation

#### Get the code:

    $ git clone https://github.com/cos-labs/osfpages-service.git
    $ cd osfpages-service
    
    #### Install Dependencies:

Setting up a virtual environment for Python 3 is recommended.

    $ pyenv virtualenv 3.6.0 osfpages-service
    $ pip install -r requirements.txt

#### Set Up Postgres:

##### OSX

    $ brew install postgres
    $ createdb
    $ brew services postgres start


### Running Tests

* `python manage.py test`
