- [CSC33045-prototype](#csc33045-prototype)
  - [Project Description](#project-description)
  - [Running The Project Using a Virtual Environment](#running-the-project-using-a-virtual-environment)
    - [Accounts](#accounts)

# CSC33045-prototype

## Project Description

This project is a prototype for CSC3045. This prototype has a SQL database and full CRUD functionality. This system also has a fully functioning login system, along with changing the UI for the pages based on who is logged in. Outside of the database, the main pages of the website are mainly just to show the UI of the system and how it would operate, the text inputs for the journal and social worker chat pages does allow users to enter text and this text does then appear on the webpage but it does not update the information in the database or send a message to anyone. Similarly to this the gallery page does not interact with the database as it would in a more complete solution, instead it interacts with the Dog API to retrieve a list of random dog images to display on the website (Note: sometimes this API will return "dead links" meaning that some of the images won't appear, this is not a bug in our code, this is a fault with the API).  

## Running The Project Using a Virtual Environment

1. Clone the repository to your computer.
2. [Install Python 3.7.9](https://www.python.org/downloads/release/python-379/) on your computer if it has not already been installed.
3. Open a terminal window (PowerShell if you're on Windows) on your computer and navigate to the directory where the project has been cloned to. To do this, open the folder where you extracted the repository, then right-click on the folder called "CSC3045-Prototype" and choose "Open in Terminal" (for Linux/Mac) or "Open Powershell window here" (for Windows).
4. In the terminal, create a virtual environment by running the following command, replacing ```<directory to python install>``` with the directory where Python 3.7.9 was installed
   - For example, if Python 3.7.9 was installed in ```C:\Python37```, the command would be: ```C:\Python37\python.exe -m venv .```.

```console
<directory to python install>\python.exe -m venv .
```

5. Activate the virtual environment by running the following command:

- For Windows

```powershell
.\Scripts\activate
```

- For Linux/Mac

```bash
source bin\activate
```

6. Install the required packages by entering the following command into the terminal (keep this terminal open).

```console
pip install -r requirements.txt
```

7. In the terminal run the following command

```console
python manage.py runserver
```

8. Now you can navigate to <http://localhost:8000/> to view the website.

### Accounts

There are 2 access levels to the system “admin” and “child”. Admin accounts have access to the database through the admin panel and have full access to all data, child accounts do not have access to the admin panel, they can see the chat, journal and gallery pages.

- Admin Account
  - Username: admin
  - Password: admin
- Child Account 1
  - Username: lemn
  - Password: h
