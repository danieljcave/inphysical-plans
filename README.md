# **InPhysical Plans**

## **Milestone Project 4 for Code Institute Full Stack Software Development.**
### Author - Daniel Cave

InPhysical Plans is a training blog that allows both users and trainer to post their training plans and interact with other users. InPhysical Plans allows users to create blog posts and like or comment on the posts. Users can interact with posts to ask questions leave reviews or improvements to the plans and the author can interact with them. 

Live Version of the website - <a href="https://inphysical-plans-e97fa8a6618e.herokuapp.com/" target="_blank">Click Here!</a>

## Table Of Contents
- [**User Experience**](#user-experience)
  - [**Target Audience**](#target-audience)
  - [**User Goals**](#user-goals)
  - [**User Stories**](#user-stories)
- [**Design**](#design)
  - [**Features**](#features)
    - [**Navbar**](#navbar)
    - [**Home page - Blog Preview**](#home-page---blog-preview)
    - [**Create a post page**](#create-a-post-page)
    - [**View Blog Post**](#view-blog-post)
    - [**View Blog Post Comments**](#view-blog-post-comments)
    - [**Update Blog Post**](#update-blog-post)
    - [**Update Comments**](#update-comments)
    - [**Delete Comments**](#delete-comments)
    - [**Delete Post**](#delete-post)
    - [**Custom Error Page**]
  - [**User Accounts**](#user-accounts)
    - [**Register Account**](#register-account)
    - [**Login Page**](#login-page)
    - [**Logout Page**](#logout-page)
    - [**Django Admin**](#django-admin)
  - [**Profile Page**](#profile)
    - [**View Profile Page**](#view-profile-page)
    - [**Edit Profile Page**](#edit-profile-page)
    - [**Delete Profile**](#delete-profile)
  - [**Additional features**](#additional-features)
    - [**Favicon**](#favicon)
  - [**Future Features**](#future-features) 
  - [**Design**](#design)
    - [**Data Models**](#data-model)
    - [**Typyography**](#typography)
  - [**Technologies Used**](#technologies-used)
    - [**Languages Used**](#languages-used)
    - [**Frameworks and Libraries Used**]
	  - [**Software and Web Applications Used**]
  - [**Testing**](#testing)
    - [**Validator Testing**](#validator-testing)
      - [**HTML Testing**](#html-testing)
      - [**W3C CSS Validator**](#w3c-css-validator)
      - [**CI Python Linter**](#ci-python-linter)
      - [**Lighthouse**](#lighthouse)
  - [**Automated Testing**](#automated-testing)
    - [**Django testing tools**](#django-testing-tools)
  - [**User Stories testing**](#user-stories-testing)
  - [**Deployment**](#deployment)
  - [**Credits**](#credits)
  - [**Acknowledgements**](#acknowledgements)

## **User Experience**
### **Target Audience**
- Fitness enthusiasts of all levels.
- Users interested in a new fitness plan or looking for ideas.
- Individuals looking to share their workout plans with others.
- Fitness lovers looking for a platform to share their knowledge with like-minded others.

### **User Goals**
- Share personal fitness plans and insights in blog posts.
- Connect with other fitness enthusiasts and build a hub for all users.
- To stay informed with the latest fitness plans and advice from all users.
- Easily navigate to blog posts in relevant content.
- Customize their profiles and engage with the other users through comments and likes.

An Agile methodology was used to plan this project. With user stories and criteria to meet. 
Using the GitHub Project board along with my Trello board. The goal of the project is to create 
a fully function blog with full CRUD capability and user profiles for posting, commenting and 
updating user profiles. Each user story has its criteria to be met and passed. All User stories 
listed were achieved with success and completed.

### **User Stories**
**Admin and Account**
- US1 - Account registration, login and logout
- US2 - Manage Posts
- US24 - Manage User Accounts
- US25 - Delete User Accounts

**Blog Posts**
- US3 - User Story: View post list
- US4 - User Story: Open a blog post
- US5 - User Story: Create a blog post
- US6 - User Story: Edit Post
- US7 - User Story: Delete post
- US8 - Placeholder Images

**User Profiles**
- US21 - View Profile
- US22 - Edit User Profile
- US23 - Delete Profile/Account

**Comments**
- US9 - View total comments
- US12 - Leave a comment
- US13 - View Comments
- US15 - Update Comments
- US16 - Delete Comments

**Likes**
- US10 - View Total Likes
- US11 - Leave a like
- US14 - View Likes

**UX/UI**
- US17 - Responsiveness
- US18 - Site Design
- US19 - System messages
- US20 - Favicon

## Design
### Features

### Navbar
The navbar is a feature that is present on all sites, it uses bootstraps-built styling and uses fixed-top to keep the navigation bar at the top of the page even when scrolling to allow users a better user experience.

On the left-hand side of the navbar holds the Blog Logo and Title, which can be clicked and takes the user to the home page.

The right-hand side of the navigation page holds the key URLs. When a user is not logged in it displays as:
- Not Logged in: Home, Register, Login and "You're Not Logged In" text to inform the user
![Navbar logged out view](/readME-assets/features/Navbar_logged_out.png)

- Logged in: Home, Create a Post, Profile, Logout and User Icon and Name
![Navbar logged in view](/readME-assets/features/nav_bar.png) 

<details>
<summary>View collapsed navbar:</summary>

![Navbar Collapse](/readME-assets/features/nav_bar_mobile.png)
</details>

### Home page - Blog Preview
The home page view is the centre of the website. This is where all of the blog posts are held for the users to view right off the bat. The home page uses both base.html and index.html. The base.html holds all of the information needed to make this website work. It holds the header and all the necessary tags, the Navbar and footer, the container for messages and the main content which uses Python block content tags to display. 

The home page divides the blog preview posts into 3 separate columns, on mobile view, it goes to a single-column view. The page will hold 6 blog post previews before pagination if a statement creates a new page. Then a button at the bottom of the page will appear for the user to browse through all of the blogs

![Blog Preview Page](/readME-assets/features/home_page.png)

<details>
<summary>View Home Page Collapsed</summary>

![HomePage Collapsed](/readME-assets/features/home_page_mobile.png)
</details>

### Create a post page:
Users who are logged into the blog are able to create posts. Once a user has registered their account they can get right into creating blog posts.

The first thing they need to do is navigate to the "Create a Post" in the nav bar. If this is not available it is because they are not logged in. If it is then they follow the link and will be brought to the Create a post page. This will allow the User to Enter a Title, Image and content. Users have the ability to edit their blog posts using the Summernote widget that offers a range of text editings, such as font colour, text sizes, table and even insert images and many more features.

Once the user is finished and is ready to submit their post, the submit link will redirect them to the newly created blog post so they are the first to see it and if any changes are needed.

![Create Blog Post](/readME-assets/features/create_post.png)

<details>
<summary>Create Blog Post Mobile</summary>

![HomePage Collapsed](/readME-assets/features/create_post_mobile.png)
</details>

### View Blog Post
All users are able to view anyone's blog post whether they are logged in or not, Users that are not logged in are not able to interact with the post such as like or commenting on posts. If they are not logged in a prompt at the comment section informs them to sign in if they want to interact with the post.

The Blog post displays the user's Title, author name and date created. Along with a link to the user's profile.
If the user that is viewing the blog is the blog's author, they will have the option to update and delete the post and will have 2 buttons available only to them.

Following down the page all of the blog content is posted as the user created it and displayed as edited.

Next is the like and comment section. The page has both like and comment counts that increase and decrease depending on the total likes and comments. If the user would like to leave feedback ask questions or have a conversation they can post a comment and will display in order.

![view blog post](/readME-assets/features/view_post.png)

<details>
<summary>Create Blog Post Mobile</summary>

![view blog post mobile](/readME-assets/features/view_post%20mobile.png)
</details>

### View Blog Post Comments
Comments are a good way for users to interact with each other, share feedback and hold conversations with each other. The page has authentication and if statements to check over certain parameters.

If the post does not have any comments then a Placeholder message is displayed as "No comments on this post".

If the user is not logged in they will not be able to make a comment. Users are prompted to either log in or register to be able to post and also leave comments and likes on the page.

Users are able to update their own comments even on posts they did not create. As seen below Chris can edit his own comment but no the rock's comment.

![View Comments](/readME-assets/features/comments.png)

<details>
<summary>View Comments Mobile</summary>

![View Comments Mobile](/readME-assets/features/comments%20mobile.png)
</details>
<details>
<summary>Comment Authentication and If Statement</summary>

![View Comments Logged Out](/readME-assets/features/comment_logged_out.png)
![No Comments](/readME-assets/features/no%20comments.png)
</details>

### Update Blog Post
Users who are logged in are able to edit their own blog posts. If the user that is logged in is the blog author they are shown an update post button. This redirects them to the blog page that uses a slug URL, which is the title of the blog post, with spaces replaced with "-". this is for better readability.

Once the user clicks update they are taken to the page that is similar to creating the post. All of their data is still there so they can make as small a change and as large a change as they want to. Once the change is made the user is redirected to the blog post that is updated.

![View Update Post](/readME-assets/features/update_post.png)
<details>
<summary>Update Blog post feedback message</summary>

![user Feedback Message](/readME-assets/features/update_post%20message.png)
</details>

### Update Comments
Users are able to update comments that are made and are only able to update their own comments. If the user would like to make a change to the comment. A small button previews under the comment similar to updating a blog post. 

![View Comment Update](/readME-assets/features/update_comment.png)
<details>
<summary>Comments message and update button</summary>

![Comment Message](/readME-assets/features/comment%20message.png)
![Comment Update Button](/readME-assets/features/comments.png)
</details>

### Delete Comments
If a user would like to delete a comment and they want it removed. If they are logged in and are the author of the comment, just like the update button and delete this comment button is next to it. The user can click this and a pop-up message displays to check if the user really does want to delete this comment. The modal asked the user to confirm that they did. if they do then the comment is deleted and the page is refreshed and the comment is removed. A message will be displayed for user feedback.

![Comment Deleted](/readME-assets/features/delete_comment.png)
<details>
<summary>Comments message delete</summary>

![Comment Message](/readME-assets/features/delte%20comment%20msg.png)
![Comment Removed](/readME-assets/features/Comment%20removed.png)
</details>

### Delete Post
If the user decides that they want to delete their blog post for whatever reason they have, they have that ability to, just like updating their post. First the blog checks that the user logged in is the user that is making the request. If the page confirms. then the user has the option to delete the post. A modal is used similar to the comment to confirm that if they delete the post and is not a mistake. A modal message is triggered and tells the user the post they want to delete and if they want to delete the post.

![Post Deleted](/readME-assets/features/delete%20post.png)

### Custom Error Pages
With the possibility of a user getting a error code from changing the URL, or trying to use the url to edit other profiles, which cannot happed due to authentication statements. I have implemented custom error pages that is display to the user and provide a reason for the error. It uses my base.html for a more diverese look, but provides the error code and reson for the error so they are not left confused. Expample of 404 not found, if a user has post saved but is deleted this error will display.

![Error 404 Page](/readME-assets/tests/custom_error.png)

## User Accounts
### Register Account
The blog has user accounts and authentication so users need to be able to login to the account to carry out user functions. When the user joins the sign they can first register their account. The Registers require a username and a password, email is optional. Once the user registers on the website they are auto-redirected to the home page and a message is displayed. Then they are free to use the website and all features.

![New User Signup Page](/readME-assets/features/signup.png)
<details>
<summary>Register New User Msg</summary>

![New User Message](/readME-assets/features/signup%20msg.png)
</details>

### Logout Page
If the user has decided they want to log out of their account then they have the ability to. The user once logged in has the logout URL in the navigation bar. when they click that they are taken to the logout page and are asked to confirm they want to log in. Once they log out they are redirected to the home page and a message is displayed to confirm they signed out and from what account.

![Signout User](/readME-assets/features/signout.png)
<details>
<summary>Signout User Msg</summary>

![Signout User Msg](/readME-assets/features/signout%20msg.png)
</details>

### Login Page
To use the features on the website, users need to be logged into the page. When the user opens the site they are on the home page, in the navigation bar they are able to sign in to the website and use the features.
Once they sign in they are redirected to the home page and are able to use the website freely.

![Signin User](/readME-assets/features/signin.png)
<details>
<summary>Signout User Msg</summary>

![Signin User Msg](/readME-assets/features/signin%20msg.png)
</details>

### Django Admin
To manage all of the content on the website a user has Admin privileges called superuser. This allows the superuser to administer the site and use the admin panel to easily manage users and content. This can delete updates and create any and all posts. This is used for any unwanted content posts or trolling.

![Admin](/readME-assets/features/admin.png)


## Profile
### View Profile Page
When users create their accounts, users profiles are automatically created for the user. This is a place where they can upload their own content and make it more personal so people can get to know them and see who they are reading or interacting with. 
The profile page has a range of fields that they can fill. Only Required is a small bio, the rest is recommended to fill out but optional. Users can upload a photo, first and last name, bio, gym focus, occupation and social media links, Twitter, facebook, Instagram and a website or other link.

This allows users to contact the authors outside the website if they want to or just get to know them on a more personal level. But is optional so users can put as much or as little as they like.

![New User Profile](/readME-assets/features/new_user_pfrofile.png)

![User Profile](/readME-assets/features/profile.png)

### Edit Profile Page
Users are checked to confirm if the profile user id matches the correct profile. if they match then they are able to update or delete their profile. The user has the same fields as before and can update or remove any information they would like to. Once they updated their profile they redirected back and received a message.

![Edit Profile](/readME-assets/features/update%20profile.png)
<details>
<summary>Edit Profile message</summary>

![Edit profile User Msg](/readME-assets/features/update%20profile%20msg.png)
</details>

### Delete Profile
User have the option to delete their accounts if they choose so. users are directed to their profile page and checked that they are indeed the profile account user. They are given an option to delete their account. A modal is used to confirm that request and users are instructed that if they delete the account they can no longer post comments or like posts. If the users choose to delete their account, the account is deleted and they are redirected to the home page and the account removed.

When a user deletes their account their posts and comments are also deleted, which they are informed so if they have a block that is removed automatically. As shown bellow

![Delete Account](/readME-assets/features/delete%20profile.png)
<details>
<summary>Delete Profile Cascade</summary>

![Before](/readME-assets/features/before.png)
![After](/readME-assets/features/after.png)
</details>

## Additional features
### Favicon
The Favicon is the small logo at the top of the website browser linked to your page, it is most helpful when a user has multiple browsers open, they can easily see which tab is yours.

![Favicon](/readME-assets/features/favicon.png)

## Future Features
- A feature I wanted to implement but was not a high priority was to display users' posts on their profile page. The feature would have been useful to view posts from the particular user if they had great posts but due to time and knowledge, I was not able to complete it.
- A search function I think would be a priority if I were to start again, being able to search keywords to find the right blog post.

## Design
### Data Model
This project is hosted on Heroku and the hosted database is ElephantSQL.
Cloudinary is used to store all the blog uploaded images and profile images. Three Custom models were created for this app. Post Model for a blog post, Comment model for comments and Profile Model created for user profiles. With the default Django User model already included.

![Post Model](/readME-assets/features/Post%20Model.png)

![Comment Model](/readME-assets/features/Comment%20model.png)

![Profile Model](/readME-assets/features/about%20model.png)

### Typography
Roboto Font is the primary font-family used in this project. 

- [Roboto Font](https://fonts.google.com/specimen/Roboto)

## Technologies Used
### Languages Used:

- HTML5
- CSS3
- JavaScript
- Python

### Frameworks and Libraries Used:

  - [Bootstrap:](https://getbootstrap.com/) Bootstrap CSS Framework is used for styling and building responsive web pages.
  - [Cloudinary:](https://cloudinary.com/) Used to store all blog images and uploaded images.
  - [Coverage:](https://coverage.readthedocs.io/en/latest/index.html) Used for measuring code coverage of Python test files.
  - [Django:](https://www.djangoproject.com/) Main Python framework used in the development.
  - [Django Allauth:](https://django-allauth.readthedocs.io/en/latest/index.html) Used for authentication and account registration.
  - [Django Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/) Used to simplify the rendering of Django forms.
  - [dj_database_url:](https://pypi.org/project/dj-database-url/) Used to allow database URLs to connect to the Postgres database.
  - [Django Countries:](https://pypi.org/project/django-countries/) Used for country selection drop-down
  - [Gunicorn:](https://gunicorn.org/) Green Unicorn, used as the Web Server to run Django on Heroku.
  - [Summernote:](https://github.com/summernote/django-summernote) To provide an editor for customizing new blog content and add images.

### Software and Web Applications Used:

  - [Google Fonts:](https://fonts.google.com/) To import font family Roboto
  - [Font Awesome:](https://fontawesome.com/) Used for style icons for nav and footer and other links
  - [Chrome DevTools:](https://developer.chrome.com/docs/devtools/) To test inside of different screen sizes
  - [GitHub:](https://github.com/) GitHub is used to store the project's code and update and pull from. As well as host user stories
  - [Heroku:](https://www.heroku.com/) For deployment and hosting of the application.
  - [HTML Validator:](https://validator.w3.org/) Check your code for HTML validation.
  - [CI Python Linter](https://pep8ci.herokuapp.com/) Used to validate python code
  - [W3 CSS Validator:](https://jigsaw.w3.org/css-validator/) Check your code for CSS validation.
  - [Codeanywhere](https://codeanywhere.com/signin) Used as virtual environment for coding
  - [ElephantSQL:](https://www.elephantsql.com/) Used Elephant to host PostgreSQL Service
  - [Stack Overflow](https://stackoverflow.com/) Used for help when hit bumps or errors

## Testing
### Validator Testing
### HTML Testing
All HTML Pages passed validation testing except for, Create_post.html.
Due to using the SummernoteWidget for blog editing the iframe caused a number of errors in the code. At first, I decided to remove the summernote and not use customization. But on further thought the lack of formability was causing a lack of engagement for the block post and a necessary for the website to serve its purpose and the formatability could not be sacrificed and hope the decision was correct to do so.

![All HTML Pages Validation](/readME-assets/tests/html_test.png)

<details>
<summary>Summernote HTML Page</summary>

![Summernote HTML Page](/readME-assets/tests/summernote_errors.png)
![Summernote Html Errors](/readME-assets/tests/html_blog_post_summernote.png)
</details>

### W3C CSS Validator:
The W3C CSS validator was used to validate the css. No issues found
![CSS Validation](/readME-assets/tests/css_test.png)

### CI Python Linter
All Python files in the blog app were tested and passed
<details>
<summary>Blog App Python Test</summary>

![admin.py](/readME-assets/tests/blog_admin_test.png)
![forms.py](/readME-assets/tests/blog_forms_test.png)
![models.py](/readME-assets/tests/blog_models_test.png)
![urls.py](/readME-assets/tests/blog_urls_test.png)
![views.py](/readME-assets/tests/blog_views_test.png)
</details>

<details>
<summary>Blog About Python Test</summary>

![admin.py](/readME-assets/tests/about_admin_test.png)
![forms.py](/readME-assets/tests/about_forms_test.png)
![models.py](/readME-assets/tests/about_models_test.png)
![urls.py](/readME-assets/tests/about_urls_test.png)
![views.py](/readME-assets/tests/about_view_test.png)
</details>

### Lighthouse:
Lighthouse Pass Test:

![Home Page Lighthouse](/readME-assets/tests/lighthouse_test.png)

## Automated Testing
### Django testing tools:

Django TestCase was used to create automatic test for python files. The rest reporting tool 'Coverage' was installed and used to test and then provide a report.

![Coverage Test](/readME-assets/tests/python_testing.png)

### User Stories testing
- To further test that the application is working correctly and functions as expected manual testing was carried out along side user stories to make sure criterai was met.

**Admin and Account**
US1 - Account registration, login and logout
	- Acceptance Criteria:
		-To register a new user, must enter username and password. (email is optional)
		- Users should not be able to register the same username if one is already created.
  		- User are able to log out of their account.
   	- I have tested:
    		That username and password are required and email optional
      		THe registering of a user with a name same as other user reports and erro.
US2 - Manage Posts
	- Acceptance Criteria:
 		Site admin can log into the admin portal with superuser account
		Site admin can manage all posts, including superuser account
		Site admin can manage all comments and likes, including super users
  	- I have tested:
   		Site admin i can log into the admin portal with superuser account
     		Site admin can manage delete and create all posts and comments including super user
       		Site admin can manage all comments and likes including super user
US24 - Manage User Accounts
	- Acceptance Criteria:
 		Superuser/admin can edit users accounts
   	- I have tested:
    		Superuser can edit all user accounts
US25 - Delete User Accounts
	- Acceptance Criteria:
 		Admins can delete users accounts
   	- I have tested:
    		Admin account can delete other user accounts

**Blog Posts**
US3 - User Story: View post list
	- Acceptance Criteria:
 		All available blog post are presented on blog page
		Posts are sorted by most recent
		Blog preview with Author, Image, Title and date created is shown on the blog preview
		Paginated view, maximum of 6 per page, Next or Prev button if more than 6
	- I have tested:
 		All the blog posts that are posted are present on the page
   		all posts are sorted most recent
     		Blog previews have all details in preview item
       		When the view reaches 6 a new page is created and the Next button is created
US4 - User Story: Open a blog post
	- Acceptance Criteria:
		Blog post Author, image, title, date created, profile link, likes and comments on screen
		Likes and comments are accessible to users logged in.
		Likes and comments are not available to users if not logged in.
  	- I have tested:
   		Blog posts with all post fields are shown on the screen
     		Like and comments responded when the user is logged in
       		likes and comments are not available if a user isn't logged in
US5 - User Story: Create a blog post
	- Acceptance Criteria:
		Registered and logged-in users will be able to create their posts
		Users should be able to complete the post form with all required fields
		Users can upload custom photos for blog posts
 	- I have tested:
  		Logged in user created own blog test post
    		User completed blog post form all required fields
      		users can upload custom photo
US6 - User Story: Edit Post
	- Acceptance Criteria:
		Registed and logged users will be able to edit their own blog posts
		Logged in users should be able to complete all required blog form fields.
 	- I have tested:
  		Logged in user can only edit own post
    		Login user can edit post and complete all required blog fields
US7 - User Story: Delete post
	- Acceptance Criteria:
		Registered and logged-in users can delete their blog posts
		Users should have to confirm that they want to delete their posts
 	- I have tested:
  		Logged in user can delete own post
    		The user confirms that the delete post with delete Modal
US8 - Placeholder Images
	- Acceptance Criteria:
 		Registered and logged-in users will be able to create their posts using the generated placeholder image
	- I have tested:
 		Not submitting an image then uses a placeholder
**User Profiles**
US21 - View Profile
	- Acceptance Criteria:
		Able to view my profile and read my information
		View other users' profiles
 	- I have tested:
  		User can view profiles and read information
    		Non-logged-in or other users can read the profile page
US22 - Edit User Profile
	- Acceptance Criteria:
		registered and logged-in users can edit their own profiles
		Only user logged in can edit their own profiles
		Users can update their chosen fields, if they don't want to add personal info they don't have to.
 	- I have tested:
  		Logged user can edit their own profile
    		Only logged in user to edit their own profile
      		Logged in users can update all fields or no fields only bio required
US23 - Delete Profile/Account
	- Acceptance Criteria:
		Registered and logged-in users can delete their profile and account
		Users are presented with a confirmation message, instructing if delete their profile they can post, comment or like.
 	- I have tested:
 		Logged in user can delete their profile
   		Logged in user is presented with confirm delete profile
**Comments**
US9 - View total comments
	- Acceptance Criteria:
		The total comments will be viewed on blog view previews
		The total comments will be viewed inside the blogs post content
 	- I have tested:
  		Total comments are visible on blog preview
    		Total comments are visible on blog post
US12 - Leave a comment
	- Acceptance Criteria:
		Registered and logged in users can leave a comment on a post
		Commenters' name, content and dates posted are visible as comment
 	- I have tested:
		Logged users can leave a comment on a post
  		User name is shown as comment name, content and date post and visible
US13 - View Comments
	- Acceptance Criteria:
		All comments are visible when viewing a blog post
		Comments are sorted by date created, to comment like a conversation
 	- I have tested:
  		All comment are visible on blog posts
    		Comments are sorted by most recent
US15 - Update Comments
	- Acceptance Criteria:
		Registered and logged-in users will be able to edit their comments
		Users should be able to edit and complete comment form
 	- I have tested:
  		Logged in user can edit their own comments
    		Logged in user can edit own comment and complete update form
US16 - Delete Comments
	- Acceptance Criteria:
		Registered and logged-in users can delete their comments on a post
		User should have to confirm before deleting their own comments
 	- I have tested:
  		Logged in user can delete own comment
    		Logged in user has delete modal appear to confirm deletion

**Likes**
US10 - View Total Likes
	- Acceptance Criteria:
		View the number of likes on the blog list preview
		Have matching like icon to allow user to like post and interact
		Display Total like count next to heart icon
  	- I have tested:
   		Can see number of likes on blog preview
 		Icon matches number of likes on post
   		Total count is displayed next to heart
US11 - Leave a like
	- Acceptance Criteria:
		The user must be registered and logged in to like a user post
		Include matching icon to display if liked or not
 	- I have tested:
  		Logged in user can leave a like, non logged in user cannot
    		User likes comment fills heart, user unlike fill is removed. Works correctly
US14 - View Likes
	- Acceptance Criteria:
		See likes in blog previews and on the blog post
		Include matching icon to likes
  	- I have tested:
   		Can see like in preview on the blog post
     		Matching icon to likes on preview

**UX/UI**
US17 - Responsiveness
	- Acceptance Criteria:
		Responsive design on different screen sizes
		Users should be able to use the website on small devices that are 320px and above
 	- I have tested:
  		Responsive design is adaptiv to all screen sizes
    		Tested on 320px and above 1400px all working as expected.
US18 - Site Design
	- Acceptance Criteria:
		Users are presented with an appealing website that is easy to navigate
		Site meets accessibility guidelines
		User is able to view all images and text on the website
 	- I have tested:
  		All usered are presented with a simple yet stylish blog design and easy to navigate and clear
    		Site passes accessability lighthouse test
      		User can view all image and text on the website. alt tags provided if not(Not the case)
US19 - System messages
	- Acceptance Criteria:
		Registered and logged-in users will get feedback through pop-up messages
		The pop-up message should disappear automatically
 	- I have tested:
  		Logged in users after action recived message display.
    		Message auto closes after 2.5seconds
US20 - Favicon
	- Acceptance Criteria:
 		User is presented with favicon that is matching design of the site
	- I have tested:
 		Favicon is displayed in user tab icon as expected.

## Deployment
I used the following steps to deply to Heroku:

## Deploying by connecting Githun to heroku
1. Top right corner in heroku select Create New App
2. I call the app InPhysical-plans and set region to "Europe"
3. Once the app is created i choose deployment method for "Connect to github"
4. After logging in and authenticating GitHub, i typed in and selected my repo that i was using for my project.
5. When the repo appeared, I clicked Connect Button.
6. Once connected i had the option to deploy.
7. I went to my setting in heroku and added the following to my Config Vars
    - CLOUDINARY_URL - Conntect to Cloudinary DB
    - DATABASE_URL - To store all my data and images
    - PORT - For local testing
    - SECRET_KEY - added my secret key to heroku settings.
8. Once i was ready, i went to my virtual enviroment and did `pip3 freeze --local > requirements.txt`
9. Once completed i created a Procfile that ran the command, `web
gunicorn inphysical_plans.wsgi` 
10. Once all completed i ran `git add .`, `git commit -m 'final deploy`, `git push`
11. THen i went back to heroku dashboard and selected deploy.
12. Waited for heroku to deploy my app and then finished.

## Credits
- CodeInstitue Blog App Project - Some code was used as a base and then fully expanded, gave the groundwork and idea to build up from.
- [Codemy.com](https://www.youtube.com/@Codemycom) Some very helpful advice and able to see how others do it and make my own or use advices.

### Acknowledgements
Would like to thank my mentor Brian Macharia who has helped very much all throught this assignment.
Along with CodeInstitute Tutors have been a great asistance.
