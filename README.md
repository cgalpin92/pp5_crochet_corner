# Crochet Corner

## Intro

  - Crochet Corner is an eCommerce platform designed for customers to explore and purchase crochet yarn and tools. Its target audience are creative individuals, serving both novice crafters and experienced crocheters alike. The site allows customers to browse a wide range of crochet tools and yarns in various colors, with filtering options to streamline their search experience. Crochet Corner aims to promote its diverse product offerings, inspire customers to make purchases, and encourage repeat visits for future purchases. To achieve these goals, user stories were crafted to focus on key functionalities such as viewing and filtering products, uploading information to the database, and enabling account creation. By providing users the ability to save contact details, the site simplifies the checkout process for a seamless and efficient shopping experience.

         

![Responsive Mockup Image]()

  ### Roles of the site:

## Database Design (Models)

I have used a total of 8 Models within this project:

- Products:
    - This model efficiently stores all essential product details, including the name, image, description, and price. Products are uploaded by the Site Admin through the Admin Center, ensuring streamlined management.

    - The color model field is a Character Field linked to an array of predefined options called COLOR_OPTIONS. This setup enables the Site Admin to assign a color category via a dropdown selection, making it easier to filter and organize products effectively.

    - There are a number of Foreign key relationships with other models:

        - ProductCategory: The product category field has a Foreign Key relationship with the ProductCategory Model. A product can only have one Product Category but a Product Category can have multiple products.

        - YarnCategory: The yarn category field has a Foreign Key relationship with the YarnCategory model. This field is not a required field as a product will either have a yarn category or tool category. Again a product can only have one Yarn or Tool category but a Yarn or Tool category can have many products within them.

        - ToolCategory: The tool category field has a Foreign Key relationship with the ToolCategory model. Agan this field is not a required field as a product with either have a tool category or yarn category. The product can only have one Tool or Yarn category but the Tool or Yarn categories can have multiple products related to it.

        - YarnBrand: The yarn brand field has a Foreign Key relationship with the YarnBrand model. This field is not a required field as a product will either have a yarn brand or tool brand. Again a product can only have one Yarn or Tool brand but a Yarn or Tool brand can have many products within them.

        - Tool Brand: The tool brand field has a Foreign Key relationship with the ToolBrand model. This field is not a required field as a product will either have a tool brand or yarn brand. Again a product can only have one Tool or Yarn brand but a Tool or Yarn brand can have many products within them.

- YarnCategory:
    - This model stores all of the Yarn weight Categories; 4 Ply, Aran and DK. The Site Admin can create new Yarn Categories from within the Admin Center as the site grows and further products with other Yarn Weights are added. Once added, these categories seamlessly integrate into the Product Model, appearing as selectable options when the Site Owner uploads a new product to the database.

- ToolCategory:
    - This model stores all of the Tool Categories; Crochet Hooks and Needles, Counters and Markers, Yarn Bowls and Other. The Site Admin can create new Tool Categories from within the Admin Center as the site grows and further products with other Tool Categories are added. Once added, these categories seamlessly integrate into the Product Model, appearing as selectable options when the Site Owner uploads a new product to the database.

- YarnBrand:
    - This model stores all of the Yarn Brands; West Yorkshire Spinners Signature, Creative Cotton, Scheepjes Chunky Monkey, and Crochet Society. The Site Admin can create new Yarn Brands from within the Admin Center as the site grows and further products by other Yarn Brands are added. Once added, these brands seamlessly integrate into the Product Model, appearing as selectable options when the Site Owner uploads a new product to the database.

- ToolsBrand:
    - This model stores all of the Tool Brands; Clover Armour, Knit Pro, Pony, Sirdar, Crochet Society and Bella Coco. The Site Admin can create new Tool Brands from within the Admin Center as the site grows and further products by other Tool Brands are added. Once added, these brands seamlessly integrate into the Product Model, appearing as selectable options when the Site Owner uploads a new product to the database.
         

- Product_Category:
    - This model stores the different Product Categories which the Site Admin can create from within the Admin Center. Currently there are only two categories; Yarn and Tools, however as the site grows to include other product types such as Yarn Patterns or Accessories, further categories can be added into this model. Once added, these categories seamlessly integrate into the Product Model, appearing as selectable options when the Site Owner uploads a new product to the database.

- Orders:
    - This model stores all relevant details for each completed order placed by a site user. Orders are generated directly from the front end of the site, capturing user-submitted information seamlessly.

    - The order status field is a Character Field linked to an array of predefined order status options: Pending, Dispatched, Return Pending, and Returned. By default, new orders are assigned a Pending status. The Site Owner can update this status within the database to reflect the order’s progression—whether it has been Dispatched, marked as Return Pending, or fully Returned.


- Order_Line_Item:
    - This model stores all relevant details for each individual item within an order. The information is generated directly from the user via the front end of the site, ensuring accurate data capture.

    - Additionally, the model includes two foreign key relationships, providing structured connections between related data entities for seamless integration within the database.

        - Order: The order model field has a Foreign Key relationship with the Order Model. One Order Line Item can only be in one order, however an order can contain many Order Line Items.

        - Product: A Order line item can relate to only one product, however a product can relate to many order line items. 






## User Experience Stories

I implemented Agile Methods to plan and develop the Crochet Corner eCommerce site, ensuring flexibility and efficiency throughout the process. By leveraging User Experience stories, I prioritized both the end user and site owner, keeping them at the heart of every design and functionality decision.

To track progress and maintain alignment with project goals, I used GitHub Projects to document and manage user stories, systematically mapping them against the final product. Every story was successfully completed by the project's conclusion, ensuring a well-structured and user-focused outcome.

__User Stories__


![user stories](user_stories_link)

- As a site user I can easily create an account so that I can check out quicker next time

    - When a user selects 'Register' they are presented with a registration page to create an account

    - Once a user has completed the form to create an account their username is present in the top of the page

    - Once an account has been created a user is able to navigate to the 'My Accounts' page successfully


- As a site user I can log into my account so that I can view previous orders

    - The site user can navigate to the 'Sign In' page and successfully sign in

    - Once signed in the user is able to select the 'My Account' page and select Order History

    - Given the user has made purchases they will be listed here, if the user has not made any previous orders it will state 'No Previous Orders'

- As a sire user I can log into my account so that I can update default contact and address information

    - Given the user has successfully signed in they can navigate to the 'My Account' page.

    - From here they can select the 'Edit' button and change the information in the required default field.

    - Once they have selected the 'Update' button the new default information is displayed.

- As a site user I can delete my account so that I no longer have saved information on Crochet Corner

    - Given the user has successfully signed in they can navigate to the 'My Account' page.

    - From here they can scroll down to the bottom of the page and select 'Delete Account'.

    - The user is taken back to the Home page and when attempting to sign in with same details the are informed the account does not exist.

- As a site user I can add orders to the shopping basket so that I can view orders before purchasing them

    - The 'Add to basket' button is visible on the product item page.

    - When selecting the above button the user is notified that the item has been added to the shopping basket.

    - When selecting the Shopping Basket icon the item they have added is listed

- As a site user I can view the shopping basket so that edit or remove items

    - The site user can select the shopping basket icon located at the top right of the page.

    - The user can select 'View shopping basket'.

    - The user can select either 'remove item' or update the quantity of the item.

- As a site owner I can upload new items to the admin portal so that new products can be displayed on the Crochet Corner page

    - The super user can log into the Admin Portal successfully.

    - They can select the products area on the database.

    - They can select the new product button and complete the required fields for uploading a new product.

    - The super user can then navigate to the Crochet Corner site and view the product either under the All Products page or through the sub-category field assigned to it when uploading the product in the admin portal.

- As a site owner I can view new orders placed by site users so that I can send out purchased products

    - The site owner can log into Crochet Corner's admin site and navigate to the Orders section

    - The site owner can filter the orders by status to view pending orders

- As a site owner I can log into the admin portal so that remove user accounts from the database

    - The site owner can log into Crochet Corner's admin site and navigate to the Users section.

    - The site owner can search for specific user account.

    - The 'delete' button is visible and the site owner can delete user the account from the database.

- As a site user I can filter products by criteria so that I can make it easier to find the product I am looking for

    - The site user can navigate to either All Products or the Products by category.

    - The site user can select the required filter options in the left hand panel when on larger screens or select the filter button on smaller screens.

    - Once they have selected the required options the remaining products listed are in relation to these options.

- As a site user I can easily navigate around the navigation menu so that I can get to a specific area of the site

    - When on larger screens the navigation menu is clearly visible at the top of the page, or when on smaller screens the navigation menu is clearly identified by a burger icon and expands when selected.

    - The different pages are clearly labelled with the current page clearly identified.

    - The user is taken to the correct page when selecting it.

- As a site user I can easily navigate to the Sign Up to the Newsletter page so that I can receive offers and tips on creating crochet items

    - The site user can navigate to and select the 'Newsletter' page in the menu list

    - They are re-directed to the Newsletter sign up form

    - Once they have completed all the required information and selected sign up they are notified by a message on the screen that this has been successfull

- As a site user I can view product information so that I can decide if the product is the correct product before adding it to the basket

    - The user can select either All Products or the product category from the navigation menu.

    - When selecting on an individual item the user is re-directed to a page which displays all the product information.

    - The product name, description, price, stock availability and image are displayed to the user.



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

__Header and Navigation Bar__

The Header and Navigation Bar seamlessly integrates the Site Name, search bar, and two distinct menus. Positioned on the left side of the screen, the Site Name — which doubles as the logo — features two distinct fonts and colors, making it visually striking and memorable.

The Search Bar sits beside the Site Name in the center of the header on medium and large screens, but shifts to the bottom of the header on smaller screens for optimal responsiveness.

The first menu, located on the right side of the header, includes the Account dropdown and Shopping Basket. These elements are fully responsive, displaying both the name and icon on medium and large screens, while only the icon appears on smaller screens for a streamlined look. Once a user has signed into their account, they can access their profile directly from this section. Their username is displayed in a distinct font, ensuring it stands out and is easily recognizable.

The second menu serves as the final component of the Header and Navigation Bar, providing intuitive navigation options. It includes links to the Home Screen, All Products—with a dropdown to filter by Price, Yarn Products—with dropdown filters for Yarn Weight and Yarn Brand, and Tools—with dropdown filters for Tool Type and Brand. This menu is also fully responsive, appearing beneath the Site Name and spanning the header’s width on larger screens. On smaller screens, it transforms into a burger icon, positioned at the top left corner and expanding vertically when selected.

The Header and Navigation Bar showcase the brand’s signature colors—Pink, Ivory, Teal, White, and Black—creating a cohesive and visually appealing design. The typography and color scheme remain consistent across all pages, ensuring a seamless user experience and effortless navigation.

__Home Page__

The Home Page is designed to be both bold and inviting, immediately drawing users in. The background features a vibrant yarn image, seamlessly connecting to the theme of the eCommerce store. At the center of the screen, a striking welcome message stands out against Crochet Corner’s signature pink background, accompanied by a teal “Shop Now” button positioned just below, encouraging users to explore the store with ease.

__Products Pages__

The Product Pages listed below can be accessed via the second navigation menu in the header. On each page, products are displayed in rows, with four items per row on larger screens, gradually adjusting to a single-item-per-row format, stacking vertically on smaller devices for optimal responsiveness.

The crochet image background is replaced with a plain Ivory background, matching the Header background for a clean and cohesive design. Each product listing features a high-quality image, product name, category, and price. The product name and category are presented in black font, while the price stands out in Crochet Corner’s signature pink font, ensuring key details are clearly visible.

Users can access detailed product information by clicking on either the product image or product name, seamlessly navigating to the product details page.

__All Products Page__

The All Products Page provides a comprehensive overview of every item available, regardless of category. This page is designed to give users a single, centralized space where they can easily browse the full selection of products.
Within the All Products dropdown menu, users can select the "By Price" option to sort items in ascending order, ensuring that the lowest-priced products appear first for quick and convenient browsing.

__Yarn Products Page__

The Yarn Products Page provides a complete selection of yarn products, allowing users to browse with ease. Through the dropdown menu, users can refine their search using three options:
- All Yarn – Displays all available yarn products, regardless of weight category or brand.

- Yarn Weight Categories – Filters yarn products by specific weight category, helping users find the perfect match.

- Yarn Brands – Allows users to filter yarn products by brand, ensuring they can quickly locate their preferred manufacturers.


__Tools Products Page__

The Tools Products Page offers a comprehensive selection of crochet tools, ensuring users can easily find the right products. Through the dropdown menu, users can refine their search using three options:
- All Tools – Displays the full range of available crochet tools, regardless of category or brand.

- Tool Categories – Filters tools by specific categories, helping users quickly locate the best fit for their needs.

- Tool Brands – Allows users to filter tools by brand, ensuring they can efficiently find products from their preferred manufacturers.

__Product Details Page__

This page presents detailed product information, organized into columns that adjust dynamically based on screen size—stacking side by side on larger screens and vertically on smaller screens for an optimal viewing experience.


- The first column features the product image, ensuring a clear visual representation. On smaller screens, the image is displayed at the top, with the remaining product details stacked below. On larger screens, it shifts to the left of the product information for a balanced layout.

- The second column presents essential product details, including the Product Name, Description, Category, and Price. To ensure clarity, the text is styled in black font, with the price highlighted in Crochet Corner’s signature pink, making it stand out.

- The final column contains essential user interaction buttons, including the product quantity selector, return to product button, and add to basket button—all styled in teal for clear visibility and consistency with the overall design.

__Shopping Basket__

The Shopping Basket serves as a dedicated space where users can view and manage the products they’ve added. The information is neatly organized in a table, displaying the product image, name, quantity, and the total price, which is calculated based on the selected quantity.

Users have access to interactive buttons, allowing them to update the quantity of an item or remove it entirely from the basket.

At the bottom of the screen, the grand total for all selected products is clearly displayed. If the user's order has not met the £40 free delivery threshold, they are informed of the remaining amount needed to qualify for free delivery.

Finally, users are presented with two action buttons:
- Keep Shopping – Redirects back to the All Products Page for further browsing.
- Checkout Securely – Takes users to the Checkout Page, where they can finalize their purchase.

__Checkout Page__

The Checkout Page expands upon the Shopping Basket, maintaining a familiar format for product details. Users can view each item's image, name, quantity, and total price, along with the grand total and delivery fees, if applicable.

Below, an intuitive order form guides users through the final steps of their purchase, requesting essential details such as name, email, phone number, and shipping address. Stripe is seamlessly integrated for secure card payments.
If any errors occur while entering information, users receive immediate feedback via error messages. Once all details are correctly provided, they can choose to finalize their order by selecting the checkout button or return to the Shopping Basket to make adjustments.

__Checkout Success Page__

Upon successfully completing their order, users are redirected to the Checkout Success Page, where they are informed that their purchase was processed successfully. They will receive an email confirmation of their order, along with a notification once it has been dispatched.
Below this message, a detailed order summary is displayed, confirming the products purchased and their respective quantities. A breakdown of the total cost, including individual product pricing, is also presented. Additionally, Delivery and Contact details are listed for reference.
At this stage, users have the option to return to the All Products Page via an interactive button, allowing them to continue browsing or make additional purchases.

__Login Page__


__Sign Up Page__


__Logout Page__



### Features left to Implement

## Technologies Used

### Languages Used:

  - HTML5
  - CSS3
  - Python
  - JavaScript

### Frameworks, Libraries and Programs Used:

__Django__
- The Django python framework has been used to build the Crochet Corner online store.

__Boostrap__
- The Bootstrap framework has been used in the project to assist with the site's styling and responsiveness.

__Crispy Forms__
- The Crispy Forms package has been used within the project to render the order form in the checkout page.

__Django All Auth__
- The All Auth package has been used to provide authorisation to the Crochet Corner store so that the project could have role based functionality.

__Balsamiq Wireframes__
- The Balsamiq wireframes programme has been used in the front end design of the site to map out how each page will appear on different screen sizes.

__Lucid Chart__
- The Lucid Chart has been used to map out the models used with the project and the relationships they have to one another.

__Github Projects__
- Github Projects has been to assist with the Agile development of the project in the form of creating, storing and monitoring the user stories of the project.

__Google Fonts__
- Google Fonts has been used to import the fonts used within the project. These fonts were Leckerli One, Poiret One, Josephin Sans, Nunito and Oregano.

__Font Awesome__
- Font Awesome has been used to add icons for aesthetic and UX purposes.
    

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

    - 
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

    - The CSS code for re-arranging the order of the Header elements for smaller screens was taken from geeksforgeeks.org - https://www.geeksforgeeks.org/how-to-reorder-div-elements-using-css-only/ 
         

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




