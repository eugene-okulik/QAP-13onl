class BaseEndpoint:
    status_code = None

    @property
    def status_code_is_200(self):
        return self.status_code == 200

    @property
    def status_code_is_404(self):
        return self.status_code == 404

    @property
    def status_code_is_401(self):
        return self.status_code == 401

    @property
    def status_code_is_400(self):
        return self.status_code == 400

    @property
    def status_code_is_500(self):
        return self.status_code == 500
