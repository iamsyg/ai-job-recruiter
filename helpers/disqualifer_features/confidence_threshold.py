# helpers/disqualifer_features/confidence_threshold.py

import json
import numpy as np

disqualifier_features = np.load(
    "disqualifier_features.npy",
    allow_pickle=True
).item()

for key in [
    "research_similarity",
    "architecture_similarity",
    "langchain_similarity",
    "cv_similarity",
    "nlp_ir_similarity",
]:
    vals = [v[key] for v in disqualifier_features.values()]
    print(key)
    print("Min :", np.min(vals))
    print("P5  :", np.percentile(vals, 5))
    print("P95 :", np.percentile(vals, 95))
    print("Max :", np.max(vals))




# research_similarity
# Min : 0.43759244680404663
# P5  : 0.47337751984596255
# P95 : 0.5539507359266281
# Max : 0.6126257181167603
# architecture_similarity
# Min : 0.4911796748638153
# P5  : 0.5391351312398911
# P95 : 0.6122543275356293
# Max : 0.6522185802459717
# langchain_similarity
# Min : 0.4969918131828308
# P5  : 0.5437565296888351
# P95 : 0.638384586572647
# Max : 0.7072199583053589
# cv_similarity
# Min : 0.4945252537727356
# P5  : 0.5439201176166535
# P95 : 0.6275948256254196
# Max : 0.7657414674758911
# nlp_ir_similarity
# Min : 0.4320640563964844
# P5  : 0.473568956553936
# P95 : 0.5833257764577865
# Max : 0.723796010017395