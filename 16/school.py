class User:
    def __init__(self, name):
        self.name = name
        self.roles = {}  # Dictionary mapping course names to roles

    # Enroll user in a course with a given role
    def enroll(self, course, role):
        self.roles[course.name] = role

    # Check if the user can perform an action in a course
    def can_perform_action(self, course, action):
        role = self.roles.get(course.name)
        if role:
            return role.can_perform(action)
        return False


class Student(User):
    def __init__(self, name, student_id, program):
        super().__init__(name)
        self.student_id = student_id
        self.program = program

    def display_info(self):
        return f"Student Name: {self.name}, ID: {self.student_id}, Program: {self.program}"# noqa


class Professor(User):
    def __init__(self, name, employee_id, department):
        super().__init__(name)
        self.employee_id = employee_id
        self.department = department
        self.managed_courses = []

    def manage_course(self, course):
        self.managed_courses.append(course)

    def display_info(self):
        managed_courses_names = [course.name for course in self.managed_courses]# noqa
        return f"Professor Name: {self.name}, ID: {self.employee_id}, Department: {self.department}, Managed Courses: {', '.join(managed_courses_names)}"# noqa 


class Role:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

    def can_perform(self, action):
        return action in self.permissions


# Roles
class Teacher(Role):
    def __init__(self):
        super().__init__("Teacher", ["canBreakout", "canGrade"])


class TechSupport(Role):
    def __init__(self):
        super().__init__("TechSupport", ["canRepair", "canModerate"])


class Course:
    def __init__(self, name):
        self.name = name
        self.users = []

    def add_user(self, user, role):
        user.enroll(self, role)
        self.users.append(user)

# Composition is used here: Course composes User instances

#instantiate courses
math101 = Course("Math 101")
physics202 = Course("Physics 202")

#instantiate users 
# Students
alice = Student("Alice", "S001", "Mathematics")
bob = Student("Bob", "S002", "Physics")

# Professors
prof_john = Professor("Prof. John", "P001", "Mathematics")
prof_smith = Professor("Prof. Smith", "P002", "Physics")


# Roles
teacher_role = Teacher()
tech_support_role = TechSupport()

# Enrolling users
math101.add_user(prof_john, teacher_role)
physics202.add_user(prof_smith, teacher_role)

math101.add_user(alice, tech_support_role) 
physics202.add_user(bob, tech_support_role)

# Professor managing courses
prof_john.manage_course(math101)
prof_smith.manage_course(physics202)


# Print user info
print(alice.display_info())
print(prof_john.display_info())

# Check if Alice can perform 'canBreakout' in Math 101
print(f"Can Alice perform 'canBreakout' in Math 101? {'Yes' if alice.can_perform_action(math101, 'canBreakout') else 'No'}")# noqa 

# Check if Prof. John can perform 'canGrade' in Math 101
print(f"Can Prof. John perform 'canGrade' in Math 101? {'Yes' if prof_john.can_perform_action(math101, 'canGrade') else 'No'}")# noqa 
