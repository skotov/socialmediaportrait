# A Portrait of a Social Media User: Results

## Experiment Setup
I compared two HTML files, both downloaded by saving my Facebook profile (right click > save as). I downloaded the first HTML file myself. To get the second one, I asked my boyfriend to download a version of my profile. I was curious to see if Facebook presents my identity differently depending on who is looking. I then analyzed the two HTML files by writing a python script to extract all the links from the HTML.

## Analysis
My profile contains links to other components of my profile (`/friends`, `/music`, `/movies`, `/tv`…) and to the profiles of some of my friends. There were, however, to surprises. In a side-by-side comparison of the links in my profile against the link’s in Erik’s version of my profile, it’s clear that my version has far more links than his does. This is strange, since you would think a lot of the components would be the same. It is possible that human error was involved. The next surprise, though, was the presence of links that took this form: `<a href=“#”></a>`. These are placeholder links that, when clicked, don’t send the user anywhere. Typically a web page’s Javascript will fill them in with the appropriate destination links. I’m curious why these links are empty, what the could contain given different parameters.

## Sonya's Version: Links

## Erik's Version: Links