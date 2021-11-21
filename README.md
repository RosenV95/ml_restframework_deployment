# ml_restframework_deployment	
A simple django rest API project I made from following several tutorials for deploying machine learning and deep learning algorithms as I wanted to learn more about how deployment of machine learning services actually works despite in a trivial environment.	

The algorithms are adjusted to work with the bankfull.ods dataset, which is a binary classificaiton dataset based on marketing data provided by a bank on whether or not a certain client buys a product dependent on multiple factors like age, employment status, home ownership and else. The algorithms can be adjusted to work pretty much for any problem as long as slight tweaks are made.	
To run locally:	
- install requirements.txt	
- run python manage.py runserver	
- open localhost:8000/api/v1/bank_classifier/predict	
- the data payload should be in a json format	
- sample input: {"age": 31, "job": "student", "marital": "married", "education": "university.degree", "default": "no", "housing": "yes", "loan": "no", "contact": "cellular", "month": "may", "day_of_week": "thu", "duration": 90, "campaign": 1, "pdays": 999, "previous": 0, "poutcome": "nonexistent", "emp.var.rate": 1.4, "cons.price.idx": 93.994, "cons.conf.idx": -36.4, "euribor3m": 4.857, "nr.employed": 5228.1}	

To run with docker	
- Change the default.conf db volume to your own local path	
- Run docker-compose up --build	
- localhost:8000/api/v1/bank_classifier/predict and use the same way as above.	

You can see the active MLalgorithms on localhost:8000/api/v1/mlalgorithms	
