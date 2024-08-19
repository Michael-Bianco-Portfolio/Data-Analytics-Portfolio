from pypdf import PdfReader
from datetime import datetime
import pandas as pd

# section_title_text parameter takes text without spaces to avoid random spaces from raw pdf text throwing off extraction
def extract_page_contents(file_location, section_title_text):
    reader = PdfReader(file_location)
    for page_number in range(len(reader.pages)):
        page = reader.pages[page_number]
        page_contents = page.extract_text()
        if section_title_text in page_contents.replace(" ", ""):
            break
    return page_contents

def scrape_page_contents_and_dates(page_contents, start_characters, end_characters):
    page_string_start = page_contents.index(start_characters)
    page_string_end = page_contents.index(end_characters)
    page_string_slice = page_contents[page_string_start:page_string_end]

    page_content_list = []
    # Input text between each \n character into list as separate items
    character_index = 0
    for character in page_string_slice:
        if character == '\n':
            temp_string_list = []
            for subsequent_character in page_string_slice[character_index + 1:]:
                if subsequent_character == '\n':
                    joined_page_content_value = ''.join(temp_string_list)
                    if joined_page_content_value == ' ':
                        break
                    else:
                        page_content_list.append(joined_page_content_value.strip())
                        break
                else:
                    temp_string_list.append(subsequent_character)
            character_index += 1
        else:
            character_index += 1

    # Remove spaces from page_contents temporarily so the variable's contents is consistent when checking for page title
        # (i.e. no random spaces in the words)
    if 'BALANCESHEETS' in page_contents.replace(' ', ''):
        date_list = page_content_list[:3]
        page_content_list = page_content_list[3:]
    elif 'STATEMENTSOFOPERATIONS' in page_contents.replace(' ', ''):
        date_list = page_content_list[0].split()
        page_content_list = page_content_list[1:]
    elif 'CONSOLIDATEDSTATEMENTSOFCASHFLOWS' in page_contents.replace(' ', '') or 'Cashflowsfromoperatingactivities' in page_contents.replace(' ', ''):
        date_list = page_content_list[0].split()
        # Omit last line in page_content_list due to date and timestamp from top of page
        page_content_list = page_content_list[2:-1]
    else:
        # Add logging here and maybe replace exit() with try/except
        print(f'Cannot determine sheet title: {page_contents}')
        exit()

    # If the subsequent line in page_content_list begins with a lowercase letter,
    # combine with prior line and delete/pop original prior line to prevent unnecessary line break entries in page_content_list
    combine_page_content_list = []
    combine_page_content_list_index = 0
    for page_content_list_item in page_content_list:
        if page_content_list_item[0].islower() == True:
            # Create new list element with line item and prior line item combined
            combine_page_content_list.append(f'{page_content_list[combine_page_content_list_index - 1]} {page_content_list_item}')
            # Delete prior line item as its covered by the new line item
            combine_page_content_list.pop(combine_page_content_list_index - 1)
        else:
            combine_page_content_list.append(page_content_list_item)
            combine_page_content_list_index += 1
    return combine_page_content_list, date_list

def create_date_values(date_list):
    date_list_clean_dates = []
    year_list = []
    month_list_1 = []
    month_list_2 = []
    month_list_3 = []
    day_list = []
    day_list_2 = []
    full_date_list = []
    # Extract year
    for date_text in date_list:
        if date_text[:4].isnumeric() == True and len(date_text) > 4:
            date_list_clean_dates.append(date_text[4:])
            date_list_clean_dates.append(date_text[:4])
        else:
            date_list_clean_dates.append(date_text)
    # Remove commas
    list_index = 0
    for clean_date in date_list_clean_dates[:4]:
        date_list_clean_dates[list_index] = clean_date.replace(',', '')
        list_index += 1
    
    # Extract year values in date_list_clean_dates to year_list, else put value into month_list_1
    for clean_date_2 in date_list_clean_dates:
        if clean_date_2[:4].isnumeric() == True and len(clean_date_2) < 5:
            year_list.append(clean_date_2)
        else:
            month_list_1.append(clean_date_2)
        
    # Remove space from strings with month and day values
    for month_text in month_list_1:
        if month_text[0].isalpha() == True:
            month_list_2.append(month_text.replace(' ', ''))
        else:
            # Add logging here later
            print('Non alphabet character leading month_list_1 list element')

    # Extract and convert month names and day numbers from month_list_2
    for text_5 in month_list_2:
        list_index_2 = 0
        for text_character in text_5:
            if text_character.isalpha() == False:
                # Month name to number conversion
                month_name = text_5[0:list_index_2]
                month_name_format = datetime.strptime(month_name, '%B')
                month_number = datetime.strftime(month_name_format, '%m')
                month_list_3.append(month_number)

                # Extract day number
                day_list.append(text_5[list_index_2:])
                list_index_2 += 1
                break
            else:
                list_index_2 += 1
    
    # Add leading 0 if day value is 1 character long
    for date_text in day_list:
        if len(date_text) < 2:
            day_list_2.append(f'0{date_text}')
        else:
            day_list_2.append(date_text)
    
    # Create full date string in correct date format (yyyy-mm-dd)
    list_index_3 = 0
    for year_value in year_list:
        full_date_list.append(f'{year_value}-{month_list_3[list_index_3]}-{day_list_2[list_index_3]}')
        list_index_3 += 1
    return full_date_list

def extract_page_content_values(page_content_list):
    # Remove dollar signs and commas
    line_item_no_dollar_comma = []
    for line_item_with_dollar in page_content_list:
        line_item_no_dollar_comma.append(line_item_with_dollar.replace('$', '').replace(',', ''))

    # Combine list elements that are meant to be on the same line
        # (i.e. combine line with leading lowercase character and the preceding line)
    combined_line_list = []
    combine_line_index = 0
    for combine_line_item in line_item_no_dollar_comma:
        if combine_line_item[0].islower() == True:
            # Create new list element with line item and prior line item combined
            combined_line_list.append(f'{line_item_no_dollar_comma[combine_line_index - 1]} {combine_line_item}')
            # Delete prior line item as its covered by the new line item
            combined_line_list.pop(combine_line_index - 1)
        else:
            combined_line_list.append(combine_line_item)
            combine_line_index += 1

    # Strip leading spaces, trailing spaces and colons
    clean_content_list = []
    for strip_line_item in combined_line_list:
        remove_colon_space = strip_line_item.strip(':').strip(' ')
        if ' )' in remove_colon_space:
            clean_content_list.append(remove_colon_space.replace(' )', ')'))
        else:
            clean_content_list.append(remove_colon_space)

    return clean_content_list

# Split lines between line titles and dollar values
def split_title_and_dollar_values(clean_content_list):
    dollar_list = []
    title_list = []
    for split_line_item in clean_content_list:
        if split_line_item[-1].isalpha() == True:
            continue
        else:
            # while [-1] is numeric, subtract from index else use index position to split line between title and dollar value
            split_line_index = -1
            while split_line_item[split_line_index].isalpha() == False:
                split_line_index -= 1
            else:
                # Due to negative indexes starting at -1 and not 0,
                    # we add back to the index number to include the correct starting/ending characters in each line
                # If the character the line is split on is ")", then add two index numbers back instead of one to prevent it cutting off
                    # The issue is avoided is due to ")" being sliced out as a non-alphabet character when it is part of the title (i.e. a false positive)
                if split_line_item[split_line_index + 1] == ')':
                    split_line_index += 2
                else:
                    split_line_index += 1

                title_list.append(split_line_item[:split_line_index])
                dollar_list.append(split_line_item[split_line_index:])

    # Clean and extract dollar values + replace dashes with zeros
    stripped_dollar_list = []
    for dollar_list_item in dollar_list:
        dollar_list_item_replace_dash = dollar_list_item.replace('—', '0')
        stripped_dollar_list.append(dollar_list_item_replace_dash.replace(' )', ')'))

    # Split each stripped dollar line item into two separate values
    split_dollar_values_list = []
    for split_dollar_item in stripped_dollar_list:
        # If the string contains ' )', then remove the extra space, then do the split function
        if ' )' in split_dollar_item:
            split_dollar_values_list.append(split_dollar_item.replace(' )', ')').split())
        else:
            split_dollar_values_list.append(split_dollar_item.split())

    # Iterate over list of lists, with index 0 to dollar_list_current_year index 1 to dollar_list_prior_year
        # and index 3 for dollar_list_prior_year_2
    # If the length of the first item in split_dollar_values_list is 2, append 0 values to the entire dollar_list_prior_year_2
        # This is due to identifying when page contents only have two columns of data, in which case zero's are placeholders for the third column
    dollar_list_current_year = []
    dollar_list_prior_year = []
    dollar_list_prior_year_2 = []
    if len(split_dollar_values_list[0]) == 2:
        for split_dollar_value_item in split_dollar_values_list:
            dollar_list_current_year.append(split_dollar_value_item[0])
            dollar_list_prior_year.append(split_dollar_value_item[1])
            dollar_list_prior_year_2.append('0')
            
    else:
        for split_dollar_value_item in split_dollar_values_list:
            dollar_list_current_year.append(split_dollar_value_item[0])
            dollar_list_prior_year.append(split_dollar_value_item[1])
            dollar_list_prior_year_2.append(split_dollar_value_item[2])

    return title_list, dollar_list_current_year, dollar_list_prior_year, dollar_list_prior_year_2

def create_report_dataframe(date_value, title_list, dollar_list):
    df_data_dict = {
        'value_date': date_value,
        'section_title': title_list,
        'value': dollar_list,
    }

    report_df = pd.DataFrame(data=df_data_dict)

    return report_df
