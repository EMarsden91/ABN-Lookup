from playwright.sync_api import sync_playwright
import json

def get_input():
    abn = input("Enter ABN or business name to look up (0 to quit): ")
    if abn.isdigit() and len(abn) > 11:
        print("ABN too long. Please try again.")
        return get_input()
    return abn


# function to take an ABN as input and run the lookup
def run_lookup():
    with sync_playwright() as p:
        abn = get_input()
        
        while abn != "0":
            browser =  p.chromium.launch(headless=False)   # true = hide browser, false = show browser
            context =  browser.new_context(viewport={"width": 1280, "height": 1200})
            page =  context.new_page()

            page.goto("https://abr.business.gov.au/") # go to the abn lookup website
            page.fill("id=SearchText", abn)   # fill in the ABN in the search box
            page.click("id=MainSearchButton")

            # Check if ABN is invalid
            if  page.locator("h1:has-text('Invalid ABN')").is_visible():
                print("Invalid ABN entered.")
                browser.close()
                abn = get_input()
                continue
            
            if ( page.locator("h2:has-text('No matching records')").is_visible() or  page.locator("h2:has-text('No matching names')").is_visible()):
                print("No matching records found.")
                browser.close()
                abn = get_input()
                continue

            # handle lookup by name
            if  page.locator("h1:has-text('Search results - Active')").is_visible(): # checks if there are results from search.
                page.locator("a[href*='/ABN/View']").first.click()  # click the first result
                
            # Extract data
            entityName =  page.locator("th:has-text('Entity name') + td").inner_text()
            activeStatus =  page.locator("th:has-text('ABN status') + td").inner_text()
            activeStatus = activeStatus.replace("\u00a0", " ")  # remove &nbsp; from html to look better
            entityType =  page.locator("th:has-text('Entity type') + td").inner_text()

            print(f"Entity Name: {entityName}")
            print(f"Active Status: {activeStatus}")
            print(f"Entity Type: {entityType}")

            # name screenshot and save it to the screenshots folder
            imageName = input("Name the screenshot you are saving: ")
            page.screenshot(path = f'screenshots/{imageName}.png')

            # set the data to be saved as a JSON file
            data = {
                "search term": abn,
                "entity_name": entityName,
                "status": activeStatus,
                "entity_type": entityType
            }

            # name the JSON file and save it in working dir
            fileName = input("Name the file you are saving: ")
            with open(f"{fileName}.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            print(f"Saved to {fileName}.json")
            browser.close()

            abn = get_input()



            


