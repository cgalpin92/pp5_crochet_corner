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


