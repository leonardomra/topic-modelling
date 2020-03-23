# topic-modelling

Small Flask API written in python used for Topic Modeling with Latent Dirichlet Allocation on a collection of documents.

The API offers two endpoints, namely:

* **`POST` /topics**
	**Data param:** `file: dataset.csv`
	**Example of success response:**
```javascript
[{"title": "Suggested Topic", "terms": ["cell", "epithelial", "type", "epithelium", "airway", "human", "tissue", "cf", "ifn", "expression"]}, {"title": "Suggested Topic", "terms": ["patient", "hospital", "study", "group", "icu", "care", "\u00b1", "result", "day", "ed"]},...]
```

---

* **`POST` /count**
	**Data param:** `file: dataset.csv`
	**Example of success response:** 
```javascript
{"count": {"analysis": 81773, "case": 83358, "include": 84623, "group": 85330, "human": 85863, "gene": 92091, ...}}
```

