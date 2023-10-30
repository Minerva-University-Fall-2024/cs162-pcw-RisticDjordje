## Inheritance vs. Composition in Zoo Management System

### Inheritance

Inheritance is a fundamental principle of object-oriented programming (OOP) where a new class (known as a subclass) derives properties and behaviors (methods) from an existing class (known as a superclass or base class). It's a way to form a hierarchical relationship between classes.

#### Example in Our Code
In our zoo management system, we've used inheritance to define specific animal classes based on a general `Animal` class.

- The `Animal` class acts as a base class with common properties like `name`, `weight`, `age`, and `diet_type`, and a common method `feed`.
- Specific animal classes such as `Lion`, `Giraffe`, `Shark`, etc., inherit from the `Animal` class. This means they automatically possess the properties and methods of `Animal`, but they can also have additional properties and behaviors specific to that animal.

```python
class Lion(Animal):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age, Animal.CARNIVORE)
```

### Composition
Composition is another OOP concept where one class is composed of one or more instances of other classes. It implies a relationship where the containing class (often called a composite) has components of other classes.

#### Example in Our Code
In our zoo system, we use composition to define relationships between `Zoo`, `Enclosure`, and `Animal`.

- An `Enclosure` contains multiple `Animal` instances. Each `Enclosure` object is responsible for the animals it contains, and the lifetime of these `Animal` objects is tied to the lifetime of the `Enclosure`.
- A `Zoo` consists of several `Enclosure` instances. The `Zoo` class doesn't inherit from the `Enclosure` class; instead, it manages various `Enclosure` objects.

```python
class Zoo:
    def __init__(self):
        self.enclosures = []

    def add_enclosure(self, enclosure):
        self.enclosures.append(enclosure)
```


## Explanation of Inheritance and Composition in IAM System

### Inheritance

Inheritance is a key object-oriented programming concept where a class (known as a subclass) derives or extends the properties and methods of another class (known as a superclass). It helps in reusing code, improving readability, and establishing a natural hierarchy for objects.

#### Usage in Our Code
- The `Student` and `Professor` classes inherit from the `User` class. This relationship implies that both students and professors are types of users, sharing common attributes such as `name` and `roles`, along with methods like `enroll` and `can_perform_action`. They also extend the `User` class with specific attributes (`student_id`, `program` for students, and `employee_id`, `department`, `managed_courses` for professors) and methods (`display_info`).

```python
class Student(User):
    def __init__(self, name, student_id, program):
        super().__init__(name)
        self.student_id = student_id
        self.program = program

    def display_info(self):
        return f"Student Name: {self.name}, ID: {self.student_id}, Program: {self.program}"
```

Similarly, `Teacher` and `TechSupport` are subclasses of the `Role` class. They inherit the basic structure of a role, including `name` and `permissions`, but are initialized with different sets of permissions relevant to their respective roles.

```python
class Teacher(Role):
    def __init__(self):
        super().__init__("Teacher", ["canBreakout", "canGrade"])
```

Composition
