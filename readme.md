## Project Goal
I want to build a simple to use API that allows users to upload a dataset, generate multiple machine learning models and receive an endpoint at which to make predictions in the future
## Project Structure
- app.py - Flask API file
- test.py - Used for testing ML model stuff in console application
- data_tools/
    - csv_tools.py - tools for loading and parsing a CSV
    - loading.py - tools for saving and loading persistent ML models
- datasets/
    - Keeps all datasets uploaded to API. Will be transitioning to some sort of blob storage
- ml_models/
    - sklearn.py - Wrapper for any sklearn models we decide to support
    - my_models.py - Wrapper for any custom ML models we want to implement
- saved_models/
    - Used as storage of persistent ML models