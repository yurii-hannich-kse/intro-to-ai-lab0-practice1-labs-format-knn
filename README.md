# Lab 0 - Labs format, KNN (guided)

In this repo that you will work with following file - `lab.ipynb`, it's your notebook that you will submit.

**! IMPROTANT !**

Follow these rules strictly

- Do not change the name of the notebook.
- Do not add any files to the repo, only modify `lab.ipynb` (Github Classroom will automatically grade only this file and send alert if other files were changed).
- Do not change the structure of the notebook (e.g., move cells, add new ones, delete existing ones) - it may break the autograder. You can only modify the content of the cells that are already there and where it is clearly stated (like 'YOUR CODE HERE').

---

## What you do in Lab 0

During L0(P1) we will:
- Open and run a Jupyter notebook.
- Implement 3 small functions (they are automatically graded):
  - `euclidean_distance(point1, point2)`
  - `classify_example(X_train, y_train, test_point, k=3)`
  - `predict(X_train, y_train, X_test, k=3)`
- Compare your implementation with `sklearn`.

**More detailed instructions for this specific lab are provided inside the notebook**

---

## Submission

1. Make sure all cells run (Kernel - Restart & Run All).
2. Commit and push **only** `lab.ipynb`.

---

## AI tools usage policy (mandatory)

AI tools can be highly beneficial in learning, especially when it comes to explaining complex concepts, answering follow-up questions, and providing examples; these applications are encouraged within this course. 

In programming assignments, AI can solve most lab tasks completely, which reduces learning; therefore, the rules below apply. 

### Prohibited (worsens learning)
- Submitting assignment materials (task descriptions, code snippets) to an AI.
- Requesting the full implementation of a specific function.

### Allowed (improves learning)
- Asking about the internal workings and main parameters of a library function/class you use. 
- Asking for **abstracted** examples on dummy data unrelated to the lab topic/dataset. 
- Asking for a step-by-step explanation of the algorithmic logic (no code). 
- Debugging help by sharing a traceback and asking where/why it happens, without requesting corrected code. 

### Allowed prompts (use only these)
**Prompt 1 - Understanding library components** 
> I am working with the [Library Name] library. Can you explain the internal logic and the main parameters of the [Function or Class Name]? Specifically, I want to understand what it does under the hood and what kind of data it expects as input and provides as the output. Do not write any code examples or pieces of solution.

**Prompt 2 - Requesting abstracted examples** 
> Can you provide a simple, abstracted code example of how to use [Function/Method Name]? Please use a dummy dataset like a small NumPy array or a basic list that is unrelated to Lab Topic, e.g., Iris dataset or Titanic data. I need to see the basic syntax for implementing this.

**Prompt 3 - Algorithmic logic explanation** 
> I need to implement the [Algorithm Name], e.g., KNN or Gradient Descent from scratch. Without providing any Python code, can you explain the step-by-step logic of how this algorithm processes data? Please use a first-principles approach to explain the mathematical or logical sequence.

**Prompt 4 - Debugging via traceback analysis** 
> I am getting an error in my code. I will provide the traceback error message below. Please analyze this error and explain where it is coming from and why it might be happening in the context of my logic. Important: Do not provide the corrected code - just help me understand the cause of the error so I can fix it myself.

### Required workflow (Gemini chat)
If you use any AI tool in a permitted manner, you must create a **separate chat per lab** (use Gemini as the default tool) and submit a link to that chat in Moodle together with your lab submission. 

Using AI tools in a prohibited manner is considered a violation of academic integrity. 

---

## Local environment setup (optional)

If you want to work locally (it's not required, you can use Google Colab), follow the instructions below:

### Option A: Conda (recommended)
1. Install Miniconda/Anaconda.
2. Create and activate an environment:

```bash
conda create -n intro-ai python=3.11 -y
conda activate intro-ai
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run Jupyter:

```bash
jupyter notebook lab.ipynb
```

### Option B: Python + venv
1. Install Python 3.11 from python.org.
2. Create and activate a virtual environment:

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Run tests locally
From the repo root:

```bash
pytest -q
```