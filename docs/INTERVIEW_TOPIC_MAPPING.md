# Interview Topics Mapping
## Alignment with Technical Assessment Requirements

This document maps your reference topics to specific interview questions, showing comprehensive coverage across all required competencies.

---

## 📊 Coverage Overview

| Topic Category | Questions | Coverage Level |
|----------------|-----------|----------------|
| Python Understanding | Q1.1-1.5, Q2.3 | ✅ Comprehensive |
| Development Practices | Q2.1-2.4 | ✅ Comprehensive |
| Database (SQL vs NoSQL) | Q3.2 | ✅ Comprehensive |
| Kubernetes | Q3.3 | ✅ Comprehensive |
| Microservices Architecture | Q3.4 | ✅ Comprehensive |
| Async Processing / Event Streaming | Q3.5 | ✅ Comprehensive |
| Production Readiness | Q3.1, Q3.6 | ✅ Comprehensive |

---

## 🐍 Python Understanding

### Your Topics:
- ✅ Say out loud what you are thinking
- ✅ Understand code
- ✅ While vs list comprehension

### Covered by Questions:

**Q1.1: General Code Understanding** (Warm-up)
- *"Can you explain what this code does?"*
- **Evaluates**: Code comprehension, communication, thinking out loud
- **Expected**: Clear articulation of domain model, Pydantic usage, StrEnum

**Q1.2-1.4: Bug Identification** (3 Critical Bugs)
- Capacity check logic bug
- Infinite loop bug
- Shared mutable state bug
- **Evaluates**: Python fundamentals, debugging skills, understanding of class vs instance variables

**Q2.3: Refactoring Philosophy**
- *"When would you prefer a list comprehension vs while loop?"*
- **Evaluates**: Pythonic code, readability vs performance trade-offs
- **Expected**: Discusses generators, early exit, maintainability

**Q1.5: Code Design Issues**
- Magic numbers, validation, encapsulation
- **Evaluates**: SOLID principles, Python best practices

---

## 🔧 Development Practices

### Your Topics:
- ✅ Review PR (found bug, improvements, unit test)
- ✅ How would you improve this code
- ✅ Refactoring
- ✅ Documentation
- ✅ What is important on a review (guidelines)
- ✅ What is your test strategy for this code
- ✅ Besides unit tests (integration tests, contract tests)
- ✅ Steps to release the code
- ✅ Linting
- ✅ CI/CD
- ✅ System tests

### Covered by Questions:

**Q2.1: Pull Request Review**
- *"Imagine this was submitted as a PR. What would you comment on?"*
- **Evaluates**: 
  - Ability to identify bugs (blocking issues)
  - Code quality improvements (nice-to-haves)
  - Prioritization skills
  - Feedback communication style
- **Expected**: Structured review with blocking bugs, refactoring suggestions, testing gaps

**Q2.2: Testing Strategy**
- *"How would you test the `DonutBox` class? What test cases would you write?"*
- **Evaluates**: 
  - Unit test coverage (basic → edge cases → boundary conditions)
  - Integration test awareness
  - Contract test understanding
  - Performance testing considerations
- **Expected Levels**:
  - Junior: 3-4 basic test cases
  - Mid: Comprehensive unit tests + integration mention
  - Senior: Multi-level strategy with parametrized tests

**Q2.4: Documentation & Code Quality**
- *"What documentation would you add to this code?"*
- **Evaluates**: 
  - Docstring quality (classes, methods)
  - When to document vs when code is self-documenting
  - Examples and usage documentation
- **Expected**: Class/method docstrings with Args, Returns, Raises, Examples

**Q3.6: CI/CD Pipeline**
- *"Walk me through a CI/CD pipeline for this project"*
- **Evaluates**:
  - Linting (black, ruff, mypy)
  - Testing stages (unit → integration → E2E → smoke)
  - Security scanning (Trivy, Snyk)
  - Staging environment
  - Canary deployments
  - Rollback strategies
- **Expected Pipeline**:
  ```
  Lint → Unit Tests → Build Docker → Security Scan → 
  Deploy Staging → Integration Tests → 
  Deploy Canary → Monitor → Full Rollout
  ```

**Q3.1: Production Readiness**
- *"Walk me through making this production-ready"*
- **Evaluates**: Complete release checklist
  - Testing strategy
  - Configuration management
  - Monitoring
  - Error handling
  - Security
  - Deployment

---

## 🗄️ DynamoDB (Non-Relational DBs)

### Your Topics:
- ✅ Ever worked with a non-relational database?
- ✅ Advantages/Disadvantages of non-sql vs sql databases
- ✅ How would you correlate to a relational database?
- ✅ When should you use one or another?
- ✅ Ever worked with DynamoDB?

### Covered by Question:

**Q3.2: Database Choice & Architecture**
- *"If you need to persist donut orders, what database would you choose and why?"*

**Evaluates**:
- SQL vs NoSQL understanding
- ACID guarantees for transactions
- Scalability considerations
- Query complexity needs
- Experience with specific databases

**Expected Discussion**:

| Aspect | SQL (PostgreSQL) | NoSQL (DynamoDB) |
|--------|------------------|------------------|
| **Use When** | Complex queries, transactions | Simple lookups, massive scale |
| **Pros** | ACID, joins, data integrity | Horizontal scaling, serverless |
| **Cons** | Vertical scaling limits | No joins, eventual consistency |
| **This Use Case** | ✅ Recommended (orders need ACID) | ⚠️ Overkill for this scale |

**Follow-up Questions**:
- "Have you worked with DynamoDB specifically?"
- "How would you model relationships in NoSQL?"
- "When is eventual consistency acceptable?"
- "Discuss caching layer (Redis) for read-heavy workloads"

**Scoring**:
- Junior: Basic SQL/NoSQL differences
- Mid: Practical trade-offs with examples
- Senior: Caching strategies, read replicas, partition keys, indexes

---

## ☸️ Kubernetes

### Your Topics:
- ✅ How can we scale based on load these containers
- ✅ How are container images deployed on kubernetes
- ✅ How can we expose an API inside a pod to the public network
- ✅ Have you ever used Helm?

### Covered by Question:

**Q3.3: Scaling & Kubernetes**
- *"This API is deployed in a Kubernetes pod and traffic is increasing. How would you scale it?"*

**Evaluates**:

1. **Scaling Based on Load**
   - Horizontal Pod Autoscaler (HPA)
   - Metrics: CPU, memory, custom metrics
   - Min/max replicas configuration
   ```yaml
   apiVersion: autoscaling/v2
   kind: HorizontalPodAutoscaler
   spec:
     minReplicas: 2
     maxReplicas: 10
     metrics:
     - type: Resource
       resource:
         name: cpu
         target:
           type: Utilization
           averageUtilization: 70
   ```

2. **How Container Images are Deployed**
   - Deployments with image tags
   - Rolling updates strategy
   - Image pull policies
   - Container registry (ECR, GCR, Docker Hub)
   ```yaml
   spec:
     template:
       spec:
         containers:
         - name: donut-api
           image: myregistry/donut-api:v1.2.3
           imagePullPolicy: Always
   ```

3. **Exposing API to Public Network**
   - **Service Types**:
     - ClusterIP (internal only)
     - NodePort (external on node IP)
     - LoadBalancer (cloud load balancer)
   - **Ingress Controller**:
     - Nginx Ingress
     - TLS termination
     - Path-based routing
   ```yaml
   apiVersion: networking.k8s.io/v1
   kind: Ingress
   metadata:
     name: donut-api-ingress
   spec:
     rules:
     - host: api.donutshop.com
       http:
         paths:
         - path: /
           pathType: Prefix
           backend:
             service:
               name: donut-api
               port:
                 number: 80
   ```

4. **Helm Experience**
   - *"Have you used Helm?"*
   - Templating Kubernetes manifests
   - Managing multiple environments (dev/staging/prod)
   - Version control for deployments
   - Helm charts structure

**Expected Knowledge by Level**:
- Mid: Understands HPA, Services, basic Ingress
- Senior: Deep K8s experience, Helm charts, networking, observability

**Additional Topics**:
- Health checks (liveness, readiness probes)
- Resource limits (CPU, memory)
- ConfigMaps and Secrets
- StatefulSets vs Deployments

---

## 🏗️ Microservices Architecture

### Your Topics:
- ✅ What is it?
- ✅ What in your opinion is the value it can bring and the use case where it's applicable

### Covered by Question:

**Q3.4: Microservices Architecture** (Senior-level)
- *"If this donut ordering system grows, would you recommend a microservices architecture? Why or why not?"*

**Evaluates**:

1. **Definition & Understanding**
   - Independent, loosely-coupled services
   - Each service owns its data
   - Communicate via APIs (REST, gRPC) or events
   - Can use different tech stacks

2. **When Microservices Add Value**
   - ✅ Different teams, different domains (orders, payments, inventory)
   - ✅ Independent scaling needs (checkout vs browsing)
   - ✅ Technology diversity requirements
   - ✅ Large team (>15-20 engineers)
   - ✅ Bounded contexts are clear

3. **When to AVOID Microservices** (Critical for Senior!)
   - ❌ Small team (<10 engineers)
   - ❌ Simple domain, few bounded contexts
   - ❌ Early stage / MVP
   - ❌ Overhead not justified
   - **Better Alternative**: Modular monolith

4. **Challenges & Trade-offs**
   - Service discovery (Consul, K8s DNS)
   - Distributed tracing (Jaeger, Zipkin)
   - Eventual consistency
   - Network latency
   - Deployment complexity (multiple services)
   - Monitoring across services
   - Debugging distributed systems

**Expected Answer** (Senior):
> "For this donut system, I'd start with a **modular monolith**, not microservices.
> 
> We can have clear modules (orders, payments, inventory) with defined boundaries.
> If the system grows and we have separate teams with different scaling needs,
> we can extract modules into microservices later.
> 
> Microservices add operational complexity (distributed tracing, service mesh,
> eventual consistency) that's only worth it at significant scale."

**Scoring**:
- Mid: Understands benefits and challenges
- Senior: **Nuanced discussion**, knows when NOT to use them, considers team size

---

## ⚡ Asynchronous Processing / Event Streaming

### Your Topics:
- ✅ Do you have experience with messaging systems?
- ✅ Have you ever worked with asynchronous messages?

### Covered by Question:

**Q3.5: Asynchronous Processing & Event Streaming**
- *"Imagine sending email receipts when a donut order is placed. How would you implement this?"*

**Evaluates**:

1. **Understanding of Async Patterns**
   
   **Approach 1: Synchronous (Anti-pattern)**
   ```python
   @app.post("/donuts")
   def create_order(request):
       order = create_order(request)
       send_email(order)  # ❌ Blocks response!
       return order
   ```
   - ❌ Blocks API response
   - ❌ User waits for email service
   - ❌ If email service down, order creation fails

   **Approach 2: Async with Queue (Better)**
   ```python
   @app.post("/donuts")
   async def create_order(request):
       order = create_order(request)
       await email_queue.publish(order)  # ✅ Non-blocking
       return order
   ```
   - ✅ Fast API response
   - ✅ Decoupled from email service
   - ✅ Can retry if email fails

   **Approach 3: Event-Driven (Best for scale)**
   ```python
   # Order Service publishes event
   await event_bus.publish("order.created", order)
   
   # Email Service subscribes
   @event_bus.subscribe("order.created")
   async def send_order_email(order):
       send_email(order)
   ```
   - ✅ Fully decoupled services
   - ✅ Multiple subscribers can react to same event
   - ✅ Event log for debugging

2. **Messaging Systems Experience**
   
   **Technologies**:
   | System | Best For | Experience Level |
   |--------|----------|------------------|
   | **RabbitMQ** | Traditional message broker, reliable | Mid+ |
   | **Apache Kafka** | High-throughput event streaming | Senior |
   | **AWS SQS/SNS** | Managed queue/pub-sub | Mid+ |
   | **Redis Pub/Sub** | Lightweight, simple use cases | Mid+ |
   | **Google Pub/Sub** | Cloud-native, serverless | Mid+ |

3. **Key Concepts to Discuss**
   
   **Delivery Guarantees**:
   - **At-most-once**: May lose messages (fast but risky)
   - **At-least-once**: May duplicate messages (requires idempotency)
   - **Exactly-once**: Most complex (Kafka transactions)
   
   **Dead Letter Queues (DLQ)**:
   - Failed messages go to DLQ
   - Manual inspection/retry
   - Prevents message loss
   
   **Idempotency**:
   - Safe to process same message multiple times
   - Use idempotency keys (order ID)
   - Example: Don't send duplicate emails
   
   **Retry Strategies**:
   - Exponential backoff
   - Max retry attempts
   - Circuit breaker pattern

4. **Event Streaming Patterns**
   
   **Event Sourcing**:
   - Store events, not current state
   - Replay events to rebuild state
   - Audit trail built-in
   
   **CQRS (Command Query Responsibility Segregation)**:
   - Separate read and write models
   - Optimized for each use case
   
   **Saga Pattern**:
   - Distributed transactions across services
   - Choreography vs Orchestration

**Follow-up Questions**:
- "Have you worked with Kafka? RabbitMQ?"
- "How do you ensure message ordering?"
- "How do you handle a consumer being down?"
- "What's the difference between queue and pub/sub?"

**Expected Knowledge by Level**:
- Junior: Basic async concept
- Mid: Message queues, basic patterns
- Senior: Event-driven architecture, experience with Kafka/RabbitMQ, discusses delivery guarantees

---

## 🚀 Production Readiness Factors

### Your Topics:
- ✅ Tests (unit, integration, contract, performance, e2e)
- ✅ Monitoring (observability, incident response, metrics, alarmistic)
- ✅ Error handling (custom exceptions, graceful exit, http responses, circuit breaking, retry mechanisms)
- ✅ Documentation (API docs, developer docs, code diagrams, LLD, guide)
- ✅ Security (Sanitization, Authentication, Data protection, external images, token exposure, secrets handling)
- ✅ Configuration Management (environment variables, configuration files, logging)
- ✅ Deployment (Containerization, orchestration, local environment)

### Covered by Question:

**Q3.1: Production Deployment**
- *"You need to deploy this API to production. Walk me through the steps to make it production-ready."*

This is the **most comprehensive question** covering all production topics.

---

### 🧪 1. Tests

**What to Look For**:

**Unit Tests** (Must Have):
```python
def test_add_donut_to_box()
def test_add_donut_to_full_box_raises_exception()
def test_box_price_calculation()
def test_any_donut_of_flavour()
def test_multiple_boxes_independent()  # Shared state bug!
```

**Integration Tests**:
```python
def test_post_donut_order_api_endpoint()
def test_get_flavours_endpoint()
def test_invalid_order_returns_400()
```

**Contract Tests**:
```python
def test_donut_request_schema_validation()
def test_donut_response_schema_matches_spec()
```

**Performance Tests**:
```bash
# Load testing with locust or k6
k6 run --vus 100 --duration 30s load_test.js
```

**E2E Tests**:
```python
def test_complete_order_workflow():
    # Create order → Verify email → Check database
```

**Coverage Target**: >80%

---

### 📊 2. Monitoring (Observability)

**What to Look For**:

**Application Performance Monitoring (APM)**:
- DataDog, New Relic, Dynatrace
- Track response times, error rates, throughput

**Metrics to Track**:
| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Response Time (p95) | <200ms | >500ms |
| Error Rate | <0.1% | >1% |
| Requests/sec | - | Sudden spike/drop |
| CPU Usage | <70% | >85% |
| Memory Usage | <80% | >90% |

**Logging Strategy**:
```python
import structlog

logger = structlog.get_logger()

logger.info(
    "order_created",
    order_id=order.id,
    user_id=user.id,
    total_price=order.total,
    duration_ms=elapsed
)
```
- Structured logging (JSON)
- Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
- Centralized aggregation (ELK stack, DataDog)
- Include correlation IDs for tracing

**Distributed Tracing**:
- Jaeger, Zipkin, AWS X-Ray
- Track requests across microservices
- Identify bottlenecks

**Alerting Rules**:
```yaml
alerts:
  - name: HighErrorRate
    condition: error_rate > 1%
    duration: 5m
    severity: critical
    action: page_on_call
  
  - name: HighLatency
    condition: p95_latency > 500ms
    duration: 10m
    severity: warning
    action: slack_channel
```

**Incident Response**:
- On-call rotation (PagerDuty, OpsGenie)
- Runbooks for common issues
- Post-mortem process (blameless)
- Disaster recovery plan

---

### 🚨 3. Error Handling

**What to Look For**:

**Custom Exceptions**:
```python
# donut_requestor/helper/exceptions.py
class DonutRequestorException(Exception):
    """Base exception for donut requestor"""
    pass

class BoxIsFullException(DonutRequestorException):
    """Raised when trying to add donut to full box"""
    pass

class InvalidFlavourException(DonutRequestorException):
    """Raised when flavour is not valid"""
    pass
```

**HTTP Status Codes** (FastAPI):
```python
from fastapi import HTTPException, status

@app.post("/donuts")
def create_order(request: DonutRequest):
    try:
        order = process_order(request)
        return order
    except BoxIsFullException:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Box capacity exceeded"
        )
    except InvalidFlavourException:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid donut flavour"
        )
    except Exception as e:
        logger.exception("Unexpected error", exc_info=e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
```

**Graceful Degradation**:
```python
# If email service is down, still process order
try:
    send_email(order)
except EmailServiceException:
    logger.warning("Email service unavailable, order processed")
    # Put in retry queue
```

**Circuit Breaker Pattern**:
```python
from pybreaker import CircuitBreaker

email_breaker = CircuitBreaker(fail_max=5, timeout_duration=60)

@email_breaker
def send_email(order):
    # If fails 5 times, circuit opens for 60s
    email_service.send(order)
```

**Retry Mechanisms**:
```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10)
)
def call_external_api():
    # Retries 3 times with exponential backoff
```

---

### 📖 4. Documentation

**What to Look For**:

**API Documentation (Automatic with FastAPI)**:
```python
@app.post(
    "/donuts",
    response_model=DonutOrder,
    status_code=201,
    summary="Create a donut order",
    description="Creates a new donut order with specified flavours and box size",
    responses={
        400: {"description": "Box capacity exceeded"},
        422: {"description": "Invalid flavour"}
    }
)
def create_order(request: DonutRequest):
    """
    Create a donut order
    
    - **boxSize**: Number of donuts the box can hold (1-12)
    - **donuts**: List of donuts with flavours
    
    Returns the created order with total price.
    """
```
- Swagger UI at `/docs`
- ReDoc at `/redoc`
- OpenAPI JSON at `/openapi.json`

**Developer Documentation**:
- README.md with setup instructions
- Architecture diagrams (C4 model)
- API integration guide
- Contributing guidelines
- ADRs (Architecture Decision Records)

**Code Documentation**:
```python
class DonutBox:
    """
    A container for donuts with fixed capacity.
    
    Manages a collection of donuts with capacity constraints
    and provides methods for adding donuts and calculating prices.
    
    Attributes:
        amount: Maximum number of donuts the box can hold
        
    Example:
        >>> box = DonutBox(amount=6)
        >>> box.add_donut(Donut(flavour=Flavour.CHOCOLATE))
        >>> box.box_price()
        2.30
    """
```

---

### 🔒 5. Security

**What to Look For**:

**Input Sanitization**:
```python
from pydantic import BaseModel, Field, validator

class DonutRequest(BaseModel):
    boxSize: int = Field(ge=1, le=12)  # Must be 1-12
    donuts: List[Donut] = Field(max_items=12)
    
    @validator('donuts')
    def validate_donut_count(cls, v, values):
        if len(v) > values.get('boxSize', 0):
            raise ValueError("Too many donuts for box size")
        return v
```
- Pydantic validation for all inputs
- SQL injection prevention (use ORMs)
- NoSQL injection prevention
- Command injection prevention

**Authentication & Authorization**:
```python
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    # Verify JWT token
    if not is_valid_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")
    return decode_token(token)

@app.post("/donuts")
def create_order(
    request: DonutRequest,
    user: User = Depends(verify_token)  # Requires auth
):
    return process_order(request, user)
```
- JWT tokens for stateless auth
- Role-based access control (RBAC)
- API rate limiting (SlowAPI, Redis)

**Rate Limiting**:
```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/donuts")
@limiter.limit("5/minute")  # Max 5 requests per minute
def create_order(request: DonutRequest):
    pass
```

**Data Protection**:
- Encrypt sensitive data at rest (AES-256)
- Use HTTPS/TLS for data in transit
- Secure handling of secrets (AWS Secrets Manager, HashiCorp Vault)
- Never log sensitive data (passwords, tokens)

**Container Security**:
```dockerfile
# Use official, minimal base images
FROM python:3.11-slim

# Don't run as root
RUN useradd -m -u 1000 appuser
USER appuser

# Scan images for vulnerabilities
# $ trivy image donut-api:latest
```

---

### ⚙️ 6. Configuration Management

**What to Look For**:

**Environment Variables**:
```python
# .env (never commit!)
DATABASE_URL=postgresql://user:pass@localhost/donutdb
REDIS_URL=redis://localhost:6379
EMAIL_API_KEY=secret_key_here
LOG_LEVEL=INFO

# config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str
    redis_url: str
    email_api_key: str
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"

settings = Settings()
```

**Configuration Files** (per environment):
```yaml
# config/production.yaml
app:
  name: donut-api
  environment: production
  debug: false

database:
  pool_size: 20
  max_overflow: 10

monitoring:
  enabled: true
  sample_rate: 1.0
```

**Logging Configuration**:
```python
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'json': {
            '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'format': '%(asctime)s %(name)s %(levelname)s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'json',
            'level': 'INFO'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/app.log',
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5,
            'formatter': 'json'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'file']
    }
}
```

---

### 🐳 7. Deployment (Containerization & Orchestration)

**What to Look For**:

**Dockerfile** (Multi-stage build):
```dockerfile
# Stage 1: Builder
FROM python:3.11-slim as builder

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --frozen

# Stage 2: Runtime
FROM python:3.11-slim

RUN useradd -m -u 1000 appuser

WORKDIR /app

COPY --from=builder /app/.venv .venv
COPY donut_requestor/ ./donut_requestor/

USER appuser

EXPOSE 8000

CMD [".venv/bin/uvicorn", "donut_requestor.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Docker Compose** (Local development):
```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/donutdb
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
  
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: donutdb
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
  
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

**Kubernetes Deployment**:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: donut-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: donut-api
  template:
    metadata:
      labels:
        app: donut-api
    spec:
      containers:
      - name: donut-api
        image: myregistry/donut-api:v1.0.0
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: donut-secrets
              key: database-url
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
```

---

## 📊 Complete Topic Coverage Summary

| Your Reference Topic | Interview Question | Coverage |
|---------------------|-------------------|----------|
| **Python understanding** | Q1.1-1.5, Q2.3 | ✅ 100% |
| **Review PR, improvements** | Q2.1 | ✅ 100% |
| **Refactoring** | Q1.5, Q2.3 | ✅ 100% |
| **Documentation** | Q2.4, Q3.1 | ✅ 100% |
| **Test strategy** | Q2.2 | ✅ 100% |
| **Unit/integration/contract tests** | Q2.2, Q3.1 | ✅ 100% |
| **Steps to release** | Q3.6 | ✅ 100% |
| **Linting, CI/CD** | Q3.6 | ✅ 100% |
| **DynamoDB / Non-relational DBs** | Q3.2 | ✅ 100% |
| **SQL vs NoSQL** | Q3.2 | ✅ 100% |
| **Kubernetes** | Q3.3 | ✅ 100% |
| **Helm** | Q3.3 | ✅ 100% |
| **Microservices** | Q3.4 | ✅ 100% |
| **Async processing / messaging** | Q3.5 | ✅ 100% |
| **Testing (all levels)** | Q2.2, Q3.1 | ✅ 100% |
| **Monitoring & observability** | Q3.1 | ✅ 100% |
| **Error handling** | Q3.1 | ✅ 100% |
| **Documentation (API, dev)** | Q2.4, Q3.1 | ✅ 100% |
| **Security** | Q3.1 | ✅ 100% |
| **Configuration management** | Q3.1 | ✅ 100% |
| **Deployment & containerization** | Q3.1, Q3.3, Q3.6 | ✅ 100% |

---

## 🎯 Quick Navigation: Finding Questions

### "I need to assess [TOPIC]"

| Topic | Go To |
|-------|-------|
| Python fundamentals | Interview Guide Q1.1-1.5 |
| Bug finding | Interview Guide Q1.2-1.4 |
| PR review | Interview Guide Q2.1 |
| Testing | Interview Guide Q2.2 |
| Documentation | Interview Guide Q2.4 |
| Production readiness | Interview Guide Q3.1 |
| Database choice | Interview Guide Q3.2 |
| Kubernetes | Interview Guide Q3.3 |
| Microservices | Interview Guide Q3.4 |
| Async/messaging | Interview Guide Q3.5 |
| CI/CD | Interview Guide Q3.6 |

---

## ✅ Confidence Checklist

Before the interview, confirm you can:

- [ ] Explain each of the 3 bugs clearly
- [ ] Provide hints if candidate gets stuck
- [ ] Discuss Pythonic refactoring (list comprehensions, generators)
- [ ] Explain CI/CD pipeline stages
- [ ] Discuss SQL vs NoSQL trade-offs
- [ ] Explain Kubernetes scaling (HPA)
- [ ] Discuss when NOT to use microservices
- [ ] Explain event-driven architecture basics
- [ ] Score objectively using evaluation form
- [ ] Provide specific, actionable feedback

---

**All topics from your reference are comprehensively covered! 🎉**
