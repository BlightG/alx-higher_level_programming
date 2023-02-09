# 0x14. JavaScript - Web scraping

## Resources
**Read or watch:**

- Working with JSON data
- The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco
- request module
- Modern JS

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google**:

### General

- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use **request** and fetch API
- How to read and write a file using fs module

### Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### General

- Allowed editors: **vi**, **vim**, **emacs**
- All your files will be interpreted on Ubuntu 14.04 LTS using node (version 10.14.x)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/node
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
- All your files must be executable
- The length of your files will be tested using wc
- You are not allowed to use var

## More Info

### Install Node 10

    $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    $ sudo apt-get install -y nodejs

### Install semi-standard

[Documentation](https://github.com/standard/semistandard)

`$ sudo npm install semistandard --global`

### Install **request** module and use it

[Documentation](https://github.com/request/request)

    $ sudo npm install request --global
    $ export NODE_PATH=/usr/lib/node_modules

**Notes**: Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

## Tasks

### 0. Readme

Write a script that reads and prints the content of a file.

- The first argument is the file path
- The content of the file must be read in **utf-8**
- If an error occurred during the reading, print the error object
- File: **0-readme.js**

### 1.Write me

Write a script that writes a string to a file.

- The first argument is the file path
- The second argument is the string to write
- The content of the file must be written in utf-8
- If an error occurred during while writing, print the error object
- File: **1-writeme.js**
