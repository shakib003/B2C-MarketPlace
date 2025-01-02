from intasend import APIService

API_PUBLISHABLE_KEY = 'ISPubKey_test_61650744-fdf5-4eb8-8058-7c5845a847d5'

API_TOKEN = 'ISSecretKey_test_9ce47238-4934-46a7-8be5-7774d96e7b3d'

service = APIService(token=API_TOKEN, publishable_key=API_PUBLISHABLE_KEY, test=True)