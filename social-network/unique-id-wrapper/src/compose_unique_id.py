'''
In the microservices architecture, the UID of each user is essentially their machine id. 
Since we are migrating the application to a serverless application, we can use any mechanisms 
as long as the uniqueness is ensured.

In this case, we use uuid4() to create a random UUID that is platform independent.
'''
import uuid

def compose_unique_id():
  return uuid.uuid4().hex
