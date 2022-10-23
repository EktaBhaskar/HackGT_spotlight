**Inspiration**

College is a busy and adventurous time for students during their academic careers, we sought to make our lives easier academically. As four college students, we could all agree that we have a busy schedule and can’t always make it to lectures, often missing key points in notes. We wanted to develop a way that saves time and provides accurate and informative notes by integrating technology. Spotlyte was developed to create a more efficient academic environment with a little retro twist. :) 


**What is Spotlyte?**

Spotlyte is a multipurpose use audio, video, and text converter that can be utilized to make college life easier and safer for students by utilizing machine learning algorithms and APIs.
College classes require a lot of information to be digested from lectures for students to learn; Spotlyte reduces the hassle of having to listen through long lectures and creates a summarized version of it.  Spotlyte also utilizes APIs to compress mp4 and wav instance footages from Youtube and Zoom to signal key movements and events that may signal action words. Overall, Spotlyte is capable of providing efficient summarized data to students through its conversion and detection systems revolving around APIs.

**How we built it**

Spotlyte was created with the use of three main APIs: FlaskAPI, YoutubeDL, and ZoomAPI that allows for text, audio, and video files to be converted and downloaded by the user. Text, audio, and video files are all compressed and summarized into text files using Google AI TTS. The server is hosted on the Google Cloud, utilzing a Linux based VM instance and a Streamlit front end. 

List of tools used: Python, Streamlit, FlaskAPI, YoutubeDL, Google Cloud, ZoomAPI, Google AI. 


**Challenges we ran into**

The creation of the back and front end of our work took lots of time to create, however, setting up a server through Google Cloud and connecting our custom domain from Domain.com proved to be more difficult than we anticipated. There was some delay in the set up of our server and Watson due to verification code issues with promotional codes by sponsors as well.

**Accomplishments that we're proud of**

The creation of everyones first ever full fledged project hosted online with functional programs is an accomplishment of its own. Utilizing AI and APIs helped us organize and compress data to be interpreted enacted us to successfully develop our detection and conversion systems. We are extremely proud of our ability to create a front and back end system with a unique concept in a timely manner to present at the exposition. 

**What we learned**

As emerging hackathon participants, we were exposed to many different tools and topics beneficial to us by sponsors and other peers during workshops that contributed to the success of our project. We learned to develop a server implementation off-site from a local host and create a domain to host our creation. Our first hand experience with brand new full-stack equipment like Docker and IBM Watson allowed us to explore topics of computer vision and AI that we couldve possibly implemented. Mentors and sponsors alike were a great asset in our development of the project.

**What's next for Spotlyte**

The next step for Spotlyte is to integrate IBM Watson to compress mp4 and wav instance footages to key moments in a videos where potential suspicious activity is detected. ZoomVideo API could be applied into security by using IBMs natural language processing system, Watson, to analyze, predict, and log actions in given video segments. We hope to develop more file types to be integrated and convert as well as adding a compliant point detection system with motion sensors that can possibly utilize Twilio API for alerts of activity  to prevent incidents at a specific instance.
