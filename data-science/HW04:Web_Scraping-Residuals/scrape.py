import sys
import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd


if len(sys.argv) < 3:
    print("Usage: python3 scrape.py <date> <xslx>")
    exit(1)

desired_date = sys.argv[1]
outpath = sys.argv[2]

url = "https://discoveratlanta.com/events/all/"

df = pd.DataFrame(columns=["title", "link"])
# query url
response = rq.get(url).text

# parse response with html.parser
soup = bs(response, "html.parser")

# grab the div that contains all the listings
all_listings = soup.find("div", class_="all-listings")
# store all listings from within the div
listings = all_listings.find_all("article")


# loop through each listing searching for events on the desired date
for listing in listings:
    # pull the list of dates for the listing
    dates = listing["data-eventdates"]

    # if the listing is happening on the desired date, get the title and link
    if desired_date in dates:
        listing_title = listing.find("h4", "listing-title").text
        listing_link = listing.find("h4", "listing-title").a["href"]

        # create temporary dataframe to concatenate to main dataframe
        temp_df = pd.DataFrame(
            [[listing_title, listing_link]],
            columns=["title", "link"],
        )
        # concatenate temp_df to main df
        df = pd.concat([df, temp_df], ignore_index=True)

# save the listings to the excel file
with pd.ExcelWriter(outpath) as writer:
    df.to_excel(writer, sheet_name=outpath, index=False)
