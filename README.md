# Data-Viz-Iris-Dataset
We've to perform 1. List down the features and their types (e.g., numeric, nominal) available in the dataset. 2. Create a histogram for each feature in the dataset to illustrate the feature distributions.  3. Create a boxplot for each feature in the dataset.  4. Compare distributions and identify outliers. 

# Result and Output
Dataset Features:
Id                 int64
SepalLengthCm    float64
SepalWidthCm     float64
PetalLengthCm    float64
PetalWidthCm     float64
Species           object
dtype: object
Outliers (IQR Method):
Id: 0 outliers
Empty DataFrame
Columns: [Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species]
Index: []
SepalLengthCm: 0 outliers
Empty DataFrame
Columns: [Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species]
Index: []
SepalWidthCm: 4 outliers
    Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm          Species
15  16            5.7           4.4            1.5           0.4      Iris-setosa
32  33            5.2           4.1            1.5           0.1      Iris-setosa
33  34            5.5           4.2            1.4           0.2      Iris-setosa
60  61            5.0           2.0            3.5           1.0  Iris-versicolor
PetalLengthCm: 0 outliers
Empty DataFrame
Columns: [Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species]
Index: []
PetalWidthCm: 0 outliers
Empty DataFrame
Columns: [Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species]
Index: []
Outliers (Z-score Method):
    Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
15  16            5.7           4.4            1.5           0.4  Iris-setosa
