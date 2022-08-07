from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs = read(path)
    list = []
    for row in jobs:
        if row['job_type'] not in list:
            list.append(row['job_type'])
    return list


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    list = []
    for row in jobs:
        if row['job_type'] == job_type:
            list.append(row)
    return list


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs = read(path)
    list = []

    for row in jobs:
        if row['industry'] == '':
            continue
        if row['industry'] not in list:
            list.append(row['industry'])
    return list


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """

    list = []
    for row in jobs:
        if row['industry'] == industry:
            list.append(row)
    return list
    return []


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """

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
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

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
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
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
