from bs4 import BeautifulSoup

def parseProfile(profile):

	# parse the HTML of my Facebook profile to get all embedded links
	for link in profile.find_all('a'):

		#get the href portion of the <a> tag
		href = str(link.get('href'))

		#this links don't give much info and show up pretty frequently
		if href == "https://www.facebook.com/sonya.kotova#" or href == "#":
			continue

		# print out the link
		print href




def main():

	profile_my_perspective = BeautifulSoup(open("sonyas_perspective.htm"), "html.parser")

	profile_eriks_perspective = BeautifulSoup(open("eriks_perspective.htm"), "html.parser")
		
	parseProfile(profile_my_perspective)

	parseProfile(profile_eriks_perspective)


if __name__ == '__main__':
    main()