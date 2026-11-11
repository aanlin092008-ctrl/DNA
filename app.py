import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

st.set_page_config(
    page_title="DNA Classifier",
    page_icon="🧬",
    layout="centered"
)

# Dataset
data = {
    "Sequence": [
        "ATGCGATC",
        "ATGCGTAC",
        "GCGCGTAT",
        "GCGCGCGC"
    ],
    "Group": ["A", "A", "B", "B"]
}

df = pd.DataFrame(data)

# Feature extraction
def extract_features(seq):
    seq = seq.upper()

    if not seq or any(base not in "ATGC" for base in seq):
        raise ValueError("Enter a valid DNA sequence containing only A, T, G and C.")

    a = seq.count("A")
    t = seq.count("T")
    g = seq.count("G")
    c = seq.count("C")
    length = len(seq)
    gc = ((g + c) / length) * 100

    return [a, t, g, c, length, gc]

# Prepare training data
X = pd.DataFrame(
    [extract_features(s) for s in df["Sequence"]],
    columns=["A", "T", "G", "C", "Length", "GC"]
)
y = df["Group"]

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Website design
st.title("🧬 DNA Sequence Classifier")
st.write("### AI/ML Based Genomic Analysis")

st.info(
    "Enter a DNA sequence to extract numerical features "
    "and predict its group."
)

sequence = st.text_area(
    "Enter DNA Sequence",
    placeholder="Example: ATGCGCGATC",
    height=100
)

if st.button("Predict Group", type="primary"):

    try:
        if not sequence.strip():
            st.warning("Please enter a DNA sequence.")
        else:
            features = extract_features(sequence.strip())

            input_data = pd.DataFrame(
                [features],
                columns=["A", "T", "G", "C", "Length", "GC"]
            )

            prediction = model.predict(input_data)[0]

            st.success(f"Predicted Group: {prediction}")

            st.subheader("Extracted DNA Features")

            result = pd.DataFrame({
                "Feature": [
                    "A Count", "T Count", "G Count",
                    "C Count", "Sequence Length", "GC Content (%)"
                ],
                "Value": features
            })

            st.table(result)

            st.caption(
                "Prediction is based on a Decision Tree trained "
                "on only four labelled sequences. It is an "
                "educational demonstration, not a validated "
                "genomic diagnostic tool."
            )

    except ValueError as error:
        st.error(str(error))

st.divider()

st.subheader("About This Project")
st.write("""
This project demonstrates DNA sequence classification
using Python, Machine Learning and feature extraction.

Algorithm: Decision Tree Classifier

Libraries: Pandas, Scikit-learn and Streamlit.
""")

st.caption("Educational AI/ML Genomics Project")
