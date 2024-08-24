**Zlecaf E-commerce in Africa**
*SABO bachir* 

# Application Setup Instructions

Before launching the application, it's required to set up a database and install certain packages.

## 1. Package Installation

The packages that our application depends on are listed in the `requirements.txt` file, along with the compatible Python version (3.6). To install them, execute the following command in the terminal:

```bash
pip install -r requirements.txt
```

## 2. Database Setup

Several files are located in the `bdd` directory. Among these files, there are two SQL files that need to be copied and executed in an SQL query editor, as well as a Python file that needs to be run in your IDE. The class that facilitates the connection between the application and the database can be found in `dao/pool_connection.py`, where you will find all the necessary information regarding this connection. (The articles to populate the database were scraped from several e-commerce sites between July and September 2021).

## 3. Launching the Application

After setting everything up, you can launch the application in your IDE by running the `main.py` file located at the root of the project, or by executing the following command in the terminal:

```bash
python3 main.py
```

Alternatively, on some operating systems, you may need to use:

```bash
python.exe main.py
```

## Additional Documentation

The PDF file `Rapport_Zlecaf_Beta_App` provides a better understanding of the Zlecaf's challenges in terms of exploiting e-commerce sites. It also outlines the steps involved in setting up this application. (Note that this application is just a prototype that will serve as a plan for a more comprehensive architecture).

Thank you for your attention!