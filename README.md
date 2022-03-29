# API

# Getting started
1. run `pip3 install -r requirements.txt` to install required dependencies

# .env configuration
Create a `.env` file in your /API directory, and add the following key value pairs:
    1. DATABASE_URL
    2. (Optional) - include the key/value pair `DEBUG=True` to have the flask server run in debug mode

# Linting
1. We've disabled # pylint: disable=no-member in order for pylint to not complain about SQLAlchemy errors.