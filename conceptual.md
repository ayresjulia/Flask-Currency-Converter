# Conceptual Exercise

_Answer the following questions below:_

* What are important differences between Python and JavaScript?  
  * Python has slightly easier syntax.  
  * JavaScript is mainly a front-end framework, Python is back-end.  
  * Python has a wide range of modules, that help with functional, imperative, object-oriented and procedural programming.  
  * JavaScript is mainly object-oriented programming, using ECMAScript language specification.  
  * JavaScript is better for developing mobile applications, while Python not so much.  

* Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") **without** your programming
  crashing.  
  
  1. my_dict = {"a": 1, "b": 2}  
     my_dict.setdefault('c','Does not exist')
  2. my_dict.get('c','Does not exist')  

* What is a unit test?  
  * testing of an individual component

* What is an integration test?  
  * testing if different components work together properly

* What is the role of web application framework, like Flask?  
  * Flask helps with writing code more efficiently, as it has great collection of modules and librarires. Flask helps with which requests to respond to from server, how to respond to requests.

* You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?  
  * Query parameters are best when used to sort and filter data when working with APIs
  * It's best to use path parameters in the applications to identify specific recourses

* How do you collect data from a URL placeholder parameter using Flask?  
  * request.args.get("param")

* How do you collect data from the query string using Flask?  
  * request.args.get("param")

* How do you collect data from the body of the request using Flask?  
  * request.form['param']

* What is a cookie and what kinds of things are they commonly used for?  
  * Cookies are a way to store small amount of information in the browser, it is a key + value pair. Most common use of cookies is to keep a user logged in to the website as they go from page to page, it enhances user experience. The website remembers information about the user and carries it on while user continues browsing a page.

* What is the session object in Flask?  
  * The session object is useful to track session data of a user. It is stored as a cookie (key + value pair) in the browser.

* What does Flask's `jsonify()` do?  
  * jsonify() is a function that helps to return data in JSON format.
