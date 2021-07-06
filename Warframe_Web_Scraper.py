from bs4 import BeautifulStoneSoup as bs 
import requests
import itertools 

# r = requests.get("https://warframe.fandom.com/wiki/Furax")
# r = requests.get("https://warframe.fandom.com/wiki/Vectis_Prime")

# Convert to bs4 object 
# soup = bs(r.content)
# contents = soup.prettify()
# print(contents)

# print(info_b.find(class_="pi-data-label pi-secondary-font").get_text()) #grabs the mastery text 
# print(info_b.find(class_="pi-data-value pi-font").get_text()) # grabs weapon mastery value 
# print(info_b.find("b").get_text()) # grabs the weapon name
# info_b = soup.find("aside")
# info_b = soup.find(class_="portable-infobox pi-background pi-europa pi-theme-wikia pi-layout-default")
# info_d = info_b.find_all(class_="pi-data-label pi-secondary-font") # keys 
# info_v = info_b.find_all(class_="pi-data-value pi-font") # values 

# # info_a = soup.find("aside") # same as info_b 

# weapon_info = {}
    
# weapon_info["Name"] = info_b.find("b").get_text()

# for (a, b) in zip(info_d,info_v):
#     conntent_key = a.get_text().replace(" ", "")
#     conntent_value = b.get_text().replace("\xa0","")
#     weapon_info[conntent_key] = conntent_value
    

# for  i in info_d: # grabs the key using class_="pi-data-label pi-secondary-font"
#     conntent_key = i.get_text().replace(" ", "")
# #   conntent_value = 
# #     print(conntent_key)
#     weapon_info[ conntent_key] = 0

# for i in info_v: # grabs the values using all the class_="pi-data-value pi-font"
#     conntent_value = i.get_text()
#     print(conntent_value)
#     weapon_info[conntent_key] = conntent_value


# for i in info_b: # only gives back Disposition(balls), Update 13.0
#     if i.find("span") == -1:
#         continue
#     elif i.find("span") == None:
#         continue
#     else:
#         print(i.find("span").get_text())

# weapon_info

# r = requests.get("https://warframe.fandom.com/wiki/Weapons")
# soup = bs(r.content)
# contents = soup.prettify()
# print(contents)

# weapon_list = soup.find(class_="tabbertab")
# weapon_list_S = soup.find(title="Secondaries")
# weapon_list_M = soup.find(title="Melees")
# weapon_list_A = soup.find(class_="tabbertab", title="Archwing")
# weapon_list_R = soup.find(title="Robotic")
# list_a = weapon_list.find_all("tr")
# war = "http://warframe.fandom.com" 
# wiki_links = []

# for i in list_a: # will get all the text from the info box thing. 
#     print(i.get_text())

# for i in weapon_list.find_all("a", title=True): # will get all the titles for the links(href). 
#         print (i['title'])

# for i in weapon_list.find_all("a", href=True): # will give the links for images ang wiki pages. 
#     print(i["href"])

# for index, i in enumerate(weapon_list_A.find_all("a", href=True)): # will give links for wiki pages. 
#     if index % 2 == 1: # if you change 1 for a 0 will give links for images.
#         wiki_links.append(i["href"])
# wiki_links
# for i in wiki_links:
#     print(war + i)

# weapon_list_A

# def get_w_info(url):
#     r = requests.get(url)
#     # Convert to bs4 object 
#     soup = bs(r.content)
#     info_b = soup.find(class_="portable-infobox pi-background pi-europa pi-theme-wikia pi-layout-default")
#     if info_b == None:
#         pass
#     info_d = info_b.find_all(class_="pi-data-label pi-secondary-font") # keys 
#     info_v = info_b.find_all(class_="pi-data-value pi-font") # values 

#     weapon_info = {}
    
#     weapon_info["Name"] = info_b.find("b").get_text()

#     for (a, b) in zip(info_d,info_v):
#         conntent_key = a.get_text().replace(" ", "")
#         conntent_value = b.get_text().replace("\xa0","")
#         weapon_info[conntent_key] = conntent_value
        
#     return weapon_info

# weapon_info_list = []

# for index, i in enumerate(weapon_list.find_all("a", href=True)): 
# will give links for wiki pages for primary weapons and put it in our function to create a list.
# #     if index == 3:
# #         continue
#     if index % 2 == 1:# if you change 1 for a 0 will give links for images.
#         relative_path = i["href"]
#         if relative_path == "/wiki/Arthemis bow":
#             continue
#         full_path = war + relative_path
#         print(full_path)
#         weapon_info_list.append(get_w_info(full_path))

# for index, i in enumerate(weapon_list_M.find_all("a", href=True)): 
# will give links for wiki pages for primary weapons and put it in our function to create a list.
#     if index % 2 == 1:# if you change 1 for a 0 will give links for images.
#         relative_path = i["href"]
#         if relative_path == "/wiki/Exalted_Blade":
#             continue
#         full_path = war + relative_path
#         print(full_path)
#         weapon_info_list.append(get_w_info(full_path))

# for index, i in enumerate(weapon_list_M.find_all("a", href=True)): 
# will give links for wiki pages for primary weapons and put it in our function to create a list.
# #     if index == 3:
# #         continue
#     if index % 2 == 1:# if you change 1 for a 0 will give links for images.
#         relative_path = i["href"]
#         if relative_path == "/wiki/Exalted_Blade":
#             continue
#         full_path = war + relative_path
#         print(full_path)
#         weapon_info_list.append(get_w_info(full_path))

# for index, i in enumerate(weapon_list_A.find_all("a", href=True)): 
# will give links for wiki pages for primary weapons and put it in our function to create a list.
# #     if index == 3:
# #         continue
#     if index % 2 == 1:# if you change 1 for a 0 will give links for images.
#         relative_path = i["href"]
#         if relative_path == "/wiki/Exalted_Blade":
#             continue
#         full_path = war + relative_path
#         print(full_path)
#         weapon_info_list.append(get_w_info(full_path))

# for index, i in enumerate(weapon_list_R.find_all("a", href=True)): 
# will give links for wiki pages for primary weapons and put it in our function to create a list.
# #     if index == 3:
# #         continue
#     if index % 2 == 1:# if you change 1 for a 0 will give links for images.
#         relative_path = i["href"]
#         if relative_path == "/wiki/Exalted_Blade":
#             continue
#         full_path = war + relative_path
#         print(full_path)
#         weapon_info_list.append(get_w_info(full_path))

# weapon_info_list

import json

def save_data(title, data):
    with open(title, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
def load_data(title):
    with open(title, encoding="utf-8") as f:
        return json.load(f)

# save_data("Warframe_weapon_data.json", weapon_info_list)
# save_data("Warframe_secondaries_weapons_data.json", weapon_info_list)
# save_data("Warframe_melees_weapons_data.json", weapon_info_list)
# save_data("Warframe_Archwings_weapons_data.json", weapon_info_list)
# save_data("Warframe_Robotics_weapons_data.json",weapon_info_list)

### impove data 
#- get the info for shedu, Arthemis bow, Exlated Blade.
#- get polarity images? 
#- separete soem of the strings.
#- find a way to grab all the types of weapons in one go. 