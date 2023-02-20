# 0x15. JavaScript - Web jQuery

### Concepts

*For this project, we expect you to look at theses concepts:*

- [JavaScript in the browser](https://intranet.alxswe.com/concepts/3)
- [Dealing with data statically versus dynamically](https://intranet.alxswe.com/concepts/35)

## Resources
Read or watch:

- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
- [Selector](https://jquery-tutorial.net/selectors/using-elements-ids-and-classes/)
- [Get and set content](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-content/)
- [Manipulate CSS classes](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/)
- [Manipulate DOM elements](https://jquery-tutorial.net/dom-manipulation/the-append-and-prepend-methods/)
- [API](https://oscarotero.com/jquery/)
- [Introduction](https://jquery-tutorial.net/ajax/introduction/)
- [GET & POST request](https://jquery-tutorial.net/ajax/the-get-and-post-methods/)
- [JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://www.youtube.com/watch?v=fEYx8dQr_cQ)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)
- [JQuery](https://jquery.com/)
- [JQuery API](https://api.jquery.com/)
- [JQuery Ajax](https://learn.jquery.com/ajax/)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google:**

### General

- Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
- How to select HTML elements in JavaScript
- How to select HTML elements with JQuery
- What are differences between **ID**, **class** and **tag name** selectors
- How to modify an HTML element style
- How to get and update an HTML element content
- How to modify the DOM
- How to make a **GET** request with JQuery Ajax
- How to make a **POST** request with JQuery Ajax
- How to listen/bind to DOM events
- How to listen/bind to user events

### Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### General

- Allowed editors: **vi**, **vim**, **emacs**
- All your files will be interpreted on Chrome (version 57.0)
- All your files should end with a new line
- A **README.md** file, at the root of the folder of the project, is mandatory
- Your code should be **semistandard** compliant with the flag **--global $**: **semistandard *.js --global $**
- You must use JQuery version 3.x
- You are not allowed to use **var**
- HTML should not reload for each action: DOM manipulation, update values, fetch data…

## More Info
### Import JQuery

     <head>
         <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    </head>

## Tasks
### 0.No JQuery

Write a JavaScript script that updates the text color of the **<header>** element to red (**#FF0000**):

- You must use **document.querySelector** to select the HTML tag
- You can’t use the JQuery API
- File: **0-script.js**

### 1. With JQuery

Write a JavaScript script that updates the text color of the **<header>** element to red (**#FF0000**):

- You can’t use **document.querySelector** to select the HTML tag
- You must use the JQuery API
- File: 1-script.js

### 2. Click and turn red

Write a JavaScript script that updates the text color of the **<header>** element to red (**#FF0000**) when the user clicks on the tag **DIV#red_header**:

- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API
- File: 2-script.js

### 3. Add \`.red\` class

Write a JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header

- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API
- File: 3-script.js