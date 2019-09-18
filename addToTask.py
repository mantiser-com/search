
from google.cloud import tasks_v2
from google.protobuf import timestamp_pb2
import json

# Create a client.
client = tasks_v2.CloudTasksClient()


def addTask(payload,in_seconds=None):
    # TODO(developer): Uncomment these lines and replace with your values.
    project = 'mantiser-com';
    queue = 'scraper-que';
    location = 'europe-west1';

    # Construct the fully qualified queue name.
    parent = client.queue_path(project, location, queue)

    # Construct the request body.
    task = {
            'app_engine_http_request': {  # Specify the type of request.
                'http_method': 'POST',
                'relative_uri': '/scrape/',
                'app_engine_routing':{
                                    "service": "worker",
                                        }
            }
    }
    if payload is not None:
        # The API expects a payload of type bytes.
        converted_payload = json.dumps(payload).encode()

        # Add the payload to the request.
        task['app_engine_http_request']['body'] = converted_payload

    if in_seconds is not None:
        # Convert "seconds from now" into an rfc3339 datetime string.
        d = datetime.datetime.utcnow() + datetime.timedelta(seconds=in_seconds)

        # Create Timestamp protobuf.
        timestamp = timestamp_pb2.Timestamp()
        timestamp.FromDatetime(d)

        # Add the timestamp to the tasks.
        task['schedule_time'] = timestamp

    # Use the client to build and send the task.
    response = client.create_task(parent, task)

    print('Created task {}'.format(response.name))
    return response