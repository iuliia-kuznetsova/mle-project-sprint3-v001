Добро пожаловать в репозиторий-шаблон Практикума для проекта 3 спринта. Цель проекта — вывести готовую модель для оценки цен на недвижимость в продакшен. 

Полное описание проекта хранится в уроке «Проект. Релиз модели в продакшен» на учебной платформе. 

Здесь укажите имя вашего бакета:
s3-student-mle-20250101-65b9b79fea

# ---------- DIRECTORY STRUCTURE ---------- #

mle-project-sprint3-v001/
│
├── venv/                                               # Virtual environment
├── services/
│   ├── instructions
│   │   ├── Instructions_stage_1.md                     # Instructions for Stage 1
│   │   ├── Instructions_stage_2.md                     # Instructions for Stage 2
│   │   ├── Instructions_stage_3.md                     # Instructions for Stage 3
│   │   └── Instructions_stage_4.md                     # Instructions for Stage 4
│   ├── ml_service/
│   │   ├── __init__.py
│   │   ├── main.py                                     # FastAPI microservice entry point
│   │   ├── model_handler.py                            # Model loading & prediction class
│   │   ├── query_check.py                              # Validation of API inputs class
│   │   ├── metrics.py                                  # Custom Prometheus metrics
│   │   └── load_test.py                                # Load simulation script
    ├── ml_service
│   │   ├── __pycache__
│   │   ├── __init__.py
│   │   ├── main_stage_1_2.py                           # FastAPI microservice entry point for Stage 1 and 2
│   │   ├── main_stage_3_4.py                           # FastAPI microservice entry point for Stage 3 and 4
│   │   ├── model_handler.py                            # Model loading & prediction class
│   │   ├── query_check.py                              # Validation of API inputs class
│   │   └── test_api.py                                 # Testing script
│   ├── models
│   │   ├── .gitkeep
│   │   └── best_model_hyperparameter_optimization.pkl  # Trained model
│   ├── prometheus
│   │   └── prometheus.yml                              # Prometheus configuration file
│   ├── test_data/                                          # Data for testing API
│   │   └── test_data.csv
│   ├── .env                                            # Environment variables
│   ├── docker-compose.yaml                             # Docker Compose configuration
│   ├── Dockerfile_stage_1_2                            # Docker build instructions for Stage 1 and 2
│   └── Dockerfile_stage_3_4                            # Docker build instructions for Stage 3 and 4│
├── .gitignore                                   
├── dashboard.jpg                                       # Screenshot of Grafana dashboard
├── dashboard.json                                      # Grafana dashboard exported
├── fix_datasource_uid.py
├── Monitoring.md                                       # Dashboard & metrics explanation
├── README.md                                           # Short project overview
└── requirements.txt                                    # Python dependencies