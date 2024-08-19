import fin_data_functions as fd, pandas as pd

file_name = 'gme_10k_report_20240203'

pdf_location = f'C:\\Users\\mnbia\\OneDrive\\Documents\\Python\\financial_data_consolidation\\Sample PDF Reports\\{file_name}.pdf'

# Extract balance sheet data
bal_sheet_raw_data = fd.extract_page_contents(pdf_location, 'CONSOLIDATEDBALANCESHEETS')
bal_sheet_content_list, bal_sheet_date_list = fd.scrape_page_contents_and_dates(bal_sheet_raw_data, 'share)', 'See ')
bal_sheet_full_date_list = fd.create_date_values(bal_sheet_date_list)
bal_sheet_clean_content_list = fd.extract_page_content_values(bal_sheet_content_list)
bal_sheet_title_list, bal_sheet_dollar_list_current_year, bal_sheet_dollar_list_prior_year, bal_sheet_dollar_list_prior_year_2 = fd.split_title_and_dollar_values(bal_sheet_clean_content_list)

# Extract operations data
ops_sheet_raw_data = fd.extract_page_contents(pdf_location, 'CONSOLIDATEDSTATEMENTSOFOPERATIONS')
ops_sheet_content_list, ops_sheet_date_list = fd.scrape_page_contents_and_dates(ops_sheet_raw_data, 'Fiscal', 'See ')
# create_date_values function is not needed here due to only showing years in statement of operations so no further cleaning needed
ops_sheet_clean_content_list = fd.extract_page_content_values(ops_sheet_content_list)
ops_sheet_title_list, ops_sheet_dollar_list_current_year, ops_sheet_dollar_list_prior_year, ops_sheet_dollar_list_prior_year_2 = fd.split_title_and_dollar_values(ops_sheet_clean_content_list)

# Extract cash flow data
cf_sheet_raw_data = fd.extract_page_contents(pdf_location, 'Cashflowsfromoperatingactivities')
cf_sheet_content_list, cf_sheet_date_list = fd.scrape_page_contents_and_dates(cf_sheet_raw_data, 'Fiscal', 'https')
# create_date_values function is not needed here due to only showing years in statement of cash flows so no further cleaning needed
cf_sheet_clean_content_list = fd.extract_page_content_values(cf_sheet_content_list)
cf_sheet_title_list, cf_sheet_dollar_list_current_year, cf_sheet_dollar_list_prior_year, cf_sheet_dollar_list_prior_year_2 = fd.split_title_and_dollar_values(cf_sheet_clean_content_list)

# Create dataframes for each section + year extracted
bal_sheet_current_year_df = fd.create_report_dataframe(bal_sheet_full_date_list[0], bal_sheet_title_list, bal_sheet_dollar_list_current_year)
bal_sheet_prior_year_df = fd.create_report_dataframe(bal_sheet_full_date_list[1], bal_sheet_title_list, bal_sheet_dollar_list_prior_year)

ops_sheet_current_year_df = fd.create_report_dataframe(ops_sheet_date_list[0], ops_sheet_title_list, ops_sheet_dollar_list_current_year)
ops_sheet_prior_year_df = fd.create_report_dataframe(ops_sheet_date_list[1], ops_sheet_title_list, ops_sheet_dollar_list_prior_year)
ops_sheet_prior_year_2_df = fd.create_report_dataframe(ops_sheet_date_list[2], ops_sheet_title_list, ops_sheet_dollar_list_prior_year_2)

cf_sheet_current_year_df = fd.create_report_dataframe(cf_sheet_date_list[0], cf_sheet_title_list, cf_sheet_dollar_list_current_year)
cf_sheet_prior_year_df = fd.create_report_dataframe(cf_sheet_date_list[1], cf_sheet_title_list, cf_sheet_dollar_list_prior_year)
cf_sheet_prior_year_2_df = fd.create_report_dataframe(cf_sheet_date_list[2], cf_sheet_title_list, cf_sheet_dollar_list_prior_year_2)

# Output to xlxs file
report_destination = r'C:\\Users\\mnbia\\OneDrive\\Documents\\Python\\financial_data_consolidation\\report_output_folder\\'
with pd.ExcelWriter(f'{report_destination}bal_sheet_report_output.xlsx') as writer:
    bal_sheet_current_year_df.to_excel(writer, sheet_name=f'{bal_sheet_full_date_list[0]}_bal_sheet', index=False)
    bal_sheet_prior_year_df.to_excel(writer, sheet_name=f'{bal_sheet_full_date_list[1]}_bal_sheet', index=False)

with pd.ExcelWriter(f'{report_destination}ops_sheet_report_output.xlsx') as writer:
    ops_sheet_current_year_df.to_excel(writer, sheet_name=f'{ops_sheet_date_list[0]}_ops_sheet', index=False)
    ops_sheet_prior_year_df.to_excel(writer, sheet_name=f'{ops_sheet_date_list[1]}_ops_sheet', index=False)
    ops_sheet_prior_year_2_df.to_excel(writer, sheet_name=f'{ops_sheet_date_list[2]}_ops_sheet', index=False)

with pd.ExcelWriter(f'{report_destination}cf_sheet_report_output.xlsx') as writer:
    cf_sheet_current_year_df.to_excel(writer, sheet_name=f'{cf_sheet_date_list[0]}_cf_sheet', index=False)
    cf_sheet_prior_year_df.to_excel(writer, sheet_name=f'{cf_sheet_date_list[1]}_cf_sheet', index=False)
    cf_sheet_prior_year_2_df.to_excel(writer, sheet_name=f'{cf_sheet_date_list[2]}_cf_sheet', index=False)

