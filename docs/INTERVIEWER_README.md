# 🍩 Interviewer Resources - Donut Requestor Code Review Exercise

Welcome! This folder contains everything you need to conduct a professional, structured technical interview using the donut requestor code review exercise.

---

## 📚 What You've Got

I've created **4 comprehensive documents** to help you run effective interviews:

### 1. 📖 INTERVIEW_GUIDE.md (Main Resource)
**Purpose**: Your complete interview playbook  
**Length**: ~12,000 words / comprehensive guide  
**Use When**: Preparing for the interview and as reference during

**What's Inside**:
- ⏱️ 60-minute interview structure
- 🐛 3 critical bugs with detailed explanations
- ❓ 14 structured questions with expected answers
- 📊 Seniority-specific evaluation matrices (Junior/Mid/Senior)
- 🎯 Scoring criteria and calibration examples
- 💡 Best practices for running the interview
- 🚫 Common pitfalls to avoid
- 📝 After-interview checklist

**Best For**: Deep preparation, understanding the "why" behind each question

---

### 2. 🎯 INTERVIEW_QUICK_REFERENCE.md (Cheat Sheet)
**Purpose**: Your during-interview cheat sheet  
**Length**: 2 pages / quick reference  
**Use When**: During the actual interview

**What's Inside**:
- ⏱️ Time allocation at a glance
- 🐛 The 3 bugs with quick prompts
- 📊 Quick scoring guide (Junior: 2.5+, Mid: 3.0+, Senior: 3.5+)
- 🎯 Key questions by section
- 💡 Hints to provide if candidate gets stuck
- ⚠️ Red flags and green flags
- 🚦 Decision framework

**Best For**: Quick reference during interview, keeping time, providing hints

**💡 Pro Tip**: Print this out or keep it on a second screen during the interview!

---

### 3. 📋 INTERVIEW_EVALUATION_FORM.md (Scoring Sheet)
**Purpose**: Objective, structured candidate evaluation  
**Length**: 8-page comprehensive form  
**Use When**: During and immediately after the interview

**What's Inside**:
- ✅ Checkboxes for each bug identification
- 📊 Competency scoring by seniority level
- 🎯 Weighted scoring calculation
- 📝 Space for evidence-based notes
- 💪 Strengths and growth areas
- 🚦 Clear hiring decision framework
- 📞 Post-interview checklist

**Best For**: Consistent evaluation, reducing bias, writing feedback

**💡 Pro Tip**: Fill this out in real-time during the interview for most accurate assessment!

---

### 4. 🗺️ INTERVIEW_TOPIC_MAPPING.md (Topic Coverage)
**Purpose**: Shows how questions align with your reference topics  
**Length**: Comprehensive mapping document  
**Use When**: Preparing, understanding coverage

**What's Inside**:
- 📊 Coverage overview (all topics 100% covered!)
- 🔗 Mapping of your reference topics to specific questions
- 📖 Detailed explanations of what to look for
- 💻 Code examples for each topic
- ✅ Quick navigation guide

**Best For**: Understanding which questions assess which skills, ensuring comprehensive coverage

---

## 🚀 Quick Start: Using These Resources

### 📅 Before the Interview (1-2 days before)

1. **Read** `INTERVIEW_GUIDE.md` (30-45 minutes)
   - Understand the 3 bugs thoroughly
   - Review expected answers by seniority level
   - Understand the scoring criteria

2. **Review** `INTERVIEW_TOPIC_MAPPING.md` (15 minutes)
   - See how questions map to competencies
   - Understand production readiness topics

3. **Familiarize yourself** with `INTERVIEW_EVALUATION_FORM.md` (10 minutes)
   - Know what you'll be scoring
   - Understand the weighted scoring for target level

4. **Print or open on second screen**: `INTERVIEW_QUICK_REFERENCE.md`

**Time Investment**: ~1 hour for first interview, 15 minutes for subsequent interviews

---

### ⏰ 30 Minutes Before Interview

1. **Review candidate's CV/profile** (10 minutes)
   - Note Python experience level
   - Any relevant tech (K8s, databases, testing frameworks)
   - Target seniority level

2. **Skim** `INTERVIEW_QUICK_REFERENCE.md` (5 minutes)
   - Refresh the 3 bugs
   - Review hints to provide

3. **Open** `INTERVIEW_EVALUATION_FORM.md` (5 minutes)
   - Have it ready to fill out during interview
   - Digital or printed version

4. **Prepare repository** (5 minutes)
   - Have `donut.py` ready to share screen
   - OR prepare to have candidate share their screen

5. **Mental preparation** (5 minutes)
   - Review opening script
   - Relax, be ready to collaborate

---

### 🎤 During the Interview (60 minutes)

**Your Setup**:
- Screen 1: `donut.py` code to share
- Screen 2: `INTERVIEW_QUICK_REFERENCE.md` (cheat sheet)
- Screen 3 (or paper): `INTERVIEW_EVALUATION_FORM.md` (scoring sheet)

**Flow**:
1. **0-5 min**: Introduction (use script from Quick Reference)
2. **5-25 min**: Part 1 - Bug hunting (3 bugs + code quality)
3. **25-40 min**: Part 2 - Dev practices (testing, PR review)
4. **40-55 min**: Part 3 - Production readiness (deployment, scaling)
5. **55-60 min**: Candidate's questions

**During Interview**:
- ✅ Fill out evaluation form in real-time
- ✅ Use Quick Reference for hints (after 3 min of struggle)
- ✅ Keep time - Part 1 is most critical!
- ✅ Let them think out loud
- ✅ Take factual notes, not opinions

---

### 📝 After the Interview

**Within 30 minutes** (while fresh):
1. **Expand notes** in evaluation form
2. **Calculate weighted score**
3. **Slack recruiter** with quick summary:
   ```
   "Just finished interview with [Name]. [Strong Yes/Yes/Maybe/No] 
   for [Level]. Full feedback coming within 24h."
   ```

**Within 24 hours**:
1. **Complete evaluation form** with:
   - Evidence-based notes (what they said/did)
   - Specific strengths (3)
   - Specific growth areas (3)
   - Level fit analysis
   - Candidate feedback (specific, balanced, respectful)

2. **Submit formal feedback** to hiring system

3. **Consider level fit**:
   - Over-qualified? → Suggest senior/lead role
   - Under-qualified? → Could they fit junior/mid role?
   - Don't just say "No" - identify the right level!

---

## 🎯 Interview Strategy by Role Level

### For Junior Candidates (0-2 years)

**Time Allocation**:
- 25 min: Bug hunting (expect to provide hints)
- 20 min: Testing basics, PR review fundamentals
- 10 min: Basic production concepts (Docker, testing)
- 5 min: Their questions

**Focus Areas**:
- Can they identify 2/3 bugs with hints?
- Do they understand basic testing?
- Can they explain their reasoning?
- Are they coachable and curious?

**Skip**:
- Kubernetes (Q3.3)
- Microservices (Q3.4)
- Event streaming (Q3.5)

**Pass Threshold**: 2.5+ / 5.0

---

### For Mid-Level Candidates (2-5 years)

**Time Allocation**:
- 20 min: Bug hunting (should find all 3 independently)
- 15 min: Testing strategy, PR review, refactoring
- 20 min: Production (CI/CD, Docker, basic K8s, database choice)
- 5 min: Their questions

**Focus Areas**:
- Do they find all 3 bugs independently within 10 minutes?
- Can they suggest Pythonic refactoring?
- Do they have a comprehensive test strategy?
- Do they understand CI/CD and deployment?

**May Skip**:
- Microservices architecture (Q3.4)
- Event streaming deep dive (Q3.5)

**Pass Threshold**: 3.0+ / 5.0

---

### For Senior Candidates (5+ years)

**Time Allocation**:
- 15 min: Bug hunting (should spot all within 5 min) + architecture discussion
- 10 min: PR review, testing strategy (expect multi-level)
- 30 min: Production, scaling, microservices, event-driven, security
- 5 min: Their questions

**Focus Areas**:
- Do they spot all 3 bugs immediately while reading?
- Do they identify shared mutable state bug without hints?
- Can they discuss when NOT to use microservices?
- Do they consider security, monitoring, incident response?
- Do they demonstrate leadership/mentorship mindset?

**Must Cover**:
- All questions, especially Q3.4 (Microservices) and Q3.5 (Event streaming)

**Pass Threshold**: 3.5+ / 5.0

---

## 🎓 Calibration: Expected Performance

### Strong Junior Performance
```
✅ Bugs: Finds capacity bug (hint), infinite loop bug (walkthrough), 
         misses shared state bug
✅ Testing: Suggests 4 basic tests (add, full box, find, price)
✅ PR Review: "Fix the bugs, add tests, maybe add comments"
✅ Production: Mentions unit tests, Docker, environment variables
✅ Communication: Clear, asks questions, thinks out loud

Score: 3.0 / 5.0 (Exceeds Junior expectations)
Decision: STRONG YES for Junior
```

### Strong Mid-Level Performance
```
✅ Bugs: All 3 bugs found independently within 8 minutes
✅ Testing: Comprehensive unit tests + integration tests mentioned
✅ PR Review: Structured, prioritized (blocking vs nice-to-have)
✅ Refactoring: Suggests list comprehension / generator expression
✅ Production: CI/CD pipeline, Docker multi-stage, K8s HPA basics
✅ Database: Chooses PostgreSQL with good reasoning (ACID, queries)

Score: 3.5 / 5.0 (Exceeds Mid expectations)
Decision: STRONG YES for Mid, consider for Senior
```

### Strong Senior Performance
```
✅ Bugs: All 3 spotted within 2 minutes of reading code
✅ Bugs: Immediately identifies shared mutable state issue
✅ Architecture: Discusses modular monolith before microservices
✅ Microservices: Knows when NOT to use them
✅ Testing: Multi-level strategy (unit, integration, contract, perf)
✅ Production: Security (rate limiting, auth), monitoring (APM, SLOs)
✅ Event-Driven: Experience with Kafka, discusses delivery guarantees
✅ CI/CD: Canary deployment, rollback strategies, monitoring
✅ Leadership: Mentions how they'd mentor juniors on these issues

Score: 4.2 / 5.0 (Significantly exceeds Senior expectations)
Decision: STRONG YES for Senior
```

---

## 🚫 Common Mistakes to Avoid

### Interviewer Mistakes

1. ❌ **Letting them struggle silently for >5 minutes**
   - ✅ Provide hints after 3 minutes to keep momentum

2. ❌ **Spending 40 minutes on Part 1 (bugs)**
   - ✅ Keep time: 20 min max on Part 1

3. ❌ **Not letting them finish thoughts**
   - ✅ Let them think out loud, even if taking time

4. ❌ **Comparing to your own approach**
   - ✅ Evaluate against role requirements, not your style

5. ❌ **Only writing feedback at the end**
   - ✅ Take notes during interview while fresh

6. ❌ **Vague feedback like "not good enough"**
   - ✅ Specific, evidence-based: "Struggled to identify capacity bug even with hints; testing knowledge limited to basic unit tests; would benefit from more production experience"

7. ❌ **Just saying "No" without level assessment**
   - ✅ "Doesn't meet Senior bar, but strong Mid-level candidate - recommend downlevel"

---

### Bias Awareness

Watch for these biases:

| Bias | Description | How to Avoid |
|------|-------------|--------------|
| **Halo Effect** | One great answer colors everything | Score each section independently |
| **Horns Effect** | One mistake overshadows everything | Look for positives even if they struggled early |
| **Recency Bias** | Last answer matters most | Review your notes from entire interview |
| **Similarity Bias** | Favor candidates like you | Use objective criteria from evaluation form |
| **Confirmation Bias** | Look for evidence supporting initial impression | Actively look for counter-evidence |
| **Cultural Fit** | Vague "gut feeling" | Focus on observable skills and behaviors |

**How to Combat Bias**:
- ✅ Use structured evaluation form
- ✅ Write evidence-based notes ("They said X" not "I felt Y")
- ✅ Discuss borderline cases with colleague
- ✅ Focus on what they demonstrated, not your impressions

---

## 📞 Need Help?

### During Interview
- It's OK to take a 2-minute break if you need to regroup
- Have `INTERVIEW_QUICK_REFERENCE.md` open for quick hints

### After Interview (Borderline Case)
- Discuss with team lead or experienced interviewer
- Review calibration examples in `INTERVIEW_GUIDE.md`
- Compare notes from evaluation form against scoring thresholds

### For Calibration
- Shadow other interviewers' sessions
- Have experienced interviewer shadow you
- Review past candidate feedback and performance correlation

---

## 🎯 Success Metrics

### Your Goal
Find the **right person for the role**, not the "perfect" candidate.

### What Success Looks Like
- ✅ Candidate feels respected and heard
- ✅ You have clear evidence for your decision
- ✅ Feedback submitted within 24 hours
- ✅ Specific, actionable feedback provided
- ✅ Clear level fit identified (not just pass/fail)

---

## 📊 Interview Coverage Summary

This interview comprehensively assesses:

| Competency | Coverage | Questions |
|------------|----------|-----------|
| **Python Fundamentals** | ✅ Comprehensive | Q1.1-1.5, Q2.3 |
| **Debugging Skills** | ✅ Comprehensive | Q1.2-1.4 (3 bugs) |
| **Testing Strategy** | ✅ Comprehensive | Q2.2 |
| **Code Review** | ✅ Comprehensive | Q2.1 |
| **Refactoring** | ✅ Comprehensive | Q1.5, Q2.3 |
| **Production Practices** | ✅ Comprehensive | Q3.1, Q3.6 |
| **Database Design** | ✅ Comprehensive | Q3.2 |
| **Kubernetes** | ✅ Comprehensive | Q3.3 |
| **Architecture** | ✅ Comprehensive | Q3.4 |
| **Event-Driven** | ✅ Comprehensive | Q3.5 |
| **CI/CD** | ✅ Comprehensive | Q3.6 |
| **Communication** | ✅ Throughout | All questions |

**All reference topics are 100% covered!** ✅

---

## 📚 Document Quick Reference

| Need | Document | Section |
|------|----------|---------|
| Understand the bugs | INTERVIEW_GUIDE.md | Part 1 (Q1.2-1.4) |
| Expected answers | INTERVIEW_GUIDE.md | All questions |
| Hints for stuck candidates | QUICK_REFERENCE.md | "Hints to Provide" |
| Scoring thresholds | QUICK_REFERENCE.md | "Quick Scoring Guide" |
| What to look for in testing | TOPIC_MAPPING.md | "Tests" section |
| Production readiness checklist | TOPIC_MAPPING.md | "Production Readiness" |
| Opening script | QUICK_REFERENCE.md | "Opening Script" |
| Time management | QUICK_REFERENCE.md | "If Running Out of Time" |
| Red flags | QUICK_REFERENCE.md | "Watch For Red Flags" |
| Evaluation form | EVALUATION_FORM.md | Complete form |

---

## ✅ Pre-Interview Checklist

Print this and check off before each interview:

**Preparation (Done 1-2 days before)**:
- [ ] Read full INTERVIEW_GUIDE.md
- [ ] Understand all 3 bugs
- [ ] Reviewed expected answers
- [ ] Familiarized with evaluation form

**Setup (Done 30 min before)**:
- [ ] Reviewed candidate CV/profile
- [ ] Identified target seniority level
- [ ] Skimmed QUICK_REFERENCE.md
- [ ] Opened EVALUATION_FORM.md for scoring
- [ ] Prepared donut.py for screen share
- [ ] Tested video/audio setup

**During Interview**:
- [ ] Used opening script
- [ ] Kept time (5-20-15-15-5)
- [ ] Filled out evaluation form in real-time
- [ ] Let candidate think out loud
- [ ] Provided hints after 3 min if stuck
- [ ] Took factual, evidence-based notes

**After Interview**:
- [ ] Expanded notes within 30 minutes
- [ ] Slacked recruiter with quick summary
- [ ] Completed evaluation form within 24 hours
- [ ] Provided specific, balanced feedback
- [ ] Identified level fit (not just pass/fail)
- [ ] Submitted to hiring system

---

## 🎓 Final Tips

### Make it Collaborative, Not Adversarial
- This is **pair programming**, not an interrogation
- You're evaluating **how they'd work on your team**
- Be warm, encouraging, but objective in assessment

### Trust the Process
- These questions are calibrated and tested
- The evaluation form reduces bias
- Focus on evidence, not gut feeling

### Remember
> "The goal is not to find someone who knows everything,
> but someone who thinks clearly, communicates well,
> and would be a strong addition to the team."

---

## 📞 Questions?

If you're unsure about anything:
1. Review the relevant section in INTERVIEW_GUIDE.md
2. Check QUICK_REFERENCE.md for quick answers
3. Consult with team lead or experienced interviewer
4. Discuss in debrief after interview

---

**You're ready! Good luck with the interview! 🚀**

*Remember: Your goal is to assess fairly and provide helpful feedback,
whether the candidate moves forward or not.*

---

## 📁 File Structure

```
donut-requestor/
├── INTERVIEWER_README.md           ← You are here (start here!)
├── INTERVIEW_GUIDE.md              ← Main guide (read first)
├── INTERVIEW_QUICK_REFERENCE.md    ← Cheat sheet (use during interview)
├── INTERVIEW_EVALUATION_FORM.md    ← Scoring sheet (fill out during/after)
├── INTERVIEW_TOPIC_MAPPING.md      ← Topic coverage (reference)
├── notes.md                        ← Original notes with bugs identified
├── donut_requestor/
│   └── model/
│       └── donut.py                ← Code with intentional bugs
└── tests/
    └── unit/
        └── model/
            └── test_donut.py       ← Existing tests
```

---

*Last Updated: 2026-01-19*  
*Version: 1.0*
