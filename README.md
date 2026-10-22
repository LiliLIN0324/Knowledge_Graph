# Knowledge Graph from Urban Policy Text · Method Comparison

Six relation-extraction pipelines, compared on the same corpora, as a step toward building a concept knowledge graph from urban-resilience policy documents (OneNYC 2050 and a Shanghai policy corpus).

**Question**: when the goal is a usable concept graph rather than a benchmark score, which extraction method gives the most coherent structure per unit of effort?

---

## Methods

| # | Notebook family | Approach | Strength | Weakness |
|---|---|---|---|---|
| 1 | `Method1_frequency*` | Term co-occurrence counts over a fixed 10-node vocabulary | Fast, fully interpretable | Blind to direction and context |
| 2 | `Method2_TF-IDF*` | TF-IDF weighting + fixed keyword nodes | Downweights corpus-wide filler | Still needs a seed vocabulary |
| 3 | `Method3_LDA_Cooccurance*` | LDA topics, then co-occurrence within topics | Finds unseeded themes | Topic count is a judgement call |
| 4 | `Method4_direct gpt*` | Direct LLM prompting for triples | Handles paraphrase and direction | Cost, variance, needs verification |
| 5 | `Method5_BerTopic*` | BERTopic with embedding clusters | Strong topic separation | Cluster labels need human naming |
| 6 | `Method6_Embedded_model_*` | Sentence-embedding similarity (bge / e5 / Qwen / Gemini / Cohere) | Multilingual, model-swappable | Similarity ≠ relation |

Every method has a `_SH` (Shanghai) counterpart, so the two corpora can be compared within the same pipeline.

Supporting notebooks: `Bert.ipynb` (fine-tuning setup), `M5/Method5_BerTopic_fine_tuning*.ipynb`, `b_SOM_kmeans_process.ipynb` (clustering borrowed from the urban-heat study — not part of the KG comparison).

## Data — not included

The corpora are **not** committed (`*.csv`, `*.json`, `*.npy`, `*.pkl` are ignored). Notebooks read them from an absolute local path such as `C:\Users\owner\Desktop\KG\OneNYC_2050_Strategic_Plan_final.txt`. To reproduce, supply the policy text and update that path in each notebook.

## Environment

Python 3 + Jupyter: `nltk`, `gensim`, `scikit-learn`, `bertopic`, `sentence-transformers`, `transformers`, `torch`, `pandas`, `matplotlib`. No `requirements.txt` is included; pin versions from the notebook imports.

## Notes

- The default branch is `cleanup`.
- `bert-base-*-finetuned-imdb*/` directories are Hugging Face Trainer output folders; only TensorBoard logs are committed and the `imdb` in the name is a leftover of the training script's default, not the dataset used.
- Files named `0.26.0'` and `2.7.0` are accidental pip output, not data.
- There is no ground-truth triple set, so this repository compares methods qualitatively; treat the tables as exploratory.

## License

Not declared.
