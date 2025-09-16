# Exercício 2 - FreeCodeCamp - Python  
## Demographic Data Analyzer  

In this challenge you must analyze demographic data using **Pandas**.  
You are given a dataset of demographic data that was extracted from the **1994 Census database**.  

### Sample of the dataset:
# Demographic Data Analyzer — Sample Table

Below is the sample rendered as a GitHub-compatible Markdown table.

| id | age | workclass         | fnlwgt | education | education-num | marital-status      | occupation         | relationship  | race  | sex    | capital-gain | capital-loss | hours-per-week | native-country | salary |
|----|-----|-------------------|--------|-----------|---------------|---------------------|--------------------|---------------|-------|--------|--------------|--------------|----------------|----------------|--------|
| 0  | 39  | State-gov         | 77516  | Bachelors | 13            | Never-married       | Adm-clerical       | Not-in-family | White | Male   | 2174         | 0            | 40             | United-States  | <=50K  |
| 1  | 50  | Self-emp-not-inc  | 83311  | Bachelors | 13            | Married-civ-spouse  | Exec-managerial    | Husband       | White | Male   | 0            | 0            | 13             | United-States  | <=50K  |
| 2  | 38  | Private           | 215646 | HS-grad   | 9             | Divorced            | Handlers-cleaners  | Not-in-family | White | Male   | 0            | 0            | 40             | United-States  | <=50K  |
| 3  | 53  | Private           | 234721 | 11th      | 7             | Married-civ-spouse  | Handlers-cleaners  | Husband       | Black | Male   | 0            | 0            | 40             | United-States  | <=50K  |
| 4  | 28  | Private           | 338409 | Bachelors | 13            | Married-civ-spouse  | Prof-specialty     | Wife          | Black | Female | 0            | 0            | 40             | Cuba           | <=50K  |

---

### Tasks to complete using Pandas:

1. **Exercício 2.1** → How many people of each race are represented in this dataset?  
   - This should be a Pandas series with race names as the index labels. (`race` column)  

2. **Exercício 2.2** → What is the average age of men?  

3. **Exercício 2.3** → What is the percentage of people who have a **Bachelor's degree**?  

4. **Exercício 2.4** → What percentage of people with **advanced education** (Bachelors, Masters, or Doctorate) make more than 50K?  

5. **Exercício 2.5** → What percentage of people **without advanced education** make more than 50K?  

6. **Exercício 2.6** → What is the **minimum number of hours** a person works per week?  

7. **Exercício 2.7** → What percentage of the people who work the **minimum number of hours per week** have a salary of more than 50K?  

8. **Exercício 2.8** → What **country** has the highest percentage of people that earn **>50K** and what is that percentage?  

9. **Exercício 2.9** → Identify the **most popular occupation** for those who earn **>50K** in **India**.  

---

### Instructions:
- Use the starter code in the file **`demographic_data_analyzer.py`**.  
- Update the code so all variables set to `None` are replaced with the appropriate calculation or code.  
- Round all decimals to the nearest **tenth**.  
---

Link GitPod:  [https://gitpod.io#snapshot/2428d216-1fab-4861-a9b6-6dcdff79c24e](https://gitpod.io/new/#snapshot/3c414380-58d3-4396-a832-753bbcf0cdf3)
