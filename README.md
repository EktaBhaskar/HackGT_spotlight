**Inspiration**

College is a busy and adventurous time for students during their academic careers, we sought to make our lives easier academically and more secure. As four college students, we could all agree that we have a busy schedule and can’t always make it to lectures, often missing key points in notes. We wanted to develop a way that saves time and provides accurate and informative notes by integrating technology. We also noted at our university an ever so need for an increasing line of security in our sociological area. With two completely different subjects to tackle, we developed a way that provides efficiency in academics and personal security. Spotlyte was developed to resolve create a more efficient academic environment while providing a safer environment for universities and the general public.


**What is Spotlyte?**

Spotlyte is a multipurpose use audio, video, and text converter that can be utilized to make college life easier and safer for students by utilizing machine learning algorithms and APIs.
College classes require a lot of information to be digested from lectures for students to learn; Spotlyte reduces the hassle of having to listen through long lectures and creates a summarized version of it.  Spotlyte also utilizes IBM Watson and APIs to compress mp4 and wav instance footages to key moments in a videos where potential suspicious activity is detected. This allows for hours of review time to be reduced to mere minutes, allowing catching crime to be more efficient and effective for law enforcement.Overall, Spotlyte is capable of providing efficient summarized data to students and creating a safer environment through its conversion and detection systems revolving around APIs and IBM Watson.


**How we built it**
Spotlyte was created with the use of three main APIs: FlaskAPI, YoutubeDL, and ZoomAPI that allows for text, audio, and video files to be converted and downloaded by the user. Text, audio, and video files are all compressed and summarized into text files using Google AI TTS. The server is hosted on the Google Cloud, utilzing a Linux based VM instance and Streamlit front end. The ZoomVideo API was integrated into security by using IBMs natural language processing system, Watson, to analyze, predict, and log actions in given video segments. Spotlyte is therefore also capable translating long mp4 and wav security footage on campus into applicable text files and compressed video files consisting of specific time intervals believed to pose a security threat. This saves time in the event of an incident and provides easy and accurate access to informative details detected by Watson. 

List of tools used: Python, Streamlit, IBM Watson & Cloud, FlaskAPI, YoutubeDL, Google Cloud, ZoomAPI, Google AI. 


**Challenges we ran into**

The creation of the back and front end of our work took lots of time to create, however, setting up a server through Google Cloud and connecting our custom domain from Domain.com proved to be more difficult than we anticipated. There was some delay in the set up of our server and Watson due to verification code issues with promotional codes by sponsors as well.

**Accomplishments that we're proud of**

The creation of everyones first ever full fledged project hosted online with functional programs is an accomplishment of its own. Utilizing AI and APIs helped us organize and compress data to be interpreted enacted us to successfully develop our detection and conversion systems. We are extremely proud of our ability to create a front and back end system with a unique concept in a timely manner to present at the exposition. 

**What we learned**

As emerging hackathon participants, we were exposed to many different tools and topics beneficial to us by sponsors and other peers during workshops that contributed to the success of our project. We learned to develop a server implementation off-site from a local host and create a domain to host our creation. Our first hand experience with brand new full-stack equipment like Streamlit and IBM Watson allowed us to explore topics of computer vision and AI. Mentors and sponsors alike were a great asset in our development of the project.

**What's next for Spotlyte?**

We hope to develop more file types to be integrated and convert as well as adding a compliant point detection system with motion sensors that can possibly utilize Twilio API for alerts of activity  to prevent incidents at a specific instance. 
