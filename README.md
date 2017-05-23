# Intro

I implemented the exercises in Python 2.7.10 with Django and Django Rest Framework. I am used to work on this stack so my choice was based on confort and

# How to run application

1. Edit messenger/settings.py with DB credentials
2. Restore db/setup.sql to a database
3. pip install -r requirements.txt
4. ./manage.py runserver --noreload

# How to run tests

1. ./manage.py test



# List of Unit Tests

1. (Implemented) Test if a conversation with no messages accept a creation of a new one
2. (Implemented) Test if a conversation between userA and userB blocks a creation of a message from userC as a receiver
3. Test if a conversation between userA and userB blocks a creation of a message from userC as a sender
4. Test if user does not exists
5. Test if conversation does not exists


# Comments

The DB script provided had some issues that I detailed them below, therefore I changed or fixed them:

- In the table "user" the field "full name" had a empty space on its name
- In the table "conversation" the field "create_at" is missing a 'd', which is not consistent with "created_at" from "message" table

