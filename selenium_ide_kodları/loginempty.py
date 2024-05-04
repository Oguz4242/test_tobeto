# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLoginempty():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_loginempty(self):
    self.driver.get("https://tobeto.com/")
    self.driver.set_window_size(1936, 1056)
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Giriş Yap")))
    self.driver.find_element(By.LINK_TEXT, "Giriş Yap").click()
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.NAME, "email")))
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.NAME, "password")))
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".btn:nth-child(3)")))
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
    assert self.driver.find_element(By.XPATH, "//p[text()=\'Doldurulması zorunlu alan*\'][1]").text == "Doldurulması zorunlu alan*"
    assert self.driver.find_element(By.XPATH, "//p[text()=\'Doldurulması zorunlu alan*\'][2]").text == "Doldurulması zorunlu alan*"
  
