![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!




# **Print Smoothies**
![Print smoothies logo](assets/images/banner.png "Print smoothies logo")

## **Site Overview**

Print(smoothies) is a fictional smoothie bar in Dublin's city centre.
This program has been developed to allow customer's to preorder their items or set up a reoccuring order to collect every week.
The program is linked via API to a Google Sheet which management can use to see data on the orders.

![Am I Responsive Screenshot](assets/images "Am I Responsive Screenshot")

## **Table Of Contents**

1. [**Site Overview**](#site-overview)
2. [**Project Goals**](#project-goals)
   - [Site Owner Goals](#site-owner-goals)
   - [How This Will Be Achieved](#how-this-will-be-achieved)
3. [**UX**](#ux)
   - [Strategy and Scope](#strategy-and-scope)
     - [User Stories](#user-stories)
     - [User Requirements](#user-requirements)
   - [Structure and Skeleton](#structure-and-skeleton)
     - [Flow Chart](#flow-chart)
   - [Surface](#surface)
4. [**Testing and Validation**](#testing-and-validation)
   - [Bugs](#bugs)
     - [Solved Bugs](#solved-bugs)
     - [Validatior Testing](#validator-testing)
     - [Unfixed Bugs](#unfixed-bugs)
5. [**Deployment and Development**](#deployment-and-development)
6. [**Credits**](#credits)
   - [Technologies Used](#technologies-used)
   - [Media](#media)
   - [Content](#content)
   - [Code](#code)
   - [Acknowledgements](#acknowledgements)

---

## **Project Goals**

### **Site Owner Goals**



### **How This Will Be Achieved**

- The site will be one page with clear instructions and feedback given to the user at all times (e.g. when hovering the mouse, on clicking, results for each round etc)
- Dimensions for an extensive list of screen sizes will be tested.

---

## **UX**

### **Strategy and Scope**

#### **User Stories**

As a user I would like:



#### **User Requirements**



### **Structure and Skeleton**

#### **Flow Chart**


### **Surface**


## **Testing and Validation**

- I tested the game in the following browsers: Chrome, Firefox and Edge.
- The game has been tested on multiple mobile devices in person and via all the available devices on Dev Tools toolbar.
- I confirmed the fonts, colors and all text items are clear, adequately contrasted, legible and easy to understand.
- Initially LightHouse returned a score of 98% as I skipped the use of 'h2' headings and began using 'h3'. This was flagged as bad practice for screen readers and all headings below 'h1' were amended.

![Lighthouse Score](assets/images/documentation/lighthouse-review.jpg)

### **Bugs**

#### **Solved Bugs**


#### **Validator testing**



#### **Unfixed bugs**

- There are no unfixed bugs.

---

## **Deployment and Development**



The live link can be found here - [Rock Paper Scissors](https://modonohoe.github.io/rock-paper-scissors/)

---

## **Credits**

### **Technologies Used**

- [Balsamiq](https://balsamiq.com/) to create the wireframes.
- [Codeanywhere](https://codeanywhere.com/) IDE for editing the site.
- [Github](https://github.com/) to host the repository and deploy the site.
- [Google Dev Tools](https://developer.chrome.com/docs/devtools/) to troubleshoot and test ideas
- [Am I Responsive?](https://ui.dev/amiresponsive) to generate an image showing responsivness of the site across multiple devices.

### **Media**

- [Vecteezy.com](https://www.vecteezy.com/free-vector/rock-paper-scissors) the The image for the rock, paper and scissors.
- [Google Fonts](https://fonts.google.com/) to source and import all fonts.
- [Font Awesome](https://fontawesome.com/) for the icons in the rules section and GitHub icon in footer.
- [Favicon](https://favicon.io/) where the site's favicon was sourced.

### **Code**

- Two JavaScript functions were adopted from the 'Rock, Paper, Scissors' walkthrough by Matt Rudge via Code Institute.

- I found this article helpful regarding font-sizing and rem [Why I change the font size to 62.5%](https://javascript.plainenglish.io/why-i-change-the-font-size-to-62-5-in-every-project-45c5ff785fb5)

### **Acknowledgements**

- Thank you to Code Institute - the content creators, my mentor, the tutors and the Slack community who all contributed to my understanding of JavaScript fundamentals during this project.

[Return to top](#table-of-contents)