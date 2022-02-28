#%%
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import classification_report
import seaborn as sns
import matplotlib.pyplot as plt
#%%
y_true_multi = [0, 0, 0, 1, 1, 1, 2, 2, 2]
y_pred_multi = [0, 1, 1, 1, 1, 2, 2, 2, 2]

cm = confusion_matrix(y_true_multi, y_pred_multi)
print(cm)
sns.heatmap(cm)
plt.savefig('sklearn_confusion_matrix.png')
#%%
print(classification_report(y_true_multi, y_pred_multi))
