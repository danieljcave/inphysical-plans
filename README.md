# **InPhysical Plans**

## **Milestone Project 4 for Code Institute Full Stack Software Development.**
### Author - Daniel Cave

InPhysical Plans is a training blog that allows both users and trainer to post their training plans and interact with other users. InPhysical Plans allows users to create blog posts and like or comment on the posts. Users can interact with posts to ask questions leave reviews or improvements to the plans and the author can interact with them. 

Live Version of the website - <a href="https://p3-battleship-dc-6afed2473960.herokuapp.com/" target="_blank">Click Here!</a>

## Table Of Contents
- [**InPhysical Plans**](#inphysical-plans)
  - [**Milestone Project 4 for Code Institute Full Stack Software Development.**](#milestone-project-4-for-code-institute-full-stack-software-development)
    - [Author - Daniel Cave](#author---daniel-cave)
  - [Table Of Contents](#table-of-contents)
  - [**User Experience**](#user-experience)
    - [**Target Audience**](#target-audience)
    - [**User Goals**](#user-goals)
    - [**User Stories**](#user-stories)
  - [Design](#design)
    - [Features](#features)
    - [Navbar](#navbar)
    - [Home page - Blog Preview](#home-page---blog-preview)
=======
* [**User Experience**](#user-experience)
    * [**Target Audience**](#target-audience)
    * [**User Goals**](#user-goals)
    * [**User Stories**](#user-stories)
* [**Design**](#design)
    * [**Features**](#features)
        * [**Navbar**](#navbar)
        * [**Home page**](#home-page---blog-preview)



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
The home page view is the centre of the website. This is where all of the blog posts are held for the users to view right off the bat. The home page uses both base.html and index.html. The base.html holds all of the information needed to make this website work. It holds the header and all the necessary tags, the Navbar and footer, the container for messages and the main content which uses python block content tags to display. 

The home page divides the blog preview posts into 3 separate columns, on mobile view, it goes to a single-column view. The page will hold 6 blog post previews before a pagination if a statement creates a new page. Then a button at the bottom of the page will appear for the user to browse through all of the blogs

![Blog Preview Page](/readME-assets/features/home_page.png)

<details>
<summary>View Home Page Collapsed</summary>
![HomePage Collapsed](/)
</details>
