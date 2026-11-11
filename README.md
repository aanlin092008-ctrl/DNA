🧬 DNA Sequence Classification Using AI/ML

📌 Project Overview

This project demonstrates how Machine Learning can classify DNA sequences into two groups (Group A and Group B) using numerical features extracted from DNA sequences.

A Decision Tree Classifier is trained using labelled DNA data to predict the group of an unknown DNA sequence.

🎯 Objectives

- Convert DNA sequences into numerical features.
- Calculate A, T, G and C nucleotide counts.
- Calculate sequence length and GC content.
- Train a Machine Learning classification model.
- Predict the group of an unknown DNA sequence.

🛠️ Technologies Used

- Python
- Google Colab
- Pandas
- Scikit-learn
- Machine Learning

📊 Dataset

The dataset contains four labelled DNA sequences:

Sequence ID| DNA Sequence| Group
S1| ATGCGATC| A
S2| ATGCGTAC| A
S3| GCGCGTAT| B
S4| GCGCGCGC| B

🧪 Features Extracted

1. Adenine (A) count
2. Thymine (T) count
3. Guanine (G) count
4. Cytosine (C) count
5. Sequence Length
6. GC Content (%)

🤖 Machine Learning Model

Algorithm: Decision Tree Classifier

The model learns patterns from the labelled DNA sequences and predicts the group of an unknown sequence.

🔍 Prediction Result

Unknown DNA Sequence: "ATGCGCGATC"

Extracted Features:

- A = 2
- T = 2
- G = 3
- C = 3
- Length = 10
- GC Content = 60%

Predicted Group: Group A

📈 Model Performance

- Training Accuracy: 100%

Note: This is training accuracy calculated on the same four sequences used for training. It does not establish the model's accuracy on unseen DNA sequences.

🌍 Application in Genomics

Machine Learning can help researchers analyse DNA patterns and identify genetic variations associated with inherited diseases.

⚠️ Limitations

- Very small training dataset.
- Limited representation of DNA patterns.
- Predictions may not generalise to unseen sequences.
- Biological validation is necessary.

🏁 Conclusion

This project demonstrates the application of Machine Learning in genomic sequence classification using Python. It shows how DNA sequences can be converted into numerical features and classified using a Decision Tree model.

👩‍💻 Author

Anlin

B.Tech – Computer Science and Engineering

Project Domain: Artificial Intelligence, Machine Learning and Computational Genomics
