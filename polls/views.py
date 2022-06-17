from os import name

from django.http import HttpResponse
from django.template import loader



def index(request):
    name = 'iTbook'
    book = [
        {'title': '','subtitle': '','isbn13': '', 'price': '', 'url': ''},
        {'title': '', 'subtitle': '','isbn13': '', 'price': '', 'url': ''},
        {'title': '', 'subtitle': '','isbn13': '', 'price': '', 'url': ''},
        {'title': '','subtitle': '', 'isbn13': '','price': '', 'url': ''},
        {'title': '', 'subtitle': '','isbn13': '', 'price': '', 'url': ''},
        {'title': '','subtitle': '', 'isbn13': '', 'price': '','url': ''},
        {'title': '', 'subtitle':'', 'isbn13': '','price': '', 'url': ''},
        {'title': '','subtitle':'', 'isbn13': '' ,'price': '','url': ''},
        {'title': '', 'subtitle': '', 'isbn13': '','price': '', 'url': ''},
        {'title': '', 'subtitle': '', 'isbn13': '','price': '', 'url': ''},
    ]
    temp = loader.get_template('hellotable.html')
    context = {
        'title' : name,
        'book' : book,
        }
    return HttpResponse(temp.render(context, request))

def index1(request):
    name = 'iTbook'
    book = [
    {'title': 'A Graduate Course in Applied Cryptography', 'subtitle': 'The indispensable tool used to protect information in computing systems', 'isbn13': '1001605608336','price':'$0.00','url':'https://itbook.store/books/1001605608336'},
    {'title': 'Information Security The Complete Reference, 2nd Edition', 'subtitle': '-', 'isbn13': '9780071784351','price':'$41.62','url':'https://itbook.store/books/9780071784351'},
    {'title': 'Information Dashboard Design','subtitle': 'The Effective Visual Communication of Data','isbn13': '9780596100162', 'price': '$4.50','url':'https://itbook.store/books/9780596100162'},
    {'title': 'Tomcat: The Definitive Guide, 2nd Edition','subtitle': 'Vital Information for Tomcat Programmers & Administrators','isbn13': '9780596101060', 'price': '$4.44','url':'https://itbook.store/books/9780596101060'},
    {'title': 'Optimizing and Accessing Information Technology','subtitle': 'Improving Business Project Execution','isbn13': '9781118000014', 'price': '$49.36','url':'https://itbook.store/books/9781118000014'},
    {'title': 'Filtering, Control and Fault Detection with Randomly Occurring Incomplete Information','subtitle': '-','isbn13': '9781118647912', 'price': '$105.57', 'url': 'https://itbook.store/books/9781118647912'},
    {'title': 'Getting an Information Security Job For Dummies','subtitle': '-','isbn13': '9781119002819', 'price': '$19.74', 'url': 'https://itbook.store/books/9781119002819'},
    {'title': 'Healthcare Information Technology Exam Guide, 2nd Edition','subtitle': 'For CHTS and CAHIMS Certifications','isbn13': '9781259836978', 'price': '$30.97', 'url': 'https://itbook.store/books/9781259836978'},
    {'title': 'Practical SharePoint 2010 Information Architecture','subtitle': '-','isbn13': '9781430241768', 'price': '$44.82', 'url': 'https://itbook.store/books/9781430241768'},
    {'title': 'Managing Risk and Information Security','subtitle': 'Protect to Enable','isbn13': '9781430251132', 'price': '$31.34', 'url': 'https://itbook.store/books/9781430251132'},
    ]
    temp = loader.get_template('hellotable.html')
    context = {
        'title' : name,
        'book' : book,
        }
    return HttpResponse(temp.render(context, request))

def index2(request):
    name = 'iTbook'
    book = [
    {'title': 'Algorithms, 4th Edition', 'subtitle': 'Essential Information about Algorithms and Data Structures', 'isbn13': '9780321573513','price':'$55.49','url':'https://itbook.store/books/9780321573513'},
    {'title': 'Python Algorithms', 'subtitle': 'Mastering Basic Algorithms in the Python Language', 'isbn13': '9781430232377','price':'$18.00','url':'https://itbook.store/books/9781430232377'},
    {'title': 'Python Algorithms, 2nd Edition','subtitle': 'Mastering Basic Algorithms in the Python Language','isbn13': '9781484200568', 'price': '$33.75','url':'https://itbook.store/books/9781484200568'},
    {'title': 'Data Mining Algorithms in C++','subtitle': 'Data Patterns and Algorithms for Modern Applications','isbn13': '9781484233146', 'price': '$9781484233146','url':'https://itbook.store/books/9781484233146'},
    {'title': 'Pro Machine Learning Algorithms','subtitle': 'A Hands-On Approach to Implementing Algorithms in Python and R','isbn13': '9781484235638', 'price': '$34.99','url':'https://itbook.store/books/9781484235638'},
    {'title': 'JavaScript Data Structures and Algorithms','subtitle': 'An Introduction to Understanding and Implementing Core Data Structure and Algorithm Fundamentals','isbn13': '9781484239872', 'price': '$26.76', 'url': 'https://itbook.store/books/9781484239872'},
    {'title': 'Introducing Algorithms in C','subtitle': 'A Step by Step Guide to Algorithms in C','isbn13': '9781484256220', 'price': '$26.91', 'url': 'https://itbook.store/books/9781484256220'},
    {'title': 'Modern Data Mining Algorithms in C++ and CUDA C','subtitle': 'Recent Developments in Feature Extraction and Selection Algorithms for Data Science','isbn13': '9781484259870', 'price': '$32.58', 'url': 'https://itbook.store/books/9781484259870'},
    {'title': 'Clojure Data Structures and Algorithms Cookbook','subtitle': '25 recipes to deeply understand and implement advanced algorithms in Clojure','isbn13': '9781785281457', 'price': '$47.52', 'url': 'https://itbook.store/books/9781785281457'},
    {'title': 'Mastering Machine Learning Algorithms','subtitle': 'Expert techniques to implement popular machine learning algorithms and fine-tune your models','isbn13': '9781788621113', 'price': '$44.99', 'url': 'https://itbook.store/books/9781788621113'},
    ]
    temp = loader.get_template('hellotable.html')
    context = {
        'title' : name,
        'book' : book,
        }
    return HttpResponse(temp.render(context, request))

def index3(request):
    name = 'iTbook'
    book = [
    {'title': 'Introduction to Data Science', 'subtitle': 'Data Analysis and Prediction Algorithms with R', 'isbn13': '1001605784278','price':'$0.00','url':'https://itbook.store/books/1001605784278'},
    {'title': 'Graph Databases For Beginners', 'subtitle': 'The #1 Platform for Connected Data', 'isbn13': '1001606307637','price':'$0.00','url':'https://itbook.store/books/1001606307637'},
    {'title': 'Critical Data Literacy','subtitle': 'Strategies to Effectively Interpret and Evaluate Data Visualizations','isbn13': '1001651514190', 'price': '$0.00','url':'https://itbook.store/books/1001651514190'},
    {'title': 'Programming Skills for Data Science','subtitle': 'Start Writing Code to Wrangle, Analyze, and Visualize Data with R','isbn13': '9780135133101', 'price': '$40.99','url':'https://itbook.store/books/9780135133101'},
    {'title': 'Learning iCloud Data Management','subtitle': 'A Hands-On Guide to Structuring Data for iOS and OS X','isbn13': '9780321889119', 'price': '$24.07','url':'https://itbook.store/books/9780321889119'},
    {'title': 'Learning Core Data for iOS','subtitle': 'A Hands-On Guide to Building Core Data Applications','isbn13': '9780321905765', 'price': '$3.72', 'url': 'https://itbook.store/books/9780321905765'},
    {'title': 'Beautiful Data','subtitle': '"The Stories Behind Elegant Data Solutions','isbn13': '9780596157111', 'price': '$18.99', 'url': 'https://itbook.store/books/9780596157111'},
    {'title': 'Visualizing Data','subtitle': 'Exploring and Explaining Data with the Processing Environment','isbn13': '9780596514556', 'price': '$19.98', 'url': 'https://itbook.store/books/9780596514556'},
    {'title': 'Data Analysis with Open Source Tools','subtitle': 'A hands-on guide for programmers and data scientists','isbn13': '9780596802356', 'price': '$3.20', 'url': 'https://itbook.store/books/9780596802356'},
    {'title': 'Communicating with Data','subtitle': 'Making Your Case With Data','isbn13': '9781098101855', 'price': '$69.99', 'url': 'https://itbook.store/books/9781098101855'},
    ]
    temp = loader.get_template('hellotable.html')
    context = {
        'title' : name,
        'book' : book,
        }
    return HttpResponse(temp.render(context, request))
