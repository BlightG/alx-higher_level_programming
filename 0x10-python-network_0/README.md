# 0x10. Python - Network #0

## Resources

**Read or watch**

- [HTTP (HyperText Transfer Protocol](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html) (*except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation*)
- [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

## Learning Objectives 
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google:**

### General

- What a URL is
- What HTTP is
- How to read a URL
- The scheme for a HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser (Application level)

### Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### General
- Allowed editors: **vi**, **vim**, **emacs**
- A **README.md** file, at the root of the folder of the project, is mandatory
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your Bash scripts should be exactly 3 lines long (**wc -l** file should print 3)
- All your files should end with a new line
- All your files must be executable
- The first line of all your bash files should be exactly **#!/bin/bash**
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- All **curl** commands must have the option **-s** (silent mode)
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using **python3** (version 3.8.5)
- The first line of all your Python files should be exactly **#!/usr/bin/python3**
- Your code should use the pycodestyle (version **2.8.\**)
- All your modules should be documented: **python3 -c 'print(__import__("my_module").__doc__)'**
- All your classes should be documented: **python3 -c 'print(__import__("my_module").MyClass.__doc__)'**
- All your functions (inside and outside a class) should be documented: **python3 -c 'print(__import__("my_module").my_function.__doc__)'** and **python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'**
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks

#### 0. cURL body size

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

- The size must be displayed in bytes
- You have to use **curl**
Please test your script in the sandbox provided, using the web server running on port 5000

#### 1. cURL to the end

Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

- Display only body of a **200** status code response
- You have to use **curl**
