from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them"""
    jobs = read(path)
    list = []
    for row in jobs:
        if row['job_type'] not in list:
            list.append(row['job_type'])
    return list


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type"""
    list = []
    for row in jobs:
        if row['job_type'] == job_type:
            list.append(row)
    return list


def get_unique_industries(path):
    """Checks all different industries and returns a list of them"""

    jobs = read(path)
    list = []

    for row in jobs:
        if row['industry'] == '':
            continue
        if row['industry'] not in list:
            list.append(row['industry'])
    return list


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry"""

    list = []
    for row in jobs:
        if row['industry'] == industry:
            list.append(row)
    return list
    return []


def get_max_salary(path):
    """Get the maximum salary of all jobs"""

    jobs = read(path)
    max = 0

    for row in jobs:
        atual = (row['max_salary'])
        if atual.isnumeric():
            convert = int(atual)
            if convert > max:
                max = convert
        else:
            continue
    return max


def get_min_salary(path):
    """Get the minimum salary of all jobs"""

    jobs = read(path)
    min = 9999999

    for row in jobs:
        atual = (row['min_salary'])
        if atual.isnumeric():
            convert = int(atual)
            if convert < min:
                min = convert
        else:
            continue
    return min


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job"""

    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(salary) != int
    ):
        raise ValueError()
    if (
        not str(job["min_salary"]).isdigit()
        or not str(job["max_salary"]).isdigit()
    ):
        raise ValueError()
    if job['min_salary'] > job['max_salary']:
        raise ValueError()
    if salary >= job['min_salary'] and salary <= job['max_salary']:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range"""
    list = []
    for row in jobs:
        if not str(salary).isdigit():
            return []
        if (
            "min_salary" not in row
            or "max_salary" not in row
            or not str(row["min_salary"]).isdigit()
            or not str(row["max_salary"]).isdigit()
            or row['min_salary'] > row['max_salary']
        ):
            continue
        if salary >= row['min_salary'] and salary <= row['max_salary']:
            list.append(row)
    return list
