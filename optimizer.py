
import json
import pandas as pd
import google.generativeai as genai

# Hardcoded Gemini API
genai.configure(api_key="AIzaSyCBUz2LJ5L4MLud-eu5ZcqHAQW7YOyVsUc")

model = genai.GenerativeModel("gemini-flash-latest")

def get_changed_files():

    with open("changed_files.txt") as f:
        return [x.strip() for x in f]


def load_coverage():

    with open("coverage_map.json") as f:
        return json.load(f)


def load_history():

    return pd.read_csv("test_history.csv")


def calculate_risk_scores(history):

    risk={}

    for _,row in history.iterrows():

        if row["status"]=="fail":
            risk[row["test"]]=10
        else:
            risk[row["test"]]=3

    return risk


def llm_remove_redundant_tests(test_list):

    prompt=f'''
You are a QA automation expert.

Given regression tests with risk priority,
remove redundant tests and keep only
important tests ensuring coverage.

Tests:
{test_list}

Return only Python list.
'''

    response=model.generate_content(prompt)

    try:
        selected=eval(response.text)
    except:
        selected=test_list

    return selected


def prioritize_tests():

    changed=get_changed_files()

    coverage=load_coverage()

    history=load_history()

    risk_scores=calculate_risk_scores(history)

    impacted_tests=[]

    for test,files in coverage.items():

        if any(f in changed for f in files):
            impacted_tests.append(test)


    sorted_tests=sorted(
        risk_scores,
        key=risk_scores.get,
        reverse=True
    )

    candidate_tests=sorted_tests[:5]

    llm_selected=llm_remove_redundant_tests(candidate_tests)

    optimized_suite=list(set(impacted_tests + llm_selected))

    return optimized_suite
