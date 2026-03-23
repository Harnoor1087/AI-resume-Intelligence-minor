from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_emb, job_emb):

    score = cosine_similarity(

        [resume_emb],
        [job_emb]

    )[0][0]

    return float(score)


def calculate_final_score(

semantic_score,
skill_score,
experience_score

):

    final = (

    0.5 * semantic_score +
    0.3 * skill_score +
    0.2 * experience_score

    )

    return final
