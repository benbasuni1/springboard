from sklearn import tree
from sklearn import metrics

# 0. Transfrom CSV to Pandas
data = pd.read_csv('GermanCredit.csv')
data.columns
data.describe()
data.head()

# 1. Build Training Set / Cross Validation
X = data.drop('RESULT', axis=1)
X.head()

y = data['RESULT']
y.head()

# 2. Train X, y with 70/30 split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .3, random_state = 3)

# 3. Set your Classifier and Fit Model
clf = tree.DecisionTreeClassifier()
clf.fit(X_train, y_train)

# 4. Apply trained classifier 
y_pred = clf.predict(X_test)

print(round(metrics.accuracy_score(y_test, y_pred), 2))
