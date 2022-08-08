from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    first = jobs[0]
    assert first == {
        "title": "Maquinista",
        "salary": "2000",
        "type": "trainee",
    }
