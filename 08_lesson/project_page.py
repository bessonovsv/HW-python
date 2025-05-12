import requests


class ProjectPage:
    base_url = "https://ru.yougile.com/api-v2/projects"
    token = ".."
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    def create_project(self, project_data):
        response = requests.post(f"{self.base_url}",
                                 json=project_data, headers=self.headers)
        return response

    def update_project(self, project_id, project_data):
        response = requests.put(f"{self.base_url}/{project_id}",
                                json=project_data, headers=self.headers)
        return response

    def get_project(self, project_id):
        response = requests.get(f"{self.base_url}/{project_id}",
                                headers=self.headers)
        return response
