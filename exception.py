class GithubApiError(Exception):

    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached!"
        else:
            message = f"The status code is {status_code}!"
        super().__init__(message)
