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
    # 2.3 Describing data graphically 
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
    # 3.4 Lists
        # Lists are mutable, they can be accessed using index, they can be sliced, they can be concatenated, they can be repeated, they can be formatted.
def lists():
    l1 = [1,2,3,4,5]
    l2 = ['one', 'two', 'three']
    l3 = [0.4, 5, 'number', True]
    #Indexing eg:
    print(l1[0]) # Output : 1
    #Reversing eg:
    print(l1[::-1]) # Output : [5, 4, 3, 2, 1]
    type(l1) #Output: list
    #Slicing eg:
    print(l1[0:3]) # Output : [1, 2, 3]
    #Concatenation eg:
    l4 = l1 + l2
    print(l4) # Output : [1, 2, 3, 4, 5, 'one', 'two', 'three']
    list(range(0,10,2))
    #Output : [0, 2, 4, 6, 8]
    l4.append("4i")
    print(l4) # Output : [1, 2, 3, 4, 5, 'one', 'two', 'three', '4i']
    l4.pop()
    print(l4) # Output : [1, 2, 3, 4, 5, 'one', 'two', 'three']
    # 3.5 Tuples
        # Tuples are immutable, they can be accessed using index, they can be sliced, they can be concatenated, they can be repeated, they can be formatted.
def tuples():
    t1 = (1,2,3,4,5)
    t2 = ('one', 'two', 'three')
    t3 = (0.4, 5, 'number', True)
    #Indexing eg:
    print(t1[0]) # Output : 1
    #Reversing eg:
    print(t1[::-1]) # Output : (5, 4, 3, 2, 1)
    type(t1) #Output: tuple
    #Slicing eg:
    print(t1[0:3]) # Output : (1, 2, 3)
    #Concatenation eg:
    t4 = t1 + t2
    print(t4) # Output : (1, 2, 3, 4, 5, 'one', 'two', 'three')
    t1[0] = 3
    # Output : TypeError: 'tuple' object does not support item assignment
    # 3.6 Dictionaries
        # Dictionaries are mutable, they can be accessed using keys, they can be sliced, they can be concatenated, they can be repeated, they can be formatted.
def dictionaries():
    d1 = {'name':"John Doe",'age':'30','city':'New York'}
    print(d1)
    # Output : {'name': 'John Doe', 'age': '30', 'city': 'New York'}
    #Indexing eg:
    print(d1['name']) # Output : John Doe
    print(d1['city']) # Output : New York
    #Reversing eg:
    print(d1[::-1]) # Output : TypeError: unhashable type: 'slice'
    type(d1) #Output: dict
    #Slicing eg:
    print(d1[0:3]) # Output : TypeError: unhashable type: 'slice'

#Question - ASSIGNMENT
# Declare a variable named ‘str’ with value as "Python course". Write queries to output the following results
    #The first character of the ‘str’
    #2nd to 5th character of the ‘str’
    #Last character of the ‘str’
    #The reverse of ‘str’ i.e. 'esruoc nohtyP'
    #Every alternate character (1st, 3rd, 5th…..) of ‘str’
    #Every alternate character (2nd, 4th, 6th….) of ‘str’ from the 2nd character

def assignment():
    str = "Python Course"
    print(str[0]) # Output : P
    print(str[1:5]) # Output : ytho
    print(str[-1]) # Output : e
    print(str[::-1]) # Output : esruoC nohtyP
    print(str[::2]) # Output : PtoCue
    print(str[1::2]) # Output : yhnCrs

    # 4. Python Libraries 
        # 4.1 NumPy
        # NumPy used for working with arrays and it is upto 50 times faster than python lists because it is written on C++.
        # The array object in NumPy is called ndarray.
#to import
import numpy as np
def numpylib():
    np1 = np.array([1,2,3,4,5])
    print(np1) # Output : [1 2 3 4 5]
    type(np1)
    # Output : numpy.ndarray
    #np.array -> defines an ndarray
    Mat1 = np.array([[1,2],[3,4]])
    print(Mat1)
    #Output: [[1 2]
    #         [3 4]]    
    #np.arange -> defines an ndarray with evenly spaced values within a given interval
    Mat2 = np.arange(0,10,1)
    print(Mat2)
    #Output: [0 1 2 3 4 5 6 7 8 9]
    #np.linspace -> defines an ndarray with evenly spaced values within a given interval
    Mat3 = np.linspace((0,10,20))
    print(Mat3)
    #Output: [ 0.          0.52631579  1.05263158  1.57894737  2.10526316  2.63157895
    #          3.15789474  3.68421053  4.21052632  4.73684211  5.26315789  5.78947368
    #          6.31578947  6.84210526  7.36842105  7.89473684  8.42105263  8.94736842
    #          9.47368421  10.        ]
    #np.random.rand -> defines an ndarray with random values
    Mat4 = np.random.rand(5,5)
    print(Mat4)
    #Output: [[0.92961609 0.31637555 0.18391881 0.20456028 0.56772503]
    #         [0.5955447  0.96451452 0.6531771  0.74890664 0.65356987]
    #         [0.74771481 0.96130673 0.0083883  0.10644438 0.29870371]
    #         [0.65641118 0.80900791 0.87219247 0.96499075 0.41192642]
    #         [0.35997806 0.54908353 0.57367585 0.9292962  0.31856895]]
    #np.random.randn -> defines an ndarray with random values
    Mat5 = np.random.randn(2,2)
    print(Mat5)
    #Output: [[-0.10757829  0.20119455]
    #         [ 0.09488596 -0.1043849 ]]
    #np.random.randint -> defines an ndarray with random integers
    Mat6 = np.random.randint(1,100,10)
    print(Mat6)
    #Output: [ 8  9  1  2  1  1  1  1  1 10]
    #np.zeros -> defines an ndarray with all zeros
    Mat7 = np.zeros((2,2))
    print(Mat7)
    #Output: [[0. 0.]
    #         [0. 0.]]
    #np.ones -> defines an ndarray with all ones
    Mat8 = np.ones((2,2))
    print(Mat8)
    #Output: [[1. 1.]
    #         [1. 1.]]
    #np.eye -> defines an ndarray with ones on the diagonal and zeros elsewhere
    Mat9 = np.eye(4)
    print(Mat9)
    #Output: [[1. 0. 0. 0.]
    #         [0. 1. 0. 0.]
    #         [0. 0. 1. 0.]
    #         [0. 0. 0. 1.]
        
        #4.2 Pandas~
        # Pandas is used for data manipulation and analysis. It is built on top of NumPy.
        # The two main data structures in Pandas are Series and DataFrame.
        # Series is a one-dimensional array with labels called index.
        # DataFrame is a two-dimensional array with labels called index and columns.
#to import
import pandas as pd
def pandaslib():
    global df 
    df = pd.read_csv("C:\python\Deep_Learning_Internshala\Customer.csv")
    # To read csv file 
    df.head()
    # To See first 5 rows
    df.tail()
    # To See last 5 rows
    df.describe()
    # To See summary statistics
    df.info()
    # To See data types of each column
    df.shape
    # To See number of rows and columns
    df.iloc["Column_Name"]
    # To See a particular column
    df.iloc[0:5]
    # To See data of first 5 rows
    df.iloc[0:5, 0:2]
    # To See data of first 5 rows and first 2 columns
        # 4.3 Seaborn
            # Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
# to import
import seaborn as sns
def seabornlib():
    sns.distplot(df.Age)
    # To See distribution plot of Age column
    sns.distplot(df.Age, kde=False)
    # To See distribution plot of Age column without density curve
    sns.distplot(df.Age, kde=False, color="red")
    # To See distribution plot of Age column without density curve and with red color
    sns.distplot(df.Age, kde=False, color="red", bins=10)
    # To See distribution plot of Age column without density curve and with red color and 10 bins
    iris = sns.load_dataset("iris")
    # To load iris dataset
    iris.shape
    # To See number of rows and columns
    sns.jointplot(x="sepal_length", y="sepal_width", data=iris)
    # To See joint plot of sepal_length and sepal_width(scatter plot)
    sns.pairplot(iris)
    # To See pair plot of iris dataset

#Assignment 2
def assignment2():
    data1 = pd.read_csv("Assignment_2_fifa18_clean.csv")
    # To read csv file
    data1.head()
    # To See first 5 rows
    data1.describe()
    # To See summary statistics - percentile, mean, std etc
    sns.displot(data1,x="Wage_Euro")
    # To see distribution plot for Wage_Euro
    sns.jointplot(x="Wage_Euro", y="Overall", data=data1)
    # To See joint plot of Wage_Euro and Overall

    #5. Intro to Machine Learning and Deep Learning
        # 5.1 Machine Learning
            # Machine Learning is the field of study that gives computers the ability to learn without being explicitly programmed.
            # When Machine tries to improve its performance based on past data
            # Machine Learning is of 3 types - Supervised Learning, Unsupervised Learning and Reinforcement Learning
            # ML Algorithms like LR, Logistic Regression, Decision Tree, ANN
        # 5.2 Deep Learning
            # Deep Learning is a subset of Machine Learning, which is a subset of Artificial Intelligence.
            # Deep Learning is inspired by the human brain, which is made up of billions of neurons.
            # Deep Learning is used to solve complex problems like image classification, speech recognition, object detection etc.
            # Neural networks are known as Deep Learning Models
        # 5.3 Type of ML Problems
            # Classification - Predicting a category or class
            # when output is categorical variable
            # Regression - Predicting a continuous value
            # when output is continuous variable
        # 5.4 Steps inn Building ML Model
            # 1. Problem Formulation - Convert business problem into Statistical Problem
            # 2. Data Tidying - Transformed collected data into a useable data table format
            # 3. Data Preprocessing - Filtering of data, aggregate values, missing value and outliers treatment, variable transformation and reduction.
            # 4. Test-Train Split - Splitting data into data used to train the model and data used for predictions
            # 5. Model Training - Building a model using training data
            # 6. Model Evaluation - Evaluating the model using test data using performance metrics.
            # 7. Prediction - setup a pipleine to use model in real life and improvement if needed

