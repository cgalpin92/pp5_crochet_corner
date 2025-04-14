Return to the [README.md](/README.md)

This document contains all the testing carried out for this project. It also includes any reported fixed or unfixed bugs.

### Manual Testing

__Responsiveness Testing__

Crochet Corner has been designed as a fully responsive website using Bootstrap and CSS, ensuring seamless functionality across various screen sizes. Through DevTools, the site has been successfully tested on multiple devices:
- Mobile: ≤ 768px
- Tablet: ≥ 768px
- Laptop: ≥ 992px
- Desktop: ≥ 1200px

The website leverages the Bootstrap Grid layout along with Table and Card components to enhance its visual structure. Product cards are displayed vertically on smaller screens and automatically transition to a horizontal layout as the screen size increases. For navigation, Bootstrap styling has been implemented to optimize user experience. The secondary navigation menu, which allows users to filter searches, is condensed into a burger icon on smaller screens and expands upon selection. On laptop screens (992px and larger), the menu transitions to a horizontal layout beneath the site name for a more intuitive browsing experience.  
Additionally, on the Basket and Checkout Success pages, information is displayed in a table format on larger screens. However, for smaller screens, the layout adapts to the Bootstrap grid system of rows and columns, ensuring a more user-friendly experience and improved readability.

__Browser Compatibility Testing__

Crochet Corner has undergone thorough testing across multiple browsers, including Chrome, Edge, Firefox, and Safari (on a mobile device). In each browser, the key functionalities were successfully verified, including account registration, login, browsing the All Products page and individual product details, uploading and editing products, and completing purchases. Additionally, all navigation elements and buttons functioned as expected, ensuring a seamless user experience across different platforms.

__Lighthouse Testing__

I have verified that the selected colors and fonts on each page are visually accessible and easy to read by conducting an evaluation using Lighthouse in Chrome DevTools.  
Additionally, Lighthouse testing has been performed to assess the site's SEO performance, best practices, and overall functionality. While the website achieved strong results in SEO, there is still room for improvement. Performance and best practices could be further optimized, likely due to image sizing and formats. With strategic refinements, the website has the potential to excel in all areas, ensuring an enhanced user experience and stronger search engine visibility.

__User Stories Testing__

- As a site user I can easily create an account so that I can check out quicker next time

    - I successfully accessed the Register page through the My Account dropdown menu and completed the account registration process. Upon signing in, my username appeared in the My Account dropdown, confirming the login. Additionally, new menu options—My Account and Logout—became available. I was able to navigate to both pages without any issues, ensuring a smooth user experience.

- As a site user I can log into my account so that I can view previous orders

    Upon signing into the store as a user, I can navigate to the My Account page and access the Order History section. If the user has made previous purchases, they are displayed here. However, if no purchases have been made, a message stating 'You have no previous orders' is shown, ensuring clear communication of order status.

- As a site user I can log into my account so that I can update default contact and address information

    - After successfully signing in, I navigated to the My Account page, where my default information was displayed. I was able to edit and update my details without any issues—unless I entered invalid information, such as letters in a phone number or an excessive number of digits. When purchasing a new item, the updated information was automatically populated in the relevant fields on the checkout screen, ensuring a seamless transaction.

- As a site user I can add orders to the shopping basket so that I can view orders before purchasing them

    - I navigated to the product details page, adjusted the quantity of items I wished to add to the basket, and selected 'Add to Basket.' The items were successfully added, confirmed by a success message at the top of the screen displaying the current basket contents. From there, I selected 'Go to Basket,' which redirected me to the basket screen, where all added items were listed along with their quantities and total cost.

- As a site user I can view the shopping basket so that edit or remove items

    - Clicking the shopping basket icon in the top-right corner of the screen redirects me to the shopping basket. If products have been added, I can adjust their quantities using the plus and minus toggle buttons or remove items entirely by selecting the 'Remove' button.

- As a site owner I can upload new items to the admin portal so that new products can be displayed on the Crochet Corner page

    - Using Superuser credentials, I successfully logged into the Admin Portal. From there, I navigated to the Products section, selected 'ADD PRODUCT,' and completed the form to create a new product. After the product was added, I accessed the front-end live site and confirmed that it was displayed under the correct category.

- As a site owner I can view new orders placed by site users so that I can send out purchased products

    - Using Superuser credentials, I successfully logged into the Admin Portal and navigated to the Orders section. I was able to filter the order list by 'Pending,' with all orders currently in pending status displayed at the top of the table for easy access and management.

- As a site owner I can log into the admin portal so that remove user accounts from the database

    - Using Superuser credentials, I successfully logged into the Admin Portal and navigated to the Users section. Selecting a user account redirected me to its details page, where I had the option to delete the account. Upon confirming deletion, the account was successfully removed from the database. Any subsequent attempt to sign in using the deleted account's credentials resulted in a message stating that the account does not exist.

- As a site user I can filter products by criteria so that I can make it easier to find the product I am looking for

    - I can filter products by Category, Brand, or Price using the Navigation menu. While a dropdown selection feature was considered a valuable addition, it has been categorized as a 'Nice to have' and will be explored in future site development. However, it is not a requirement for the current functionality of the site.

- As a site user I can easily navigate around the navigation menu so that I can get to a specific area of the site

    - On larger screens, I can navigate around the navigation menu which is prominently displayed at the top of the page, while on smaller screens, it is represented by a burger icon that expands when selected, ensuring intuitive accessibility. Each page is clearly labeled, with the current page distinctly identified by the Page Header. Selecting a page correctly redirects me to the intended destination, ensuring a seamless and user-friendly navigation experience.

- As a site user I can easily navigate to the Sign Up to the Newsletter page so that I can receive offers and tips on creating crochet items

    - I accessed the Newsletter sign-up page via the footer link and completed the embedded Mailchimp registration form. Upon submitting my email address, a confirmation message appeared, verifying that my subscription was successfully registered.

- As a site user I can view product information so that I can decide if the product is the correct product before adding it to the basket

    - I am able to select a product, either through the All Products page or through the filtered category or brand page. I am re-directed to the details screen which lists; the product name, sku, description and price.

- As a site user I can delete my account so that I no longer have saved information on Crochet Corner

    This user story was removed, as the ability for users to delete their own accounts was categorized as a 'Nice to have' feature rather than a core requirement. While it may be considered in future site development, its absence does not currently affect the overall user experience.

__Features Testing__

- I have tested the responsiveness of both the Header and Navigation menu across all screen sizes. All links within these sections function correctly when selected, ensuring seamless navigation across devices.

![header and navigation menu in mobile format](/media/header_mobile.png)

![header and navigation menu in tablet format](/media/header_tablet.png)

![header and navigation menu in desktop format](/media/header_desktop.png)

- I successfully registered a user account, signed in, and signed out, with confirmation messages displayed at each step to verify the process.

- I successfully added multiple items to the basket and adjusted their quantities using the plus and minus toggle buttons. Additionally, I was able to remove items from the basket using the 'Remove' button. In each instance—whether adding, updating, or removing items—corresponding confirmation messages were triggered, ensuring a clear and responsive user experience.

- I successfully completed purchases as both an authenticated and non-authenticated user, ensuring smooth transactions across both user states. When attempting a purchase with a declined card or an incorrectly completed checkout form, the transaction was appropriately declined. In all instances, the correct event was accurately recorded within Stripe, ensuring proper tracking and payment security.

- I successfully accessed the My Account page while signed into the website. However, when attempting to navigate to this page as an unauthenticated user, access was restricted, ensuring proper account security and user authentication protocols.

- I successfully navigated to the Product Management page while logged in as a Superuser, where I was able to upload a new product to the store without issues. When attempting to access the URL as a non-superuser, I was appropriately informed that access is restricted, ensuring secure management of product-related functionalities.

- I successfully edited existing products in the store while logged in as a Superuser. However, when attempting to access this page as a regular user or an unauthenticated visitor, access was appropriately restricted, ensuring secure product management within the platform.

### Validator Testing

__HTML__

- edit_product.html
    - Error: An img element must have an alt attribute, except under certain conditions.
        - I believe this error has been generated through using Django Crispy forms to generate the product image into the Edit Product form. I cannot acces the img element so am unable to add an alt attribute.  
    - Error: Duplicate attribute id.
        - I believe this error is a result of using Django Crispy forms to render the product image into the edit product form and cannot be accessed.
    - Error: Element p not allowed as child of element strong in this context.
        - I cannot find this section of code within the edit_product.html file so believe it is a result of using Django Cripsy forms.
    
    ![html validation error for edit_product.html](/media/html_error_edit_product.png)

- add_product.html:
    - Error: Duplicate attribute id.
        - I believe this error is a result of using Django Crispy forms to render the product image upload field into the add product form and cannot be accessed.
    - Error: Element p not allowed as child of element strong in this context.
        - I cannot find this section of code within the add_product.html file so believe it is a result of using Django Cripsy forms.
    
    ![html validation error for add_product.html](/media/html_error_add_product.png)

- All other HTML tests passed the validator.


__CSS__

I have passed the CSS code from the three seperate css files; base.css, profile.css and checkout.css, through the official (Jigsaw) validator. On all three occassions no errors were found.

![css validation](/media/css_validator_testing.png)

__JavaScript__

Have run the JavaScript code through jshint.
Warnings have appeared but no errors.
The warnings have stated that the variables and syntaxes used are only available in ES6. I do not believe any action is required here as it is not affecting the running of my code.

__Python__

The Python code has been thoroughly tested by installing Flake8 in the IDE and running 'python3 -m flake8 --exclude .venv,.vscode,migrations', which identifies all Python errors and displays them in the terminal while excluding Django auto-generated code. Issues such as excessive whitespace, overly long lines, and unused variables were largely resolved. However, five specific errors were intentionally retained, as they were necessary for the proper functionality of their associated functions. A screenshot of the remaining errors has been included below:

![python errors](/media/python_erros.png)


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


