# Full-Stack Data Analytics Platform

This project is a real-time, full-stack data analytics platform that integrates web development, data engineering, DevOps, and cloud infrastructure into a single cohesive system.

---

## Repository Structure

```
fullstack-data-analytics-platform/
├── backend/                 # Flask API and PostgreSQL integration
├── frontend/                # HTML/CSS templates, Plotly & Matplotlib visualizations
├── data_pipeline/           # ETL workflows, notebooks, and data processing scripts
├── docker/                  # Docker configurations for local deployment
├── terraform/               # Infrastructure-as-Code for AWS deployment
├── .github/workflows/       # GitHub Actions for CI/CD automation
├── Jenkinsfile              # Jenkins pipeline definition
└── README.md
```

---

## Features

### Backend  
- Developed with **Flask**
- Connects to a **PostgreSQL** database
- Exposes endpoints for data querying and analytics

### Frontend  
- Built using **Flask templating**, **HTML/CSS**
- Includes interactive dashboards powered by **Matplotlib** and **Plotly**

### Data Pipeline  
- Built with **PySpark**, **Pandas**, and **NumPy**
- Performs ETL operations and batch processing
- Includes Jupyter notebooks for data exploration

### CI/CD & DevOps  
- Automated builds with **Jenkins** and **GitHub Actions**
- Packaged and deployed via **Maven**
- Includes pipelines for testing, building, and deploying updates

### Cloud Deployment  
- Hosted on **AWS EC2** and **S3**
- Access and security managed with **IAM roles and policies**

### Containerization  
- Application is fully containerized using **Docker**
- **Docker Compose** used for multi-container orchestration

### Code Quality & Security  
- **SonarQube** integrated to maintain clean, secure code
- Static code analysis included in the CI/CD pipeline

### Development Tools  
- Developed using **VS Code**
- Data exploration and prototyping in **Jupyter Notebook**
- Uses Python **virtual environments** for dependency isolation

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fullstack-data-analytics-platform.git
   cd fullstack-data-analytics-platform
   ```

2. Set up virtual environments and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r backend/requirements.txt
   ```

3. Run the Flask app:
   ```bash
   cd backend
   python app.py
   ```

4. Run ETL pipeline:
   ```bash
   cd data_pipeline/etl
   python run_etl.py
   ```

---

## Deployment

### Local (Docker Compose)
```bash
cd docker
docker-compose up --build
```

### Cloud (AWS with Terraform)
```bash
cd terraform
terraform init
terraform apply -auto-approve
```

---

## CI/CD

- GitHub Actions configured in `.github/workflows/`
- Jenkins pipeline defined in `Jenkinsfile`
- Automatically triggers on pushes and pull requests to main
