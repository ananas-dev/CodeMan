# CodeMan

CodeMan is a BOT to manage slippi connect codes for ssbm.

## Installation

```sh
pip install -r requirements.txt
```

## How to make it work

To make the bot work you have to change 4 variables:

ENTERTOKENHERE in bot.py with your bot token

DBTOKEN in db.py with your database token (using mongodb)

DBNAME in db.py with the name of the db and DBCOLLECTION with the collection of the db (using mongodb)

## Here is a list of commands:

`&add`

Adds your connect code to the database.

> Ex: &add NNAS#903

`&code`

Shows your code or the one of someone else.

> Ex: - &code - &code @someone

`&whois`

Finds a discord username from a code.

> Ex: whois NNAS#903

`&ask`

Asks for you if someone want to play.

> Ex: &ask @netplay

`&how`

to Shows this message.