# 1.Introduction to the Course 
    # Deep Learning help computers to behave and understand like human, it is the subfield of Artificial Intelligence.
    # Deep Learning is a subset of Machine Learning, which is a subset of Artificial Intelligence.
    # In this course I will be tested through self-assessment quizzes, code challenges and practical assignments.
    # Not only this, I will be making many projects with the guidance of Instructors at Internshala.

    # Neural networks are building blocks of Deep Learning models
    # Neural networks are inspired by the human brain, which is made up of billions of neurons.


# 2. Basics of Statistics
    # 2.1 Types of Data - Qualitative and Quantitive 
        # Qualitative data is categorical data, which is further divided into two types - Nominal and Ordinal
        # Examples: Gender (Male/Female), Color(Red/Green)
        # Nominal refers to unordered values. Example: Gender, Nationality etc
        # Ordinal refers to ordered values or ranked values. Example: Rating like not satisfied, satisfied, highly satsified etc
        # Quantitive data is numerical data i.e can be measured numerically, which is further divided into two types - Discrete and Continuous.
        # Examples: Age, Height, Weight etc
        # Discrete data is countable data. Example: Number of students in a class, Number of cars in a parking lot etc
        # Continuous data is measurable data. Example: Height, Weight etc
    # 2.2 Types of Statistics - Descriptive Statistics and Inferential Statistics
        # Descriptive Stats consists of methods of organizing and describing data  using tables, graphs etc
        # Measures of Central Tendency -  Mean, Mode, Median
        # Measures of Dispersion - Range, Variance, Standard Deviation
        #Inferential Stats consists of methods that use sample results to help make decisions or predictions. LR, Decision Tree, Neural Networks are its examples or tools.
    # 2.3 Describig data graphically 
        # Histograms, Box Plots, Scatter Plots, Bar Graphs, Pie Charts etc
        # Frequency Distribution for qualitative data lists all categories and no. of elements that belong to each of the categories.
        # Frequency Distribution for quantative data lists all classes and number of values that belong to each class. Here we have grouped data.
        # Symmetric graph - data is represented in perfect normal curve.
        # Skewed graph - 
            # Positively skewed graph - data is concentrated on the left side of the graph.
            # Negatively skewed graph - data is concentrated on the right side of the graph.
    # Measures of Central Tendency
        # Mean - Average of all values; Mean = Sum of all values / Number of values
        # Median - Middle value of all values, rank data in ascending order. 
        # Mode - Most frequently occuring value in the data. 
        # Bimodal if data has 2 modes, Multimodal if data has multiple modes.
        # Prefer to treat outliers before calculating any of the above.
    # Measures of Dispersion
        # Range - Difference between highest and lowest value in the data. Range = largest value - smallest value
        # Variance - Average of squared differences from the mean. Variance = ((x - u)^2)/N 
        # Standard Deviation - Square root of variance. 
        # Standard Deviation is the most commonly used measure of dispersion.

# 3. Python Basics
    # 3.1 Arithmetic Operations
        # Addition, Subtraction, Multiplication, Division, Modulus, Exponentiation, Floor Division
def arithmetic():
    a  = 10
    b = 5
    add = a+b 
    sub = a-b
    mul = a*b
    div = a/b
    mod = a%b
    exp = a**b
    floor = a//b
    print(a>b) # Output : True
    print(add, sub, mul, div, mod, exp, floor)
    # Output : 15 5 50 2.0 0 100000 2
    # 3.2 Variables
        # Variables are used to store values in the memory, they are case sensitive and reassigned, can be of any length, can contain only letters, numbers and underscore, they can not be keywords or special characters.
        # Variables can be of any data type.
    # 3.3 Strings
        # Strings are immutable, they can be accessed using index, they can be sliced, they can be concatenated, they can be repeated, they can be formatted.
def str():
    str1 = "Internshala DL Course"
    #Indexing eg:
    print(str1[0]) # Output : I
    #Reversing eg:
    print(str1[::-1]) # Output : esruoC LD alahsnret nretnI
    #Slicing eg:
    print(str1[0:10]) # Output : Internshal 
    #Concatenation eg:
    str2 = " is awesome"
    print(str1+str2) # Output : Internshala DL Course is awesome
    #formatting
    age = 20
    name = "Rahul"
    print("My name is {} and I am {} years old".format(name, age)) # Output : My name is Rahul and I am 20 years old
    #functions 
    print(str1.lower()) # Output : internshala dl course
    print(str1.upper()) # Output : INTERNSHALA DL COURSE
    print(str1.split()) # Output : ['Internshala', 'DL', 'Course']
    print(str1.replace("DL", "Deep Learning")) # Output : Internshala Deep Learning Course
    print(len(str1)) # Output: 24
    print(str1.count("a")) # Output : 2
    