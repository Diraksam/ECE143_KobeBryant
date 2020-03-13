# ECE143: Analyzing Career Statistics and Shooting Trends of Kobe Bryant 
#### Group 12:
  Diraksa Munajat  
  Hoanan Peng  
  Guanqing Li  
  Onur Tepençelik  

#### Overview:
- Build
- Data Cleaning
- Plotting and Analysis


## Build
Following dependencies are needed to run the code:
  - NumPy
  - Pandas
  - Matplotlib
  - Plotly (4.5.4)
  - urllib
  #### - Dependencies can be build with the following command/s:
    - pip install -name-
    Example:
    - pip install plotly==4.5.4

Additional dependencies that we used for data extraction and cleaning
  - BeautifulSoup
  
The main datasets are extracted from basketballreference.com using BeautifulSoup and directly downloaded from Kaggle.

After building all the dependencies, simply run main.py in the Jupyter notebook to get the following output described and shown in the Kobe notebook.
  
## Data Cleaning

The shot selection dataset from Kaggle requires just a bit of cleaning. The shots that contained missing information in the 
shot_made_flag column are omitted.

The basketball reference dataset did not require cleaning. Two new columns are added for seasons and seconds remaining until
end of quarter, for further analysis.

## Plotting and Analysis

Data is analyzed and visualized using various techniques. Visualizing the shot attempts on a basketball court is very effective
for analyzing shooting trends. Bar, pie, radar and line plots are used to analyze career statistics of Kobe Bryant.

