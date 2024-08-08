# scripts/data_downloader.py
import time
import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DataDownloader:
    def __init__(self, project_folder_path):
        self.project_folder_path = project_folder_path

    def download_data(self):
        print("Starting data download...")
        try:
            # Set up Chrome options to specify download directory
            download_dir = os.path.join(self.project_folder_path, 'data', 'raw')
            os.makedirs(download_dir, exist_ok=True)
            print("Download directory set to:", download_dir)

            options = webdriver.ChromeOptions()
            prefs = {"download.default_directory": download_dir}
            options.add_experimental_option("prefs", prefs)
            print("Chrome options configured with download directory.")

            # Initialize the Chrome driver
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get("https://www.ilboursa.com/marches/cotation_PX1")

            # Wait until the download link is present and clickable
            wait = WebDriverWait(driver, 40)
            download_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/marches/download/PX1')]")))
            print("Download link found.")
            download_link.click()

            # Wait for the new page to load and the download button to become clickable
            download_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(@class, 'btnR ml10')]")))
            print("Download button found.")
            download_button.click()

            # Wait for the download to complete
            time.sleep(60)  # Increase if needed
            print("Data download completed.")
            print("Files in raw directory:", os.listdir(download_dir))

        except Exception as e:
            logging.error(f"Error during download: {e}")
        finally:
            driver.quit()

if __name__ == "__main__":
    project_folder_path = os.getcwd()
    downloader = DataDownloader(project_folder_path=project_folder_path)
    downloader.download_data()