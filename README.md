# Animal Activity Analyzer  
**Course:** The Mind of Animals: Possibility of Coexistence with Humans (RGC-2103-01)

A simple project that processes acceleration sensor data and classifies animal behavior.  
Data was handled in Kaggle, and an LLM (Gemini) in Google Colab was used to generate a short explanation.

## Steps
1. Load and clean sensor data (Kaggle).
2. Compute acceleration magnitude and cluster behavior (K-Means).
3. Summarize activity by minute.
4. Send the summary to Gemini for an AI-generated explanation.

## Tools
- Kaggle (Pandas, scikit-learn)
- Google Colab (Gemini API)

## Dataset
Kaggle: [https://www.kaggle.com/datasets/animal-behavior-prediction](https://www.kaggle.com/datasets/obulikarthikeyan/animal-behavior-prediction)
