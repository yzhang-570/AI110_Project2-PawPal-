# PawPal+ Project Reflection

## 1. System Design
The user is able to enter details about their pet and personal priorities, add and manage tasks, and generate schedule recommendations based on this information.

Classes:
1. Owner
- Attributes: name, gender, age
- Methods: setName, setGender, setAge

2. Pet
- Attributes: name, sex, age
- Methods: setName, setSex, setAge

3. Task
- Attributes: Name, Date, Repeat (X times daily, 2x daily, 1x daily, weekly, biweekly, monthly, yearly), Duration, Type (Pet Care, Constraint), Priority Level, Time Preference (morning, noon, evening), Pet
- Methods: setName, setDuration, setFrequency, setType, setPriority, setTimePreference

4. Scheduler
- Attributes: taskList
- Methods: addTask, removeTask, editTask


**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
