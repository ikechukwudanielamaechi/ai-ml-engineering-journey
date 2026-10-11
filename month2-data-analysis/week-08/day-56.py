#27th September 2026


"""🐍 Python Practice
Continue using only the Pandas/NumPy/Python concepts you’ve already learned.
Use the same dataset from yesterday:
import pandas as pd

data = {
    "video_id": ["V001", "V002", "V003", "V004", "V005", "V006"],
    "signer_id": ["S01", "S02", "S01", "S03", "S02", "S01"],
    "sign": ["HELLO", "HELP", "HELLO", "YES", "HELP", "NO"],
    "environment": ["indoor", "outdoor", "outdoor", "indoor", "indoor", "outdoor"],
    "quality": ["good", "good", "poor", "good", "poor", "good"]
}

df = pd.DataFrame(data)
Task 1 — Column selection
Create:
sign_data
containing only:
sign
quality

Task 2 — Multiple filtering
Create:
outdoor_hello
containing only videos that are:
HELLO AND outdoor
Then create:
hello_or_help
containing videos that are:
HELLO OR HELP

Task 3 — Grouped analysis
Calculate:
videos per sign
videos per signer
videos per sign + signer
The third one should use:
groupby(["sign", "signer_id"])

Task 4 — Investigate
Using your results, answer:
Which signer contributed the most videos to the dataset?
and:
Which sign has the most videos?
Then answer:
Does the dataset appear balanced across signs?
Be careful: “not perfectly balanced” and “unusable” are not the same conclusion.

Task 5 — Assertions
Write at least 3 assertions testing properties you can actually establish from this dataset.
Don’t use assertions just to satisfy the requirement.
Each should test something meaningful."""


#PYTHON ANSWER 


#Task 1
sign_data = df[["sign", "quality"]]

#Task 2
outdoor_hello =df[(df["sign"] == "HELLO") & (df["environment"] == "outdoor")]
hello_or_help= df[(df["sign"] == "HELLO") | (df["sign"] == "HELP")]

#Task 3
videos_per_sign = df["sign"].value_counts()
videos_per_signer = df["signer_id"].value_counts()
videos_per_sign_signer = df.groupby(["sign", "signer_id"]).size()


#Task 4
#Which signer contributed the most videos?
#S01 contributed the most videos (3 videos total: 2 ⁠HELLO⁠ and 1 ⁠NO⁠).
                                 
#Which sign has the most videos?
# ⁠HELLO⁠ and ⁠HELP⁠ are tied for the most videos (2 videos each).
 # Does the dataset appear balanced across signs?
 #No, it is slightly imbalanced, but usable. ⁠HELLO⁠ and ⁠HELP⁠ have 2 samples each, while ⁠YES⁠ and ⁠NO⁠ have 1 sample each. While not perfectly uniform, the imbalance is minor rather than catastrophic. However, because the total dataset is so small (6 samples total), it needs more data overall before drawing reliable conclusions.


#Task 5
# 1. Verify total count integrity (no rows dropped during analysis)
assert videos_per_signer.sum() == len(df), "Total videos per signer does not equal total rows"
# 2. Verify that S01 is indeed the top contributing signer
assert videos_per_signer.idxmax() == "S01", "Signer S01 should be the top contributor"
# 3. Verify that every unique sign has at least 1 video recorded
assert (videos_per_sign >= 1).all(), "Every sign class must have at least one sample"


