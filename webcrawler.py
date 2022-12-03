import requests

def check_link_different(link, starting_website) -> bool: #checks if link is different
  if link == starting_website:
    return False

  elif link == starting_website + "/":
    return False

  else:
    return True

def check_link_valid(link) -> bool: #checks link is a http link
  if link[0:4] == "http":
    #print("Link is valid.")
    return True
    
  elif link[0:4] != "http":
    #print("link is not valid")
    return False

def check_onList(link) -> bool:
  if link in links:
    return False
    
  elif link not in links:
    return True

def get_data(link) -> str:
  response = requests.get(link)
  data = response.text
  return data

def find_links_on_webpage(link, data):
  href_index = 0
  
  while True:
    href_index = data.find("href",href_index+1)
    end_index = data.find("\"",href_index+6)
    link = data[href_index+6:end_index]
    
    link_http = check_link_valid(link)
    link_not_on_list = check_onList(link)
    if href_index == -1:
      print(f"found all links on:\n{current_website}\n")
      return '1'
      
    elif link_http and link_not_on_list:
      links.append(link)
      file = open("websites-visited.txt","a")
      file.write(f"\n{link} ({len(links)})\n") #when it discovers new link it writes the link to a file + the amount of links its discovered so far. 
      file.close()

    else:
      pass


link = "https://www.lockheedmartin.com/en-us/products/littoral-combat-ship-lcs.html" #webcrawlers starting link
current_website = link
links = []
links.append(link)
file = open("websites-visited.txt","w")
file.close()

list_index = 0

while True:
  try:
    current_website = links[list_index]
    data = get_data(links[list_index])
    find_links_on_webpage(links[list_index], data)
    list_index += 1
  except:
    print("problem happened")
    list_index += 1
