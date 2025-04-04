# Crochet Corner

## Intro

  - Crochet Corner is an eCommerce platform designed for customers to explore and purchase crochet yarn and tools. Its target audience are creative individuals, serving both novice crafters and experienced crocheters alike. The site allows customers to browse a wide range of crochet tools and yarns in various colors, with filtering options to streamline their search experience. Crochet Corner aims to promote its diverse product offerings, inspire customers to make purchases, and encourage repeat visits for future purchases. To achieve these goals, user stories were crafted to focus on key functionalities such as viewing and filtering products, uploading information to the database, and enabling account creation. By providing users the ability to save contact details, the site simplifies the checkout process for a seamless and efficient shopping experience.

         

![Responsive Mockup Image]()

  ### Roles of the site:

## Database Design (Models)


## User Experience Stories


 ![user stories](user_stories_link)

  __User Stories__


## Design

  __Color Scheme__

  - During the design process for Crochet Corner, I explored numerous crochet websites to draw inspiration for the color palette. A common trend among these sites was the use of pale background colors paired with bright, bold hues for logos and headings. To make the Logo stand out against the soft Ivory and Cream backgrounds, Pink was chosen as the primary color, naturally capturing the user's attention. This vibrant Pink theme is carried through to the headings and the My Profile page, ensuring a cohesive and visually appealing experience. Teal was selected for all buttons, complementing the Pink accents while creating a standout effect that ensures clarity and usability across the site. Black is used for all remaining text, providing a crisp, clean contrast that ties the design together with clarity and consistency
  
  __Typography__

   - The Crochet Corner website uses a blend of four distinct fonts to craft its unique and appealing visual identity. The logo combines the playful character of Leckerli One with the sleek elegance of Poiret One, creating a striking and memorable visual identity. For headings, the clean elegance of Josephin Sans enhances readability and structure, while Oregano introduces a warm, personal touch to elements such as usernames and messages. Nunito, renowned for its excellent readability, provides a seamless foundation for the remaining text, ensuring a smooth and user-friendly experience. Together, these fonts harmonize to enhance the website's charm, functionality, and personality.

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

    - Unsupported lookup 'name' for ForeignKey or join in the field is not permitted:
        This error occured when first creating the search query within the Yarn dropdown menu and running the site to test the code. When selecting one of the categories from the Yarn dropdown menu in the main-menu header, an error page appeared with the following error "Unsupported lookup 'name' for ForeignKey or join in the field is not permitted". 
        Through searching online found some suggestions that the issue was related to the variable used within the view. The original GET request code wrote:

            if 'yarn_category' in request.GET:
                yarn_categories = request.GET['yarn_category'].split(',')
                products = products.filter(yarn_category__name__in=yarn_categories)
                yarn_categories = YarnCategory.objects.filter(name__in=yarn_categories)
        
        This code was written following guidance from the Boutique Ado walkthrough project.
        This error was resolved through changing 'name to 'yarn_category_name' as this matches the category name field the the YarnCategory model. The new code now appears as:

            if 'yarn_category' in request.GET:
                yarn_categories = request.GET['yarn_category'].split(',')
                products = products.filter(yarn_category__yarn_category_name__in=yarn_categories)
                yarn_categories = YarnCategory.objects.filter(yarn_category_name__in=yarn_categories)

        Now, when running the site and selecting a Yarn category from the Yarn dropdown menu the results successfully produce a list of the products within that category.


    - UnboundLocalError: cannot access local variable 'yarn_categories' where it is not associated with a value:
        This error occured when creating the search query with the Tools dropdown menu and running the site to test the code. When selecting one of the categories from the Tools dropdown menu in the main-header, an error page appeared with the following error "UnboundLocalError: cannot access local variable 'yarn_categories' where it is not associated with a value". When refreshing back to the home page and selecting a category from the Yarn dropdown menu a similar error page appeared, however this time referencing the 'tool_categories' - "UnboundLocalError: cannot access local variable 'tool_categories' where it is not associated with a value". This suggested that even though in the URL the correct name query is referenced (yarn_categories when selecting from the Yarn dropdown and tool_categories when selecting from the Tool dropdown), the other query within the context is still being searched for. 
        This error has been resolved through setting the other query back to None at the start of each GET request:

            if 'yarn_category' in request.GET:
                tool_categories = None
                yarn_categories = .....

            if 'tool_category' in request.GET:
                yarn_categories = None
                tool_categories = .....
        
        Now, when running the site and selecting a category from either the Yarn dropdown menu or Tools dropdown menu, the results successfully produce a list of the products within that category.

    - Invalid filter: 'calc_subtotal':
        This error occured when attempting to create a custom template filter to calculate the individual total cost of an item in the basket dependent on the quantity of that item. When running the site to test the code received an error page stating "Invalid filter: 'calc_subtotal'". 
        Removed the name argument on the filter decorator to explicitly set the name of the filter to the name of the function without applying an additional argument. This did not fix the error. Also found solution online to add the custom template filter to the built in templates in settings.py, again this did not resolve the error. Added some print statements above the return statement within the code to see if anything appeared in the terminal when refreshing the page, nothing appeared. This suggested that there was an issue between the custom template filter setup and the basket.html document. Eventually discovered a typo at the top of the html page.
        This error was resolved through amending the typo. I had used brackets instead of curly braces when writing the template tag to extend the custom template filter page.

            (% load basket_tools %)

            {% load basket_tools %}

    - Plus and Minus buttons unresponsive in basket.html:
        When creating the plus and minus buttons in basket.html to allow the user to edit the quanitity of the product in the basket and running the site to test the code, the buttons were unresponsive. They were working successfully in the products details page, however completely unresponsive in the basket page.
        I had followed the steps to create this from the Boutique Ado walkthrough project and it had been discovered that the fix for this was to replace the IDs in each button with classes so that they could be used more than once and avoid preventing the script from running due to duplicate ID issues. Also found I had missed an input group class in the top div element.
        Followed the below steps to resolve the issue:

            Changed:
            <div class="input-group">
                <div class="input-group-prepend">
                    <button class="decrement-qty btn rounded" data-item_id="{{ item.item_id }}" id="decrement-qty_{{ item.item_id }}">
                        <i class="fa-solid fa-minus"></i>
                    </button>
                </div>
                <input type="number" class="form-control qty_input" name="quantity" value="{{ item.quantity }}" min="1" max="99" data-item_id="{{ item.item_id }}" id="id_qty_{{ item.item_id }}">
                <div class="input-group-append">
                    <button class="increment-qty btn rounded" data-item_id="{{ item.item_id }}" id="increment-qty_{{ item.item_id }}">
                        <i class="fa-solid fa-plus"></i>
                    </button>
            
            To:
            <div class="input-group input-group-{{ item.item_id }}">
                <div class="input-group-prepend">
                    <button class="decrement-qty btn rounded decrement-qty_{{ item.item_id }}" data-item_id="{{ item.item_id }}">
                        <i class="fa-solid fa-minus"></i>
                    </button>
                </div>
                <input type="number" class="form-control qty_input id_qty_{{ item.item_id }}" name="quantity" value="{{ item.quantity }}" min="1" max="99" data-item_id="{{ item.item_id }}" id="">
                <div class="input-group-append">
                    <button class="increment-qty btn rounded increment-qty_{{ item.item_id }}" data-item_id="{{ item.item_id }}">
                        <i class="fa-solid fa-plus"></i>
                    </button>

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

    - The CSS code for re-arranging the order of the Header elements for smaller screens was taken from geeksforgeeks.org - https://www.hostinger.co.uk/tutorials/website-color-schemes 
         

### Content

    - The ispiration for the design and color palette for Crochet Corner was taken from:
        - Hostinger Tutorial - https://www.hostinger.co.uk/tutorials/website-color-schemes
        - Woolbox - https://www.woolbox.co.uk/
        - Lovecrafts - https://www.lovecrafts.com/en-gb
        - Crochet Society - https://crochetsociety.co.uk/?srsltid=AfmBOorCd5txlg3MBThMtyktYVhozNK0YdPAZmnp9OKtDt4Yj5dqrWiw
    - Pricing and item description is taken from:
        - Woolbox - https://www.woolbox.co.uk/
        - Lovecrafts - https://www.lovecrafts.com/en-gb
        - Crochet Society - https://crochetsociety.co.uk/?srsltid=AfmBOorCd5txlg3MBThMtyktYVhozNK0YdPAZmnp9OKtDt4Yj5dqrWiw
 
### Media

    - Homepage image taken from Pexels - https://www.pexels.com/search/crochet%20shopping/
    - Product images taken from:
        - Woolbox - https://www.woolbox.co.uk/
        - Lovecrafts - https://www.lovecrafts.com/en-gb 
        - Crochet Society - https://crochetsociety.co.uk/?srsltid=AfmBOorCd5txlg3MBThMtyktYVhozNK0YdPAZmnp9OKtDt4Yj5dqrWiw 




