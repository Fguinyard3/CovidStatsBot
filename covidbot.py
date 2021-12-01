import smtplib
from selenium import webdriver


class Covid():
    def __init__(self):
        self.driver = webdriver.Chrome("C:\\Users\\User\\CovidApp\\venv\\chromedriver.exe")
    

    def fetch(self):
            self.driver.get('https://www.worldometers.info/coronavirus/')
            table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]')
            country = table.find_element_by_xpath("//td[contains(., 'USA')]")
            row = country.find_element_by_xpath("./..")
            data = row.text.split(" ")
            total_cases_USA = data[2]
            new_cases_USA = data[3]
            total_deaths_USA = data[4]
            new_deaths_USA = data[5]
            total_recovered_USA = data[6]
            new_recovered_USA = data[7]
            active_cases_USA = data[8]
            critical_condition_USA = data[9]
            total_test_USA = data[12]

            print(data) 


            print("Country: " + country.text)
            print("Total cases: " + total_cases_USA)
            print("New cases: " + new_cases_USA)
            print("Total deaths: " + total_deaths_USA)
            print("New deaths: " + new_deaths_USA)
            print("Total recoveries: " + total_recovered_USA)
            print("New recoveries: " + new_recovered_USA)
            print("Active cases: " + active_cases_USA)
            print("Serious cases: " + critical_condition_USA)
            print("Total test: " + total_test_USA)

            send_mail(country.text, total_cases_USA, new_cases_USA, total_deaths_USA, new_deaths_USA, active_cases_USA, total_recovered_USA, new_recovered_USA, critical_condition_USA, total_test_USA)

            self.driver.close()
        
            self.driver.quit()

def send_mail(country, total_cases_USA, new_cases_USA, total_deaths_USA, new_deaths_USA, active_cases_USA, total_recovered_USA, new_recovered_USA, critical_condition_USA, total_test_USA):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('YourEmail@domain.com', 'Password')

    subject = 'USA Covid-19 stats'

    body = 'Daily COVID-19 stats for' + country + '\
        \nTotal cases: ' + total_cases_USA +'\
        \nNew cases: ' + new_cases_USA + '\
        \nTotal deaths: ' + total_deaths_USA + '\
        \nNew deaths: ' + new_deaths_USA + '\
        \nActive cases: ' + active_cases_USA + '\
        \nTotal recoveries: ' + total_recovered_USA + '\
        \nNew recoveries: ' + new_recovered_USA + '\
        \nCritical cases: ' + critical_condition_USA  + '\
        \nTotal Covid-19 Test: ' + total_test_USA + '\
        \nReference Link: https://www.worldometers.info/coronavirus/'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'Covid',
        'Recipient@domain.com',
        msg
    )
    print('Email has been sent.')

    server.quit()



bot = Covid()
bot.fetch()
