# ICONic needs

**Needs expressed to be heard**

Our website is designed to give individuals with intellectual disabilities an easy and clear way to express their needs. By clicking on icons representing common requests and needs, such as hungry, tired, go outside, take a bath.

The user can quickly and easily communicate their needs to their caregiver. This tool helps both the user and the caregiver have a safer and more efficient daily routine, where the user feels heard and understood.


[Link to live site]("link here")

## Features

### Existing features
#### Icon-Based Communication System
Variety of Icons: A wide range of icons representing common needs (e.g., hunger, tiredness, emotions, activities) that users can select.
Customizable Icons: The cargiver has the ability to add or modify icons to cater to the user’s personal needs.
Categorized Icons: Icons can be organized into clear categories like "Basic Needs", "Emotions", "Activities", etc.

#### Simple User Interface (UI)
Large, Easy-to-Click Icons: Icons are clear, big, and visually intuitive, making it easy for users with limited motor skills to navigate.
Text Labels: Icons include text labels to provide clarity and support for those who can read.
Visual Feedback: Provides visual confirmation by enlarging the chossen icon.

#### Message Notification System
Automatic Notifications: When an icon is clicked, an automated message is sent to the caregiver’s device (e.g., mobile, tablet, or computer).
------Message Details: The notification include the icon selected and the time, and a short description of the need.

#### Caregiver Tools
Caregiver Access: Caregivers can view and manage messages, receive notifications, and track user activity. And caregiver can add, edit and delete icons to meet the user's needs.
------Favorite Icons: Users can mark icons they frequently use as "favorites" for quick access.
------Activity Log: History of requests made by the user, which can be useful for long-term care planning.

#### Security and Privacy
Secure Login: Password-protected access for caregivers and users to maintain privacy and data security.

#### Support for Multiple Devices
Cross-Platform Compatibility: Accessible on smartphones, tablets, and desktops to ensure ease of use across different devices.

### Features for the future
Text-to-Speech: Text on icons can be read aloud to assist those with vision or reading difficulties.

Language Options: Multiple languages to accommodate users and caregivers from different linguistic backgrounds.

High Contrast Mode: Visual support for users with visual impairments by enabling a high-contrast design.

Feedback System: Users can give feedback (e.g., "I feel better" or "This worked") to indicate if their need has been addressed.

Multiple Requests: Users can select multiple icons at once if they have more than one need.

Emotion Tracking: Track emotional status over time, helping caregivers understand patterns (e.g., frequent "angry" or "tired" requests).

Care Plan Integration: Allow caregivers to tailor responses based on the individual’s care plan and specific needs.

Data Encryption: Encrypting all communication to protect sensitive information.

Anonymous Usage: For individuals who do not want to share personal information, the platform could allow anonymous use.

## Improvements for the future

## Accessability
The website is simple and clear, with large, colorful icons representing different needs, such as "hungry," "tired," and "sad." Each icon has a short text to clarify its meaning. The user taps on the icons to express their needs. The design is clean, with large buttons and enough space to prevent mistakes. There is a confirmation when an icon is tapped. The colors are contrasting, but still soft and easy to read. Everything is designed to be easy to use with both touch screens and a mouse.

### Accessability testing
**WAVE Web Accessibility Evaluation Tools**
https://wave.webaim.org/

screenshot

**Lihthouse**

screenshot

**Web Content Accessibility Guidelines (WCAG)**
https://www.w3.org/TR/WCAG22/
We have reviewed parts of the guidelines and can conclude that much more work can be done on the website to make it even more accessible. Due to the limited development time, during a hackathon, we were only able to fulfill some of the requirements. For future improvements, the WCSG will be continuously followed.

Examples of features that needs improvement to meet WCAG:
- Make sure everything works for keyboard-only users
- Make it easy for people to log in without having to remember information
- Except for captions and images of text, text can be resized without assistive technology up to 200 percent without loss of content or functionality.
- More examples can be found at [features for the future](#features-for-the-future).

## Design

### User Stories

<details>

<summary>User Story 1</summary>

<p></p>

</details>


### Media
We hav not used blinking or flashing content as it can cause migraines, dizziness, nausea, and seizures. Comply with WCAG  Seizures and Physical Reactions guidlines

### Colors
Something about good contrast for accessibility while ensuring the design remains soft enough to be safe for people with epilepsy.......

### Typography
**Textspacing**
Comply with the WCAG Text Spacing guidelines
Line height (line spacing) to at least 1.5 times the font size;
Spacing following paragraphs to at least 2 times the font size;
Letter spacing (tracking) to at least 0.12 times the font size;
Word spacing to at least 0.16 times the font size.


### Wireframes

<details>

<summary> Page Name </summary>

![Link to wireframe]("Link goes here")

</details>

### Custom Models
The **UserProfile model** manages users with two roles: CareGiver (CG) and EndUser (EU). It links to the User model via a one-to-one relationship and includes common fields like name, email, about, and created_at. The role field distinguishes between CareGivers and EndUsers, with a ForeignKey linking EndUsers to their CareGiver. The model allows CareGivers to manage multiple EndUsers while ensuring clear role-based associations.

The **Group model** represents categories of icons (e.g., "Basic Needs", "Emotions") with a unique name and an optional description.

The **Icon model** represents icons used by EndUsers to communicate with CareGivers. Caregivers can create and manage icons, each associated with a name, image, and optional group. Icons can be marked as default or active, and are linked to a Group. Only Caregivers can own icons, and the model supports hiding/unhiding icons based on the is_active field.

The **Notification model** represents a notification sent by a CareGiver to a user, linked to an icon. It includes a caregiver (who sends the notification), a user (who receives it), and an icon (representing the type of notification). The model also tracks when the notification was sent (notified_at) and whether it was successfully sent (is_sent).

---- more models?
## Database Design
### Entity Relationship Diagram

----screenshot

## Security Features and Defensive Design

### User Authentication
User authentication is applied to protect user data and prevent unauthorized access. During registration, users create a unique username and a strong password, following stringent security requirements. The login process securely verifies these credentials.

### Form Validation
Should a form be submitted with incorrect or missing information, it will not proceed, and the user will receive a notification identifying the field that triggered the error.

### Database Security
The env.py file securely stores the database URL and secret key to safeguard against unauthorized database access, a setup established prior to the initial push to GitHub.

To enhance site security, Cross-Site Request Forgery (CSRF) tokens have been implemented across all forms.

### Error Page
404 - Page Not Found error page was created to guide them back to the site.

## Testing

### Lighthouse Score
**Lighthouse**: Google Lighthouse is a web performance and SEO auditing tool that analyzes web pages, providing detailed reports and recommendations for improving page speed, accessibility, and user experience. [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)

----screenshot

### HTML Validator
**HTML Validation Service**: A tool to check the markup validity of Ib documents in HTML. [HTML Validation](https://validator.w3.org/)

----screenshot

### CSS Validator
**CSS Validation Service**: A service to check the validity of Cascading Style Sheets (CSS). [CSS Validation](https://jigsaw.w3.org/css-validator/)

---screenshot

### Python Validator
**CI Python Linter**: A Code Insitute tool to validate Python. [CI Python Linter](https://pep8ci.herokuapp.com/)

----screenshot


### Manual Testing
------- Full manual testing can be seen in [TESTING.md](TESTING.md) file.


## Bugs/Issues

### Resolved Bugs/Issues

### Unresolved Bugs/Issues

## Deployment
### Heroku
- Create an account or log in to **Heroku**.
  - On the dashboard, click on **"New"** and select **"Create new app"**.
  - Give the app a unique name and select the region closest to you. Then click **"Create app"** to confirm.
---------.......continue

### Forking repository
- Forking enables you to create a personal copy of an existing repository on a remote server. To do so with the specified repository:

- Navigate to the **[repository](https://github.com/aslinedvinsson/Axisofaccesshack)** on GitHub.
- Click on the **"Fork"** button located at the top right corner of the page.
- This action will generate a copy of the repository under ythe own GitHub account.

## Tools/Technologies

### Languages
* HTML5 - Provides the content and structure for the website.
* CSS - Provides the styling for the website.
* Python - Provides the functionality for the site.
* Django - Used as the Python framework for the website.
* Javascript - Adds interactivity and dynamic features to the website.

### Frameworks and Libraries
- **Django**: A high-level Python framework that enctheages rapid development and clean, pragmatic design. [Django](https://www.djangoproject.com/)
- **Bootstrap**: A front-end framework for developing responsive and mobile-first websites. [Bootstrap](https://getbootstrap.com/)
-
### Code
The Code Institute's repository boilerplate for Gitpod was utilized

### Design

### Media

### Editors

### Other Tools

## Credits


### Disclaimer
The content available on this site is solely for hackathon purpose and should not be interpreted as a professional tool.