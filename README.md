# Michael Bianco Data Analytics Portfolio
## About
Hello and welcome to my portfolio! I am a data analyst professional with a financial industry background seeking to apply and grow my technical skillset. I have experience in SQL Server, Power BI, Excel, Python, Alteryx, VBA and statistical concepts. A self-starter, I have leveraged my skills to create practical tools for myself and my colleagues to assist outside of my position's responsibilities. My client-facing experiences highlight my relationship management skills to define and guide business needs.
	
My projects aim to demonstrate my knowledge and skills for necessary analytical tools and concepts. There are more projects in development and this page will be updated as they are completed. Thank you for your time!
## Table of Contents
* [About](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio/tree/main?tab=readme-ov-file#about)
* [Portfolio Projects](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio/tree/main?tab=readme-ov-file#portfolio-projects)
    * Python
        * [Grey Poupon Lyrics Analysis](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio/tree/main?tab=readme-ov-file#grey-poupon-lyrics-analysis)
    * Power BI
        * [North American Breeding Bird Survey Dashboard](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio?tab=readme-ov-file#north-american-breeding-bird-survey-dashboard)
    * SQL
    	* [Philadelphia_Home_Internet_Access](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio/tree/main?tab=readme-ov-file#philadelphia-home-internet-access)
 * [Education](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio/tree/main?tab=readme-ov-file#education)
 * [Certificates](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio/tree/main?tab=readme-ov-file#certificates)
 * [Citations](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio/tree/main?tab=readme-ov-file#citations)
 * [Contact](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio/tree/main?tab=readme-ov-file#contact)
## Portfolio Projects
### Grey Poupon Lyrics Analysis
**Code:** [Grey Poupon Lyrics Analysis](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio/blob/main/grey_poupon_lyrics_analysis.ipynb)

**Goal:** Perform analysis on songs mentioning Grey Poupon in their lyrics to uncover insights and linguistic trends

**Description:** Grey Poupon, a brand of Dijon mustard, is used frequently in Hip Hop music as an allegory for "status, luxury and class" [[1]](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio/tree/main?tab=readme-ov-file#citations). To provide further insight into its use within the music genre, data is scraped and cleaned from a variety of web sources to perform analysis to illustrate hidden patterns related to its use. The combined dataset consists of song titles, artist names, lyric snippets and word categories (i.e. nouns, verbs, etc.).

**Skills:** Python, Pandas, Jupyter Notebooks, linguistic analysis, exploratory analysis, web scraping, data visualization

**Technology:** Python, Pandas, Matplotlib, Selenium, Beautiful Soup, TextBlob, pyautogui, Jupyter Notebooks

**Results:** Scraped multiple web sources to extract, clean and organize music data for analysis. Conclusions included total songs found that reference the mustard brand, most common nouns and verbs in the lyric snippets, alternative spellings of "grey" and "poupon" and count of words that rhyme with "poupon" (among others). Visualizations were created to accompany most of the conclusions presented.
### North American Breeding Bird Survey Dashboard
**Walkthrough File:** [North American Breeding Bird Survey Walkthrough](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio/blob/main/north_american_breeding_bird_survey_walkthrough.pdf)

**Dashboard File:** [North American Breeding Bird Survey Dashboard](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio/blob/main/north_american_breeding_bird_survey_dashboard.pbix)

**Source Files:** [Source files zip folder](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio/blob/main/bird_survey_data.zip)

**Goal:** Load, clean, calculate and present data from the North American Breeding Bird Survey Dataset (1966 - 2021) in a Power BI dashboard. Additionally, a Key Performance Indicator is devised to measure the Data Collection Success Rate of the most recent year (the target goal is 90% of samples submitted meeting the survey's data quality criteria).

**Description:** The North American Breeding Bird Survey (BBS) is a cooperative effort between the U.S. Geological Survey's Eastern Ecological Science Center and Environment Canada's Canadian Wildlife Service to monitor the status and trends of North American bird populations [[2]](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio?tab=readme-ov-file#citations). The combined datasets include the latitude + longitude, weather metrics, and bird species observed. Dashboard visuals include an interactive population map, top ten highest species observed, line graph for population over time, and a Key Performance Indicator for the Data Collection Success Rate of the most recent year. This dashboard's scope is limited to locations in Pennsylvania.

**Skills:** M language usage, DAX language usage, data cleaning in Power Query, utilizing multiple varieties of Power BI visuals, Key Performance Indicator creation, Power BI measures, DAX calculated columns, debugging

**Technology:** Power BI, M language, DAX language, Power Query

**Results:** Imported, cleaned, and organized raw data in Power Query with the M language. Did further data organization, labelling, and calculations with the DAX language. Created visualizations to summarize data and collection accuracy with filters to allow further exploration by end users. Created a Key Performance Indicator to measure the Data Collection Success Rate for ensuring the accuracy and integrity of the data.

**Note:** Refer to north_american_breeding_bird_survey_walkthrough.pdf for a step-by-step walkthrough of the dashboard's creation. The original dashboard file (north_american_breeding_bird_survey_dashboard.pbix) and the source data (bird_survey_data.zip) is also available in this repository for reference.
### Philadelphia Home Internet Access
**SQL File & Commentary:** [Philadelphia_Home_Internet_Access](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio/blob/main/Philadelphia_Home_Internet_Access.sql)

**Query Results File:** [Philadelphia Home Internet Access Query Results](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio/blob/main/Philadelphia_Home_Internet_Access_Query_Results.pdf)

**Source Files:** [Source files zip folder](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio/blob/main/PHL_Internet_School_Data.zip)

**Goal:** Build, clean, and analyze a database for analysis of survey responses regarding availability of internet and awareness of technology assistance programs in the city of Philadelphia. The goal of the analysis is to uncover insights to assist future initiatives for increasing awareness of PHLConnectED, an internet assistance program [[3]](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio?tab=readme-ov-file#citations). 

**Description:** The data utilized is from the 2021 Philadelphia Household Internet Assessment Survey and Schools datasets, provided by OpenDataPhilly [[4]](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio?tab=readme-ov-file#citations) [[5]](https://github.com/Michael-Bianco-Portfolio/Data-Analytics-Portfolio?tab=readme-ov-file#citations). The 2021 Philadelphia Household Internet Assessment Survey is a survey assessment on home broadband and device access in the City of Philadelphia in 2021, while Schools is a dataset with information regarding to public (School District of Philadelphia), charter, private and archdiocesan schools in the city. After combining, the data available includes internet formats available in respondent households, zip codes of respondents, school names, school zip codes, and yearly household income of respondents, among others.

**Skills:** Exploratory analysis, Transact SQL (T-SQL or TSQL), SQL Server, SQL Server Management Studio 20 (SSMS), Key Performance Indicator (KPI) creation, Common Table Expressions (CTE's), stored procedures, SQL views, join clauses, group by statements, data cleaning, database creation

**Technology:** Transact SQL (T-SQL or TSQL), SQL Server, SQL Server Management Studio 20 (SSMS)

**Results:** Imported, cleaned, and combined datasets into a single database. Calculated a KPI to measure the share of respondents unaware of PHLConnectED to measure the success of community outreach + funding efforts, and calculated it for each ZIP code and school. Also calculated amount of respondent households with less than $50,000 yearly income for each ZIP code and school, as well as the number of respondent households that have either no internet or only mobile internet for each zip code. Created a procedure for standardizing a commonly-used query for simplicity and consistency for other users, along with a view to provide specific data for analysis by Power BI.

**Note:** Refer to Philadelphia_Home_Internet_Access.sql for the code and commentary, and refer to Philadelphia_Home_Internet_Access_Query_Results.pdf for screenshots of the SQL query outputs. The source data (PHL_Internet_School_Data.zip) is also available in this repository for reference.
## Education
The University of Scranton: B.S. in Operations Management, Minors in E-Commerce and Business Leadership
## Certificates
[Microsoft Power BI - A Complete Introduction](https://www.udemy.com/certificate/UC-cb8ee79f-abdb-4790-b678-e8b646ed324f/) (Udemy - Issued Feb 2022)

[pandas Essential Training](https://www.linkedin.com/learning/certificates/42160b4137a91c6f0ce2331b576adfef9394f2a6414c5ed02d76183974ea0813) (Issued Aug 2022 - LinkedIn)

[Excel - Introduction to VBA](https://www.linkedin.com/learning/certificates/448a1a3fb4fc11b4aee66d519f9fbc10ff92c09bb60abfdd5e23ecbfaaaf2be1) (Issued Jun 2021 - LinkedIn)
## Citations
1. Caswell, Estelle and Sarah Frostenson. “How Grey Poupon Became Hip-Hop’s Favorite Condiment.” Vox, 12 Oct. 2016, www.vox.com/videos/2016/10/12/13250360/grey-poupon-in-hip-hop
2. (Keith_Pardieck@usgs.gov), Keith Pardieck. BBS - USGS Patuxent Wildlife Research Center, www.pwrc.usgs.gov/bbs/. Accessed 24 June 2024. 
## Contact
LinkedIn Profile: https://www.linkedin.com/in/mbianco1/
