classDiagram
    class Owner {
        +String name
        +String gender
        +int age
        +setName(name)
        +setGender(gender)
        +setAge(age)
    }

    class Pet {
        +String name
        +String sex
        +int age
        +setName(name)
        +setSex(sex)
        +setAge(age)
    }

    class Task {
        +String name
        +int duration
        +int priorityLevel
        +String repeat
        +String type
        +String timePreference
        +setName(name)
        +setDuration(minutes)
        +setFrequency(repeat)
        +setType(type)
        +setPriority(level)
        +setTimePreference(slot)
    }

    class Scheduler {
        +List~Task~ taskList
        +addTask(task)
        +removeTask(task)
        +editTask(task)
    }

    Owner "1" --> "1..*" Pet : owns
    Scheduler "1" o-- "0..*" Task : manages