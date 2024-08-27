# Inference Service

This project provides a scalable inference service using a pre-trained RandomForest model.

## Setup

1. Clone the repository:
    ```
    git clone https://github.com/your-repo/inference_service.git
    ```
2. Build the Docker image:
    ```
    docker build -t inference_service .
    ```
3. Run the Docker container:
    ```
    docker run -p 8000:8000 inference_service
    ```
4. Send a request to the API:
    ```
    curl -X POST "http://localhost:8000/predict/" -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
    ```

## Scaling

This service can be scaled using Docker Swarm or Kubernetes. For load balancing, consider using Nginx or Traefik.

## Monitoring

Basic logging is implemented to track requests and responses. You can also integrate Prometheus for more advanced monitoring.

## Testing

Unit tests are provided to ensure API functionality. Run the tests using:
