# US-Visa-Approval-Prediction

- Anaconda: https://www.anaconda.com/
- Vs code: https://code.visualstudio.com/download
- Git: https://git-scm.com/
- MLOPs Tool: https://www.evidentlyai.com/
- MongoDB: https://account.mongodb.com/account/login
- Data link: https://www.kaggle.com/datasets/moro23/easyvisa-dataset

## Problem Statement

With the increasing volume of US visa applications, accurately predicting approval outcomes has become essential. By analyzing key applicant features such as continent, education, job experience, training, employment status, and age, we can build a model that streamlines decision making and enhances processing efficiency.

## Problem Solution

I developed a classification machine learning model to predict US visa approvals based on applicant features. This project encompasses the entire machine learning lifecycle, from data ingestion to deployment.

## Tools & Technologies Used

- **Programming Language**: Python
- **Data Manipulation**: NumPy, Pandas
- **Data Visualization**: Matplotlib, Seaborn
- **Containerization**: Docker
- **Database**: MongoDB (for storing unstructured data)
- **API Development**: FastAPI (for quick API development with automatic interactive documentation), Flask (for creating simple web applications)
- **Model Monitoring**: Evidently (to track changes in data distributions)
- **CI/CD Tool**: GitHub Actions (automates testing and deployment processes)
- **Cloud Services**:
  - **AWS EC2**: Scalable virtual servers to run applications
  - **AWS ECR**: Simplifies management and storage of Docker images
  - **AWS S3**: Scalable storage for data and model artifacts

## Git Commands Used

```bash
git status
git add "Your file name"
git add .
git commit -m "commit message"
git push origin main
```

## How to Run This Project

1. Create a new conda environment:
   ```bash
   conda create -n visa python=3.8 -y
   ```
2. Activate the environment:
   ```bash
   conda activate visa
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Project Workflow

1. Update constants.
2. Update configuration entity.
3. Update artifact entity.
4. Update components.
5. Update pipeline.
6. Update main file.

## Export the Environment Variables

```bash
export MONGODB_URL="mongodb+srv://<username>:<password>...."
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
```

## AWS CI/CD Deployment with GitHub Actions

1. Log in to the AWS console.
2. Create an IAM user for deployment.
3. Create an ECR repository to store the Docker image.
4. Create an EC2 instance (e.g., using Ubuntu).
5. Access the EC2 instance and install Docker.
6. Configure EC2 as a self-hosted runner.
7. Set up GitHub secrets for secure access.



