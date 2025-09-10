import json
from langchain.tools import StructuredTool

# -------------Search by name tool---------------- #
def search_by_name(name_query, json_path="SampleDatatset\employees_dataset.json"):
    """
    Search employees by full or partial name.
    Returns a list of matching employees (without embeddings).
    """
    with open(json_path, "r") as f:
        data = json.load(f)
    employees = data["employees"]

    results = []
    for emp in employees:
        if name_query.lower() in emp.get("name", "").lower():
            emp_copy = emp.copy()
            results.append(emp_copy)
    return results

search_by_name_tool = StructuredTool.from_function(
    func=search_by_name,
    name="search_by_name",
    description="Search employees by full or partial name. Returns all matching employees."
)

# -------------Search by experience tool---------------- #
def search_by_experience(min_exp, json_path="SampleDatatset\employees_dataset.json"):
    """
    Search employees with at least `min_exp` years of experience.
    Returns a list of matching employees (without embeddings).
    """
    with open(json_path, "r") as f:
        data = json.load(f)
    employees = data["employees"]

    results = []
    for emp in employees:
        if emp.get("experience_years", 0) >= min_exp:
            emp_copy = emp.copy()
            results.append(emp_copy)
    return results

search_by_experience_tool = StructuredTool.from_function(
    func=search_by_experience,
    name="search_by_experience",
    description="Search employees with at least the given number of years of experience."
)

