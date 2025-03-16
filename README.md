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

## Project Structure

The project follows a standard Python package structure:

```
/escape_crew_email_service
├── main.py              # Entry point that imports the app
├── app/                 # Main application package
│   ├── __init__.py      # Package initialization
│   ├── main.py          # FastAPI app definition
│   ├── config.py        # Configuration settings
│   ├── routers/         # API route definitions
│   │   ├── __init__.py
│   │   └── orders.py    # Order confirmation endpoints
│   ├── services/        # Business logic
│   │   ├── __init__.py
│   │   └── email_service.py # Email generation and sending
│   ├── templates/       # Email templates
│   │   └── order_confirmation.html
│   └── models/          # Data models
│       ├── __init__.py
│       └── order.py     # Order data model
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
└── tests/               # Unit and integration tests
    ├── integration/     # Integration tests
    └── unit/            # Unit tests
```

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

### 4. Configure environment variables

Copy the example environment file and update it with your values:

```bash
cp .env.example .env
```

Then edit the `.env` file with your actual configuration:

```
MAILTRAP_API_TOKEN=your_mailtrap_api_token
EMAIL_SENDER=orders@yourcompany.com
COMPANY_NAME=Your Company Name
SUPPORT_EMAIL=support@yourcompany.com
```

### 5. Run the application

```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000

### 6. API Documentation

FastAPI automatically generates OpenAPI documentation for the API. Visit:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Docker Build and Run

### Build the Docker image

#### For local development on Apple Silicon (M-series) or AWS ECS deployment
```bash
# Build using the default target platform (linux/amd64)
docker build -t escape_crew_email_service .

# Or explicitly specify the target platform
docker build -t escape_crew_email_service --build-arg TARGETPLATFORM=linux/amd64 .
```

### Run the container

```bash
docker run -p 8000:8000 --env-file .env escape_crew_email_service
```

Note: Make sure your .env file is properly set up before running the container.

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

## Email Template Customization

The email templates can be found in the `app/templates` directory. They use Jinja2 templating syntax.

To customize the templates:

1. Edit `app/templates/order_confirmation.html` for the HTML version
2. Update the text version in `app/services/email_service.py`
3. Test your changes by sending a test email

## AWS ECS Deployment

### Prerequisites

- AWS CLI installed and configured
- ECR repository created
- ECS cluster created

### Deployment Steps

1. **Build and tag the Docker image**

```bash
docker build -t escape_crew_email_service .
```

2. **Authenticate Docker to ECR**

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin your-account-id.dkr.ecr.us-east-1.amazonaws.com
```

3. **Tag the image**

```bash
docker tag escape_crew_email_service:latest your-account-id.dkr.ecr.us-east-1.amazonaws.com/escape_crew_email_service:latest
```

4. **Push the image to ECR**

```bash
docker push your-account-id.dkr.ecr.us-east-1.amazonaws.com/escape_crew_email_service:latest
```

5. **Deploy using ECS**

Follow AWS documentation for deploying containers to ECS.

## Troubleshooting

### Common Issues

1. **Email not being sent**
   - Check Mailtrap API token is correct
   - Verify the sender email is properly configured
   - Check logs for detailed error messages

2. **Docker platform compatibility issues**
   - When building on Apple Silicon (M-series) for x86 servers, our Dockerfile uses ARG TARGETPLATFORM
   - If you encounter platform issues, explicitly set `--build-arg TARGETPLATFORM=linux/amd64`
   - Ensure Docker has Rosetta 2 enabled for x86 emulation on Apple Silicon
   - If you see "exec format error" when running containers, verify you built with the correct platform


2. **API returning 500 errors**
   - Check application logs for exceptions
   - Verify environment variables are properly set
   - Check correct import paths in the code

3. **Container fails to start**
   - Check for proper environment configuration
   - Verify Python path is correctly set in Dockerfile
   - Check Docker logs for startup errors

## Security Considerations

- Store API keys and sensitive configuration in environment variables or AWS Secrets Manager
- Use HTTPS for all API endpoints 
- Sanitize all input data
- Regularly update dependencies to patch security vulnerabilities

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/my-new-feature`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Note**: This is a school project intended as a proof of concept only, not for production use.
