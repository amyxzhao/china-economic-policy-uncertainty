README_Updating_EPU_TPU_Index


The EPU_TPU index code was originally written by Liu Dingqian. Yan Wang was responsible for updates and code modifications from May 2022 to January 2025.

1. Setup Instructions
Step 1: Prepare Your Environment
Read the file "EPU Documentation.docx" to set up your working environment. Follow the steps outlined in the document to ensure your system is ready to process the updates.
Provide a brief description of the updates made (e.g., month and year).

Summary of Scripts and Outputs
Script Name	Purpose	Output Files
scrap gmrb to update.ipynb	Scrapes Guangming Daily data	Monthly news data file
scrap rmrb to update.ipynb	Scrapes Renmin Daily data	Monthly news data file
update index_2025.py	Updates EPU and TPU indices	Daily and monthly EPU/TPU index data files

2. Download Monthly Newspaper Data
Step 2: Use Jupyter Notebooks to Scrape Data
1. Open the following scripts in Jupyter Notebook:
   - scrap gmrb to update_2025.ipynb (for Guangming Daily)
   - scrap rmrb to update_2025.ipynb (for Renmin Daily)
2. Update the scripts:
   - Modify the month and year parameters to match the new month you want to scrape.
3. Run each script to download the newspaper data for the respective source.
   - Save the data in the folder specified during your setup.
3. Update the Mainland China EPU and TPU Indices
Step 3.1: Run the Update Script
1. Use the updated script update index_2025.py:
   - This version includes adjustments made specifically for Renmin Daily starting December 2024 (modifications located in lines 295-316). This is the only difference between update index_2025.py and the update index.py version
   - The script generates four key files:
     - Daily EPU Index: update2024_on_D_epu03
     - Daily TPU Index: update2024_on_D_tpu03
     - Monthly EPU Index: update2024_Dec_epu
     - Monthly TPU Index: update2024_Dec_tpu
Step 3.2: Verify Outputs
Ensure all four files are saved correctly in the designated folder.
4. Update the Master Excel File
Step 4.1: Paste the Updated Data
1. Open the file China_Mainland_Paper_EPU.xlsx.
2. Copy the monthly EPU and TPU data from the outputs of update index_2025.py and paste them into the corresponding sections of the Excel file.
Step 4.2: Share the Updated File
1. Email the updated China_Mainland_Paper_EPU.xlsx to:
   - To:
     - Scott Ross Baker <s-baker@kellogg.northwestern.edu>
     - Steven J Davis <stevend5@stanford.edu>
   - CC:
     - Xuguang Sheng <sheng@american.edu>

