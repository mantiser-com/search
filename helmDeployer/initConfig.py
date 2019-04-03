import subprocess


def setupGcloud():
    '''
    This will setup and test configs
    '''
    process = subprocess.Popen('gcloud auth activate-service-account --key-file /keys/reference-fact-144618-b3c83d8a097a.json', shell=True, stdout=subprocess.PIPE)
    print(process.communicate())
    if process.returncode == 0:
    	print("Sucessfull activted service account ")
    else:
    	print("Error activated service account")
    process2 = subprocess.Popen('gcloud container clusters get-credentials cluster-1 --zone europe-west2-c --project reference-fact-144618', shell=True, stdout=subprocess.PIPE)
    print(process2.communicate())
    if process2.returncode == 0:
    	print("Sucessfull activted cluster ref")
    else:
    	print("Error activated cluster")
