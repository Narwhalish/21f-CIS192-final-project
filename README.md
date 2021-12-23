# CIS 192 Final Project

#### Project Members: Aryan Nagariya, Lorenzo Lucena, Bryan Yao

## Description

This Final Project consists of a web application that given credentials to Piazza and a class code, would provide a CloudWord and a Frequency Plot of the posts in a Piazza Class. We can divide the project in three components. First, the Piazza posts are extracted from the PIAZZA API, and desired information is retrieved. Secondly, we process the data, and utilizing the NLTK and WordCloud libraries, a Wordcloud and Frequency Plot PNG images are generated from the processed data. Thirdly, we display our information using Django onto a web application for our user to be able to access the tool through an interface and personalize their experience by introducing their own credentials.

##Instructions

Note that class code that for a class on piazza can be found by navigating to the class's piazza page and then looking at the code that comes after "class/". For example, below is the URL for CIS 262's piazza page -- "https://piazza.com/class/kst1kcki9vh7k6". Hence, the class code is "kst1kcki9vh7k6". Note that if you click on a particular post, the ID of the post will follow the class code [Example for Post #1023 -- "https://piazza.com/class/kst1kcki9vh7k6?cid=1023"]. 

##Limitations

Note that a first party Piazza API is not avaiable. Therfore, we had to use a third party piazza API. Unfortunately, there do seem be quite a few restrictions in terms of how many times one can make an API call in a certain time frame. For example, initially we would attempt to extract all posts from a class; however, the Piazza API would error out after around 60 posts. To get around this, we set a timer.sleep after every function call and set the post limit to 50 at a time by default. Note that this means the wordcloud we generate by default gets the last 50 posts from the class. The limit can be changed quite easily with a tradeoff of having a higher timer.sleep (around ~1 min) -- resulting in out app running for over >1 hr. For this project, as a proof of concept, we chose to set the limit to 50 posts. 


## Code Structure

The assignment was divided among three team members according to the three stages mentioned earlier. The code consists of a file that accesses the information from Piazza, and another that processes and generates the content of our webpage, all incorporated to a Django Framework.

## Submission Requirements

1. Class Definition: 
2. Two First Party Packages: JSON, Time
3. Two Third Party Packages: Django, NLTK, WordCloud, Matplotlib

## Installation

Libraries WordCloud, NLTK are needed. 


