from locust import TaskSet, HttpLocust, task


class GetToken(TaskSet):
    @task
    def fire(self):
        rsp = self.client.post(
            '/tokens', json={'sns_type': 'google', 'access_token': '123'}
        )
        print(rsp.content)


class Users(HttpLocust):
    task_set = GetToken
    min_wait = 1000
    max_wait = 1000
