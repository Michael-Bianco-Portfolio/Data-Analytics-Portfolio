-- Note: For screenshots of the query output, please refer to Philadelphia_Home_Internet_Access_Walkthrough.pdf

-- Create table to fill with School CSV data
Create Table Schools (
X VARCHAR(50),
Y VARCHAR(50),
OBJECTID int,
AUN int,
SCHOOL_NUM int,
LOCATION_ID int,
SCHOOL_NAME VARCHAR(100),
SCHOOL_NAME_LABEL VARCHAR(100),
STREET_ADDRESS VARCHAR(100),
ZIP_CODE int,
PHONE_NUMBER VARCHAR(25),
ACTIVE VARCHAR(5),
GRADE_LEVEL VARCHAR(50),
GRADE_ORG VARCHAR(50),
ENROLLMENT int,
TYPE int,
TYPE_SPECIFIC VARCHAR(20)
)


-- Import School data
Bulk Insert Schools
From 'C:\Users\mnbia\OneDrive\Documents\SQL Projects\Philly Home Internet Access\Schools.csv'
With (
FieldTerminator = ',',
RowTerminator = '\n',
FirstRow = 2
)

-- 1.1
-- Now we can see the columns set up with their headers
Select * From Schools
Order By OBJECTID

-- 1.2
-- Initially the data loads, but we notice a discrepancy in GRADE_ORG (such as OBJECTID 1)
	-- Instead of "9-12" as a value in GRADE_ORG, it was converted to a date serial number (45547 which means Sep 12)
	-- This is most likely due to the source file being created in Microsoft Excel, a known limitation
-- We will query this value and replace all instances with "9-12"
Update Schools
Set GRADE_ORG = '9-12'
Where GRADE_ORG = '45547'


-- Create table to fill with PHL_Household_Internet_2021_Data CSV data
Create Table PHL_INTERNET (
OBJECTID SMALLINT,
RESP_ID INT,
YEAR SMALLINT,
INTERVIEW_DATE DATE,
RESP_STATE TINYINT,
RESP_COUNTY TINYINT,
ZIP_CODE INT,
ZIP_CODE_POP_DENSITY_QUINTILE TINYINT,
RESP_AGE TINYINT,
RESP_GENDER	TINYINT,
RESP_COMBINED_SEX_BY_AGE TINYINT,
RESP_RACE_WHITE	BIT,
RESP_RACE_BLACK	BIT,
RESP_RACE_ASIAN	BIT,
RESP_RACE_INDIGENOUS_AMERICAN BIT,
RESP_RACE_PACIFIC_ISLANDER BIT,
RESP_RACE_OTHER_RACE BIT,
RESP_RACE_UNKNOWN BIT,
RESP_RACE_DECLINED BIT,
RESP_RACE_OTHER_RACE_DETAIL	VARCHAR(100),
RESP_ETHNICITY_HISPANIC	TINYINT,
RESP_COMBINED_RACE_ETHNICITY TINYINT,
RESP_BIRTH_COUNTRY TINYINT,
RESP_COMBINED_RACE_ETH_BIRTH TINYINT,
RESP_COMBINED_RACE_BY_AGE TINYINT,
RESP_RACE_BY_EDU TINYINT,
LANGUAGE INT,
RESP_EDU_LEVEL TINYINT,
RESP_EDU_4_CATEGORIES TINYINT,
RESP_COMBINED_SEX_BY_EDU TINYINT,
RESP_COMBINED_AGE_BY_EDU TINYINT,
HH_INCOME TINYINT,
HH_ADULTS_COUNT	TINYINT,
HH_18_OR_UNDER_COUNT TINYINT,
HH_WITH_KIDS_5_TO_18 TINYINT,
HH_K_12_HOUSEHOLD BIT,
HH_MOBILE_INTERNET TINYINT,
HH_WIRED_BROADBAND TINYINT,
HH_SATELLITE_INTERNET TINYINT,
HH_DIAL_UP_INTERNET TINYINT,
HH_ANY_INTERNET_ACCESS TINYINT,
HH_CP_LANDLINE TINYINT,
HH_LL_CELL_PHONE TINYINT,
HH_LL_SMARTPHONE TINYINT,
RESP_LL_CELL_PHONE TINYINT,
HH_COMBINED_PHONE_ACCESS TINYINT,
HH_COMPUTER	TINYINT,
HH_TABLET TINYINT,
HH_WITH_KIDS_COMP_PROGRAMS TINYINT,
HH_WITH_KIDS_INTERNET_PROGRAMS TINYINT,
HH_INTERNET_INTERRUPTED	TINYINT,
RESP_AWARE_PHLCONNECT TINYINT,
RESP_AWARE_FREE_INTERNET TINYINT,
RESP_AWARE_FED_PROGRAM TINYINT,
HH_DISCOUNT_INTERNET_SIGN_UP TINYINT,
HH_ABILITY_TO_KEEP_INTERNET TINYINT,
HH_NO_DISCOUNT_INTERNET_REASON TINYINT,
HH_NO_DISCOUNT_INTERNET_OTHER VARCHAR(500),
RESP_INTERNET_SATISFACTION TINYINT,
HH_NO_BB_REASON_INTERNET_COST TINYINT,
HH_NO_BB_REASON_COMP_COST TINYINT,
HH_NO_BB_REASON_SMARTPHONE TINYINT,
HH_NO_BB_REASON_OTHER_LOCATION TINYINT,
HH_NO_BB_REASON_UNINSTALLABLE TINYINT,
HH_NO_BB_REASON_PRIVACY	TINYINT,
HH_NO_BB_REASON_TECH_COMFORT TINYINT,
HH_NO_BB_REASON_NOT_WANT TINYINT,
HH_NO_BB_REASON_DEBT TINYINT,
HH_NO_BB_REASON_OTHER TINYINT,
HH_NO_BB_REASON_PRIMARY	TINYINT,
RESP_NO_BB_PAST_INTERNET TINYINT,
RESP_BB_COST_LIMIT TINYINT,
INTERVIEW_PHONE_TYPE BIT,
RDD_TYPE TINYINT,
STATISTICAL_WEIGHT DECIMAL
)

-- Import survey file data to database
Bulk Insert PHL_INTERNET
From 'C:\Users\mnbia\OneDrive\Documents\SQL Projects\Philly Home Internet Access\PHL_Household_Internet_2021_Data.csv'
With (
FieldTerminator = ',',
RowTerminator = '\n',
FirstRow = 2
)

-- 2.
-- We will now use the survey data to pinpoint ZIP codes with the highest ratio of repondents unaware of PHLConnectED
	-- Then, we will identify the schools in the respective ZIP codes for targeting outreach + funding efforts
-- First, how many households are unaware of PHLConnectED per ZIP code?
	-- Includes unaware_ratio, which shows the percentage of respondents unaware of PHL Connect
	-- This ratio can be useful for measuring the success of community outreach + funding efforts
With RESP_TOTAL
As(
	Select ZIP_CODE, Count(RESP_ID) As TOTAL_RESP_COUNT
	From PHL_INTERNET
	Group By ZIP_CODE
)
Select p.ZIP_CODE, Count(RESP_ID) As UNAWARE_COUNT, TOTAL_RESP_COUNT, (Cast(Count(RESP_ID) as decimal) / Cast(TOTAL_RESP_COUNT As Decimal)) As UNAWARE_RATIO
From PHL_INTERNET As p
	Left Join RESP_TOTAL As r On p.ZIP_CODE = r.ZIP_CODE
Where RESP_AWARE_PHLCONNECT In(2, 8)
Group By p.ZIP_CODE, TOTAL_RESP_COUNT
Order By UNAWARE_RATIO Desc

-- 3.
-- Now we will see which schools have the highest unaware ratios in their zip code
	-- However, there are many zip codes with 100% due to low total respondents
		-- We will make some edits to the query to filter those out (i.e. > 5)
		-- Then, determine which schools have the highest unaware ratios
With RESP_TOTAL
As(
	Select ZIP_CODE, Count(RESP_ID) As TOTAL_RESP_COUNT
	From PHL_INTERNET
	Group By ZIP_CODE
)
Select p.ZIP_CODE, s.SCHOOL_NAME_LABEL, s.STREET_ADDRESS, Count(RESP_ID) As Resp_Unaware_Count, TOTAL_RESP_COUNT, (Cast(Count(RESP_ID) As Decimal) / Cast(TOTAL_RESP_COUNT As Decimal)) As UNAWARE_RATIO
From PHL_INTERNET As p
	Left Join RESP_TOTAL As r On p.ZIP_CODE = r.ZIP_CODE
	Inner Join Schools As s On p.ZIP_CODE = s.ZIP_CODE
Where RESP_AWARE_PHLCONNECT In(2, 8)
	And r.TOTAL_RESP_COUNT > 5
Group By p.ZIP_CODE, s.SCHOOL_NAME_LABEL, s.STREET_ADDRESS, r.TOTAL_RESP_COUNT
Order By UNAWARE_RATIO Desc
-- Now we can see the schools with the highest rates of families unaware of PHLConnectED within their ZIP code!

-- 4.
-- Next, let's utilize income data to identify which schools have the highest eligible population per zip code
	-- For research purposes, we will set the threshold at $50,000 household income per year
	-- We will create custom grouping on existing survey responses to identify those over and under threshold
	-- Values 1 through 5 for hh_income will represent income up to $50,000
With income_table
As (
	Select
	RESP_ID,
	HH_INCOME,
	Case
		When HH_INCOME <= 5 Then 'Under 50000'
		When HH_INCOME In(98, 99) Then 'No Data'
		Else 'Over 50000'
	End As INCOME_LEVEL
	From PHL_INTERNET
)
Select
	p.ZIP_CODE, SCHOOL_NAME_LABEL, s.STREET_ADDRESS, Count(i.INCOME_LEVEL) As Under_50k_Count
From PHL_INTERNET As p
	Left Join income_table As i On p.RESP_ID = i.RESP_ID
	Inner Join Schools As s on p.ZIP_CODE = s.ZIP_CODE
Where INCOME_LEVEL = 'Under 50000'
Group By p.ZIP_CODE, s.SCHOOL_NAME_LABEL, s.STREET_ADDRESS, INCOME_LEVEL
Order By Under_50k_Count Desc

-- 5.
-- Now, we will look at the count of respondents/households that have either no internet or only mobile internet for each zip code
	-- "Does not have internet" or "has solely mobile-only internet" is part of the qualifying criteria for PHLConnectED
Select ZIP_CODE, Count(ZIP_CODE) As RESP_QUALIFY_COUNT
From PHL_INTERNET
Where HH_K_12_HOUSEHOLD = 1
	And (HH_ANY_INTERNET_ACCESS = 2 Or (HH_MOBILE_INTERNET = 1 And HH_SATELLITE_INTERNET = 2 And HH_WIRED_BROADBAND = 2 And HH_DIAL_UP_INTERNET = 2))
Group By ZIP_CODE
Order By RESP_QUALIFY_COUNT Desc

-- Last, we will create a procedure and view to optimize the use of existing query results and limit external database access to only the required data

-- 6.
-- In order to standardize a commonly-used query for simplicity and consistency for other users, we will create a procedure
	-- In this example, we will create a procedure with the query above for the program's qualifying criteria (either respondent does not have internet or has solely mobile-only internet
	-- Additionally, this procedure will allow the user to change the filter criteria for different internet types (dial up, broadband, etc.) as needed
Create Procedure QUALIFYING_RESPONDENTS
@HH_MOBILE_INTERNET TINYINT,
@HH_SATELLITE_INTERNET TINYINT,
@HH_WIRED_BROADBAND TINYINT,
@HH_DIAL_UP_INTERNET TINYINT
As
SET NOCOUNT ON
Select ZIP_CODE, Count(ZIP_CODE) As RESP_QUALIFY_COUNT
From PHL_INTERNET
Where HH_K_12_HOUSEHOLD = 1
	And (HH_ANY_INTERNET_ACCESS = 2 Or (HH_MOBILE_INTERNET = @HH_MOBILE_INTERNET And HH_SATELLITE_INTERNET = @HH_SATELLITE_INTERNET And HH_WIRED_BROADBAND = @HH_WIRED_BROADBAND And HH_DIAL_UP_INTERNET = @HH_DIAL_UP_INTERNET))
Group By ZIP_CODE
Order By RESP_QUALIFY_COUNT Desc

-- Now we will run a sample query with the procedure we just created
	-- Here we will change the criteria to count respondents that do not have internet or that have either satellite or dial up internet
Execute QUALIFYING_RESPONDENTS @HH_MOBILE_INTERNET = 2, @HH_SATELLITE_INTERNET = 1, @HH_WIRED_BROADBAND = 2, @HH_DIAL_UP_INTERNET = 1

-- 7.
-- In some cases, it is necessary to create a view to help limit access to data for users and applications 
	-- For example, there may be a subset of data that is needed for a Power BI Dashboard, as opposed to the whole database
	-- Here we will create a view that has a query providing specific data for analysis and use by Power BI
Create View POWER_BI_INTERNET_SCHOOLS As
Select s.SCHOOL_NAME_LABEL, s.STREET_ADDRESS, s.ZIP_CODE, Count(RESP_ID) As Resp_Count
From Schools As s
	Inner Join PHL_INTERNET As i On s.ZIP_CODE = i.ZIP_CODE
Group By s.SCHOOL_NAME_LABEL, s.STREET_ADDRESS, s.ZIP_CODE

-- Querying the view, we get the school name, street address, zip code and respondent count
	-- Uses for Power BI include bar chart visualization showing amount of respondents per zip code, table listing the schools in the zip code with the highest respondent count, etc.
Select *
From POWER_BI_INTERNET_SCHOOLS

-- In conclusion, we accomplished the following:
	-- Build a relational database with two file sources
	-- Clean minor formatting errors
	-- Count how many households are unaware of PHLConnectED in each ZIP code
	-- Create a KPI (unaware_ratio) to target and measure results of outreach/funding efforts for PHLConnectED awareness
	-- Determine which schools have the highest count of survey respondents making under $50,000 a year within the school's zip code
	-- Count the number of respondents that have either no internet or only mobile internet for each zip code
	-- Create a procedure to standardize and streamline the query for respondents with no internet or only mobile internet per zip code
	-- Create a view to provide only the necessary data to external Power BI users

-- Sources:
	-- “Philadelphia Household Internet Assessment Survey.” OpenDataPhilly, opendataphilly.org/datasets/philadelphia-household-internet-assessment-survey/. Accessed 21 July 2024. 
	-- “Schools.” OpenDataPhilly, opendataphilly.org/datasets/schools/. Accessed 21 July 2024. 
