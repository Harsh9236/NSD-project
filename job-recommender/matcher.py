import json

def load_json_file(filename):
    """Loads data from a JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {filename}.")
        return None

def match_keywords(skills_keywords, jobs_data):
    """Matches keywords from skills_keywords in job skills and counts matches."""
    job_matches = []
    for job in jobs_data:
        match_count = 0
        for job_skill in job['Skills']:
            if job_skill in skills_keywords:
                match_count += 1
        job_matches.append({'ID': job['ID'], 'matches': match_count})
    return job_matches

def sort_jobs_by_matches(job_matches):
    """Sorts jobs based on the number of matches in descending order."""
    return sorted(job_matches, key=lambda item: item['matches'], reverse=True)

def get_top_recommendations(sorted_jobs, top_n=5):
    """Returns the top N job IDs from the sorted list."""
    recommendations = []
    count = 0
    for job in sorted_jobs:
        if count < top_n and job['matches'] > 0: # Ensure we only recommend jobs with at least one match. Remove `and job['matches'] > 0` if you want to include jobs with 0 matches in recommendations.
            recommendations.append(job['ID'])
            count += 1
        elif count >= top_n:
            break
    return recommendations

def write_recommendations_to_json(recommendations, filename="recommendations.json"):
    """Writes the recommendations to a JSON file."""
    recommendation_data = {"recommendations": recommendations}
    with open(filename, 'w') as f:
        json.dump(recommendation_data, f, indent=4)
    print(f"Recommendations saved to {filename}")

def main():
    """Main function to execute the keyword matching and recommendation process."""
    skills_data = load_json_file("skills.json")
    jobs_data = load_json_file("jobs.json")

    if skills_data is None or jobs_data is None:
        return

    job_matches = match_keywords(skills_data, jobs_data)
    sorted_jobs = sort_jobs_by_matches(job_matches)
    top_recommendations = get_top_recommendations(sorted_jobs)

    write_recommendations_to_json(top_recommendations)

if __name__ == "__main__":
    main()
