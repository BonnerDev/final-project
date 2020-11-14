## Children in out of home care
### Introduction: 
My idea for my final project is to collect, analyse and visualize data on children in out of home care in Australia. I am looking to make an easily digestable, infographic type website with easy to read graphs and statistics for those who are looking into either fostering and raising awareness on the actual numbers for children in out of home care in Australia. I would like to make this open for any NFP agencies to be able to use my visualisations for their cause if they so wish.  

### Methodology: 

1. Create HTML and CSS files with layouts and stylings that will hold my visualisations. To include a dashboard with multiple plots.

2. Search for and collect data from for WA and also QLD, some other data to be included from AIHW for the whole of Australia.  

3. Clean the data using Panda's, dropping any columns which had data that is not useful for visualising.

4. Create SQL database and import data into database, create schema of tables and show the links if any.

5. Create impactful visualisations using a mixture of Plotly, Matplotlib and static images with text overlay. 

6. Use Scikit-Learn to predict future numbers of children in out of home care using historical data from 2008 to 2017. 

6. Serve up the app using git hub pages. 

### Ideas for Visualizing
1. I want to show the differences in Non Indigenous and Indigenous children in out of home care throughout WA, from 2008 to 2017. I will visualise this using a plotly grouped bar graph with one colour for Indigenous and one for Non Indigenous. Then show some predictive analysis on where we might see these numbers going based on histroical data. 
2. data from 2012 to 2013 showing the relationship to their carer based on Indigenous or not using double bar chart and group by type of carer
3. data from 2012 to 2013 showing length of out of home care in relation to how many placements they have been in, show what percentage of them in each bracket of length of out of home care, show what is the average number of placements for each length of out of home care 
4. Children receiving child protection services, by age group, Indigenous status and state or territory. 

### This project was created using the following:
1. PostgreSQL
2. Flask
3. Heroku
4. JavaScript
5. jQuery
6. Bootstrap
7. HTML
8. CSS
9. Google charts
10. Pandas
11. Scikit
12. SQLalchemy
13. Plotly
14. Matpltlib


### links to where data has been sourced from
Data source #1 (QLD)
https://data.gov.au/dataset/ds-qld-a6fb9c5d-88b5-470e-af25-e9c3539013dc/details?q=children

Data Source #2 (WA)
https://catalogue.data.wa.gov.au/dataset/swas-for-cpfs
https://catalogue.data.wa.gov.au/dataset/children-in-the-ceos-care-on-30-june-2008-2017/resource/0109e6d3-a77c-4ace-8be2-9c36267c4279

Data Source #3 (All of Australia)
https://www.aihw.gov.au/reports/child-protection/child-protection-australia-children-in-the-child-protection-system/data

Data source #4 (census data for WA 2016)
https://quickstats.censusdata.abs.gov.au/census_services/getproduct/census/2016/quickstat/5?opendocument
