🌍 Currency Tracker API
A production-ready currency tracking API built with FastAPI, Docker, SQLite and external financial API integration.
This project fetches real-time exchange rates (USD/BRL and EUR/BRL), stores them in a database, and exposes REST endpoints for querying both the latest rate and historical data.
Designed as a backend foundation for financial systems and future cloud-native architecture.
🚀 Features
✅ Real-time currency quotation (USD & EUR)
✅ External API integration (AwesomeAPI)
✅ Persistent storage with SQLite
✅ RESTful API design
✅ Frontend integration (HTML + JavaScript)
✅ Dockerized environment
✅ Clean architecture structure (service, repository, schema layers)
🏗 Architecture Overview
Copiar código

Client (HTML + JS)
        ↓
FastAPI Application
        ↓
Service Layer (External API Integration)
        ↓
Repository Layer (Database Persistence)
        ↓
SQLite Database
Project structure:
Copiar código

app/
│
├── main.py
├── config.py
├── database/
├── model/
├── repository/
├── schema/
├── service/
├── static/
└── templates/
📡 API Endpoints
Get Current Exchange Rate
Copiar código

GET /cotacao/{currency}
Example:
Copiar código

/cotacao/USD
Response:
Json
Copiar código
{
  "currency": "USD",
  "value": 5.42
}
Get Historical Data
Copiar código

GET /historico
Returns the last stored exchange rates from the database.
⚙️ Environment Variables
Create a .env file:
Copiar código

API_URL=https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL
DATABASE_URL=sqlite:///./currency.db
APP_ENV=development
🐳 Running with Docker
Build the image:
Copiar código

docker build -t currency-api .
Run the container:
Copiar código

docker run -p 5000:8000 currency-api
Access:
Copiar código

http://localhost:5000
💻 Running Locally (Without Docker)
Install dependencies:
Copiar código

pip install -r requirements.txt
Run server:
Copiar código

uvicorn app.main:app --reload
🧠 Technical Decisions
FastAPI
Chosen for:
High performance
Automatic OpenAPI documentation
Strong typing with Pydantic
Layered Architecture
Separation of concerns:
service → External API logic
repository → Database operations
schema → Response validation
model → Database models
This structure prepares the project for scalability and microservice evolution.
📊 Future Improvements (Roadmap)
This project is evolving toward a production-grade financial microservice architecture.
Planned upgrades:
☁️ Cloud Infrastructure
Deploy on AWS
Infrastructure as Code using Terraform
Amazon RDS (PostgreSQL)
Docker + ECS or Kubernetes
🔐 Security Layer
Implement encryption/hash validation using .NET microservice
Secure secrets management (AWS Secrets Manager)
JWT authentication
📈 Data & Analytics
Historical trend analysis
Currency volatility metrics
Integration with financial dashboards
Chart.js frontend visualization
🧩 Architecture Evolution
Event-driven architecture with Kafka
Task orchestration with Airflow
Background jobs for scheduled currency updates
CI/CD pipeline
🎯 Purpose of the Project
This project is part of a backend/data engineering portfolio focused on:
Financial systems
International market data
API integration
Scalable architecture design
Cloud-ready backend services
🛠 Tech Stack
Python 3.11
FastAPI
Pydantic
SQLite
Docker
JavaScript (Fetch API)
Jinja2 Templates
📌 Author
Pedro Luis 
Data engineer| Financial Systems Enthusiast
Focused on international market technologies and scalable architecture.