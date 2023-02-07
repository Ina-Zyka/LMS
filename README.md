# Library Management System
Library Management System is a console based application in python which uses text files to store books and users information. The application has different features like authentication, authorization and registration. We have two type of users: 1) Admin, who performs actions such as add a book, remove a book and display a book and 2) Students/Personnel who can also login and perform actions like borrow a book, display a book, search a book, return book and pay a fine.

### Tasks

#### 1. UML Diagrams
A UML diagram is a diagram based on the Unified Modeling Language with the purpose of visually representing a system along with its main actors, roles, actions, artifacts or classes, in order to better understand, alter, maintain, or document information about the system.

Here are the UML diagrams for our Library Management System:

##### - [Class Diagram](https://github.com/Ina-Zyka/LMS/blob/main/images/UML%20Class%20Diagram.png)


##### - [Activity Diagram](https://github.com/Ina-Zyka/LMS/blob/main/images/UML%20Actitvity%20Diagram.jpg)

##### - [Use Case Diagram](https://github.com/Ina-Zyka/LMS/blob/main/images/UML%20UseCase%20Diagram.jpg)


#### 3. SonarCloud Metrics:
SonarCloud is a cloud-based code analysis service designed to detect code quality issues, continuously ensuring the maintainability, reliability and security of the code.

##### URL: https://sonarcloud.io/project/overview?id=Ina-Zyka_LMS

##### a. Reliability:
https://sonarcloud.io/component_measures?id=Ina-Zyka_LMS&metric=new_reliability_rating&view=list

##### b. Security:
https://sonarcloud.io/component_measures?id=Ina-Zyka_LMS&metric=new_security_rating&view=list

##### c. Duplications:
https://sonarcloud.io/component_measures?id=Ina-Zyka_LMS&metric=new_duplicated_lines_density&view=list

#### 4. Clean Code Development:
Clean code is a set of principles for writing code that is easy to understand and modify. In this case, “understandable” means that the code can be immediately understood by any experienced developer. The following characteristics of clean code are what make it easy to read:
1.The entire application’s order of execution is logical and clearly structured
2.The connection between different parts of the code is quite obvious
3.The task or role of each class, function, method, and variable is immediately understandable

Code is easy to modify if it can be adapted and extended. This also makes it easier to correct errors in the code. Clean code is thus very easy to maintain. Easily modifiable code has the following characteristics:

1.Classes and methods are small and only have one single task
2.Classes and methods are predictable, work as expected
3.The code uses unit tests

##### a.	Use of constant variables
https://github.com/Ina-Zyka/LMS/blob/main/src/constants.py

##### b.	Meaningful names (variables, classes, methods)
Class names as noun or noun phrase: e.g.  class Books, class User

##### c.	Functions and methods are small (easier to debug), serve one purpose and take 1-3 arguments
https://github.com/Ina-Zyka/LMS/blob/main/src/books.py#L37

##### d.	Error Handling (use of customized exceptions)
https://github.com/Ina-Zyka/LMS/blob/main/src/library.py#L79
##### e.	Use of decorators
https://github.com/Ina-Zyka/LMS/blob/main/src/books.py#L71




