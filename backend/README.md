
# Inventory Tracker Server 
### Introduction
Inventory Tracker checks local websites for stock updates of new items. It provides alerts to users when it notices a change. A low update interval is used to minimize traffic on the vendors' networks.

### Features
* Public users can view inventory information for all vendors
* Users can sign up for and login into their accounts
* Authenticated users can create, edit, and delete alerts for stock updates

### Requirements
* A Linux environment 
* Python 3.10.6
* Redis
* PostgreSQL

### Installation/Usage
* Create a virtual environment, activate it and install the libraries from the requirements.txt file.  
    ```
    python3 -m venv /path/to/new/virtual/environment
    source <venv>/bin/activate
    pip install -r requirements.txt
    ```
* Make sure your PostgreSQL and Redis services are enabled and running. This project uses the Redis Queue library. You can create as many workers as needed by running the command within the virtual environment. Set them to follow the 'tracker-tasks' queue.
    ```
    rq worker tracker-tasks
    ```
* Create a .env file in the root directory, include your PostgreSQL database URI and JWT secret. You can also provide a Redis url if you aren't using `redis://`.
    ```
    /.env  
    DATABASE_URI=postgresql+psycopg2://[user]:[password]@[address]:[port]/[database]
    SECRET_KEY=you-will-never-guess-this
    REDIS_URL=
    ```
* Upgrade your database to match the necessary schema. This project uses `Flask-Migrate` to manage databse migrations. After any changes to the models a migration must be created with `flask db migrate -m "Migration description."`, the database must then be upgraded again.
    ```
    flask db upgrade
    ```
* Running `flask shell` will create a shell environment within the app context. It has access to a variety of tools to manage the database. Use this to add a database entry to for each vendor you support. 
    ```
    flask shell
    add_vendor(name = "Test Vendor", url = "testurl.com")
    ```
* You can now run the application  with `flask run`.    

### Endpoints


| HTTP Verbs | URI | Action | Authentication |
| --- | --- | --- | --- |
| GET | / | Retrieves a list of vendors supported by the api | |
| GET | /:vendor | Retrieves basic information about a vendor |  |
| GET | /:vendor/inv | Retrieves a list of the vendor's inventory | |
| GET | /:vendor/:item_id |Retrieves information about a specific item | |
| POST | /auth/signup | To sign up a new user account |
| POST | /auth/login | To login an existing user account | Basic Auth |
| GET | /:user | Retrieves data for a user | JWT Required |
| POST | /:user | Update user information and settings | JWT Required |
| DELETE | /:user | Deletes the selected user | JWT Required |
| GET | /:user/alerts | Retrieves a list of the user's alerts | JWT Required |
| POST | /:user/alerts | Creates a new alert for a user | JWT Required |
| GET | /:user/:alert_id | Retrieves a specified alert | JWT Required |
| POST | /:user/:alert_id | Updates a specified alert | JWT Required |
| DELETE | /:user/:alert_id | Deletes a specified alert | JWT Required |
| GET | /search?vendor_name=:vendor&terms=:terms | Returns results after searching vendor inventory |


### Authenticating Requests
Login requests should include a Basic Auth header. Requests that require a JWT should recieve one from `/auth/login` and includes it in their `'access-tokens'` header.

### Flask Shell Commands
| Command | Description |
| --- |  --- |
| db | The SQLAlchemy database object. You can read about how to use this to manipulate the databse in the SQLAlchemy docs. |
| Vendor, Item, User, Alert | The ORM models for creating and querying data. |
| add_vendor(name= {Vendor Name}, url= {Vendor URL}) | Add a vendor to the database with the supplied parameters. |
| drop_records(table: db.Model) | Drops all records  in the provided table.|
| updater.run() | Runs the web scrapers to update the inventory items. |

### Technologies Used

### Authors

### License
