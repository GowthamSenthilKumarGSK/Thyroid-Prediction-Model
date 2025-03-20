import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

data2 = pd.read_csv("predictive_final_dataset.csv")
data2.replace('?', float('nan'), inplace=True)

st.set_page_config(page_title="thyroid", page_icon=":white_check_mark:", layout="wide")
st.title(" :white_check_mark: THYROID PREDICTION")
st.subheader("The most common thyroid disorder is hypothyroidism. Hypo- means deficient or under(active), so hypothyroidism is a condition in which the thyroid gland is underperforming or producing too little thyroid hormone.. Recognizing the symptoms of hypothyroidism is extremely important")
st.subheader("")
st.markdown("<h3 style='color:yellow;font-size:16px;'>sex - sex patient identifies (str)</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>age - age of the patient (int)</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>on_thyroxine - whether patient is on thyroxine (bool)</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>query on thyroxine - *whether patient is on thyroxine (bool)</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>on antithyroid meds - whether patient is on antithyroid meds (bool)", unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>sick - whether patient is sick (bool)", unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>pregnant - whether patient is pregnant (bool)", unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>thyroid_surgery - whether patient has undergone thyroid surgery (bool)", unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>I131_treatment - whether patient is undergoing I131 treatment (bool)", unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>query_hypothyroid - whether patient believes they have hypothyroid (bool)", unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>query_hyperthyroid - whether patient believes they have hyperthyroid (bool)", unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>lithium - whether patient * lithium (bool)", unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>goitre - whether patient has goitre (bool)", unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>tumor - whether patient has tumor (bool)", unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>hypopituitary - whether patient * hyperpituitary gland (float)",unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>psych - whether patient * psych (bool)",unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>TSH_measured - whether TSH was measured in the blood (bool)",unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>TSH - TSH level in blood from lab work (float)",unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>T3_measured - whether T3 was measured in the blood (bool)",unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>T3 - T3 level in blood from lab work (float)",unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>TT4_measured - whether TT4 was measured in the blood (bool)",unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>TT4 - TT4 level in blood from lab work (float)",unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>T4U_measured - whether T4U was measured in the blood (bool)",unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>T4U - T4U level in blood from lab work (float)",unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>FTI_measured - whether FTI was measured in the blood (bool)",unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>FTI - FTI level in blood from lab work (float)",unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>TBG_measured - whether TBG was measured in the blood (bool)",unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>TBG - TBG level in blood from lab work (float)",unsafe_allow_html=True)
st.markdown("<h3 style='color:yellow;font-size:16px;'>referral_source - (str)",unsafe_allow_html=True)
st.subheader("")
st.sidebar.header('Input Your Health Metrics')

age = st.sidebar.slider('Age', min_value=0, max_value=120, value=50)

# Use radio button for selecting gender
sex = st.sidebar.radio("Sex", ["Male", "Female"])

yes_no_variables = ['query on thyroxine', 'on antithyroid medication', 'sick', 'pregnant', 'thyroid surgery', 'I131 treatment', 'query hypothyroid', 'query hyperthyroid', 'lithium', 'goitre', 'tumor', 'hypopituitary', 'psych']
input_values = {}
for var in yes_no_variables:
     input_values[var] = st.sidebar.checkbox(f'{var} (Yes/No)')

for var, value in input_values.items():
     input_values[var] = 1 if value else 0

################################################# BAR  CHART #######################################################################


# Load the dataset
data2 = pd.read_csv("predictive_final_dataset.csv")

# Define the binary feature variables
yes_no_variables = ['query on thyroxine', 'on antithyroid medication', 'sick', 'pregnant',
                    'thyroid surgery', 'I131 treatment', 'query hypothyroid', 'query hyperthyroid',
                    'lithium', 'goitre', 'tumor', 'hypopituitary', 'psych']

# Initialize input values
input_values = {}

# Collect user input for each feature variable
for var in yes_no_variables:
    # Generate a unique key for each checkbox
    checkbox_key = f'{var}_checkbox'
    input_values[var] = st.sidebar.checkbox(f'{var} (Yes/No)', key=checkbox_key)

# Filter the data based on selected input values
filtered_data = data2.copy()

for var, value in input_values.items():
    filtered_data = filtered_data[filtered_data[var] == value]

# Create a bar plot using Plotly Express
st.markdown("<h3 style='color:green;font-size:32px;'>Distribution of people having thyroid by Sex (1 is male 0 is female)</h3>", unsafe_allow_html=True)

fig = px.bar(filtered_data, x='sex', y='on thyroxine', color='sex')
st.plotly_chart(fig)

st.subheader("")


######################################################### PLOT ON THE BASIS OG AGE AND SEX ################################################################


# # Print selected age and sex
# st.write("Selected Age:", age)
# st.write("Selected Sex:", sex)

# # Filter data based on age and sex
# filtered_data = data2[(data2['age'] == age) & (data2['sex'] == sex)]

# # Count males and females
# gender_counts = filtered_data['sex'].value_counts()

# # Plot pie chart if there are any records
# if not gender_counts.empty:
#     # Create a pie chart using Plotly Express
#     fig = px.pie(names=gender_counts.index, values=gender_counts.values, title=f'Count of Male and Female at Age {age} ({sex})')
#     st.plotly_chart(fig)
# else:
#     st.write("No data available for the selected age and sex.")

# # Plot bar chart if there are any records
# if not filtered_data.empty:
#     # Create a bar chart using Plotly Express
#     fig = px.bar(x=gender_counts.index, y=gender_counts.values, color=gender_counts.index,
#                  labels={'x': 'Sex', 'y': 'Count'}, title=f'Count of Male and Female at Age {age} ({sex})')
#     st.plotly_chart(fig)
# else:
#     st.write("No data available for the selected age and sex.")


# st.subheader("")


########################################################## CORRELATION PLOT ##################################################################


st.markdown("<hr/>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>OVERALL ANALYSIS</h2>", unsafe_allow_html=True)
target_variable = 'on thyroxine'

numeric_columns = data2.select_dtypes(include=['int', 'float']).columns

# Calculate correlations
correlations = data2[numeric_columns].corr()[target_variable].drop(target_variable)

# Visualize correlations using a bar plot
st.subheader('Correlation with the people who are taking Thyroxine')
colors = sns.color_palette("coolwarm", len(correlations))
fig, ax = plt.subplots(figsize=(9, 8))
sns.barplot(x=correlations.values, y=correlations.index, ax=ax, palette=colors)
plt.xlabel("Correlation")
plt.ylabel("Predictor Variable")
plt.title(f"Correlation with Target Variable: {target_variable}")
st.pyplot(fig)



############################################################### HAVING ON THYROXINE ################################################################


# Load the dataset
data2 = pd.read_csv("predictive_final_dataset.csv")

# Filter data for 'on thyroxine' as 1
positive_df = data2[data2['on thyroxine'] == 1]

# Count male, female, and '?' values
gender_counts = positive_df['sex'].value_counts(dropna=False)
question_mark_count = positive_df['sex'].eq('?').sum()

# Define colors for male, female, and '?'
colors = ['skyblue', 'lightcoral', 'lightgreen']

# Create a horizontal bar plot
fig, ax = plt.subplots(figsize=(8, 4))  # Adjust figsize as needed
bar_width = 0.3

# Plot bars for male and female
ax.barh(y=[0], width=[gender_counts.get(0, 0)], color=colors[1], label='Female', height=bar_width)
ax.barh(y=[bar_width], width=[gender_counts.get(1, 0)], color=colors[0], label='Male', height=bar_width)

# Plot bar for '?'
ax.barh(y=[2 * bar_width], width=[question_mark_count], color=colors[2], label='?', height=bar_width)

# Set labels and title
ax.set_xlabel('Count')
ax.set_yticks([0, bar_width, 2 * bar_width])
ax.set_yticklabels(['Female', 'Male', '?'])
ax.set_title('Gender Distribution among Patients on Thyroxine')

# Add legend
ax.legend()

# Remove grid lines
ax.grid(False)

# Show plot
st.pyplot(fig)

# Display count of male, female, and '?' values
st.write("Male:", gender_counts.get(1, 0))
st.write("Female:", gender_counts.get(0, 0))
st.write("?:", question_mark_count)


###################################################### NOT HAVING ON THYROXINE ################################################################


# Load the dataset
data2 = pd.read_csv("predictive_final_dataset.csv")

# Filter data for 'on thyroxine' as 0 (not taking thyroxine)
negative_df = data2[data2['on thyroxine'] == 0]

# Count male, female, and '?' values
gender_counts = negative_df['sex'].value_counts(dropna=False)
question_mark_count = negative_df['sex'].eq('?').sum()

# Define colors for male, female, and '?'
colors = ['skyblue', 'lightcoral', 'lightgreen']

# Create a horizontal bar plot
fig, ax = plt.subplots(figsize=(8, 4))  # Adjust figsize as needed
bar_width = 0.3

# Plot bars for male and female
ax.barh(y=[0], width=[gender_counts.get(0, 0)], color=colors[1], label='Female', height=bar_width)
ax.barh(y=[bar_width], width=[gender_counts.get(1, 0)], color=colors[0], label='Male', height=bar_width)

# Plot bar for '?'
ax.barh(y=[2 * bar_width], width=[question_mark_count], color=colors[2], label='?', height=bar_width)

# Set labels and title
ax.set_xlabel('Count')
ax.set_yticks([0, bar_width, 2 * bar_width])
ax.set_yticklabels(['Female', 'Male', '?'])
ax.set_title('Gender Distribution among Patients NOT on Thyroxine')

# Add legend
ax.legend()

# Remove grid lines
ax.grid(False)

# Show plot
st.pyplot(fig)

# Display count of male, female, and '?' values
st.write("Male:", gender_counts.get(1, 0))
st.write("Female:", gender_counts.get(0, 0))
st.write("?:", question_mark_count)


st.subheader("")


 ################################################# BOX PLOT #########################################################

st.markdown("<h3 style='color:green;font-size:32px;'>Box plot analysis</h3>", unsafe_allow_html=True)
numerical_features = ['TSH', 'T3', 'TT4', 'T4U', 'F1I', 'TBG']

# # Filter data and drop rows with missing values
data_filtered = data2.dropna(subset=numerical_features)


# # Define styling parameters for box plots
boxplot_style = {
    'boxprops': dict(color='blue'),  # Box color
    'whiskerprops': dict(color='blue'),  # Whisker color
    'capprops': dict(color='blue'),  # Cap color
    'flierprops': dict(marker='o', markerfacecolor='red', markersize=8),  # Outlier style
    'medianprops': dict(color='orange', linewidth=2)  # Median line style
}

# Create subplots
fig, axes = plt.subplots(3, 2, figsize=(14, 16))

# Plot box plots for each numerical feature
for ax, num_feature in zip(axes.flatten(), numerical_features):
    sns.boxplot(x='on thyroxine', y=num_feature, data=data_filtered, ax=ax, **boxplot_style)
    ax.set_title(f'Distribution of {num_feature} by Thyroxine Medication Status')
    ax.set_xlabel('Thyroxine Medication Status')
    ax.set_ylabel(num_feature)
    ax.grid(True)  # Add gridlines for better visualization

# Adjust layout
plt.tight_layout()

# Display the plot
st.pyplot(fig)

# Perform analysis and generate descriptive text
analysis_text = """
### Analysis of Numerical Features by Thyroxine Medication Status:
Box Color (Blue): The box represents the interquartile range (IQR) of the data distribution. It extends from the lower to the upper quartile values, with the median marked by the orange line inside the box.

Whisker Color (Blue): The whiskers extend from the box to the minimum and maximum values within a certain range (usually 1.5 times the IQR). Outliers beyond this range are plotted individually as red circles.

Outlier Symbol (Red Circles): Outliers are data points that fall significantly outside the rest of the data. They are marked by red circles in the plot.

Median Line (Orange): The median line inside the box represents the median value of the data distribution.


The box plots above illustrate the distribution of numerical features among individuals based on their Thyroxine Medication Status. Here are some key observations:

- *TSH (Thyroid-Stimulating Hormone):*
  - The median TSH level appears to be higher in individuals not on thyroxine medication compared to those on medication.
  - There is a wider interquartile range (IQR) for TSH levels among individuals not on medication, indicating greater variability.

- *T3 (Triiodothyronine):*
  - The distribution of T3 levels seems to be slightly higher in individuals on thyroxine medication, with fewer outliers compared to those not on medication.
  - The median T3 level appears to be relatively consistent across both groups.

- *TT4 (Total Thyroxine):*
  - Individuals on thyroxine medication exhibit a narrower range of TT4 levels compared to those not on medication.
  - The median TT4 level is relatively higher in individuals on medication.

- *T4U (Thyroxine Utilization):*
  - T4U levels appear to be distributed similarly among individuals regardless of thyroxine medication status, with moderate variability in both groups.
  - There is no significant difference in median T4U levels between the two groups.

- *FTI (Free Thyroxine Index):*
  - The distribution of FTI levels shows a similar pattern to TT4 levels, with individuals on medication having a narrower range and higher median FTI levels compared to those not on medication.

- *TBG (Thyroxine-Binding Globulin):*
  - TBG levels exhibit a wide range of values, with a noticeable number of outliers in both groups.
  - There is no apparent difference in the distribution of TBG levels between individuals on and off thyroxine medication.

Overall, these box plots provide insights into the distribution and variability of various thyroid-related biomarkers among individuals with different Thyroxine Medication Status.
"""

# Print descriptive text
st.markdown(analysis_text, unsafe_allow_html=True)

st.subheader("")


################################################ PIE CHART ####################################################










import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.markdown("<h3 style='color:green;font-size:32px;'>pie chart shows the percentage distribution of different categories within a specific feature variable</h3>", unsafe_allow_html=True)
# Load the dataset
data2 = pd.read_csv("predictive_final_dataset.csv")

# Define the binary feature variables
feature_variables = ['query on thyroxine', 'on antithyroid medication', 'sick', 'pregnant',
                     'thyroid surgery', 'I131 treatment', 'query hypothyroid', 'query hyperthyroid',
                     'lithium', 'goitre', 'tumor', 'hypopituitary', 'psych', 'TSH measured',
                     'T3 measured', 'TT4 measured', 'T4U measured', 'F1I measured', 'TBG measured']

# Initialize colors for the pie chart
colors = ['skyblue', 'lightcoral']

# Calculate the number of rows and columns for the subplots grid
num_rows = 5  # Number of rows for the grid
num_cols = 4  # Number of columns for the grid
total_plots = num_rows * num_cols

# Create subplots
fig, axes = plt.subplots(num_rows, num_cols, figsize=(16, 20))

# Flatten the axes array for easy iteration
axes = axes.flatten()

# Create pie charts for each feature variable
for i, feature_variable in enumerate(feature_variables):
    if i < total_plots:  # Make sure we only create as many plots as the grid can accommodate
        # Calculate counts for each category of the feature variable
        counts = data2[feature_variable].value_counts()

        # Create a pie chart
        ax = axes[i]
        ax.pie(counts, labels=counts.index, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.set_title(f'Distribution of {feature_variable}')
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Add a title to the entire grid
plt.suptitle('Distribution of Binary Feature Variables')

# Adjust layout
plt.tight_layout()

# Display the plot
st.pyplot(fig)

# Summary
st.write("### Summary:")
st.write("The pie charts above represent the distribution of binary feature variables in the dataset.")
st.write("Each pie chart shows the percentage distribution of different categories within a specific feature variable.")
st.write("These visualizations provide insights into the prevalence or occurrence of various binary conditions or attributes in the dataset.")
st.write(f"Of particular interest is the distribution of the target variable 'on thyroxine', which indicates whether a patient is taking thyroxine medication. Understanding the distribution of this variable is crucial for predictive modeling and assessing the prevalence of thyroid disorders.")

#################################3