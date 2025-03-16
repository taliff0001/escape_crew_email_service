# Escape Crew Email Service Development Guidelines

## Build & Run Commands
```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
uvicorn main:app --reload

# Testing
pytest                    # Run all tests
pytest tests/unit/        # Run unit tests only
pytest tests/integration/ # Run integration tests only
pytest --cov=app          # Run tests with coverage
```

## Code Style Guidelines
- **Formatting**: Follow PEP 8 conventions
- **Imports**: Group imports by standard lib, third-party, local modules (with blank lines)
- **Types**: Use type hints for all function parameters and return values
- **Error Handling**: Use try-except blocks with specific exceptions; FastAPI HTTPException for API errors
- **Naming Conventions**:
  - Classes: PascalCase (e.g., OrderItem)
  - Functions/Variables: snake_case (e.g., send_order_confirmation)
  - Constants: UPPERCASE_WITH_UNDERSCORES
- **API Design**: Follow RESTful principles with consistent endpoint structure
- **Documentation**: Use docstrings for modules, classes, and functions
- **Async**: Prefer async functions for API endpoints

## Project Structure
The codebase follows a standard FastAPI structure with routers, services, models, and templates.