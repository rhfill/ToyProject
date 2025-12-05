A simple API to test Github Actions.
# Local Development
1. Install dependencies
```bash
pip install -r requirements.txt
```
2. Run the app:
```bash
uvicorn main:app --host 0.0.0.0 --port 8084
```

To test the docker locally, run the following commands:
```bash
docker build -t fastapi-app .
docker run -d -p 8084:8084 --name fastapi-container fastapi-app
```

# Cloud Deployment
This project deploys automatically to an AWS EC2 instance using GitHub Actions. 

## Prerequisites on the server
- An Ubuntu 24.04 EC2 instance.
- Configure security groups to allow SSH(22) and Custom TCP(8084).

### Server Configuration
1. SSH into the instance
2. Install Docker and Git
```bash
sudo apt update && sudo apt install -y docker.io git
```

## Automate Deployment with Github Actions
See `.github/workflows/aws.yml`
### Set Up secrets in GitHub Actions
1. Navigate to Settings > Secrets and variables > Actions
2. Add your EC2 instance public IP to EC2_HOST
3. Add your private key to EC2_SSH_KEY (Note that if you are using .pem, make sure to include the the "BEGIN RSA PRIVATE KEY" and "END RSA PRIVATE KEY" lines. )

### Trigger the deployment workflow
Every time you push code to the `main` branch, GitHub Actions will automatically deploy the FastAPI server.
You can test it in your browser:
```
http://{Your EC2 public IP}:8084/year
http://{Your EC2 public IP}:8084/month
```

Done! You've now set up a GitHub Actions workflow.

# Limitations & Future Directions
1. Set up a reverse proxy so we don't need to include the port number in requests. 
2. Set up HTTPS.
3. When setting up the EC2 security group, whitelist specific GitHub IP ranges or use an AWS OIDC provider instead of allowing all IP addresses, which is a security risk.
4. Move to AWS ECS for better container orchestration and scalability.  