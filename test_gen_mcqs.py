import json

# Let's verify we can generate clean MCQs
sample_q = {
    "id": 1,
    "topic": "Parliament",
    "type": "statement",
    "q": "Consider the following statements regarding the Speaker of Lok Sabha:\n1. The Speaker ceases to hold office if he ceases to be a member of the Lok Sabha.\n2. The Speaker can be removed only by a resolution passed by a special majority of two-thirds of the members present and voting.\n3. The Speaker presides over a joint sitting of both Houses of Parliament.",
    "options": [
        "(a) 1 and 2 only",
        "(b) 1 and 3 only",
        "(c) 2 and 3 only",
        "(d) 1, 2 and 3"
    ],
    "answer": "(b)",
    "explanation": "Statement 2 is incorrect: The Speaker is removed by an effective majority (majority of all the then members of the House) under Article 94(c), not a 2/3rds special majority. Statements 1 and 3 are correct under Articles 94(a) and 118(4)."
}
print(sample_q)
