# Pitch

A python flask web app enabling users to pitch their ideas into different categories and allowing for upvotes and downvotes.

By: Moses Babu

## Description
This web-app allows the user to submit their pitches,have them voted and commented upon.

## Setup/Installation Requirements
* Live site can be accessed from the following link


### Known Bugs
The panels are sometimes irregular due to different pitch sizes.
One can like/dislike as many times as possible, not once for each user as is supposed

### Behaviour Driven Development
* The program should return all pitches on the home page as the main page<br>
Given:All pitches<br>
When: View is changed to home page<br>
Then: Pitches from all users are shown<br>

* One should receive an email when signing up<br>
Given:A sign up feature<br>
When: User successfully signs up <br>
Then: Email is sent to the email registered with<br>

* The program should display a user's profile picture<br>
Given: A choice to upload a profile picture<br>
When: User uploads profile picture<br>
Then: The image should be displayed to the user<br>

* Votes should be recorded and displayed to all the users<br>
Given:A like/dislike option is given<br>
When: User likes/dislikes a pitch <br>
Then: The value is added to the number of likes/dislikes<br>


### Technologies Used
* Atom was the source code editor of choice.
* Git and Github were used as my local and online repositories respectively.
* Flask was used as the micro-framework based on the python language
* Heroku was used in deploying the live site


### Support and contact details
* Contact me through my email: mosesarara@gmail.com
* The source code is also contained within the folder containing this ReadMe with comments on the code thus third-party support can be offered.

### License
&copy 2020 **pitches by moses babu**
