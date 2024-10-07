# COADpred: A Tool for Identification of Colon Adenocarcinoma using Machine Learning.
Colon adenocarcinoma is a type of cancer that starts in the glandular cells lining the colon. Biomarkers are crucial to identify, as they help in early diagnosis, predicting prognosis, and guiding personalized treatment, improving patient outcomes and survival rates. Biomarkers are pivotal in this regard, providing noninvasive means for early detection, facilitating prompt treatment initiation, and potentially boosting survival rates. Hence, the recognition and validation of biomarkers are of primary importance in effectively addressing colon adenocarcinoma cancer.


## Introduction

COADPred is an innovative solution designed for identifying colon adenocarcinoma (COAD) through transcriptomic profiling. By leveraging advanced machine learning algorithms, this cutting-edge technology analyzes tissue biomarkers to provide a highly accurate prognosis of colon cancer.

Moreover, the integration of machine learning allows for continuous improvement of the predictive model’s accuracy as more data is gathered, enhancing its reliability and effectiveness. COADPred represents a significant breakthrough in early detection of colon cancer, potentially leading to earlier interventions and improved patient outcomes.

To further strengthen our approach, we selected 54 features using a range of Feature Selection Methods. These include the Fast Correlation-Based Filter Method (FCBF), Spike and Slab ("spikeslab"), Univariate statistical tests (F-test), and wrapper methods like Boruta and Recursive Feature Elimination (RFE). Additionally, we employed embedded methods such as XGBoost, SVC linear with the SelectFromModel class from scikit-learn, Random Forest, Extra Trees with Feature Importance, and LASSO (a regularization-based embedded method). By combining Filter, Wrapper, and Embedded feature selection techniques, we used an ensemble approach to identify features present in at least five methods. These 54 features show potential as biomarkers for classifying and predicting normal versus cancerous patients.



Installation and Usage:

You can install the package using the following command:


    git clone https://github.com/GITractCancer/COADPred.git
    cd COAD



### Predict using COADPred

    import pandas as pd
    from COADPred import predict

    df = pd.read_csv("path/to/your/data.csv")

    predict(df, model_type='svc')

    
Specify the model type you want to use Models


## Models

The following classifiers are supported:

    svc
    rf
    ab
    xgb
    dt
    et
    lr
    gnb
    knn
    mlp
