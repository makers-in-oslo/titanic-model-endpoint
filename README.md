# Endpoint for a titanic ML model

- Models contain pickled scikit-learn models
- The app contains a single end point which accepts POST requests
- The payload must be key-value pairs, where the keys are the column headings in the Titanic dataset from Kaggle

```
{
    "pclass":1,
    "sex":"female",
    "age":22.0,
    "sibsp":1,
    "parch":0,
    "fare":7.25,
    "embarked":"S",
    "name":"Dr. D", 
    "cabin": "KingPing",
    "ticket": "Some 1234",
    "passengerid":123
}
```

The .yml files are used to create a conda environment
- environment-dev.yml titanic-ml-endpoint-develop
- environment2.yml titanic-ml-endpoint

The dev environment contains packages not needed to deploy the app

