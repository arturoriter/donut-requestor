# Technical Interview Evaluation Form
## Python Backend Engineer - Code Review Exercise

---

## 📋 Interview Details

**Candidate Name**: _________________________________

**Target Level**: ☐ Junior (0-2 yrs)  ☐ Mid (2-5 yrs)  ☐ Senior (5+ yrs)

**Interviewer**: _____________________________________

**Date**: ___________  **Start Time**: ______  **End Time**: ______

**Interview Format**: ☐ On-site  ☐ Video Call  ☐ Phone

---

## 🐛 PART 1: Code Understanding & Bug Identification (15 min)

### General Code Comprehension
Can the candidate explain what the code does?

☐ Excellent - Clear, structured explanation  
☐ Good - Understands main concepts  
☐ Adequate - Basic understanding  
☐ Poor - Struggles to explain  

**Notes**: 
```




```

---

### Bug #1: Capacity Check (Line 37)
**Bug**: `if self.amount - 1 <= 0:` doesn't track actual donut count

**Identification**:  
☐ Spotted immediately (<1 min)  
☐ Identified independently (1-3 min)  
☐ Identified with gentle hint (3-5 min)  
☐ Required significant help (>5 min)  
☐ Did not identify  

**Fix Proposed**:  
☐ Correct fix: `if len(self._donuts) >= self.amount:`  
☐ Partially correct approach  
☐ Incorrect fix  

**Notes**: 
```


```

---

### Bug #2: Infinite Loop (Lines 44-47)
**Bug**: `index += 1` inside if-block causes infinite loop when flavour not found

**Identification**:  
☐ Spotted immediately (<1 min)  
☐ Identified independently (1-3 min)  
☐ Identified with gentle hint (3-5 min)  
☐ Required significant help (>5 min)  
☐ Did not identify  

**Refactoring Approach**:  
☐ Pythonic solution (any/generator expression)  
☐ For-loop with early return  
☐ Fixed while loop with correct increment  
☐ No improvement suggested  

**Notes**: 
```


```

---

### Bug #3: Shared Mutable State (Line 27) - *Senior-level indicator*
**Bug**: `_donuts: list[Donut] = []` is class variable, shared across instances

**Identification**:  
☐ Spotted immediately (<1 min) - **Strong Senior indicator**  
☐ Identified independently (2-5 min)  
☐ Identified with hint about multiple instances  
☐ Understood after explanation  
☐ Did not identify / understand  

**Explanation Quality**:  
☐ Excellent - Explained implications with examples  
☐ Good - Understood the problem  
☐ Adequate - Basic understanding  
☐ Poor - Struggled to grasp concept  

**Notes**: 
```


```

---

### Additional Code Quality Issues Identified

Check all that candidate mentioned:

☐ Magic number (0.20 base cost) should be a constant  
☐ Missing validation (amount > 0 in __init__)  
☐ `DonutBox` should inherit from `BaseModel` for consistency  
☐ `amount` should be private with property accessor  
☐ Missing docstrings  
☐ `_price_by_flavour` as instance variable pattern  
☐ Other: _________________________________

**Quality of Analysis**:  
☐ Comprehensive (4+ issues)  
☐ Good (2-3 issues)  
☐ Basic (1 issue)  
☐ Limited (0 issues)  

**Notes**: 
```


```

---

## 🧪 PART 2: Development Practices & Code Quality (15 min)

### Pull Request Review Skills

**Question**: "How would you review this PR?"

**Review Structure**:  
☐ Excellent - Prioritized, actionable, structured  
☐ Good - Clear feedback with categories  
☐ Adequate - Basic comments  
☐ Poor - Vague or no structure  

**Included**:  
☐ Identified blocking issues (critical bugs)  
☐ Suggested improvements (refactoring, style)  
☐ Asked about tests  
☐ Considered security/performance  
☐ Balanced (positives + improvements)  

**Notes**: 
```




```

---

### Testing Strategy

**Question**: "What tests would you write for `DonutBox`?"

**Test Cases Mentioned**:

*Basic (expected for Junior+)*:  
☐ Add donut successfully  
☐ Add to full box raises exception  
☐ Find donut by flavour (found)  
☐ Find donut by flavour (not found)  
☐ Calculate box price  

*Intermediate (expected for Mid+)*:  
☐ Empty box price (base cost only)  
☐ Multiple boxes don't share state  
☐ Invalid capacity (zero/negative)  
☐ Boundary test (exactly at capacity)  

*Advanced (expected for Senior)*:  
☐ Parametrized tests for flavours/prices  
☐ Invalid enum value validation  
☐ Performance/edge cases  

**Beyond Unit Tests**:  
☐ Integration tests (API endpoints)  
☐ Contract tests (API schemas)  
☐ Performance tests  
☐ E2E tests  

**Overall Testing Competency**:  
☐ Expert (5/5) - Comprehensive, multi-level strategy  
☐ Strong (4/5) - Good unit + some integration  
☐ Competent (3/5) - Solid unit test plan  
☐ Basic (2/5) - Few basic tests  
☐ Limited (1/5) - Minimal testing knowledge  

**Notes**: 
```




```

---

### Refactoring & Code Quality

**Question**: "When would you use list comprehension vs while loop?"

**Discussion Quality**:  
☐ Excellent - Discusses readability, performance, use cases  
☐ Good - Understands trade-offs  
☐ Adequate - Basic preference  
☐ Limited - No clear reasoning  

**Documentation Question**: "What documentation would you add?"

☐ Class docstrings with examples  
☐ Method docstrings (Args, Returns, Raises)  
☐ Inline comments for complex logic  
☐ Understands when NOT to over-document  

**Notes**: 
```


```

---

## 🚀 PART 3: Production Readiness & Architecture (20 min)

### Production Deployment

**Question**: "How would you make this production-ready?"

**Mentioned** (check all):

*Testing*:  
☐ Unit tests with >80% coverage  
☐ Integration tests  
☐ Contract/API tests  
☐ Performance testing  

*Error Handling*:  
☐ Custom exception handling  
☐ Proper HTTP status codes  
☐ Graceful degradation  
☐ Retry mechanisms  

*Configuration*:  
☐ Environment variables  
☐ Config files (dev/staging/prod)  
☐ Never commit secrets  

*Logging & Monitoring*:  
☐ Structured logging  
☐ Log levels (DEBUG, INFO, ERROR)  
☐ APM/monitoring tools  
☐ Alerting  

*Security*:  
☐ Input sanitization  
☐ Authentication/Authorization  
☐ Rate limiting  
☐ HTTPS/TLS  

*Containerization*:  
☐ Docker  
☐ Multi-stage builds  
☐ Image scanning  

**Production Readiness Score**:  
☐ Expert (5/5) - Comprehensive, security-aware  
☐ Strong (4/5) - Covers most areas  
☐ Competent (3/5) - Basic deployment knowledge  
☐ Basic (2/5) - Limited production experience  
☐ Limited (1/5) - No production experience  

**Notes**: 
```




```

---

### Database Choice & Architecture

**Question**: "What database would you choose for persisting orders?"

**Database Chosen**:  
☐ PostgreSQL (Relational)  
☐ DynamoDB (NoSQL)  
☐ Other: __________________

**Reasoning Quality**:  
☐ Excellent - Discusses ACID, queries, trade-offs  
☐ Good - Clear reasoning with examples  
☐ Adequate - Basic understanding  
☐ Limited - No clear rationale  

**SQL vs NoSQL Understanding**:  
☐ Excellent - Can articulate when to use each  
☐ Good - Understands differences  
☐ Basic - Superficial knowledge  
☐ Limited - No experience  

**Additional Topics Discussed**:  
☐ Caching layer (Redis)  
☐ Read replicas / scaling  
☐ Schema design  
☐ Migration strategy  

**Notes**: 
```


```

---

### Scaling & Kubernetes *(Mid+ level)*

**Question**: "How would you scale this in Kubernetes?"

**Mentioned**:  
☐ Horizontal Pod Autoscaler (HPA)  
☐ Scaling metrics (CPU, memory, custom)  
☐ Load balancing (Services, Ingress)  
☐ Health checks (liveness, readiness)  
☐ Exposing to public (Ingress, LoadBalancer)  

**Kubernetes Experience**:  
☐ Expert - Deep hands-on experience  
☐ Intermediate - Has deployed to K8s  
☐ Basic - Theoretical knowledge  
☐ None - No K8s experience  

**Helm Experience**:  
☐ Yes, used Helm charts  
☐ Heard of it, not used  
☐ No experience  

**Notes**: 
```


```

---

### Microservices & Architecture *(Senior level)*

**Question**: "Would you use microservices for this? Why/why not?"

**Response**:  
☐ Excellent - Nuanced, knows when NOT to use  
☐ Good - Discusses trade-offs  
☐ Adequate - Basic understanding  
☐ Limited - No clear opinion  
☐ N/A - Not asked (Junior candidate)  

**Key Points Discussed**:  
☐ Start with modular monolith  
☐ Microservices complexity only worth it at scale  
☐ Team size considerations  
☐ Bounded contexts / domains  

**Challenges Mentioned**:  
☐ Service discovery  
☐ Distributed tracing  
☐ Eventual consistency  
☐ Network latency  
☐ Deployment complexity  

**Notes**: 
```


```

---

### Asynchronous Processing *(Senior level)*

**Question**: "How would you handle sending email receipts asynchronously?"

**Approach**:  
☐ Event-driven architecture (Kafka, SNS/SQS)  
☐ Message queues (RabbitMQ, Redis)  
☐ Async/await with background tasks  
☐ Basic understanding  
☐ No experience  
☐ N/A - Not asked  

**Discussed**:  
☐ At-least-once vs exactly-once delivery  
☐ Dead letter queues  
☐ Idempotency  
☐ Retry strategies  

**Notes**: 
```


```

---

### CI/CD Pipeline *(Mid+ level)*

**Question**: "Describe a CI/CD pipeline for this project"

**Pipeline Stages Mentioned**:  
☐ Linting (black, ruff, mypy)  
☐ Unit tests with coverage  
☐ Integration tests  
☐ Docker build  
☐ Security scanning (Trivy, Snyk)  
☐ Staging deployment  
☐ Smoke/sanity tests  
☐ Production deployment  

**Advanced Concepts**:  
☐ Canary deployments  
☐ Blue-green deployments  
☐ Rollback strategy  
☐ Monitoring during deployment  

**CI/CD Experience**:  
☐ Expert - Designed pipelines from scratch  
☐ Intermediate - Used and modified pipelines  
☐ Basic - Theoretical knowledge  
☐ Limited - No experience  

**Notes**: 
```


```

---

## 💬 Communication & Collaboration

### Thinking Out Loud
☐ Excellent - Consistently explained reasoning  
☐ Good - Usually explained approach  
☐ Adequate - Some explanation with prompting  
☐ Limited - Mostly silent  

### Asking Questions
☐ Excellent - Asked clarifying questions  
☐ Good - Asked when stuck  
☐ Adequate - Few questions  
☐ Limited - No questions asked  

### Handling Uncertainty
☐ Excellent - Admits uncertainty, proposes approach  
☐ Good - Acknowledges gaps, willing to learn  
☐ Adequate - Struggles with uncertainty  
☐ Poor - Defensive or claims false expertise  

### Collaboration Style
☐ Excellent - Receptive to hints, collaborative  
☐ Good - Open to discussion  
☐ Adequate - Somewhat collaborative  
☐ Poor - Dismissive or argumentative  

**Notes**: 
```


```

---

## 🎯 Overall Competency Scoring

Rate each competency (1-5 scale):  
**1** = Well below expectations  
**2** = Below expectations  
**3** = Meets expectations  
**4** = Exceeds expectations  
**5** = Significantly exceeds expectations  

### For Junior Level (0-2 years)

| Competency | Score | Weight | Weighted |
|------------|-------|--------|----------|
| Python Fundamentals | __/5 | 30% | ____ |
| Bug Identification | __/5 | 25% | ____ |
| Testing Basics | __/5 | 20% | ____ |
| Code Quality | __/5 | 15% | ____ |
| Communication | __/5 | 10% | ____ |
| **TOTAL** | | **100%** | **__/5** |

**Pass Threshold: 2.5+**

---

### For Mid-Level (2-5 years)

| Competency | Score | Weight | Weighted |
|------------|-------|--------|----------|
| Python Fundamentals | __/5 | 20% | ____ |
| Bug Identification | __/5 | 20% | ____ |
| Testing & Quality | __/5 | 20% | ____ |
| Production Practices | __/5 | 20% | ____ |
| Architecture & Design | __/5 | 10% | ____ |
| Communication | __/5 | 10% | ____ |
| **TOTAL** | | **100%** | **__/5** |

**Pass Threshold: 3.0+**

---

### For Senior Level (5+ years)

| Competency | Score | Weight | Weighted |
|------------|-------|--------|----------|
| System Design | __/5 | 25% | ____ |
| Production Expertise | __/5 | 20% | ____ |
| Code Quality & Review | __/5 | 15% | ____ |
| Testing Strategy | __/5 | 10% | ____ |
| Bug Identification | __/5 | 10% | ____ |
| DevOps & Deployment | __/5 | 10% | ____ |
| Leadership & Communication | __/5 | 10% | ____ |
| **TOTAL** | | **100%** | **__/5** |

**Pass Threshold: 3.5+**

---

## 🚦 Hiring Decision

### Overall Assessment

**Recommended Level**:  
☐ Junior (0-2 years)  
☐ Mid-Level (2-5 years)  
☐ Senior (5+ years)  
☐ Not a fit for any level  

**Hiring Recommendation**:  
☐ **Strong Yes** - Top 10% of candidates, clear hire  
☐ **Yes** - Solid fit for level, would hire  
☐ **Maybe** - Borderline, need more data / other interviews  
☐ **No** - Does not meet bar  

**If "No" or "Maybe", could they fit a different level?**  
☐ Over-qualified - consider for senior/lead role  
☐ Right fit for target level  
☐ Better fit for _____________ level (explain below)  
☐ Not recommended for any level  

---

## 💪 Key Strengths (Top 3)

1. ________________________________________________________________

2. ________________________________________________________________

3. ________________________________________________________________

---

## 📈 Areas for Growth (Top 3)

1. ________________________________________________________________

2. ________________________________________________________________

3. ________________________________________________________________

---

## 📊 Evidence-Based Observations

*Write specific examples of what they said or did*

**What went well**:
```






```

**What didn't go well**:
```






```

**Notable quotes or examples**:
```






```

---

## 🔍 Level Fit Analysis

*If recommending a different level than target, explain why with evidence*

```









```

---

## 📝 Feedback for Candidate

*Specific, balanced, respectful feedback to be shared via recruiter*

**Strengths to highlight**:
```




```

**Constructive feedback**:
```




```

**Recommended next steps** (if applicable):
```




```

---

## ✅ Post-Interview Checklist

☐ Feedback submitted to recruiter within 24 hours  
☐ Notified recruiter immediately after interview (Slack quick summary)  
☐ Reviewed for bias (halo effect, confirmation bias, similarity bias)  
☐ Scoring is evidence-based, not gut feeling  
☐ Candidate feedback is specific, balanced, and actionable  
☐ Clear recommendation on level fit (not just pass/fail)  

---

## 📞 Follow-up Questions for Debrief

*If this is one of multiple interviews*

☐ How did they perform in other technical interviews?  
☐ How was their system design / coding interview?  
☐ Cultural / behavioral fit assessment?  
☐ Any concerns from other interviewers?  
☐ Compensation expectations vs. level?  

---

## Additional Notes

```













```

---

**Interviewer Signature**: ____________________________  **Date**: __________

**Reviewed By** (if applicable): ____________________________  **Date**: __________

---

## 🔒 Confidentiality Notice

This evaluation is confidential and should only be shared with the hiring team and HR. 
Do not share candidate performance details publicly or with unauthorized personnel.

---

*Form Version 1.0 | Donut Requestor Code Review Exercise*
