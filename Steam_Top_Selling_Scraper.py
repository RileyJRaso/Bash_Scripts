from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class SteamTopScraper(object):
  def __init__(self):
    self.driver = webdriver.Chrome(executable_path=r"./chromedriver")

  def scrape(self):
    #get to the steam website
    self.driver.get('https://store.steampowered.com/')

    #Click the top selling tab
    Link_For_Top_Selling = self.driver.find_element_by_id("tab_topsellers_content_trigger")
    Link_For_Top_Selling.click()

    #header for data
    with open('Steam_Top_List.txt', 'w+') as f:
        f.write("For All Of Steam:" + "\n")

    #get data and save to file
    self.Get_Top_Selling_Front_Page()

    #go to Action games page
    element_to_hover_over = self.driver.find_element_by_id("genre_tab")
    hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
    hover.perform()
    Game_Tab = self.driver.find_element_by_id("genre_flyout")
    Game_Genres = Game_Tab.find_elements_by_class_name("popup_menu_item")
    Action_Games = Game_Genres[6]
    Action_Games.click()

    #header for data
    with open('Steam_Top_List.txt', 'a') as f:
        f.write("\nFor Action Games:" + "\n")

    #get data and save to file
    self.Get_Top_Selling_Not_Front_Page()

    #go to Action games page
    element_to_hover_over = self.driver.find_element_by_id("genre_tab")
    hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
    hover.perform()
    Game_Tab = self.driver.find_element_by_id("genre_flyout")
    Game_Genres = Game_Tab.find_elements_by_class_name("popup_menu_item")
    Advenure_Games = Game_Genres[7]
    Advenure_Games.click()

    #header for data
    with open('Steam_Top_List.txt', 'a') as f:
        f.write("\nFor Advenure Games:" + "\n")

    #get data and save to file
    self.Get_Top_Selling_Not_Front_Page()

  def Get_Top_Selling_Front_Page(self):
    #Click the top selling tab
    Link_For_Top_Selling = self.driver.find_element_by_id("tab_topsellers_content_trigger")
    Link_For_Top_Selling.click()

    #grab the top selling table:
    Top_Selling_Table = self.driver.find_element_by_id("tab_topsellers_content")
    Top_Selling_Table_Names = Top_Selling_Table.find_elements_by_class_name("tab_item_name")
    Top_Selling_Table_Prices = Top_Selling_Table.find_elements_by_class_name("discount_final_price")

    #getting the text out of the results
    List_Of_Names = []
    List_Of_Prices = []
    for Names in Top_Selling_Table_Names:
      List_Of_Names.append(Names.text)

    for Prices in Top_Selling_Table_Prices:
      List_Of_Prices.append(Prices.text)

    with open('Steam_Top_List.txt', 'a') as f:
      for index in range(len(List_Of_Names)):
          f.write(str(index + 1) + ": " + List_Of_Names[index] + "\t" + List_Of_Prices[index] + "\n")

  def Get_Top_Selling_Not_Front_Page(self):
    #Click the top selling tab
    Link_For_Top_Selling = self.driver.find_element_by_id("tab_select_TopSellers")
    Link_For_Top_Selling.click()

    #grab the top selling table:
    Top_Selling_Table = self.driver.find_element_by_id("tab_content_TopSellers")
    Top_Selling_Table_Names = Top_Selling_Table.find_elements_by_class_name("tab_item_name")
    Top_Selling_Table_Prices = Top_Selling_Table.find_elements_by_class_name("discount_final_price")

    #getting the text out of the results
    List_Of_Names = []
    List_Of_Prices = []
    for Names in Top_Selling_Table_Names:
        List_Of_Names.append(Names.text)

    for Prices in Top_Selling_Table_Prices:
        List_Of_Prices.append(Prices.text)

    with open('Steam_Top_List.txt', 'a') as f:
        for index in range(len(List_Of_Names)):
            f.write(str(index + 1) + ": " + List_Of_Names[index] + "\t" + List_Of_Prices[index] + "\n")
def main():
  scraper = SteamTopScraper()
  print('Scraping site For top 10 games...')
  scraper.scrape()

if __name__ == '__main__':
  main()
