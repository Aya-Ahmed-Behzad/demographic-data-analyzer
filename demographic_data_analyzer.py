import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    
    df= pd.read_csv('adult.data.csv')
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    
    race_count = df['race'].value_counts()
    # What is the average age of men?
 
    average_age_men = (df.loc[df['sex'] == 'Male'].age.mean()).round(1)
    # What is the percentage of people who have a Bachelor's degree?
    
    b= df['education'].value_counts().Bachelors
    t= df['education'].shape[0]

    percentage_bachelors = (b*100/t).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    edu= df.loc[(df['education'] =='Bachelors') | 
        (df['education'] =='Masters')|(df['education'] =='Doctorate')]
    z= edu.shape[0]

    
    higher_education = round((z*100/t),1)
    lower_education = round(((t-z)*100/t),1)

    # total num with salary >50K
    total_rich= df.loc[df['salary']  == ">50K"].shape[0]
    higher_rich= edu.loc[edu['salary'] == ">50K"].shape[0]

    # percentage with salary >50K
    higher_education_rich =round((edu.loc[edu['salary'] == ">50K"].shape[0])*100/z,1)
    lower_education_rich = round((total_rich- higher_rich)*100/(t-z),1)

    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = int(df['hours-per-week'].min())
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week']== min_work_hours].shape[0]

    rich_percentage = round(((df.loc[(df['hours-per-week']== min_work_hours) & (df['salary']== ">50K")].shape[0])*100/num_min_workers),1)


    # What country has the highest percentage of people that earn >50K?
    rich= df.loc[df['salary']  == ">50K"]
    countries= df['native-country'].value_counts()
    rdict={}
    series=pd.Series(rdict)
    for country in countries.index:
        r=rich.loc[rich['native-country']== country].shape[0]
        t=df.loc[df['native-country']== country].shape[0]
        z=r*100/t
        series[country]= round(z,1)


    sort= series.sort_values(ascending = False)
    highest_earning_country = sort.index[0]
    highest_earning_country_percentage = sort.iloc[0]

    # Identify the most popular occupation for those who earn >50K in India.
    occ= df.loc[(df['salary']  == ">50K")&(df['native-country']=='India'),'occupation'].value_counts()
    top_IN_occupation = occ.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
