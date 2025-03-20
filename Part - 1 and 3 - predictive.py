print("HARSHAN FINAL*")



import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

training_data=pd.read_csv("C:/Users/nithi/OneDrive/Desktop/scl/hypothyroid.csv",nrows=2500)
complete_data=pd.read_csv("C:/Users/nithi/OneDrive/Desktop/scl/hypothyroid.csv")

dependent_attr=training_data.iloc[0:2999, 2:15]

#print(training_data.columns)

independent_attr=training_data['binaryClass']

logr=LogisticRegression()
logr.fit(dependent_attr,independent_attr)

print("The Beta i's vals are:  ",logr.coef_)

betais=logr.coef_
betais=np.array(betais)
max_betais_index = np.argmax(betais)
colnames=list(dependent_attr.columns)
most_influfac=colnames[max_betais_index]

least_betais_index=np.argmin(betais)
least_influfac=colnames[least_betais_index]

print("------------------------------------------------------------------")

print("the maximum value of the Beta is: ",max(betais[0]))
print("Thus the factor influencing the most is: ",most_influfac)

print("------------------------------------------------------------------")
print("The factor that has most neglib;e or least impact is: ",min(betais[0]))
print("Thus the attribute is: ",least_influfac)

print("intercept of the model is: ",logr.intercept_)

#prediction using train split model
outcome=complete_data['binaryClass']
predictors=complete_data.iloc[:, 2:15]
 
xtrain, xtest, ytrain, ytest=train_test_split(predictors,outcome,train_size=0.8,random_state=42)
model=LogisticRegression()
model.fit(xtrain,ytrain)
y_preds=model.predict(xtest)
accuracy=accuracy_score(ytest,y_preds)
print("The predicted value is: ",y_preds)
print("The accuracy of the model is: ", accuracy*100,"%")

if(accuracy>90):
    print("the model can be used for prediction")
    
    
    
    
    
    
    
    
    
    
    
    
print("NITHIN FINAL*")

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns

#Confusion matrix
confusion_matrix = confusion_matrix(ytest, y_preds)
print(confusion_matrix)
plt.figure(figsize=(8, 6))
plt.title('Confusion Matrix')
sns.heatmap(confusion_matrix, annot=True, cmap='Blues', fmt='g')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.show()

# Classification report
print("\nClassification Report:")
print(classification_report(ytest, y_preds))


# Train logistic regression model
logr = LogisticRegression()
logr.fit(xtrain, ytrain)

# Predict probabilities
y_probs = logr.predict_proba(xtest)[:, 1]

# Convert target variable to binary format
ytest_binary = (ytest == 'P').astype(int)

# Compute ROC curve
fpr, tpr, thresholds = roc_curve(ytest_binary, y_probs)

# Compute AUC score
auc_score = auc(fpr, tpr)

# Plot ROC curve
import matplotlib.pyplot as plt

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (AUC = %0.2f)' % auc_score)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()

print("AUC Score:", auc_score)

# Get the absolute values of the logistic regression coefficients
coefficients_abs = np.abs(logr.coef_)[0]

# Create a DataFrame to store feature names and their corresponding coefficients
feature_coefficients = pd.DataFrame({
    'Feature': dependent_attr.columns,
    'Coefficient': coefficients_abs
})

# Sort the DataFrame by coefficient values in descending order
feature_coefficients = feature_coefficients.sort_values(by='Coefficient', ascending=False)

# Print the top 5 features with the highest coefficients
print("Top 5 Features Influencing Hypothyroidism or Hyperthyroidism:")
print(feature_coefficients.head(5))
