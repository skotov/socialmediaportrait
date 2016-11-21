# A Portrait of a Social Media User

## Introduction
In the first chapter of his book “You Are Not A Gadget”, Jaron Lanier argues that technology has an immense impact on human experience. Technology’s impact is so strong that it even plays a role in defining what it means to be human. I further explore this by creating a portrait of myself, as defined by Facebook’s software. More specifically, I extracted all the links in the HTML of my Facebook profile. My goal was to further explore how this data can be used to define me as a human user of the social networking service.

I chose links for my portrait because they are critical in determining relationships between a user and the rest of their social network. In graph theory, most information about a given node comes from the nature of it’s connections to other nodes - it is rarely useful on it’s own. Thus, it seemed fitting to reduce my profile to a list of links - the means by which web pages connect to other web pages.

I made two versions of the portrait based off of two different versions of my Facebook profile:
1) [sonyas_links_organized.md](My profile as viewed by myself) (i.e. logged in as myself)
2) [eriks_links_organized.md](My profile as viewed by someone else) (i.e. logged in, but not as myself)

## Experiment Setup
I compared two HTML files, both downloaded by saving my Facebook profile (right click > save as). I downloaded the first HTML file myself. To get the second one, I asked my boyfriend, Erik, to download a version of my profile. I was curious to see if Facebook presents my identity differently depending on who is looking. I then analyzed the two HTML files, in part by writing a python script to extract all the links from the HTML.

## Results
The links embedded in my profile’s HTML did not contain too many surprises. My profile contains links to other components of my profile (`/friends`, `/music`, `/movies`, `/tv`…) and to the profiles of some of my friends. One thing I found unexpected, though, is that Erik’s version of my profile was very different. It had none of the links in my profile. This is strange, since you would think a lot of the components would be the same. 
	
The one other thing I found surprising was the presence of links that took this form: `<a href=“#”></a>`. There were about seven of these kinds of links in my profile. These are placeholder links that, when clicked, don’t send the user anywhere. Typically a web page’s Javascript will fill them in with the appropriate destination links. I’m curious why these links are empty and what they could contain had the algorithm decided to fill them in.

## Analysis
In the introduction to her book *Control and Freedom: Power and Paranoia in the Age of Fiber Optics*, Wendy Hui Kyong Chun argues that rhetoric around early internet discussed the technology as giving users unprecedented amounts of control and freedom. In reality, however, the use of technologies such as packet sniffing and cookies *without users’ knowledge* opened up more avenues for tracking information on users, thereby leading to more control. Chun states: “The problem is not with the control protocols that drive the Internet…but rather with the way these protocols are simultaneously hidden and amplified.” 

In the context of this article, boiling my Facebook profile down to a series of links underscores the kind of information Facebook tracks on me: who my closest friends are, what I enjoy,  where I go, and what I look like. Reading my experiment in the context of this quote also raises questions. Why don’t I get a say in what these links are? Why is it that I have absolutely no clue how they chose some of these links? This becomes a problem in the context of Lanier’s argument: this text file generated by a mysterious algorithm is used to drive fundamental human interactions. In fact, Lanier would even argue that these text files define what it means to be human.

The most powerful aspect of this experiment was the demystification: it underscores the fact that Facebook pages are just text that gets rendered to a screen. This contradicts the widespread attitude about social media profiles. As Lanier states: “Communication is now often experienced as a superhuman phenomenon that towers above individuals. A new generation has come of age with a reduced expectation of what a person can be, and of who each person might become.” My Facebook profile is used, in our society, to define me as a human. Creating this portrait — a list of plain text links — underscored the notion that a human is so much more than a text file. This leads me to a contradiction: a portrait should depict a human, yet there is very little in this portrait that is truly *human*f.

## Appendix 1: Works Cited
Chun, Wendy Hui Kyong. “Introduction.” Control and Freedom: Power and Paranoia in the Age of Fiber Optics. Cambridge, Massachusetts: The MIT Press. Print.

Lanier, Jaron. “Chapter 1: Missing Persons." You Are Not A Gadget. New York: Alfred A. Knopf, 2010. Print.

## Appendix 2: Files
1. [sonyas_perspective.htm](/sonyas_perspective.htm): The version of my Facebook profile displayed to me
2. [eriks_perspective.htm](/eriks_perspective.htm): The version of my Facebook profile displayed to my boyfriend, Erik
3. [app.py](/app.py): Python script used to extract links from both versions of my profile
4. [sonyas_links_organized.md](sonyas_links_organized.md): A thematically organized list of all links extracted from my version of my Facebook profile
5. [eriks_links_organized.md](eriks_links_organized.md): A thematically organized list of all links extracted from Erik's version of my Facebook profile
4. [sonyas_links.txt](/sonyas_links.txt): Plain text list of links extracted from my version of my Facebook profile
5. [eriks_links.txt](/eriks_links.txt): Plain text list of links extracted from Erik's version of my Facebook profile
