from GUVI_Task16.pages.population_page import PopulationPage
def test_population(driver):

    page = PopulationPage(driver)

    page.open_url("https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live")

    try:
        while True:

            population = page.get_population()
            print("Population:", population)

    except KeyboardInterrupt:
        print("Stopped by User")





