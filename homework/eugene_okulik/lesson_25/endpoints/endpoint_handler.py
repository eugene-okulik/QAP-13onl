class Endpoint:
    status_code = None

    @property
    def status_code_is_200(self):
        return self.status_code == 200
