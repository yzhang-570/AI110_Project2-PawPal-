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
It considers task completion status, priority, and preferred time.
- How did you decide which constraints mattered most?
I decided that the order above - from most to least important - was what mattered most, because only tasks that are incomplete should be scheduled. High priority tasks should also be considered before taking preferred times into account.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
My scheduler only supports 2 frequencies: daily and weekly.
- Why is that tradeoff reasonable for this scenario?
This allows focus on generating weekly schedules rather than monthly or yearly ones to stay within the scale of this demo.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
I found AI to be especially useful for generating test cases. It allowed me to quickly get up to speed with translating edge cases into proper tests and documenting methods with proper commenting.
- What kinds of prompts or questions were most helpful?
I really liked questions exploring different approaches, such as whether to include scheduling recurring tasks as logic within the Task or Scheduling class based on OOP principles. AI's recommendation was the put it in the Scheduling class to follow the Single Responsibility Principle (SRP).

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
When AI recommended passing Task objects to check conflicts, I didn't initally accept it, because I thought that the scheduled time was the only parameter needed and this would make the required inputs more explicit.

- How did you evaluate or verify what the AI suggested?
I later discovered that I also needed duration to calculate the full window of the potential scheduling time of a new task, so I accepted AI's suggestions.

---

## 4. Testing and Verifi
I tested core scheduling behaviors: task sorting by priority and duration, filtering by pet and completion status, and conflict detection when tasks overlap in time. I also tested edge cases like tasks with no preferred time and duplicate task names.
- Why were these tests important?
Testing was important because it validated that the scheduling logic held up after refactoring. Without tests, it would be hard to know whether changes to class structure or method signatures broke existing behavior. They also made the expected inputs and return types explicit and visible in a practical way.

**b. Confidence**

- How confident are you that your scheduler works correctly?
I am fairly confident in the core behaviors covered by tests. The pytest suite isolates each modular piece, so regressions are caught quickly. I am less confident about untested interactions between multiple pets, tasks, and full schedule generation as a whole.
- What edge cases would you test next if you had more time?
I would test scheduling tasks that span midnight, tasks with identical priority but different durations, and generating a full weekly plan with conflicts present to verify how the scheduler resolves or reports them.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I am most satisfied with the testing setup. Starting with basic classes and a demo UI, then layering in pytest alongside manual checks in main, made it much easier to verify correctness incrementally. Being able to see the practical impact of changes through both printed output and assertion-based tests gave me real confidence in the implementation.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
I would redesign the filter logic to be more composable. Rather than having two separate filter methods or forcing both filters into one, I would use an approach that can chain multiple conditions flexibly. I would also improve schedule generation to handle conflicts more gracefully instead of simply skipping them.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
Testing feels like extra weight at first, but it is essential for ensuring correctness after refactoring and for making the practical impact of changes visible, including how parameters and return types are actually used. Using both pytest (for isolating modular behavior and verifying requirements) and main (for manually printing and reviewing complex outputs like sorted lists) together gave the best coverage. Starting small, like with basic classes and a demo UI, and growing from there kept complexity manageable. Classes standardized memory and operations in a structured way even without a database, and relationships between classes had to be represented through aggregations. AI was most useful for streamlining documentation, getting up to speed with test cases for manual review, writing commit messages, and exploring different design approaches, such as whether to use two separate filter methods or one combined method for two filters.
you had another iteration, what would you improve or redesign?


**c. Key takeaway**