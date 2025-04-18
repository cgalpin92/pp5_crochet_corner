# Crochet Corner

## Intro

  - Crochet Corner is a B2C eCommerce platform designed for customers to explore and purchase crochet yarn and tools. Its target audience are creative individuals, serving both novice crafters and experienced crocheters alike. The site allows customers to browse a wide range of crochet tools and yarns in various colors, with filtering options to streamline their search experience. Crochet Corner aims to promote its diverse product offerings, inspire customers to make purchases, and encourage repeat visits for future purchases. To achieve these goals, user stories were crafted to focus on key functionalities such as viewing and filtering products, uploading information to the database, and enabling account creation. By providing users the ability to save contact details, the site simplifies the checkout process for a seamless and efficient shopping experience.

![Responsive Mockup Image](/media/responsive_mockup.png)

### Roles of the site:

__Business Owner__

- Goals: The business owner aims to build a thriving e-commerce platform specializing in crochet supplies. Their vision includes a visually engaging website with a seamless and secure payment system to attract and grow their customer base. Additionally, they require efficient inventory management, allowing for easy updates and modifications through a secure, interactive front-end interface. Acknowledging the competitive market, the owner prioritizes differentiation and outstanding customer service to enhance user experience and drive long-term success.

- Authenticated Access: The business owner has secure, authenticated access to both the front-end interface and back-end database of the eCommerce store. This allows them to efficiently manage the platform by modifying and removing products, overseeing user accounts, creating new product categories, and approving orders, ensuring seamless operation and control.

__Site User__

- Goals: The site user seeks a seamless and hassle-free purchasing experience for crochet supplies. They value a visually appealing interface, a diverse selection of reasonably priced products, and clear, detailed descriptions to ensure they can make informed purchasing decisions. Additionally, they want the ability to manage their customer data, including default contact and delivery information, as well as access their order history—viewing both current order statuses and past purchases for a smooth and transparent shopping experience.

- Authenticated Access: The site user can access the eCommerce store both as an authenticated and non-authenticated visitor, with the ability to browse and purchase items unrestricted by login status. However, to save contact and delivery information, track orders, and view order history, authenticated access is required, ensuring a personalized and secure shopping experience.

## Database Design (Models)

I have used a total of 9 Models so far within this project. There is potential for further models to be created as the eCommerce store grows. The current models in use are listed below:

__Products:__
- This model efficiently stores all essential product details, including the name, image, description, and price. Products are uploaded by the Site Admin through the Admin Centre, ensuring streamlined management. 

- The color model field is a Character Field linked to an array of predefined options called COLOR_OPTIONS. This setup enables the Site Admin to assign a color category via a dropdown selection, making it easier to filter and organize products effectively. 

- There are a number of Foreign key relationships with other models:
    - ProductCategory: The product category field has a Foreign Key relationship with the ProductCategory Model. A product can only have one Product Category, but a Product Category can have multiple products. 

    - YarnCategory: The yarn category field has a Foreign Key relationship with the YarnCategory model. This field is not a required field as a product will either have a yarn category or tool category. Again, a product can only have one Yarn or Tool category, but a Yarn or Tool category can have many products within them. 

    - ToolCategory: The tool category field has a Foreign Key relationship with the ToolCategory model. Again, this field is not a required field as a product with either have a tool category or yarn category. The product can only have one Tool or Yarn category, but the Tool or Yarn categories can have multiple products related to it. 

    - YarnBrand: The yarn brand field has a Foreign Key relationship with the YarnBrand model. This field is not a required field as a product will either have a yarn brand or tool brand. Again, a product can only have one Yarn or Tool brand, but a Yarn or Tool brand can have many products within them. 

    - Tool Brand: The tool brand field has a Foreign Key relationship with the ToolBrand model. This field is not a required field as a product will either have a tool brand or yarn brand. Again, a product can only have one Tool or Yarn brand, but a Tool or Yarn brand can have many products within them.

__YarnCategory:__
- This model stores all the Yarn weight Categories; 4 Ply, Aran and DK. The Site Admin can create new Yarn Categories from within the Admin Centre as the site grows and further products with other Yarn Weights are added. Once added, these categories seamlessly integrate into the Product Model, appearing as selectable options when the Site Owner uploads a new product to the database.

__ToolCategory:__
- This model stores all the Tool Categories; Crochet Hooks and Needles, Counters and Markers, Yarn Bowls and Other. The Site Admin can create new Tool Categories from within the Admin Centre as the site grows and further products with other Tool Categories are added. Once added, these categories seamlessly integrate into the Product Model, appearing as selectable options when the Site Owner uploads a new product to the database.

__YarnBrand:__
- This model stores all the Yarn Brands; West Yorkshire Spinners Signature, Creative Cotton, Scheepjes Chunky Monkey, and Crochet Society. The Site Admin can create new Yarn Brands from within the Admin Centre as the site grows and further products by other Yarn Brands are added. Once added, these brands seamlessly integrate into the Product Model, appearing as selectable options when the Site Owner uploads a new product to the database.

__ToolsBrand:__
- This model stores all the Tool Brands; Clover Armour, Knit Pro, Pony, Sirdar, Crochet Society and Bella Coco. The Site Admin can create new Tool Brands from within the Admin Centre as the site grows and further products by other Tool Brands are added. Once added, these brands seamlessly integrate into the Product Model, appearing as selectable options when the Site Owner uploads a new product to the database.

__Product_Category:__
- This model stores the different Product Categories which the Site Admin can create from within the Admin Centre. Currently there are only two categories; Yarn and Tools, however as the site grows to include other product types such as Yarn Patterns or Accessories, further categories can be added into this model. Once added, these categories seamlessly integrate into the Product Model, appearing as selectable options when the Site Owner uploads a new product to the database.

![Model Relationships between Product App models](/media/products_app_models.png)

__Orders:__
- This model stores all relevant details for each completed order placed by a site user. Orders are generated directly from the front end of the site, capturing user-submitted information seamlessly. 

- The order status field is a Character Field linked to an array of predefined order status options: Pending, Dispatched, Return Pending, and Returned. By default, new orders are assigned a Pending status. The Site Owner can update this status within the database to reflect the order’s progression—whether it has been Dispatched, marked as Return Pending, or fully Returned.

__Order_Line_Item:__
- This model stores all relevant details for each individual item within an order. The information is generated directly from the user via the front end of the site, ensuring accurate data capture. A field was added called product_name to capture the name of the product purchased at time of purchase. This field was introduced to prevent a user's order history changing when product names are updated by the site admin.

- Additionally, the model includes two foreign key relationships, providing structured connections between related data entities for seamless integration within the database.
    - Order: The order model field has a Foreign Key relationship with the Order Model. One Order Line Item can only be in one order; however, an order can contain many Order Line Items. 

    - Product: An Order line item can relate to only one product; however, a product can relate to many order line items. 

![Model Relationships between Checkout App models](/media/checkout_app_models.png)

__UserProfile:__  
- This model stores a user's default contact and address details along with their Order History. The information is generated either by saving contact and delivery details during checkout or by updating the default contact and delivery form within the My Account page.
- It has a one-to-one relationship with Django's built-in user model, as each user can have only one set of default information.

![UserProfile Model](/media/user_profile_model.png)

## User Experience Stories

I implemented Agile methodologies to plan and develop the Crochet Corner eCommerce site, ensuring flexibility and efficiency throughout the process. By leveraging User Experience stories, I kept both the end user and site owner at the core of every design and functionality decision. 
To maintain adaptability and prioritize essential features, the User Stories and their acceptance criteria were categorized into three tiers: Must Have, Should Have, and Could Have. This approach ensured that critical functionalities necessary for the site's initial release were addressed first, while potential enhancements in the Could Have category were earmarked for future development. 
To track progress and maintain alignment with these project goals, I used GitHub Projects to document and manage user stories, systematically mapping them against the final product. 
During development, one User Story was removed, as both the story and its acceptance criteria were deemed unnecessary for the initial release and scheduled for future review. This User Story has been documented below for reference. All remaining User Stories were successfully completed by the project's conclusion, ensuring a well-structured and user-focused outcome.

[Link to user stories](https://github.com/users/cgalpin92/projects/4/views/1)

![user stories](/media/user_stories.png)

__User Stories__

- As a site user I can easily create an account so that I can check out quicker next time

    - When a user selects 'Register' they are presented with a registration page to create an account

    - Once a user has completed the form to create an account their username is present in the top of the page

    - Once an account has been created a user is able to navigate to the 'My Accounts' page successfully

- As a site user I can log into my account so that I can view previous orders

    - The site user can navigate to the 'Sign In' page and successfully sign in

    - Once signed in the user is able to select the 'My Account' page and select Order History

    - Given the user has made purchases they will be listed here, if the user has not made any previous orders it will state 'No Previous Orders.’

- As a sire user I can log into my account so that I can update default contact and address information

    - Given the user has successfully signed in they can navigate to the 'My Account' page.

    - From here they can select the 'Edit' button and change the information in the required default field.

    - Once they have selected the 'Update' button the new default information is displayed.

- As a site user I can add orders to the shopping basket so that I can view orders before purchasing them

    - The 'Add to basket' button is visible on the product item page.

    - When selecting the above button, the user is notified that the item has been added to the shopping basket.

    - When selecting the Shopping Basket icon, the item they have added is listed

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

    - The site user can select the required filter options in the left-hand panel when on larger screens or select the filter button on smaller screens.

    - Once they have selected the required options the remaining products listed are in relation to these options.

- As a site user I can easily navigate around the navigation menu so that I can get to a specific area of the site

    - When on larger screens the navigation menu is clearly visible at the top of the page, or when on smaller screens the navigation menu is clearly identified by a burger icon and expands when selected.

    - The different pages are clearly labelled with the current page clearly identified.

    - The user is taken to the correct page when selecting it.

- As a site user I can easily navigate to the Sign Up to the Newsletter page so that I can receive offers and tips on creating crochet items

    - The site user can navigate to and select the 'Newsletter' page in the menu list

    - They are re-directed to the Newsletter sign up form

    - Once they have completed all the required information and selected sign up, they are notified by a message on the screen that this has been successfull

- As a site user I can view product information so that I can decide if the product is the correct product before adding it to the basket

    - The user can select either All Products or the product category from the navigation menu.

    - When selecting on an individual item the user is re-directed to a page which displays all the product information.

    - The product name, description, price, stock availability and image are displayed to the user.

- REMOVED: As a site user I can delete my account so that I no longer have saved information on Crochet Corner

    - Given the user has successfully signed in they can navigate to the 'My Account' page.

    - From here they can scroll down to the bottom of the page and select 'Delete Account'.

    - The user is taken back to the Home page and when attempting to sign in with same details they are informed the account does not exist. 

## Design

  __Color Scheme__

  - During the design process for Crochet Corner, I explored numerous crochet websites to draw inspiration for the color palette. A common trend among these sites was the use of pale background colors paired with bright, bold hues for logos and headings. To make the Logo stand out against the soft Ivory and Cream backgrounds, Pink was chosen as the primary color, naturally capturing the user's attention. This vibrant Pink theme is carried through to the headings and the My Profile page, ensuring a cohesive and visually appealing experience. Teal was selected for all buttons, complementing the Pink accents while creating a standout effect that ensures clarity and usability across the site. Black is used for all remaining text, providing a crisp, clean contrast that ties the design together with clarity and consistency.
  
  __Typography__

   - The Crochet Corner website uses a blend of four distinct fonts to craft its unique and appealing visual identity. The logo combines the playful character of Leckerli One with the sleek elegance of Poiret One, creating a striking and memorable visual identity. For headings, the clean elegance of Josephin Sans enhances readability and structure, while Oregano introduces a warm, personal touch to elements such as usernames and messages. Nunito, renowned for its excellent readability, provides a seamless foundation for the remaining text, ensuring a smooth and user-friendly experience. Together, these fonts harmonize to enhance the website's charm, functionality, and personality.

  __Wireframes__

  - Wireframes were used to map out the design of the site including how features would behave responsively:

  - Home Screen
  ![home page](/media/home_page_wireframe.png)

  - Product Page
  ![products page](/media/products_page_wireframe.png)

  - Products Details Page
  ![product details page](/media/product_details_wireframe.png)

  - Basket Page
  ![basket page](/media/shopping_basket_wireframe.png)

  - Checkout Page
  ![checkout page](/media/checkout_screen_wireframe.png)

  - Checkout Success Page
  ![checkout success page](/media/checkout_success_wireframe.png)

  - My Account Page
  ![my account page](/media/my_account_wireframe.png)

  - Order History Page
  ![order history page](/media//order_history_wireframe.png)

  - Product Management Page
  ![product management page](/media/product_management_wireframe.png)

  - Newsletter Sign up page
  ![newsletter sign up page](/media/newsletter_wireframe.png)

## Marketing

  ### eCommerce Business Model
  - Crochet Corner is a dedicated eCommerce store operating under the Business-to-Consumer model, offering a wide range of crochet supplies directly to customers. The purchasing process is seamless, with a straightforward single-payment transaction. Upon completing their purchase, customers receive an instant email notification, ensuring a smooth and hassle-free shopping experience.

  ### Marketing Strategies
  - Crochet Corner has implemented a variety of marketing strategies to enhance its online presence and reach a wider audience.

  -__Facebook Mockup__
  - A dedicated Facebook page has been launched to enhance engagement and drive business sales. Below is a mockup of the page. The profile picture proudly features the Crochet Corner logo, while the cover photo showcases the website’s background image, creating a cohesive and visually appealing brand identity. Additionally, the Facebook page serves as a platform to announce new items being added to the website, keeping customers informed and excited about the latest offerings.

    ![facebook mockup page](/media/crochet_corner_facebook_mockup.png)

  -__Search Engine Optimisation__
  - Meta Tags
    - The website incorporates both long-tail and short-tail keywords to optimize search engine crawling, enhancing visibility and improving rankings.
    - The process for identifying the most effective keywords has been thoroughly documented below, ensuring a strategic approach to optimizing search engine performance.
        1. Any words associated with the theme of the eCommerce site were recorded.
        2. Google Search was utilized to find any relating keywords; these were also recorded.
        3. The list of keywords were assessed and any that were deemed too generic or not specifically related to products Crochet Corner provides were removed.
        4. Wordtracker was used to assess the volume and competition for the remaining keywords. 
        5. The keywords which had the higher volume but lower competition were selected to be used within the project. 
    - This structured approach ensures that the chosen keywords effectively enhance search engine ranking and online discoverability.

    ![keywords table](/media/keywords_table.png)

  __Sitemap File__
  - I utilized Code Institute's recommended XML-Sitemaps generator to create the sitemap.xml file, which has been included in the root directory of the project. The sitemap.xml has been generated using the live deployed site.

    [Sitemap.xml](/sitemap.xml)  
    [Live Site](https://pp5-crochet-corner-16779e21224b.herokuapp.com/)

__Robots.txt file__
- Below is a screenshot of the robots.txt file for this project:
![robots.txt](/media/robots_txt_file.png)


## Features

### Existing Features

__Header and Navigation Bar__

The Header and Navigation Bar seamlessly integrates the Site Name, search bar, and two distinct menus. Positioned on the left side of the screen, the Site Name — which doubles as the logo — features two distinct fonts and colors, making it visually striking and memorable.

The Search Bar sits beside the Site Name in the centre of the header on medium and larger screens but shifts to the bottom of the header on smaller screens for optimal responsiveness.

The first menu, located on the right side of the header, includes the Account dropdown and Shopping Basket. These elements are fully responsive, displaying both the name and icon on medium and large screens, while only the icon appears on smaller screens for a streamlined look. Once a user has signed into their account, they can access their profile directly from this section. Their username is displayed in a distinct font, ensuring it stands out and is easily recognizable.

The second menu serves as the final component of the Header and Navigation Bar, providing intuitive navigation options. It includes links to the Home Screen, All Products—with a dropdown to filter by Price, Yarn Products—with dropdown filters for Yarn Weight and Yarn Brand, and Tools—with dropdown filters for Tool Type and Brand. This menu is also fully responsive, appearing beneath the Site Name and spanning the header’s width on larger screens. On smaller screens, it transforms into a burger icon, positioned at the top left corner under the logo and expanding vertically when selected.

The Header and Navigation Bar showcase the brand’s signature colors—Pink, Ivory, Teal, White, and Black—creating a cohesive and visually appealing design. The typography and color scheme remain consistent across all pages, ensuring a seamless user experience and effortless navigation.

![header mobile](/media/header_mobile.png)
![header tablet](/media/header_tablet.png)
![header desktop](/media/header_desktop.png)

__Home Page__

The Home Page is designed to be both bold and inviting, immediately drawing users in. The background features a vibrant yarn image, seamlessly connecting to the theme of the eCommerce store. At the centre of the screen, a striking welcome message stands out against Crochet Corner’s signature pink background, accompanied by a teal “Shop Now” button positioned just below, encouraging users to explore the store with ease.

![homepage](/media/home_page.png)

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

    ![all products page mobile](/media/all_products_mobile.png)
    ![all products page tablet](/media/all_products_tablet.png)
    ![all products page desktop](/media/all_products_desktop.png)

__Product Details Page__

This page presents detailed product information, organized into columns that adjust dynamically based on screen size—stacking side by side on larger screens and vertically on smaller screens for an optimal viewing experience.

- The first column features the product image, ensuring a clear visual representation. On smaller screens, the image is displayed at the top, with the remaining product details stacked below. On larger screens, it shifts to the left of the product information for a balanced layout.

- The second column presents essential product details, including the Product Name, Description, Category, and Price. To ensure clarity, the text is styled in black font, with the price highlighted in Crochet Corner’s signature pink, making it stand out.

- The final column contains essential user interaction buttons, including the product quantity selector, return to product button, and add to basket button—all styled in teal for clear visibility and consistency with the overall design.

    ![product details page mobile](/media/product_details_mobile.png)
    ![product details page desktop](/media/product_details_desktop.png)

__Shopping Basket__

The Shopping Basket serves as a dedicated space where users can view and manage the products they’ve added. The information is neatly organized in a table, displaying the product image, name, quantity, and the total price, which is calculated based on the selected quantity.

Users have access to interactive buttons, allowing them to update the quantity of an item or remove it entirely from the basket.

At the bottom of the screen, the grand total for all selected products is clearly displayed. If the user's order has not met the £40 free delivery threshold, they are informed of the remaining amount needed to qualify for free delivery.

Finally, users are presented with two action buttons:
- Keep Shopping – Redirects back to the All Products Page for further browsing.
- Checkout Securely – Takes users to the Checkout Page, where they can finalize their purchase.

![shopping basket page mobile](/media/shopping_basket_mobile.png)
![shopping basket page mobile 2](/media/shopping_basket_mobile2.png)
![shopping basket tablet and desktop](/media/shopping_basket_table_and_desktop.png)

__Checkout Page__

The Checkout Page expands upon the Shopping Basket, maintaining a familiar format for product details. Users can view each item's image, name, quantity, and total price, along with the grand total and delivery fees, if applicable.

Below, an intuitive order form guides users through the final steps of their purchase, requesting essential details such as name, email, phone number, and shipping address. Stripe is seamlessly integrated for secure card payments.
If any errors occur while entering information, users receive immediate feedback via error messages. Once all details are correctly provided, they can choose to finalize their order by selecting the checkout button or return to the Shopping Basket to make adjustments.

![checkout](/media/checkout_desktop.png)
![checkout page 2](/media/checkout_desktop2.png)
![checkout](/media/checkout_desktop3.png)

__Checkout Success Page__

Upon successfully completing their order, users are redirected to the Checkout Success Page, where they are informed that their purchase was processed successfully. They will receive an email confirmation of their order, along with a notification once it has been dispatched.
Below this message, a detailed order summary is displayed, confirming the products purchased and their respective quantities. A breakdown of the total cost, including individual product pricing, is also presented. Additionally, Delivery and Contact details are listed for reference.
At this stage, users have the option to return to the All Products Page via an interactive button, allowing them to continue browsing or make additional purchases.

![checkout success page mobile and tablet](/media/checkout_success_page_tablet_and_mobile.png)
![checkout success page desktop](/media/checkout_success_page_desktop.png)

__Login Page__

The login page is accessible via the My Account dropdown menu for unauthenticated users. If a user has not yet created an account, they are prompted to sign up first, with the word 'Sign-Up' functioning as a clickable link that redirects them to the registration page. Below this, users can enter either their username or email address along with the password they set during registration. 
For convenience, a 'Remember Me' option is available, allowing users to stay signed in for future visits without needing to log in again. The page features two buttons: 'Home,' which returns users to the home screen, and 'Sign In,' which grants access to their account. Upon successful login, a confirmation message appears, notifying the user of their successful sign-in. Additionally, when accessing the My Account dropdown menu, their username is displayed in Crochet Corner’s signature pink font, reinforcing brand identity.

![login page](/media/sign_in_screen.png)

__Sign Up Page__

The Sign-Up page is accessible via the My Account dropdown menu for unauthenticated users. If a user has already created an account, they are prompted to sign in, with the word 'Sign-In' functioning as a clickable link that redirects them to the login page.
To register, users must enter their email address, confirm it, choose a username, and create a password—ensuring the password matches upon confirmation. The page features a single 'Sign-Up' button, which redirects users to a confirmation page acknowledging their initial registration and informing them that email verification is required to proceed.
Once the email is verified, a success message appears, confirming the completion of registration. Additionally, upon accessing the My Account dropdown menu, their username is displayed in Crochet Corner’s signature pink font, reinforcing brand identity.

![sign in screen tablet and laptop](/media/registration_screen.png)

__Logout Page__

The Logout page is accessible to authenticated users via the My Account dropdown menu in the header. Upon selecting Logout, users are prompted to confirm their decision before proceeding. They are presented with two options:
- Sign Out: This option logs the user out of the store, redirects them to the home page, and displays a confirmation message notifying them of a successful logout. When they access the My Account dropdown menu, they will see the Login and Register options available.
- Return to Home: This option redirects the user to the home page while keeping them signed in. Their login status is confirmed by the presence of their username in the My Account dropdown menu. 
This ensures a clear and user-friendly logout experience, giving users control over whether they remain signed in or log out completely.

![sign out screen](/media/sign_out_page.png)
![sign out message](/media/sign_out_message.png)

__My Account Page__

The My Profile page is accessible to authenticated users via the My Account dropdown menu. It features an editable form displaying the user's default delivery and contact information. Users can update their details by modifying the necessary fields and selecting the 'Update' button, after which a success message confirms the changes. Additionally, the page includes a button that provides quick access to the user's order history, ensuring a seamless account management experience.

![my account page](/media/my_profile.png)

__Order History Page__

The Order History page is accessible to authenticated users through the My Profile page. It displays a complete list of the user's past orders, with the most recent ones appearing at the top for easy access. By selecting an order number, users are redirected to the Order Confirmation received at the time of purchase, with a success message confirming the action.

![order history page](/media/order_history.png)

__Product Management Page__

The Product Management page is exclusively accessible to authenticated Site Admin users via the My Account dropdown menu. Upon selecting this link, they are directed to a form that enables them to add a new product to the store. The page provides two options:
- Cancel: Redirects the Site Admin to the All Products page.
- Add Product: Saves the new product to the database and redirects the Site Admin to the Product Details page, accompanied by a success message confirming the addition.

Similarly, a product can be edited by selecting the Edit button, either from the All Products list or within the Product Details page. This action opens a form pre-filled with the existing product information, allowing the Site Admin to update relevant fields as needed. After selecting the Update button, the system redirects them to the updated Product Details page, displaying a success message confirming the changes.

![product management](/media/product_management.png)

__Newsletter Sign Up Page__

The Newsletter sign-up page is accessible to all users via a footer link. It features the home screen’s background image, with a concise form centrally positioned. The form, embedded through Mailchimp, is styled using Crochet Corner's signature typography and color palette. Users are required to enter only their email address in the provided box, with an option to return to the home screen via a dedicated button.

![newsletter](/media/newsletter.png)

### Features left to Implement

__Order again button__  
This button would sit within the user's order history. The Order again button will prefill the basket with the order items which they could further edit the quantity or remove items from previous order they do not wish to order again.

__Edit current products from with Product Admin__  
This would be an additional feature to the current Edit button on each individual product. When the site admin is logged in, they will be able to navigate to Product Admin and from here select Edit Current Products. This will take the to a page which lists the products which they can select and edit.

__Approve pending orders within product admin__  
This would be a feature for a site admin. Once signed into the site they would be able to access Product Admin which would have a new landing page. From here they will have the option to Add new product, edit current products or approve pending orders.

__Color choices in Yarn Product Details page__  
When on the details page for a Yarn Product, the site user can select the same product but a different color from a selection listed under the product details. This would take them to the product details of the color choice of the item they have selected. 

__Delete Account Button__  
As previously mentioned, this was an original User Story but was not deemed critical for the store’s initial release. In future development, I plan to introduce a 'Delete Account' button on the My Account page, allowing users to remove their accounts and associated data from the store if they choose to do so.

## Technologies Used

### Languages Used:

  - HTML5
  - CSS3
  - Python
  - JavaScript

### Frameworks, Libraries and Programs Used:

__Django__
- The Django python framework has been used to build the Crochet Corner online store.

__Bootstrap__
- The Bootstrap framework has been used in the project to assist with the site's styling and responsiveness.

__Crispy Forms__
- The Crispy Forms package has been used within the project to render the order form in the checkout page.

__Django All Auth__
- The All-Auth package has been used to provide authorisation to the Crochet Corner store so that the project could have role-based functionality.

__Balsamiq Wireframes__
- The Balsamiq wireframes programme has been used in the front-end design of the site to map out how each page will appear on different screen sizes.

__Lucid Chart__
- The Lucid Chart has been used to map out the models used with the project and the relationships they have to one another.

__GitHub Projects__
- GitHub Projects has been to assist with the Agile development of the project in the form of creating, storing, and monitoring the user stories of the project.

__Google Fonts__
- Google Fonts has been used to import the fonts used within the project. These fonts were Leckerli One, Poiret One, Josephin Sans, Nunito and Oregano.

__Font Awesome__
- Font Awesome has been used to add icons for aesthetic and UX purposes.
    
__Stripe__
- Stripe has been used to handle payments.

__Mailchimp__
- Mailchimp has been used for the newsletter sign up form.

__AWS Hosting Services__
- AWS has been used to store static and media files for the deployed site.

## Testing

A separate document has been created to record the Testing for this project -  [TESTING.md](/TESTING.md)

## Deployment

### Forking:
By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate this [GitHub Repository](https://github.com/cgalpin92/pp5_crochet_corner)
2. At the top of the Repository just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Cloning:
1. Log in to GitHub and locate this [GitHub Repository](https://github.com/cgalpin92/pp5_crochet_corner)
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
-__Prior steps__
To project required the following steps prior to the deployment to Heroku.
  - install gunicorn 23.0.0 - the production equivalent of manage.py runserver
    - The creation of Procfile with the inclusion of web: gunicorn crochet_corner.wsgi:application - the command Heroku uses to find the correct .py file to run and start the server
  - add .herokuapp.com to ALLOWED_HOSTS within settings.py

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
            - DATABASE_URL: Your PostgreSQL database URL
            - SECRET_KEY: Your Django secret key
            - AWS_ACCESS_KEY_ID: Your AWS Access Key ID
            - AWS_SECRET_ACCESS_KEY: Your AWS Secret Access Key
            - USE_AWS: True
        - Select __Add__    
    - Link the Heroku app to the repository:
        - Select __Deploy__ from the top of the page.
        - Scroll down to __Deployment method__
        - Select __GitHub. Connect to GitHub__
        - Enter your repository name and click search
        - Select connect next to your repository name
    - Click on __Deploy__

### AWS S3 Bucket Creation

The project used AWS for the purpose of storing media and static files in the deployed site. Setting up media and static storage for projects using AWS requires configuring an S3 bucket, updating project settings, and ensuring proper permissions. Here is a general overview of the steps:

__Setup up your S3 Bucket__

1. Sign in to the AWS Console. Create an account if you do not have one already.
2. Search for S3 in the AWS console.
3. Create a new bucket, matching your Heroku project name, and select your region.
4. Uncheck "Block all public access".
5. Enable ACLs under "Object Ownership" and select "Bucket owner preferred".
6. Under the "Properties" tab, activate static website hosting and set "index.html" and "error.html".
7. Paste the provided CORS configuration under the "Permissions" tab:

        [
        {
            "AllowedHeaders": ["Authorization"],
            "AllowedMethods": ["GET"],
            "AllowedOrigins": ["*"],
            "ExposeHeaders": []
        }
        ]
8. Note your ARN string.

__Adjust your ARN string:__

1. Go to "Bucket Policy" and select "Policy Generator".
2. Set "Policy Type" as "S3 Bucket Policy", "Effect" as "Allow", "Principal" as "*", and "Actions" as "GetObject".
3. Paste your ARN into the "Amazon Resource Name(ARN)" field.
4. Generate the policy, copy it, and paste it into the Bucket Policy Editor.
5. Append "/*" to the end of the "Resource" key before saving.
6. Enable "List" in the ACL (Access Control List) for Everyone.

__Create User and User Group in IAM__

1. Open IAM (Identity and Access Management) service.
2. Create a new user group (e.g., "group-your-app-name").
3. Attach the "AmazonS3FullAccess" policy to your group.
4. Review and create the policy.
5. Attach this policy to your group.
6. Add a new user to the group, selecting "Programmatic Access". Download the .csv file with the user's Access key ID and Secret Access Key.

__Create Media Folder__

1. In S3, create a new folder called "media" to hold your image files.
2. Upload the required files for your project into this folder.
3. Set "Manage Public Permissions" to "Grant Public Read Access to this object(s)".

__Connect AWS to your Django Project__

1. In your IDE terminal install the required packages:

        pip3 install boto3
        pip3 install django-storages

2. Add 'storages' to the INSTALLED_APPS in settings.py.
3. Add your AWS secret variables to the env.py file.
4. Import required modules in settings.py.
5. Set your secret key.
6. Configure the database settings.
7. Configure static and media files settings.
8. Add required imports and configurations to your URLS.py.
9. Set up AWS configurations.
10. Create custom_storages.py file.
11. Create Procfile in the root directory.
12. Adjust your allowed hosts.

Now you can commit and push your changes to your GitHub repository using the following commands:

        git add .
        git commit -m "Commit Message"
        git push

## Credits

### Code

    - The Boutique Ado walkthrough was used as a boilerplate for setting up the Ecommerce site as well as some further code and guidance for building particular elements of the project.

    - The CSS code for re-arranging the order of the Header elements for smaller screens was taken from geeksforgeeks.org - https://www.geeksforgeeks.org/how-to-reorder-div-elements-using-css-only/ 
         

### Content

    - The inspiration for the design and color palette for Crochet Corner was taken from:
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

