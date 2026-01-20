# Python Backend Engineer - Technical Interview Guide
## Code Review Exercise: Donut Requestor

---

## 📋 Interview Structure (60 minutes)

| Section | Duration | Focus |
|---------|----------|-------|
| Introduction & Warm-up | 5 min | Set the tone, explain process |
| Code Understanding & Bug Identification | 20 min | Python fundamentals, debugging |
| Development Practices & Code Quality | 15 min | Testing, refactoring, PR review |
| Production Readiness & Architecture | 15 min | Deployment, scalability, monitoring |
| Candidate Questions | 5 min | Their questions about role/team |

---

## 🎯 Pre-Interview Preparation (5-10 minutes before)

### Checklist:
- [ ] Review candidate's CV/profile (focus on Python experience, testing, deployment)
- [ ] Identify their seniority level expectation (Junior, Mid, Senior)
- [ ] Have the repository ready: `https://github.com/ricardomfmartins/donut-requestor`
- [ ] Prepare to share screen OR have them share theirs
- [ ] Have evaluation form ready (see scoring section below)
- [ ] Review notes.md for bug details and expected answers

---

## 🚀 Opening the Interview (5 minutes)

### Your Introduction:
```
"Hi [Name], thanks for joining today. I'm [Your Name], [Your Role] at [Company].
Today we'll do a code review exercise - something similar to what we do daily.

Here's how we'll spend the next hour:
1. I'll show you a small Python codebase with intentional bugs
2. We'll discuss what you see, identify issues, and talk about improvements
3. Then we'll discuss how you'd prepare this for production
4. This is collaborative - please think out loud so I can follow your reasoning
5. There are no trick questions - if you get stuck, just ask

Before we start, do you have any questions about the format?"
```

**⚠️ Key Point**: Emphasize collaboration and thinking out loud!

---

## 📝 Part 1: Code Understanding & Bug Identification (20 minutes)

### Setup
Share the `donut.py` file on screen. Give them 2-3 minutes to read silently first.

```
"Take a couple minutes to read through this DonutBox class. 
Think out loud as you go through it - what does it do? What stands out to you?"
```

---

### Q1.1: General Code Understanding (Warm-up)
**Question**: *"Can you explain what this code does? What's the purpose of the `DonutBox` class?"*

**What to Look For**:
- Can they articulate the domain model clearly?
- Do they identify the key components (Flavour enum, Donut model, DonutBox)?
- Communication clarity

**Expected Answer** (any level):
> "It's a model for managing donuts in a box. You can add donuts with different flavours, 
> check the box capacity, search for specific flavours, and calculate the total price."

**Scoring**:
- ✅ Junior+: Can explain the basic purpose
- ✅ Mid+: Identifies the use of Pydantic, StrEnum, and basic validation
- ✅ Senior: Quickly identifies design patterns and potential issues

---

### Q1.2: Bug #1 - Capacity Check Logic ⭐ CRITICAL

**Question**: *"Looking at the `add_donut` method, is there anything that catches your attention about the capacity check?"*

**If stuck, provide hint**: *"What happens when the box has `amount=2` and we add 3 donuts?"*

**The Bug**:
```python
def add_donut(self, donut: Donut):
    if self.amount - 1 <= 0:  # ❌ WRONG!
        raise BoxIsFullException(...)
```

**Expected Answer**:
> "The condition is wrong. It checks if `amount - 1 <= 0`, which only raises an exception 
> when amount is 0 or 1. It should check if the current number of donuts equals or exceeds 
> the capacity: `if len(self._donuts) >= self.amount`"

**Follow-up Question**: *"How would you fix this?"*

**Expected Fix**:
```python
def add_donut(self, donut: Donut):
    if len(self._donuts) >= self.amount:
        raise BoxIsFullException("You can't add more donuts to the box.")
    self._donuts.append(donut)
```

**Scoring**:
- ✅ Junior: Identifies the bug with hints
- ✅ Mid: Identifies bug independently within 2-3 minutes
- ✅ Senior: Spots it immediately while reading the code

---

### Q1.3: Bug #2 - Infinite Loop ⭐ CRITICAL

**Question**: *"Now look at the `any_donut_of_flavour` method. What happens if we call this with a flavour that's NOT in the box?"*

**The Bug**:
```python
def any_donut_of_flavour(self, flavour: Flavour) -> bool:
    result = False
    index = 0
    while index < len(self._donuts):
        if self._donuts[index].flavour == flavour:
            result = True
            index += 1  # ❌ Only increments when TRUE!
    return result
```

**Expected Answer**:
> "This will cause an infinite loop! The `index += 1` is inside the if-block, 
> so if the flavour doesn't match, index never increments and we loop forever."

**Follow-up**: *"How would you refactor this?"*

**Expected Answers**:

**Option 1 - Fix the loop**:
```python
def any_donut_of_flavour(self, flavour: Flavour) -> bool:
    for donut in self._donuts:
        if donut.flavour == flavour:
            return True
    return False
```

**Option 2 - Pythonic (preferred)**:
```python
def any_donut_of_flavour(self, flavour: Flavour) -> bool:
    return any(donut.flavour == flavour for donut in self._donuts)
```

**Scoring**:
- ✅ Junior: Identifies the bug with hints, suggests Option 1
- ✅ Mid: Identifies independently, suggests for-loop or list comprehension
- ✅ Senior: Immediately spots it, suggests Pythonic solution (Option 2)

---

### Q1.4: Bug #3 - Shared Mutable State ⭐ CRITICAL (Senior-level question)

**Question**: *"Look at how `_donuts` is defined at the class level. What problem could this cause?"*

**If stuck**: *"What happens if we create two separate `DonutBox` instances and add donuts to each?"*

**The Bug**:
```python
class DonutBox:
    amount: int
    _donuts: list[Donut] = []  # ❌ Class variable! Shared across ALL instances!
```

**Expected Answer**:
> "This is a shared mutable state issue. `_donuts` is a class variable, not an instance variable.
> All DonutBox instances will share the same list. If you create two boxes and add donuts to one,
> they'll appear in both boxes!"

**Demo Example**:
```python
box1 = DonutBox(amount=3)
box2 = DonutBox(amount=5)

box1.add_donut(Donut(flavour=Flavour.CHOCOLATE))
print(len(box2.donuts))  # Prints 1! ❌ Bug!
```

**Expected Fix**:
```python
class DonutBox:
    amount: int
    _donuts: list[Donut]  # Type annotation only
    
    def __init__(self, amount: int):
        self.amount = amount
        self._donuts = []  # ✅ Each instance gets its own list
```

**Scoring**:
- ❌ Junior: May not identify this without significant hints
- ✅ Mid: Identifies with hints, understands the problem
- ✅ Senior: Identifies independently, explains implications clearly

---

### Q1.5: Code Design Issues

**Question**: *"What other improvements would you suggest for this code?"*

**Look for these observations**:

1. **Magic Number** (`0.20` in `box_price`):
   ```python
   # Better:
   BASE_BOX_COST = 0.20
   
   def box_price(self) -> float:
       return self.BASE_BOX_COST + sum(donut.price() for donut in self._donuts)
   ```

2. **Missing Validation**:
   ```python
   def __init__(self, amount: int):
       if amount <= 0:
           raise ValueError("Box amount must be positive")
       self.amount = amount
       self._donuts = []
   ```

3. **Encapsulation**: Make `amount` private with property
4. **Inconsistent with Pydantic**: `DonutBox` doesn't inherit from `BaseModel`

**Scoring**:
- ✅ Junior: Identifies 1-2 improvements
- ✅ Mid: Identifies 3+ improvements with reasoning
- ✅ Senior: Comprehensive analysis including architectural concerns

---

## 🧪 Part 2: Development Practices & Code Quality (15 minutes)

### Q2.1: Pull Request Review

**Question**: *"Imagine this code was submitted as a PR by a colleague. What would you comment on in your review?"*

**Expected Answer Structure** (look for):
- [ ] **Blocking Issues**: Critical bugs that must be fixed
- [ ] **Code Quality**: Refactoring suggestions, style issues
- [ ] **Testing**: Missing test cases
- [ ] **Documentation**: Missing docstrings, unclear logic
- [ ] **Security/Performance**: Any concerns

**Excellent Answer Example**:
> "I'd mark this as 'Request Changes' because of critical bugs:
> 1. **Blocking**: Fix the capacity check bug - this breaks core functionality
> 2. **Blocking**: Fix the infinite loop in `any_donut_of_flavour`
> 3. **Blocking**: Fix the shared mutable state issue
> 4. **Recommend**: Add validation for amount > 0
> 5. **Nice-to-have**: Extract magic number, add docstrings
> 6. **Required**: Add unit tests for these scenarios"

**Scoring**:
- ✅ Junior: Identifies 2-3 critical bugs, basic suggestions
- ✅ Mid: Structured review with priorities, identifies most issues
- ✅ Senior: Comprehensive, prioritized review with alternatives

---

### Q2.2: Testing Strategy

**Question**: *"How would you test the `DonutBox` class? What test cases would you write?"*

**Expected Test Cases**:

**Must Have** (Junior+):
```python
def test_add_donut_to_box():
    """Test adding a donut successfully"""
    
def test_add_donut_to_full_box_raises_exception():
    """Test that adding to full box raises BoxIsFullException"""
    
def test_any_donut_of_flavour_found():
    """Test finding a donut by flavour"""
    
def test_any_donut_of_flavour_not_found():
    """Test searching for non-existent flavour"""
```

**Should Have** (Mid+):
```python
def test_box_price_calculation():
    """Test total price with multiple donuts"""
    
def test_empty_box_price():
    """Test price of empty box (should be base cost only)"""
    
def test_multiple_boxes_independent():
    """Test that multiple boxes don't share state"""
    
def test_box_with_zero_capacity():
    """Test invalid capacity raises error"""
```

**Nice to Have** (Senior):
```python
def test_box_at_exactly_capacity():
    """Boundary test - box exactly at capacity"""
    
def test_invalid_donut_flavour():
    """Test Pydantic validation for invalid flavour"""
    
@pytest.mark.parametrize("flavour,expected_price", [...])
def test_donut_prices():
    """Parametrized test for all flavour prices"""
```

**Follow-up**: *"Besides unit tests, what other testing would you do?"*

**Expected Answer**:
- **Integration Tests**: Test API endpoints end-to-end
- **Contract Tests**: Validate API request/response schemas
- **Performance Tests**: Load testing if this is high-traffic
- **E2E Tests**: Full user workflows

**Scoring**:
- ✅ Junior: Identifies 3-4 basic test cases
- ✅ Mid: Comprehensive unit test plan + mentions integration testing
- ✅ Senior: Complete testing strategy across multiple levels

---

### Q2.3: Code Refactoring Philosophy

**Question**: *"The `any_donut_of_flavour` method uses a while loop. When would you prefer a list comprehension or generator expression instead?"*

**Expected Discussion Points**:
- **Readability**: Pythonic code is more maintainable
- **Performance**: Generators for large datasets (lazy evaluation)
- **Early Exit**: Sometimes explicit loops are clearer (e.g., when returning early)

**Example Comparison**:
```python
# While loop (verbose, error-prone)
def any_donut_of_flavour(self, flavour: Flavour) -> bool:
    index = 0
    while index < len(self._donuts):
        if self._donuts[index].flavour == flavour:
            return True
        index += 1
    return False

# For loop (better)
def any_donut_of_flavour(self, flavour: Flavour) -> bool:
    for donut in self._donuts:
        if donut.flavour == flavour:
            return True
    return False

# Generator expression (best - Pythonic)
def any_donut_of_flavour(self, flavour: Flavour) -> bool:
    return any(donut.flavour == flavour for donut in self._donuts)
```

**Scoring**:
- ✅ Junior: Understands the difference, prefers readability
- ✅ Mid: Can discuss trade-offs with examples
- ✅ Senior: Discusses performance implications, memory, readability balance

---

### Q2.4: Documentation & Code Quality

**Question**: *"What documentation would you add to this code?"*

**Expected Answer**:

**Class Docstrings**:
```python
class DonutBox:
    """
    A container for donuts with a fixed capacity.
    
    Attributes:
        amount: Maximum number of donuts the box can hold
        
    Example:
        >>> box = DonutBox(amount=6)
        >>> box.add_donut(Donut(flavour=Flavour.CHOCOLATE))
        >>> box.box_price()
        2.30
    """
```

**Method Docstrings**:
```python
def add_donut(self, donut: Donut):
    """
    Add a donut to the box.
    
    Args:
        donut: The donut to add
        
    Raises:
        BoxIsFullException: If the box is already at capacity
    """
```

**When NOT to over-document**:
- Self-explanatory code doesn't need comments
- Avoid obvious comments like `# increment index`

**Scoring**:
- ✅ Junior: Basic docstrings for classes/methods
- ✅ Mid: Comprehensive docstrings with examples
- ✅ Senior: Discusses when to document vs. when code should be self-documenting

---

## 🚀 Part 3: Production Readiness & Architecture (15 minutes)

### Q3.1: Deployment Preparation

**Question**: *"You need to deploy this API to production. Walk me through the steps you'd take to make it production-ready."*

**Look for these categories** (adjust depth based on seniority):

#### 1. **Testing** (Must mention)
- Unit tests with >80% coverage
- Integration tests for API endpoints
- Contract tests for API schemas
- Performance/load testing

#### 2. **Error Handling**
- Custom exception handling
- Proper HTTP status codes (400, 404, 500)
- Graceful degradation
- Retry mechanisms for external services

#### 3. **Configuration Management**
- Environment variables for secrets
- Configuration files (dev/staging/prod)
- Never commit credentials

#### 4. **Logging & Monitoring** ⭐ (Critical for Mid+)
- Structured logging (JSON format)
- Log levels (DEBUG, INFO, ERROR)
- Application Performance Monitoring (APM)
- Alerting for critical errors

#### 5. **Security** ⭐ (Critical for Senior)
- Input sanitization
- Authentication & Authorization
- Rate limiting
- HTTPS/TLS

#### 6. **Containerization** (Expected for Mid+)
- Dockerfile with multi-stage builds
- Docker Compose for local dev
- Image scanning for vulnerabilities

**Scoring**:
- ✅ Junior: Mentions testing, basic error handling, environment variables
- ✅ Mid: Comprehensive coverage of 4-5 categories with specifics
- ✅ Senior: All categories covered + discusses trade-offs and priorities

---

### Q3.2: Database Choice (Architecture Decision)

**Question**: *"If you need to persist donut orders, what database would you choose and why?"*

**Expected Discussion** (look for reasoning, not just an answer):

**Option 1: PostgreSQL (Relational)** ⭐ Recommended
- **Pros**: 
  - ACID guarantees for orders/transactions
  - Complex queries (e.g., "top-selling flavours", pricing history)
  - Data integrity with foreign keys
  - JSON support for flexible fields
- **Cons**: 
  - Harder to scale horizontally
  - Schema migrations can be complex

**Option 2: DynamoDB (NoSQL)**
- **Pros**: 
  - Scales automatically
  - Fast for key-value lookups
  - Serverless, low maintenance
- **Cons**: 
  - Limited query flexibility
  - No joins
  - Eventual consistency by default

**Follow-up**: *"Have you worked with non-relational databases? When would you choose NoSQL over SQL?"*

**Expected Answer**:
> "Choose NoSQL when:
> - You need horizontal scalability at massive scale
> - Schema is flexible/changing rapidly
> - Simple access patterns (key-value lookups)
> 
> Choose SQL when:
> - You need complex queries and joins
> - ACID transactions are critical
> - Data relationships are important"

**Scoring**:
- ✅ Junior: Can explain basic differences between SQL/NoSQL
- ✅ Mid: Discusses trade-offs with practical examples
- ✅ Senior: Considers caching layers (Redis), read replicas, architectural patterns

---

### Q3.3: Scaling & Kubernetes (Mid-Senior level)

**Question**: *"This API is deployed in a Kubernetes pod and traffic is increasing. How would you scale it?"*

**Expected Answers**:

**Horizontal Pod Autoscaler (HPA)**:
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: donut-api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: donut-api
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

**Discuss**:
- Scaling based on CPU, memory, or custom metrics
- Load balancing with Services/Ingress
- Health checks (liveness, readiness probes)

**Follow-up**: *"How would you expose this API to the public internet?"*

**Expected Answer**:
- **Service**: ClusterIP → LoadBalancer or NodePort
- **Ingress**: Nginx Ingress Controller with TLS
- **API Gateway**: AWS API Gateway, Kong, etc.

**Follow-up**: *"Have you used Helm?"*

**Expected Discussion** (if experienced):
- Helm charts for templating Kubernetes manifests
- Managing environments (dev/staging/prod)
- Version control for deployments

**Scoring**:
- ✅ Mid: Understands HPA, basic Kubernetes concepts
- ✅ Senior: Discusses scaling strategies, networking, Helm, observability

---

### Q3.4: Microservices Architecture (Senior-level)

**Question**: *"If this donut ordering system grows, would you recommend a microservices architecture? Why or why not?"*

**Look for balanced reasoning**:

**When Microservices Make Sense**:
- Different teams owning different domains (order service, payment service, inventory)
- Independent scaling needs (payment processing vs. browsing catalogue)
- Technology diversity (some services need different languages/frameworks)

**When to Stay Monolithic**:
- Small team (< 10 engineers)
- Simple domain with few bounded contexts
- Early stage / MVP
- Overhead of distributed systems not justified

**Expected Answer**:
> "I'd start with a modular monolith, not microservices. For a donut ordering system,
> you could have clear modules (orders, payments, inventory) that could later be extracted
> if needed. Microservices add complexity (distributed tracing, service mesh, eventual
> consistency) that's only worth it at scale."

**Follow-up**: *"What challenges come with microservices?"*

**Expected Challenges**:
- Service discovery
- Distributed tracing
- Eventual consistency
- Deployment complexity
- Network latency
- Monitoring across services

**Scoring**:
- ✅ Mid: Understands microservices benefits and challenges
- ✅ Senior: Nuanced discussion, knows when NOT to use them, considers team size

---

### Q3.5: Asynchronous Processing & Event Streaming

**Question**: *"Imagine sending email receipts when a donut order is placed. How would you implement this?"*

**Expected Approaches**:

**Option 1: Synchronous (Simple but risky)**:
```python
@app.post("/donuts")
def create_order(request: DonutRequest):
    order = create_order(request)
    send_email(order)  # ❌ Blocks response if email service is slow/down
    return order
```

**Option 2: Asynchronous (Better)**:
```python
@app.post("/donuts")
async def create_order(request: DonutRequest):
    order = create_order(request)
    await email_queue.publish(order)  # ✅ Non-blocking
    return order
```

**Option 3: Event-Driven (Best for scale)**:
```python
# Order Service publishes event
await event_bus.publish("order.created", order)

# Email Service subscribes to event
@event_bus.subscribe("order.created")
async def send_order_email(order):
    send_email(order)
```

**Follow-up**: *"Have you worked with messaging systems? Which ones?"*

**Common Technologies**:
- **RabbitMQ**: Traditional message broker
- **Apache Kafka**: High-throughput event streaming
- **AWS SQS/SNS**: Managed queue/pub-sub
- **Redis Pub/Sub**: Lightweight for simple use cases

**Expected Discussion**:
- **Guarantees**: At-least-once vs. exactly-once delivery
- **Dead Letter Queues**: Handling failures
- **Idempotency**: Safe retries

**Scoring**:
- ✅ Junior: Understands concept of async processing
- ✅ Mid: Can discuss message queues, basic patterns
- ✅ Senior: Deep experience with event-driven architecture, discusses trade-offs

---

### Q3.6: CI/CD Pipeline

**Question**: *"Walk me through a CI/CD pipeline you'd set up for this project."*

**Expected Pipeline Stages**:

```yaml
# .github/workflows/ci.yml (example)
name: CI/CD Pipeline

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run linters
        run: |
          black --check .
          ruff check .
          mypy .
      - name: Run unit tests
        run: pytest --cov=donut_requestor --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v2
  
  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Build Docker image
        run: docker build -t donut-api:${{ github.sha }} .
      - name: Scan image for vulnerabilities
        run: trivy image donut-api:${{ github.sha }}
  
  deploy-staging:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to staging
        run: kubectl apply -f k8s/staging/
      - name: Run smoke tests
        run: pytest tests/smoke/
  
  deploy-production:
    needs: deploy-staging
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: production  # Requires approval
    steps:
      - name: Canary deployment (10% traffic)
        run: kubectl apply -f k8s/canary/
      - name: Monitor metrics for 15 minutes
        run: ./scripts/monitor-canary.sh
      - name: Full rollout
        run: kubectl apply -f k8s/production/
```

**Key Concepts to Discuss**:
- **Linting**: black, ruff, mypy for code quality
- **Testing**: Unit → Integration → E2E → Smoke tests
- **Security**: Image scanning (Trivy, Snyk)
- **Staging Environment**: Pre-production testing
- **Canary Deployments**: Gradual rollout (10% → 50% → 100%)
- **Rollback Strategy**: Automated rollback on error rate spike

**Scoring**:
- ✅ Junior: Understands basic CI (linting, testing, building)
- ✅ Mid: Includes security scanning, staging, basic deployment
- ✅ Senior: Comprehensive pipeline with canary, monitoring, rollback strategy

---

## 🎯 Evaluation Criteria & Scoring

### Competency Matrix

Rate each area on a scale:
- **1** = Below expectations for level
- **2** = Meets some expectations
- **3** = Meets expectations
- **4** = Exceeds expectations
- **5** = Significantly exceeds expectations

---

### Junior Python Engineer (0-2 years experience)

| Competency | Weight | Score (1-5) | Notes |
|------------|--------|-------------|-------|
| **Python Fundamentals** | 30% | | Can read code, understand basic syntax |
| **Bug Identification** | 25% | | Identifies 2/3 bugs with hints |
| **Testing Basics** | 20% | | Knows unit testing concepts |
| **Code Quality** | 15% | | Understands clean code principles |
| **Communication** | 10% | | Explains thinking clearly |

**Passing Score**: 2.5+ average

**Expected Performance**:
- ✅ Identifies capacity bug with hints
- ✅ Spots infinite loop issue
- ✅ Suggests 3-4 unit tests
- ✅ Can explain PR review basics
- ❌ May struggle with shared mutable state bug
- ❌ Limited production/architecture experience

---

### Mid-Level Python Engineer (2-5 years experience)

| Competency | Weight | Score (1-5) | Notes |
|------------|--------|-------------|-------|
| **Python Fundamentals** | 20% | | Solid Python knowledge, Pythonic code |
| **Bug Identification** | 20% | | Identifies all 3 bugs independently |
| **Testing & Quality** | 20% | | Comprehensive test strategy |
| **Production Practices** | 20% | | CI/CD, monitoring, deployment |
| **Architecture & Design** | 10% | | Database choice, API design |
| **Communication** | 10% | | Clear, structured explanations |

**Passing Score**: 3.0+ average

**Expected Performance**:
- ✅ Identifies all 3 bugs independently within 10 minutes
- ✅ Suggests Pythonic refactoring (list comprehensions, generators)
- ✅ Comprehensive unit test plan + integration tests
- ✅ Structured PR review with priorities
- ✅ Discusses CI/CD, Docker, basic Kubernetes
- ✅ Can justify SQL vs. NoSQL choice
- ⚠️ May have limited experience with microservices/event streaming

---

### Senior Python Engineer (5+ years experience)

| Competency | Weight | Score (1-5) | Notes |
|------------|--------|-------------|-------|
| **System Design** | 25% | | Microservices, scalability, trade-offs |
| **Production Expertise** | 20% | | Monitoring, incident response, reliability |
| **Code Quality & Review** | 15% | | Architectural concerns, security |
| **Testing Strategy** | 10% | | Multi-level testing, contract tests |
| **Bug Identification** | 10% | | Spots all issues immediately |
| **DevOps & Deployment** | 10% | | K8s, canary, CI/CD pipelines |
| **Leadership & Communication** | 10% | | Mentoring, clear explanations |

**Passing Score**: 3.5+ average

**Expected Performance**:
- ✅ Spots all 3 bugs within 5 minutes while reading code
- ✅ Identifies shared mutable state bug immediately
- ✅ Provides architectural refactoring suggestions
- ✅ Discusses when NOT to use microservices
- ✅ Experience with event-driven architecture
- ✅ Comprehensive CI/CD pipeline design
- ✅ Security considerations (rate limiting, auth, input validation)
- ✅ Can discuss incident response and monitoring strategies
- ✅ Demonstrates mentorship mindset (how they'd help junior devs)

---

## 📊 Evaluation Form Template

```
Candidate: _______________________
Position: Junior / Mid / Senior Python Engineer
Interviewer: _____________________
Date: ___________________________

PART 1: CODE UNDERSTANDING & BUG IDENTIFICATION
□ Capacity Check Bug (identified independently / with hints / not identified)
□ Infinite Loop Bug (identified independently / with hints / not identified)
□ Shared Mutable State (identified independently / with hints / not identified)
□ Code Quality Issues (number identified: ___)

PART 2: DEVELOPMENT PRACTICES
□ PR Review Quality: Poor / Basic / Good / Excellent
□ Testing Strategy: Limited / Unit tests / Multi-level / Comprehensive
□ Refactoring Skills: Basic / Good / Pythonic / Excellent

PART 3: PRODUCTION READINESS
□ Deployment Knowledge: Limited / Basic / Good / Comprehensive
□ Database Choice: Poor reasoning / Adequate / Good / Excellent
□ Scaling/Architecture: N/A / Basic / Good / Expert-level

COMMUNICATION & COLLABORATION
□ Thinks out loud: Rarely / Sometimes / Consistently
□ Asks clarifying questions: No / Few / Good questions
□ Explains reasoning: Unclear / Adequate / Clear / Excellent

OVERALL ASSESSMENT:
Recommended Level:
□ Junior (0-2 years)
□ Mid-Level (2-5 years)
□ Senior (5+ years)
□ Not a fit

Decision:
□ Strong Yes (top 10% of candidates at this level)
□ Yes (solid fit for level)
□ Maybe (borderline, would need input from other interviews)
□ No (doesn't meet bar)

Key Strengths:
1. _______________________________
2. _______________________________
3. _______________________________

Areas for Growth:
1. _______________________________
2. _______________________________
3. _______________________________

Evidence-Based Notes:
[Write specific examples of what they said/did]

Suggested Level: If not fitting target level, would they be strong at a different level?
□ Over-qualified (consider senior role instead)
□ Right fit for target level
□ Better fit for [Junior/Mid] role
□ Not recommended

Feedback for Candidate (to be shared via recruiter):
[Specific, balanced, respectful feedback]
```

---

## ⏰ Time Management Tips

### If Running Short on Time:
1. **Prioritize**: Focus on bug identification (Part 1) - this is core
2. **Skip**: Can skip Q3.4 (Microservices) or Q3.5 (Event Streaming) for Mid-level
3. **Combine**: Ask "How would you deploy this to production?" instead of breaking it down

### If Candidate is Stuck:
1. **Gentle Prompts**: 
   - "What happens if we try to add 3 donuts to a box with amount=2?"
   - "Let's trace through this loop step by step..."
2. **Move On**: If stuck for >3 minutes, provide the answer and move to next question
3. **Note It**: Document where they struggled for feedback

### If Candidate is Exceeding Expectations:
1. **Go Deeper**: Ask about edge cases, performance implications
2. **Explore Architecture**: Dive into Part 3 questions earlier
3. **Note It**: Document their expertise for potential senior/lead roles

---

## 🚫 Common Pitfalls to Avoid

### For Interviewers:

1. **Don't**: Ask brain teasers or trick questions
   - ✅ Do: Focus on real-world scenarios

2. **Don't**: Let them silently struggle for >5 minutes
   - ✅ Do: Provide hints to keep momentum

3. **Don't**: Compare to your own approach ("I would have done X...")
   - ✅ Do: Evaluate against role requirements

4. **Don't**: Focus only on bugs
   - ✅ Do: Balance debugging, design, and production skills

5. **Don't**: Rush through questions
   - ✅ Do: Let them think out loud and finish thoughts

6. **Don't**: Judge based on "culture fit" or gut feeling
   - ✅ Do: Use objective criteria from evaluation form

### Watch for Bias:

- **Halo Effect**: Don't let one great answer color everything
- **Recency Bias**: Early performance matters too, not just last question
- **Similarity Bias**: Don't favor candidates who solve problems like you do
- **Confirmation Bias**: If you liked their CV, don't only see positives

---

## 📝 After the Interview

### Within 30 Minutes:
1. **Expand Notes**: While fresh in mind, write detailed observations
2. **Fill Evaluation Form**: Complete scoring objectively
3. **Slack Recruiter**: Quick summary ("Strong yes for mid-level, will submit full feedback shortly")

### Within 24 Hours:
4. **Submit Formal Feedback**: Use evaluation form template
5. **Identify Level Fit**: Don't just say "No" - could they fit a different level?
6. **Write Candidate Feedback**: Specific, balanced, respectful
   - ✅ Good: "Strong understanding of Python fundamentals. Bug identification was solid. Would benefit from more experience with production deployments and CI/CD pipelines. Recommend gaining hands-on experience with Docker and Kubernetes."
   - ❌ Bad: "Not good enough." / "Didn't know Kubernetes."

### Feedback Template:

```
STRONG YES / YES / MAYBE / NO for [Junior/Mid/Senior] Python Engineer

Technical Performance:
- [Specific strength with example]
- [Specific strength with example]
- [Area for improvement with example]

Communication & Collaboration:
- [How they explained their thinking]

Recommended Next Steps:
- [Proceed to next round / Not moving forward / Consider different level]

Level Fit Analysis:
If recommending different level, explain why with evidence:
"While this candidate didn't demonstrate senior-level system design skills,
they showed strong mid-level capabilities in testing, code quality, and 
debugging. Recommend considering for Mid-Level role."
```

---

## 🎓 Calibration: Example Candidate Responses

### Candidate A: Strong Junior

**Capacity Bug**: Identified with hint about trying to add 3 donuts to size-2 box

**Infinite Loop**: Struggled initially, identified after walking through loop step-by-step

**Shared State**: Did not identify even with hints

**Testing**: Suggested 4 basic unit tests (add donut, box full, check flavour, calculate price)

**Production**: Mentioned unit testing, Docker, and environment variables

**Verdict**: ✅ **STRONG YES for Junior** - Solid fundamentals, good learning potential

---

### Candidate B: Borderline Mid

**Capacity Bug**: Identified independently within 3 minutes

**Infinite Loop**: Spotted immediately, suggested for-loop refactor

**Shared State**: Identified with hint about creating two boxes

**Testing**: Comprehensive unit test plan, mentioned integration tests

**Production**: Discussed CI/CD basics, Docker, but limited K8s experience

**PR Review**: Structured, prioritized feedback

**Verdict**: ✅ **YES for Mid-Level** - Meets bar, would grow into role

---

### Candidate C: Weak Senior / Strong Mid

**Capacity Bug**: Spotted while reading code

**Infinite Loop**: Identified immediately, suggested Pythonic solution

**Shared State**: Spotted immediately, explained implications

**Testing**: Multi-level strategy (unit, integration, contract, performance)

**Production**: Good CI/CD knowledge, but limited experience with microservices

**Architecture**: Chose PostgreSQL with good reasoning, but couldn't deeply discuss scaling strategies

**Verdict**: ⚠️ **MAYBE for Senior / STRONG YES for Mid+** - Lacks depth in system design for senior, but excellent mid-level candidate

---

### Candidate D: Strong Senior

**Capacity Bug**: Spotted in first 30 seconds of reading

**Infinite Loop**: Immediately identified, discussed performance implications

**Shared State**: Spotted immediately, provided examples of impact

**Testing**: Comprehensive strategy including contract tests, discussed test pyramid

**Production**: Detailed CI/CD with canary deployment, monitoring, rollback

**Architecture**: 
- Discussed when NOT to use microservices
- Experience with event-driven architecture
- Security considerations (rate limiting, auth)
- Mentioned incident response and SLOs

**Communication**: Clear, mentoring mindset evident

**Verdict**: ✅ **STRONG YES for Senior** - Top 10% candidate

---

## 🔑 Key Takeaways

### What Makes This Interview Effective:
1. ✅ **Real Code Review**: Mirrors actual daily work
2. ✅ **Multiple Competencies**: Tests debugging, design, production skills
3. ✅ **Level Differentiation**: Clear expectations per seniority
4. ✅ **Objective Scoring**: Reduces bias
5. ✅ **Collaborative**: Tests how they work with others

### Remember:
- 🎯 **Goal**: Find the right person for the role, not the "perfect" candidate
- 🤝 **Collaboration**: You're evaluating how they'd work on your team
- 📊 **Evidence**: Base decisions on what they demonstrated, not gut feel
- 💡 **Growth**: Consider potential, not just current skills
- ⏱️ **Timely**: Submit feedback within 24 hours

---

## 📚 Additional Resources

### For Calibration:
- Review feedback from previous candidates
- Discuss borderline cases with team lead
- Shadow other interviewers' sessions

### For Improvement:
- Collect feedback from candidates (via recruiter)
- Track: Are your recommendations accurate in future performance?
- Update this guide based on learnings

---

**Good luck with the interview! 🚀**

*Remember: Your goal is to assess objectively and provide actionable feedback, 
whether the candidate moves forward or not.*
