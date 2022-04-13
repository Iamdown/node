from django.test import TestCase

# Create your tests here.
import uuid
namespace = uuid.uuid1()
print(uuid.uuid5(namespace, "hallo"))