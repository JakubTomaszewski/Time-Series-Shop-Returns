# Predicting daily number of returns using time series

## About the project

Some part of the project has been created for a Computer Science course at my University (Warsaw University of Technology). After passing the semester I have decided to develop the project more, by testing more models, adding new features, and deploying them with `Docker`.

---

## Project description

W ramach projektu wcielamy się w rolę analityka pracującego w firmie „eSzoppping” 
– sklepu internetowego z akcesoriami komputerowymi. Praca na tym stanowisku nie jest łatwa – 
zadanie dostajemy w formie enigmatycznego opisu i to do nas należy doprecyzowanie szczegółów 
tak, aby dało się je zrealizować. To oczywiście wymaga zrozumienia problemu, przeanalizowania 
danych, czasami negocjacji z szefostwem. Oprócz analiz i wytrenowania modeli, musimy 
przygotować  je do wdrożenia produkcyjnego –  zakładając, że w przyszłości będą pojawiać się 
kolejne ich wersje, z którymi będziemy eksperymentować. 
Jak każda szanująca się firma internetowa, eSzoppping zbiera dane dotyczące swojej działalności – 
są to: 
• baza użytkowników, 
• katalog produktów, 
• historia sesji użytkowników, 
• dane dotyczące wysyłki zakupionych produktów.

„Chyba w lepszy sposób musimy zacząć obsługiwać zwroty zakupionych u nas towarów. 
Konsultanci narzekają, że nie są w stanie tego inaczej zorganizować w magazynie nie mając 
pojęcia ilu takich przypadków mogą się spodziewać – trzeba im jakoś pomóc.”

---

## Project plan

- Define a business goal
- Define success criteria
- Analyze the data
- Clean the data
- Prepare the data
- Training a model
- Testing
- Dockerizing created models
- Deployment
- Perform A/B Tests

---

## Technologies

- Data analysis and modeling


![Python 3.8](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=blue)
![numpy](https://img.shields.io/badge/Numpy-1.22.4-777BB4?style=for-the-badge&logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/Pandas-1.4.2+-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![scitit-learn](https://img.shields.io/badge/scikit_learn-0.23.2-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=F7931E)

- Deployment

![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![JS](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![React JS](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)


---


## Preparing the environment

The packages used to create this project are located in the [requirements.txt](requirements.txt) file.

For creating a development environment i recommend using conda. Simply run the command below

```shell
$ conda create --name my_env --file requirements/conda_requirements.txt
```

Or install it in an existing environment

```shell
$ conda install --file requirements/conda_requirements.txt
```

If you with to use pip, install the requirements by running the following command

```shell
$ pip install -r requirements/pip_requirements.txt
```


## Launching the app

In order to deploy the model microservice run the following command

```shell
$ docker run -dp 8020:8020 --name returns-prediction-app jtomasz/returns-prediction-app:backend
```

You can also pull the container from DockerHub manually

```shell
$ docker pull jtomasz/returns-prediction-app:backend
```

Or build the image by yourself

```shell
$ docker build -t returns-prediction-app -f Dockerfile_backend .
```


