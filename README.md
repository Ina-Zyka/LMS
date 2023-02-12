# Library Management System
Library Management System is a console based application in python which uses text files to store books and users information. The application has different features like authentication, authorization and registration. We have two type of users: 1) Admin, who performs actions such as add a book, remove a book and display a book and 2) Students/Personnel who can also login and perform actions like borrow a book, display a book, search a book, return book and pay a fine.

### Tasks

#### 1. UML Diagrams
A UML diagram is a diagram based on the Unified Modeling Language with the purpose of visually representing a system along with its main actors, roles, actions, artifacts or classes, in order to better understand, alter, maintain, or document information about the system.

Here are the UML diagrams for our Library Management System:

##### - [Class Diagram](https://github.com/Ina-Zyka/LMS/blob/main/images/UML%20Class%20Diagram.png)

##### - [Activity Diagram](https://github.com/Ina-Zyka/LMS/blob/main/images/UML%20Actitvity%20Diagram.jpg)

##### - [Use Case Diagram](https://github.com/Ina-Zyka/LMS/blob/main/images/UML%20UseCase%20Diagram.jpg)


#### 2. DDD (Domain Driven Design)
Domain Driven Design is about mapping business domain concepts into software artifacts. It is used for complex needs, connecting the implementation to an evolving model of the core business concepts. It puts the focus on the problem domain and basically helps identify the architecture and inform about the mechanics that the software needs to replicate. [Here]() you can find the DDD diagram of our LMS project.


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
Clean code is a set of principles for writing code that is easy to understand and modify. In this case, “understandable” means that the code can be immediately understood by any experienced developer. The following characteristics of clean code are what make it easy to read: The entire application’s order of execution is logical and clearly structured, the connection between different parts of the code is quite obvious, the task/role of each class, function, method, and variable is immediately understandable.

Code is easy to modify if it can be adapted and extended. This also makes it easier to correct errors in the code. Clean code is thus very easy to maintain. Easily modifiable code has the following characteristics: Classes and methods are small and only have one single task, classes and methods work as expected, the code uses unit tests.

[Here](https://github.com/Ina-Zyka/LMS/blob/main/images/CheatSheet.jpeg) you can find the Cheatsheet.

##### Clean Code:

##### a.	Use of constant variables
https://github.com/Ina-Zyka/LMS/blob/main/src/main/python/constants.py

##### b.	Meaningful names (variables, classes, methods)
Class names as noun or noun phrase: e.g.  class Books, class User

##### c.	Functions and methods are small (easier to debug), serve one purpose and take 1-3 arguments
https://github.com/Ina-Zyka/LMS/blob/main/src/main/python/books.py#L37

##### d.	Error Handling (use of customized exceptions)
https://github.com/Ina-Zyka/LMS/blob/main/src/main/python/library.py#L79

##### e.	Use of decorators
https://github.com/Ina-Zyka/LMS/blob/main/src/main/python/books.py#L71


#### 5. Build Management
The tool we used to build our LMS is PyBuilder. The Build of the project was successful, [here](https://github.com/Ina-Zyka/LMS/blob/main/images/Build%20successful.png) you can find a screenshot. Furthermore, here you can check the [build file](https://github.com/Ina-Zyka/LMS/blob/main/build.py) and the [setup file](https://github.com/Ina-Zyka/LMS/blob/main/setup.py).

#### 6. Unit-Tests
The build was successful and all unit tests passed. [Here](https://github.com/Ina-Zyka/LMS/blob/main/images/Build%20successful.png) you can see the result.

#### 7. Continuous Delivery
In this project, I have used Circle-CI for CI/CD pipeline. For each push, we have a new build and the code quality is published to sonarcloud automatically.
[Here](https://app.circleci.com/pipelines/github/Ina-Zyka/LMS/24/workflows/e8c281d7-7e59-4269-91af-687b7ea30253/jobs/27) you can see the Circle-CI pipeline.

#### 8. Pycharm IDE
In this project I decided to use Pycharm IDE and some of my favorite Key-Shortcuts are:

* ctrl + d – Duplicate code

* ctrl + shift + z – Redo

* ctrl + shift + f – Format file / code

* ctrl + shift + k – Commit 

* ctrl + shift + 8 – Activate rectangle selection 

#### 9. DSL snippet
A Domain Specific Language is a programming language with a higher level of abstraction optimized for a specific class of problems. Regular Expressions (short Regex) are Strings that work as a DSL to do some common tasks within other Strings. [Here](https://github.com/Ina-Zyka/LMS/blob/main/src/main/python/library.py#L60) is a sample of code that uses regex.

#### 10. Functional Programming

Below are some aspects of functional programming used in LMS project:

* Final data structures

  Illustration of [final data structures](https://github.com/Ina-Zyka/LMS/blob/main/src/main/python/books.py#L7)

* Side effect free functions
  
  Illustration of [side effect free function](https://github.com/Ina-Zyka/LMS/blob/main/src/main/python/books.py#L33)

* Higher-order functions
  
  Since decorators are the most common use of higher-order functions in Python, [here](https://github.com/Ina-Zyka/LMS/blob/main/src/main/python/books.py#L71) we      have a sample of it, where fine_calc_decorator is callable function and calculate_fine is the actual function inside the wrapper function.

* Functions as parameters
  
  For this point, we have two examples:
  1. A function called [user_role](https://github.com/Ina-Zyka/LMS/blob/main/src/main/python/library.py#L17) is stored to the variable [user_username_pass_check](https://github.com/Ina-Zyka/LMS/blob/main/src/main/python/library.py#L39).  
  2. [Here](https://github.com/Ina-Zyka/LMS/blob/main/src/main/python/main.py#L32) you see a function called [validate_type](https://github.com/Ina-Zyka/LMS/blob/main/src/main/python/library.py#L97) which accepts as a parameter the function [valid_usertype_check](https://github.com/Ina-Zyka/LMS/blob/main/src/main/python/library.py#L66).                                                       

* Anonymous functions

  In the project we have used the anonymous function called [Lambda](https://github.com/Ina-Zyka/LMS/blob/main/src/main/python/library.py#L55). This function 
  can have any number of arguments but only one expression, which is evaluated and returned.








