# ----- INSTRUCTIONS -----#
# ----- PROJECT STAGE 1: MICROSERVICE USING VENV -----#

'''
  Building and running the FastAPI microservice using virtual environment.
'''
The root directory of the project: /home/mle-user/mle_projects/mle-project-sprint3-v001

# Prerequisites
- docker installed and running
- the root directory of the project: `/home/mle-user/mle_projects/mle-project-sprint3-v001`
- `.env` file located in `services/.env`
- `requirements.txt` file located in the project root
- trained model file is at `services/models/best_model_hyperparameter_optimization.pkl`
- dockerfile `Dockerfile_stage_1_2` in `services/`
- api script `main_stage_1_2.py` in `services/ml_service`

# Create virtual environment
- install extension
```bash
sudo apt-get install python3.10-venv
```
- create .venv
```bash
python3 -m venv .venv
```
- run .venv
```bash
source .venv/bin/activate
```
# Install packages
```bash
pip install -r requirements.txt
```

# Make the .venv to run automatically after this and only this project has been opened
- create .vscode folder 
```bash
mkdir -p .vscode
```
- create settings.json
nano .vscode/settings.json
- add this script into the settings.json
{
    "python.pythonPath": ".venv/bin/python"
}
- check whether virtual environment runs after the project has been opened
```bash
which python
```

# Run virtual environment manually
```bash
source .venv/bin/activate
```

# Check the list of installed packages
```bash
pip list
```

# Deactivate virtual environment if needed
```bash
deactivate
```

# Delete virtual environment if needed
```bash
deactivate
rm -rf .venv
```

# Run all following commands from the root directory 
# Change working directory to the root, if needed
```bash
cd mle_projects/mle-project-sprint3-v001
```

# Run FastApi using uvicorn
```bash
uvicorn services.ml_service.main_stage_1_2:app --reload
```

# Open a new terminal and test the microservice using a Curl request
```bash
  curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "apartment_id": "apartment_test",
    "model_params": {
      "f1": 3.0,
      "f2": 0.0,
      "f5": 2.0,
      "f6": 3.0,
      "f7": 3.0,
      "f8": 3.0,
      "f9": 3.0,
      "f15": 4.0,
      "f17": 4.0,
      "f19": 4.0,
      "f20": 3.0,
      "f21": 1.0,
      "f23": 2.0,
      "f24": 4.0,
      "f25": 4.0,
      "f26": 3.0,
      "f27": 3.0,
      "f28": 3.0,
      "f29": 0.0,
      "f31": 2.0,
      "f32": 3.0,
      "f33": 4.0,
      "f34": 3.0,
      "f35": 3.0,
      "f36": 3.0,
      "f39": 4.0,
      "f41": 4.0,
      "f43": 4.0,
      "f44": 2.0,
      "f45": 4.0,
      "f47": 3.0,
      "f48": 2.0,
      "f49": 3.0,
      "f50": 2.0,
      "f51": 4.0,
      "f52": 3.0,
      "f53": 4.0,
      "f54": 3.0,
      "f55": 3.0,
      "f56": 3.0,
      "f57": 4.0,
      "f58": 3.0,
      "f59": 3.0,
      "f60": 3.0,
      "f61": 3.0,
      "f62": 3.0,
      "f63": 3.0,
      "f64": 3.0,
      "building_type": 2,
      "build_decade": 2010
    }
  }'
```
# Expected response format
{
  'apartment_id': str,
  'price': float
}

# Get access to the microservice front page
Open browser and navigate to http://127.0.0.1:8000

# Get access to interactive API documentation
Open browser and navigate to http://127.0.0.1:8000/docs