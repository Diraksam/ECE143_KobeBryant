# ECE143: Data Analysis
##### Diraksa Munajat  
##### Hoanan Peng  
##### Guanqing Li  
##### Onur Tepençelik  


#### Overview:
- Build
- Data Cleaning
- Plotting and Analysis


## Build
Following dependencies are needed to run the code:
  - NumPy
  - Pandas
  - Matplotlib
  - Plotly
  - urllib

Additional dependencies that we used for data extraction and cleaning
  - BeautifulSoup
  
The main datasets is extracted from basketballreference.com using BeautifulSoup and directly downloaded from Kaggle.

After building all the dependencies, simply run main.py to obtain all the plots.
  
## Data Cleaning

The shot selection dataset from Kaggle requires just a bit of cleaning. The shots that contained missing information in the 
shot_made_flag column are omitted.

The basketball reference dataset did not require cleaning. Two new columns are added for seasons and seconds remaining until
end of quarter, for further analysis.

## Plotting and Analysis

Data is analyzed and visualized using various techniques. Visualizing the shot attempts on a basketball court is very effective
for analyzing shooting trends. Bar, pie, radar and line plots are used to analyze career statistics of Kobe Bryant.

