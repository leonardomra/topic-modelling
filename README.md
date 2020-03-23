# topic-modelling

Small Flask API written in python used for Topic Modeling with Latent Dirichlet Allocation on a collection of documents.

The API offers two endpoints, namely:

* **`POST` /topics**
* **Data param:** `file: dataset.csv`
* **Example of success response:**
```javascript
[{"title": "Suggested Topic", "terms": ["cell", "epithelial", "type", "epithelium", "airway", "human", "tissue", "cf", "ifn", "expression"]}, {"title": "Suggested Topic", "terms": ["patient", "hospital", "study", "group", "icu", "care", "\u00b1", "result", "day", "ed"]},...]
```

---

* **`POST` /count**
* **Data param:** `file: dataset.csv`
* **Example of success response:** 
```javascript
{"count": {"analysis": 81773, "case": 83358, "include": 84623, "group": 85330, "human": 85863, "gene": 92091, ...}}
```

---

The dataset can be either generated or acquired here [GitHub](https://www.kaggle.com/xhlulu/cord-19-eda-parse-json-and-generate-clean-csv). The link also provides the necessary documentation on the format and structure of the dataset.
This API is based on this [notebook](https://www.kaggle.com/danielwolffram/topic-modeling-finding-related-articles).
For more information on Topic Modelling with Latent Dirichlet Allocation, check this [article](https://towardsdatascience.com/topic-modeling-and-latent-dirichlet-allocation-in-python-9bf156893c24)!
