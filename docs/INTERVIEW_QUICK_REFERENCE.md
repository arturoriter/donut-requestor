# Interview Quick Reference Card
## Donut Requestor Code Review - Interviewer Cheat Sheet

---

## ⏱️ Time Allocation (60 min total)

| Section | Time | Key Focus |
|---------|------|-----------|
| Intro | 5 min | Set expectations, relax candidate |
| **Bug Hunting** | 20 min | 3 critical bugs + code quality |
| **Dev Practices** | 15 min | Testing, PR review, refactoring |
| **Production** | 15 min | Deployment, scaling, architecture |
| Q&A | 5 min | Their questions |

---

## 🐛 The 3 Critical Bugs

### Bug #1: Capacity Check ⚠️
```python
# Line 37: WRONG - doesn't track actual donut count
if self.amount - 1 <= 0:

# Should be:
if len(self._donuts) >= self.amount:
```
**Prompt if stuck**: "What happens with amount=2 and 3 donuts?"

---

### Bug #2: Infinite Loop ⚠️
```python
# Lines 44-47: index only increments when flavour matches!
while index < len(self._donuts):
    if self._donuts[index].flavour == flavour:
        result = True
        index += 1  # ❌ Inside if-block!
```
**Prompt if stuck**: "Trace this loop when flavour ISN'T found"

**Pythonic Fix**: `return any(donut.flavour == flavour for donut in self._donuts)`

---

### Bug #3: Shared Mutable State ⚠️ (Senior-level)
```python
# Line 27: Class variable shared across ALL instances!
_donuts: list[Donut] = []

# Should be instance variable in __init__:
def __init__(self, amount: int):
    self._donuts = []  # Each box gets its own list
```
**Prompt if stuck**: "What if we create two DonutBox instances?"

---

## 📊 Quick Scoring Guide

### Junior (0-2 years)
- ✅ Finds 2/3 bugs with hints
- ✅ Suggests 3-4 basic tests
- ✅ Understands PR review basics
- ⚠️ May miss shared state bug
- ⚠️ Limited production experience

**Pass**: 2.5+ / 5.0

---

### Mid-Level (2-5 years)
- ✅ Finds all 3 bugs independently (<10 min)
- ✅ Pythonic refactoring (list comprehensions)
- ✅ Comprehensive test strategy
- ✅ CI/CD, Docker, basic K8s
- ✅ Can justify SQL vs NoSQL
- ⚠️ May lack microservices experience

**Pass**: 3.0+ / 5.0

---

### Senior (5+ years)
- ✅ Spots all bugs in first read (<5 min)
- ✅ Architectural refactoring suggestions
- ✅ Discusses when NOT to use microservices
- ✅ Event-driven architecture experience
- ✅ Security considerations
- ✅ Mentorship mindset

**Pass**: 3.5+ / 5.0

---

## 🎯 Key Questions by Section

### Part 1: Bug Hunting (20 min)
1. "What does this code do?" (warm-up)
2. "Anything wrong with `add_donut` capacity check?"
3. "What happens in `any_donut_of_flavour` if flavour not found?"
4. "How is `_donuts` initialized?" (Senior question)
5. "What other improvements do you see?"

### Part 2: Dev Practices (15 min)
6. "How would you review this PR?"
7. "What tests would you write?"
8. "When would you use list comprehension vs while loop?"
9. "What documentation would you add?"

### Part 3: Production (15 min)
10. "Walk me through making this production-ready"
11. "What database would you choose and why?"
12. **(Mid+)** "How would you scale this in Kubernetes?"
13. **(Senior)** "Would you use microservices here? Why/why not?"
14. **(Senior)** "How would you handle async email sending?"

---

## 🚦 Decision Framework

### Strong Yes ⭐
- Exceeds expectations at target level
- Top 10% of candidates
- Clear hire

### Yes ✅
- Solid fit for level
- Would contribute immediately
- Hire

### Maybe ⚠️
- Borderline performance
- Need other interview inputs
- OR better fit at different level

### No ❌
- Doesn't meet bar for any level
- Don't move forward

---

## 💡 Hints to Provide (if stuck >3 min)

| Question | Hint |
|----------|------|
| Capacity bug | "Try adding 3 donuts to amount=2 box" |
| Infinite loop | "Walk through loop when flavour isn't found" |
| Shared state | "Create two boxes and add to one - what happens?" |
| Testing | "Think about edge cases: empty box, full box, invalid input" |
| Production | "Consider: testing, monitoring, deployment, security" |

---

## ⚠️ Watch For Red Flags

- ❌ Can't identify ANY bugs even with hints
- ❌ No testing knowledge
- ❌ Can't explain their reasoning
- ❌ Argumentative or dismissive of feedback
- ❌ Claims expertise but can't demonstrate

---

## ✅ Green Flags

- ✅ Thinks out loud
- ✅ Asks clarifying questions
- ✅ Discusses trade-offs
- ✅ Admits uncertainty ("I'm not sure, but I'd research...")
- ✅ Collaborative tone
- ✅ Considers user impact

---

## 📝 After Interview (Do within 24 hours!)

1. **Immediately**: Expand notes while fresh
2. **Within 30 min**: Slack recruiter with quick summary
3. **Within 24 hours**: Submit formal feedback

### Feedback Template:
```
[STRONG YES / YES / MAYBE / NO] for [Level]

Strengths:
- [Specific example]
- [Specific example]

Growth Areas:
- [Specific example]

Level Fit:
[If different level, explain why with evidence]

Decision: [Move forward / different level / don't proceed]
```

---

## 🎤 Opening Script

> "Hi [Name], I'm [You]. Today we'll do a code review exercise.
> 
> Here's the format:
> - I'll show you Python code with intentional bugs
> - We'll discuss what you see and how to improve it
> - Then talk about production readiness
> - **Please think out loud** so I can follow your reasoning
> - No trick questions - if stuck, just ask
> 
> Any questions before we start?"

---

## 🛑 If Running Out of Time

**Priority Order** (skip from bottom):
1. ✅ Bug identification (Part 1) - MUST COVER
2. ✅ Testing & PR review (Part 2) - MUST COVER
3. ✅ Production basics (Q10-11) - MUST COVER
4. ⚠️ Kubernetes (Q12) - Can skip for Junior
5. ⚠️ Microservices (Q13) - Can skip for Mid
6. ⚠️ Event streaming (Q14) - Can skip for Mid

---

## 🧭 Level Redirection

**If Over-Qualified**:
> "You're demonstrating senior-level skills. Have you considered our senior role?"

**If Under-Qualified**:
> Note for feedback: "Doesn't meet [Level] bar, but strong fundamentals for [Lower Level]"

---

## 🔑 Remember

- 🎯 Evaluate against role requirements, not your approach
- 🤝 This is collaborative, not adversarial
- 📊 Document evidence, not feelings
- ⏱️ Keep time, but let them finish thoughts
- 💡 Hints are OK after 3 minutes of struggle
- 🚫 No brain teasers or tricks

---

## 📞 Need Help?

- **During interview**: Take a 2-min break if needed
- **After interview**: Discuss borderline cases with team lead
- **Calibration**: Review past feedback to calibrate standards

---

**Good luck! You've got this! 🚀**
