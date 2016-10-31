import pandas as pd
import numpy as np
import datetime

"""
PYTHON TEST

Pandas is a widely used tool for analyzing tabular data structures (spreadsheets, SQL tables, etc.) in Python.
It is one of Social Fulcrum's core tools for managing and analyzing data, and is part of the majority of our work.

Reference Documentation:

Pandas Documentation: http://pandas.pydata.org/pandas-docs/version/0.18.0/
Pandas Tutorial: http://pandas.pydata.org/pandas-docs/version/0.18.1/tutorials.html
Installing Pandas (or using a web service): http://pandas.pydata.org/pandas-docs/stable/install.html

In this file, please write a main function that reads the sample_dataset.csv included in this repository
into a Pandas DataFrame object and prints answer to the questions posed in the function.

Documentation for the sample_dataset can be found in sample_dataset_documentation.md.

The function does not need to return a value.

"""

def main():

	"""
	QUESTION 1
	
	Is there a meaningful relationship between the client's CPM and major calendar
	events (such as US holidays)?

	To answer, please print the mean CPM for holidays and non-holidays.
	Feel free to change the pre-set variable names if you like.

	More information on CPM can be found here:
	https://en.wikipedia.org/wiki/Cost_per_mille
	"""
    #sourced bank holiday info from http://www.bluesock.com/bank_holidays_csv.php
    df= pd.read_csv('sample_dataset.csv')
    holidays = pd.read_csv('bank_holidays.csv')
    #sort by bank holiday
    bank_holidays=holidays[holidays.Type == "Bank Holiday"]
    #convert to datetime
    bank_holidays['Date']=pd.to_datetime(bank_holidays.Date)
    df['date']=pd.to_datetime(df.date)
    #get CPM and assign column
    df["CPM"] = df.spend/(df.impressions/1000)
    #merging to get holiday info
    merged=pd.merge(df,bank_holidays, how='left', left_on=df.date, right_on=bank_holidays.Date)
    #assigning holidays and non holidays
    Holidays= merged[merged['Bank Holiday']==True]
    Non_holidays= merged[merged['Bank Holiday']!=True]

    holiday_cpm= np.mean(Holidays['CPM'])
    non_holiday_cpm=np.mean(Non_holidays['CPM'])

    print 'CPM by holiday/non-holiday:\n'
    print 'Holiday CPM:',holiday_cpm,'Non-Holiday CPM:',non_holiday_cpm
    print '\n\n'

	"""
	QUESTION 2
	
	What are the most and least expensive audiences by:
		- CPM? https://en.wikipedia.org/wiki/Cost_per_mille
		- CPC? http://www.wordstream.com/cost-per-click
		- Cost per pixel_5?
		- Cost per pixel_10?

	To answer, please print the audience field for each metric.
	Feel free to change the pre-set variable names if you like.

	More information on CPM can be found here:
	https://en.wikipedia.org/wiki/Cost_per_mille
	"""	
    #CPM cost per milli dataframe containing means grouped by audience, sorted
    CPM=df[['audience','CPM']].groupby(by=['audience']).mean().sort_values(['CPM'], ascending=False)
    #indexing to get min and max
    cpm_audience_high=CPM.ix[:1]
    cpm_audience_low=CPM.ix[-1:]

    print 'Highest and lowest CPM:\n'
    print 'High:',cpm_audience_high,'\n''Low',cpm_audience_low
    print '\n\n'
    
    #removed zero clicks from averages
    no_click=df[df.clicks>0]
    #CPC cost per click sorted anf grouped by audience
    CPC=no_click[['audience','CPC']].groupby(by=['audience']).mean().sort_values(['CPC'], ascending=False)
    cpc_audience_high=CPC.ix[:1]
    cpc_audience_low=CPC.ix[-1:]
    print 'Highest and lowest CPC:\n'
    print 'High: ',cpc_audience_high,'\n'' Low: ', cpc_audience_low
    print '\n\n'
    
    #removing zeros from pixels
    no_pix5_zero=df[df.pixel_5>0]
    #creating cost per pixel as CPP5
    no_pix5_zero['CPP5']=no_pix5_zero.spend/no_pix5_zero.pixel_5
    #grouping/sorting
    pixel5=no_pix5_zero[['audience','CPP5']].groupby(by=['audience']).mean().sort_values(['CPP5'], ascending=False)
    pixel5_audience_high=pixel5.ix[:1]
    pixel5_audience_low=pixel5.ix[-1:]
    print 'Highest and lowest pixel_5:\n'
    print 'High: ',pixel5_audience_high,'\n'' Low: ',pixel5_audience_low
    print '\n\n'

    #Follows same logic as pixel_5
    no_pix10_zero=df[df.pixel_10>0]
    no_pix10_zero['CPP10']=no_pix10_zero.spend/no_pix10_zero.pixel_10
    pixel10=no_pix10_zero[['audience','CPP10']].groupby(by=['audience']).mean().sort_values(['CPP10'], ascending=False)
    pixel10_audience_high=pixel10.ix[:1]
    pixel10_audience_low=pixel10.ix[-1:]
    print 'Highest and lowest pixel_10:\n'
    print 'High: ',pixel10_audience_high,'\n'' Low: ',pixel10_audience_low
    print '\n\n'

	return None


if __name__ == '__main__':
	main()