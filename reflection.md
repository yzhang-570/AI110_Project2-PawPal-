# PawPal+ Project Reflection

## 1. System Design
The user is able to enter details about their pet and personal priorities, add and manage tasks, and generate schedule recommendations based on this information.


**a. Initial design**

- Briefly describe your initial UML design.
My UML diagram shows 4 classes, Pet, Owner, Task, and Schedule. Owner and Pet have a one to many relationship. Schedule and task have a one to many relationship as well, and schedule aggregates tasks in a list. None of the other classes are aggregated, as it is assumed that the user is the owner, 
- What classes did you include, and what responsibilities did you assign to each?
Pet and Owner both store identifying information. Task stores crucial information regarding what it is (name), timing, preferences and priority levels, and whether it is a pet care task or an owner's constraint. 

**b. Design changes**

- Did your design change during implementation?
Yes.
- If yes, describe at least one change and why you made it.
1. Representing relationships between the classes, owner and pet, as part of the owner class since the application won't retrieve data from a database.
2. Add a genereatePlan method to create an entry point for scheduling logic.
3. Attach an ID to tasks to ensure uniqueness and prevents conflicts with repeated names.
4. Modifying classes to better represent all relationships - ex. Owner aggregating all of their tasks and closely follow the descriptions of them from part 2.

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
