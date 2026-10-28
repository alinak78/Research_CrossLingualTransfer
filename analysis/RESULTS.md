# Recomputed pilot audit

Unit: 60 authored scenarios, reused across conditions. Invalid outputs count as errors.
Intervals are descriptive Wilson intervals over these scenarios, not population guarantees.
Exact paired McNemar tests; Holm correction across all 18 selected contrasts. Exploratory, not preregistered.

| Model | A | H | G | E_sparse | E_full | F | D_sparse | D_full |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| llama3 | 37/60 | 28/60 | 10/60 | 31/60 | 36/60 | 15/60 | 16/60 | 14/60 |
| hex1 | 52/60 | 25/60 | 10/60 | 27/60 | 36/60 | 23/60 | 25/60 | 28/60 |
| sarvam | 55/60 | 29/60 | 20/60 | 28/60 | 40/60 | 32/60 | 33/60 | 36/60 |

A: English + RAG; H/G: Kannada/romanized unprimed without RAG; E: Kannada primed without RAG; F: Kannada unprimed + RAG; D: Kannada primed + RAG.

| Model | A vs B | Contrast | Delta pp | A only correct | B only correct | Label flips | Exact p | Holm p |
|---|---|---|---:|---:|---:|---:|---:|---:|
| hex1 | H vs G | script_unprimed | +25.0 | 21 | 6 | 50 | 0.00592 | 0.05925 |
| hex1 | E_sparse vs M_sparse | script_sparse | +26.7 | 20 | 4 | 46 | 0.00154 | 0.01853 |
| hex1 | E_full vs M_full | script_full | +35.0 | 25 | 4 | 43 | 0.00010 | 0.00166 |
| hex1 | F vs H | retrieval_unprimed | -3.3 | 5 | 7 | 32 | 0.77441 | 1.00000 |
| hex1 | D_sparse vs E_sparse | retrieval_sparse | -3.3 | 6 | 8 | 30 | 0.79053 | 1.00000 |
| hex1 | D_full vs E_full | retrieval_full | -13.3 | 2 | 10 | 22 | 0.03857 | 0.30859 |
| llama3 | H vs G | script_unprimed | +30.0 | 23 | 5 | 47 | 0.00091 | 0.01283 |
| llama3 | E_sparse vs M_sparse | script_sparse | +38.3 | 24 | 1 | 43 | 0.00000 | 0.00003 |
| llama3 | E_full vs M_full | script_full | +28.3 | 21 | 4 | 39 | 0.00091 | 0.01283 |
| llama3 | F vs H | retrieval_unprimed | -21.7 | 5 | 18 | 40 | 0.01062 | 0.09560 |
| llama3 | D_sparse vs E_sparse | retrieval_sparse | -25.0 | 5 | 20 | 40 | 0.00408 | 0.04485 |
| llama3 | D_full vs E_full | retrieval_full | -36.7 | 4 | 26 | 43 | 0.00006 | 0.00101 |
| sarvam | H vs G | script_unprimed | +15.0 | 16 | 7 | 37 | 0.09314 | 0.55884 |
| sarvam | E_sparse vs M_sparse | script_sparse | +16.7 | 15 | 5 | 38 | 0.04139 | 0.30859 |
| sarvam | E_full vs M_full | script_full | +26.7 | 19 | 3 | 35 | 0.00086 | 0.01283 |
| sarvam | F vs H | retrieval_unprimed | +5.0 | 7 | 4 | 17 | 0.54883 | 1.00000 |
| sarvam | D_sparse vs E_sparse | retrieval_sparse | +8.3 | 9 | 4 | 22 | 0.26685 | 1.00000 |
| sarvam | D_full vs E_full | retrieval_full | -6.7 | 3 | 7 | 19 | 0.34375 | 1.00000 |

English without RAG is absent: A cannot establish the effect of retrieval in English.
All 3,420 source rows have unique model/condition/scenario keys and agree with JSONL primary labels and archived hits1 scores.
Invalid primary outputs: 33. No API calls were made.
