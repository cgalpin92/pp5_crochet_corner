# Crochet Corner

## Intro

  - Crochet Corner is an Ecommerce Site for customers to purchase Crochet Yarn and Crochet Tools. Its target audience will be that of creative individuals, both novices and experienced crocheters alike. Customers can browse different crochet tools and different types of crochet yarn of various colors, filtering by these types to assist with their searching experience. The main goals of Crochet Corner is to promote these different Crochet products, encourage customers to purchase these products and to return in the future to purchase further products again. The user stories that helped assist in reaching these goals for both the customer and the business were based around viewing and filtering products, uploading information to the database and creating accounts for users so that they could save contact information for easier checkout in the future.
        

![Responsive Mockup Image]()

  ### Roles of the site:

## Database Design (Models)


## User Experience Stories


 ![user stories](user_stories_link)

  __User Stories__


## Design

  __Color Scheme__

  __Typography__

  __Wireframes__

## Marketing

  ### eCommerce Business Model

  ### Marketing Strategies

  -__Facebook Mockup__
  -__Search Engine Optimisation__

## Features

### Existing Features

### Features left to Implement

## Technologies Used

### Languages Used:

  - HTML5
  - CSS3
  - Python
  - JavaScript

### Frameworks, Libraries and Programs Used:

## Testing

### Manual Testing

__Responsiveness Testing__


__Browser Compatibility Testing__


__Lighthouse Testing__


__User Stories Testing__



__Features Testing__

### Validator Testing

__HTML__


__CSS__

__JavaScript__

__Python__

### Bugs

  - __Fixed Bugs__

  - __Unfixed Bugs__

## Deployment

### Forking:
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate this [GitHub Repository](repo_link)
2. At the top of the Repository just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Cloning:
1. Log in to GitHub and locate this [GitHub Repository](repo_link)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

For further information and a more detailed explanation, click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)

### Heroku
This project was deployed using Heroku.
-__Prior stepts__
To project required the following steps prior to the deployment to Heroku.
  - install gunicorn ~=20.1 - the production equivalent of manage.py runserver
    - The creation of Profile with the inclusion of web:gunicorn baking_bliss.wsgi - the command heroku uses to find the correct .py file to run and start the server
  - add .herokuapp.com to ALLOWED_HOSTS within settings.py
  - install for whitenoise to handle the static files.

- __Steps for deployment:__
    - Fork or clone this repository
    - Create a new Heroku app
        - Login to Heroku and select __Create New App__
        - Create app name
        - Select your __region__
        - Select __Create App__
    - Change Heroku Settings
        - Select __Settings__
        - Scroll down to __Config Var__ section and select __reveal config var__
        - Enter the following information into the __Key__ and __value__ inputs:
            - __Key:__ COLLECT_STATIC_FILES
            - __Value:__ 1
        - Select __Add__    
    - Link the Heroku app to the repository:
        - Select __Deploy__ from the top of the page.
        - Scroll down to __Deployment method__
        - Select __GitHub. Connect to GitHub__
        - Enter your repository name and click search
        - Select connect next to your repository name
    - Click on __Deploy__

### AWS S3 Bucket Creation

### Stripe Configuration

## Credits

### Code

    - The Boutique Ado walkthrough was used as a boilerplate for setting up the Ecommerce site as well as some further code and guidance for building particular elements of the project.
         

### Content
 
### Media




