import selenium
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = selenium.webdriver.Chrome(executable_path="C:/chromedriver_win32 (1).zip/chromedriver.exe")

driver.implicitly_wait(50)
driver.maximize_window()

#To navigate the url

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(30)

#To set a reset password

driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/div[2]/input').send_keys("Admin")
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]').click()
time.sleep(5)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(30)

time.sleep(5)

#Test case 1
#forget password link validation on login page

driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(5)

driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(5)


driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
time.sleep(5)

#Test cases 2
#Header validation on admin page
#usermanagement verification

UserManagement = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span').text
print(UserManagement)
read_text = "User Management"

assert read_text in UserManagement

print("UserManagement verified")

#Job verification

Job = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span').text
print(Job)
read_text = "Job"

assert read_text in Job

print("Job verified")

#organization verification

Organization = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span').text
print(Organization)
read_text = "Organization"

assert read_text in Organization

print("Organization verified")

#Qualifications verification

Qualifications = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span').text
print(Qualifications)
read_text = "Qualifications"

assert read_text in Qualifications

print("Qualifications verified")

#Nationalities verification

Nationalities = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a').text
print(Nationalities)
read_text = "Nationalities"

assert read_text in Nationalities

print("Nationalities verified")

#corporateBranding verification

CorporateBranding = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a').text
print(CorporateBranding)
read_text = "Corporate Branding"

assert read_text in CorporateBranding

print("Corporate Branding verified")

#configuration verification

Configuration = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]').text
print(Configuration)
read_text = "Configuration"

assert read_text in Configuration

print("Configuration verified")

time.sleep(5)

#Test case 3
#Main menu validation on Admin page

#Admin verification

Admin = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').text
print(Admin)

read_text = "Admin"

assert read_text in Admin

print("Admin verified")

#Pim verification

PIM = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').text
print(PIM)

read_text = "PIM"

assert read_text in PIM

print("PIM verified")

#leave verification

Leave = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span').text
print(Leave)

read_text = "Leave"

assert read_text in Leave

print("Leave verified")

#Time verification

Time = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a').text
print(Time)

read_text = "Time"

assert read_text in Time

print("Time verified")

#Recruitment verification

Recruitment = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a').text
print(Recruitment)

read_text = "Recruitment"

assert read_text in Recruitment

print("Recruitment verified")

#Myinfo verification

MyInfo = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a').text
print(MyInfo)

read_text = "My Info"

assert read_text in MyInfo

print("My Info verified")

#performance verification

Performance = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span').text
print(Performance)

read_text = "Performance"

assert read_text in Performance

print("Performance verified")

#Dashboard verification

Dashboard = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span').text
print(Dashboard)

read_text = "Dashboard"

assert read_text in Dashboard

print("Dashboard verified")

#Directory verification

Directory = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span').text
print(Directory)

read_text = "Directory"

assert read_text in Directory

print("Directory verified")

#Maintenance verification

Maintenance = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span').text
print(Maintenance)

read_text = "Maintenance"

assert read_text in Maintenance

print("Maintanance verified")

#Buzz verification

Buzz = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span').text
print(Buzz)

read_text = "Buzz"

assert read_text in Buzz

print("Buzz verified")


driver.close()
driver.quit()
print("test completed")