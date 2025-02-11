import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.vector import Vector

# Create a Firestore client
db = firestore.client()

# Reference to the 'users' collections
collectionRef = db.collection(u'users')

# Example document with vector embedding
doc = {
    "name": "Your Document Name",
    "description": "Some description about the document",
    "embedding_field": Vector([0.18332680, 0.24160706, 0.3416704])  # Vector embedding field
}

# Initialize the Firebase app using a service account key
cred = credentials.Certificate("path/to/your/service-account-key.json")
firebase_admin.initialize_app(cred)

# Add data to Firestore
doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
  u'first': u'Ada',
  u'last': u'Lovelace',
  u'born': 1815  # Birth year of Ada Lovelace
})

# Read data from Firestore
doc = doc_ref.get()
if doc.exists:
  print(f'Document data: {doc.to_dict()}')  # Print document data if it exists
else:
  print(u'No such document!')  # Print message if document does not exist