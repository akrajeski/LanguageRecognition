# German Language Recognition
This project is committed to helping those whose primary language is not German and are preparing to increase their fluency based on a CEFR (Common European Framework of Reference for Languages) scale. 
This project has multiple facets, and uses Machine Learning Techniques in order to interact with the user to determine their skill level.
Two notebooks are included in this. The first tracks different types of models as well as data visualization.
The second (2_finalized_alg) contains the code necessary to run the application.

# Limitations and Potential Future Improvements
The data is limited, and a lot of the CEFR is not verified through Goethe or other German resources. 
The data should be re-evaluated with additional weighting.
Some sentences that are basic (e.g. Hallo! Mein Name ist ___) can be found in all levels, therefore when tested gives an incorrect rating.
Vocabulary lists can be added in order to better predict the skill level.

A lot of this should be changed within the data collection itself.



### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
