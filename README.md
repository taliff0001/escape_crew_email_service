# Order Confirmation Email Service

A FastAPI-based microservice that sends order confirmation emails through Mailtrap. This service accepts order information via a REST API and automatically generates and sends personalized order confirmation emails.

## Features

- **REST API Endpoint**: Accepts customer order data and triggers email notifications
- **Templated Emails**: Generates professional HTML and plain-text emails using Jinja2 templates
- **Background Processing**: Handles email generation and sending in background tasks for faster API responses
- **Containerized**: Packaged as a Docker container for easy deployment
- **AWS Ready**: Designed for deployment on AWS ECS
- **Configurable**: Environment-based configuration for different deployment scenarios

## System Architecture

![System Architecture](https://via.placeholder.com/800x400.png?text=System+Architecture)

The service follows a microservice architecture pattern:

1. Frontend or ordering system sends order data to the API
2. FastAPI processes the request and validates the data
3. Email generation and sending happens in the background
4. Order confirmation is sent to customer via Mailtrap
5. API returns success/failure response to the caller

## Prerequisites

- Python 3.12+
- Docker
- AWS Account (for production deployment)
- Mailtrap Account and API Key

## Local Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/taliff0001/escape_crew_email_service.git
cd escape_crew_email_service
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create .env file

```bash
cp .env.example .env
```

Edit the `.env` file and add your Mailtrap API key and other configuration:

```
MAILTRAP_API_TOKEN=your_mailtrap_api_token
EMAIL_SENDER=orders@yourcompany.com
COMPANY_NAME=Your Company Name
SUPPORT_EMAIL=support@yourcompany.com
```

### 5. Run the application

```bash
uvicorn escape_crew_email_service.main:app --reload
```

The API will be available at http://localhost:8000

### 6. API Documentation

FastAPI automatically generates OpenAPI documentation for the API. Visit:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Docker Build and Run

### Build the Docker image

```bash
docker build -t escape_crew_email_service_image .
```

### Run the container

```bash
docker run -p 8000:8000 --env-file .env oescape_crew_email_service
```

## API Usage

### Send Order Confirmation

**Endpoint**: `POST /api/order-confirmation`

**Request Body**:

```json
{
  "order_id": "ORD-12345",
  "customer": {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "address": "123 Main St, Anytown, USA",
    "phone": "+1 555-123-4567"
  },
  "items": [
    {
      "product_id": "PROD-001",
      "name": "Wireless Headphones",
      "quantity": 1,
      "price": 79.99
    },
    {
      "product_id": "PROD-002",
      "name": "Phone Case",
      "quantity": 2,
      "price": 19.99
    }
  ],
  "total": 119.97,
  "order_date": "2025-03-15T14:30:00Z",
  "shipping_method": "Express",
  "estimated_delivery": "2025-03-20T00:00:00Z"
}
```

**Response**:

```json
{
  "status": "success",
  "message": "Order confirmation email sent"
}
```

## AWS ECS Deployment

### Prerequisites

- AWS CLI installed and configured
- ECR repository created
- ECS cluster created

### Deployment Steps

1. **Build and tag the Docker image**

```bash
docker build -t order-confirmation-service .
```

2. **Authenticate Docker to ECR**

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin your-account-id.dkr.ecr.us-east-1.amazonaws.com
```

3. **Tag the image**

```bash
docker tag order-confirmation-service:latest your-account-id.dkr.ecr.us-east-1.amazonaws.com/order-confirmation-service:latest
```

4. **Push the image to ECR**

```bash
docker push your-account-id.dkr.ecr.us-east-1.amazonaws.com/order-confirmation-service:latest
```

5. **Create an ECS Task Definition**

Use the AWS Console or AWS CLI to create a task definition that uses your ECR image. Make sure to:

- Set environment variables for configuration
- Configure appropriate CPU and memory settings
- Set up logging to CloudWatch
- Configure networking and security groups

6. **Create or Update ECS Service**

Use the AWS Console or AWS CLI to create or update an ECS service using your task definition.

7. **Configure Auto Scaling (Optional)**

Set up application auto-scaling for your ECS service based on CPU utilization or custom metrics.

### Infrastructure as Code

For production deployments, consider using:

- AWS CloudFormation
- AWS CDK
- Terraform

Example templates are available in the `infra` directory.

## Email Template Customization

The email templates can be found in the `app/templates` directory. They use Jinja2 templating syntax.

To customize the templates:

1. Edit `app/templates/order_confirmation.html` for the HTML version
2. Update the text version in `app/services/email_service.py`
3. Test your changes by sending a test email

## Testing

### Running Tests

```bash
pytest
```

### Test Coverage

```bash
pytest --cov=app
```

### Integration Testing with Mailtrap

The tests use Mailtrap's API to verify email delivery. To run integration tests:

```bash
pytest tests/integration
```

## Project Structure

```
/app
├── main.py              # FastAPI app entry point
├── routers/             # API route definitions
│   └── orders.py        # Order confirmation endpoints
├── services/            # Business logic
│   └── email_service.py # Email generation and sending
├── templates/           # Email templates
│   └── order_confirmation.html
├── models/              # Data models
│   └── order.py         # Order data model
├── config.py            # Configuration settings
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
└── tests/               # Unit and integration tests
    ├── unit/            # Unit tests
    └── integration/     # Integration tests
```

## Security Considerations

- Store API keys and sensitive configuration in AWS Secrets Manager or Parameter Store
- Use HTTPS for all API endpoints
- Implement proper authentication for production deployments
- Sanitize all input data
- Use AWS IAM roles with least privilege principle
- Regularly update dependencies to patch security vulnerabilities

## Monitoring and Logging

### CloudWatch Integration

The service is configured to send logs to AWS CloudWatch when deployed on ECS.

### Metrics

- API Request Count and Latency
- Email Send Success/Failure Rate
- Background Task Queue Size

### Alerts

Consider setting up CloudWatch Alarms for:

- High error rates
- Elevated API latency
- Failed email deliveries

## Troubleshooting

### Common Issues

1. **Email not being sent**
   - Check Mailtrap API token is correct
   - Verify the sender email is properly configured
   - Check logs for detailed error messages

2. **API returning 500 errors**
   - Check application logs for exceptions
   - Verify environment variables are properly set
   - Check database connectivity (if applicable)

3. **Container fails to start**
   - Check for proper environment configuration
   - Verify CPU/memory allocation is sufficient
   - Check Docker logs for startup errors

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/my-new-feature`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- FastAPI for the excellent web framework
- Mailtrap for email testing capabilities
- Jinja2 for templating
- AWS for cloud infrastructure services

---

**Note**: This is a school project intended as a proof of concept only, not for production use.
