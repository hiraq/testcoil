import unittest
import json

from bson.objectid import ObjectId
from faker import Faker

from http import HTTPStatus
from tests import build_full_app

DEBUG = False

class NewsTest(unittest.TestCase):
    def setUp(self):
        self.app = build_full_app()
        self.headers = {'Accept': 'application/vnd.api+json', 'Content-Type': 'application/vnd.api+json'}
        self.faker = Faker()

    def test_create_success(self):
        data = {'title': self.faker.sentence(), 'content': ''.join(self.faker.paragraphs())}
        request, response = self.app.test_client.post('/v1/news/', headers=self.headers, data=json.dumps(data), debug=DEBUG)
        self.assertEqual(HTTPStatus.CREATED, response.status)
    
    def test_create_duplicate_title(self):
        title = self.faker.sentence()
        data = {'title': title, 'content': ''.join(self.faker.paragraphs())}

        request1, response1 = self.app.test_client.post('/v1/news/', headers=self.headers, data=json.dumps(data), debug=DEBUG)
        self.assertEqual(HTTPStatus.CREATED, response1.status)
        
        request2, response2 = self.app.test_client.post('/v1/news/', headers=self.headers, data=json.dumps(data), debug=DEBUG)
        self.assertEqual(HTTPStatus.CONFLICT, response2.status)

    def test_read_success(self):
        title = self.faker.sentence()
        data = {'title': title, 'content': ''.join(self.faker.paragraphs())}
        request, response = self.app.test_client.post('/v1/news/', headers=self.headers, data=json.dumps(data), debug=DEBUG)
        self.assertEqual(HTTPStatus.CREATED, response.status)

        body = json.loads(response.body)
        data = body.get('data')
        id = data.get('id')
        
        request2, response2 = self.app.test_client.get('/v1/news/{}'.format(id), headers=self.headers, debug=DEBUG)
        self.assertEqual(HTTPStatus.OK, response2.status)

        body2 = json.loads(response2.body)
        data2 = body2.get('data')
        attrs = data2.get('attributes')
        self.assertEqual(title, attrs.get('title'))

    def test_read_not_found(self):
        id = ObjectId()
        request, response = self.app.test_client.get('/v1/news/{}'.format(str(id)), headers=self.headers, debug=DEBUG)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status)

    def test_delete_success(self):
        title = self.faker.sentence()
        data = {'title': title, 'content': ''.join(self.faker.paragraphs())}
        request, response = self.app.test_client.post('/v1/news/', headers=self.headers, data=json.dumps(data), debug=DEBUG)
        self.assertEqual(HTTPStatus.CREATED, response.status)

        body = json.loads(response.body)
        data = body.get('data')
        id = data.get('id')

        request, response = self.app.test_client.delete('/v1/news/{}'.format(id), headers=self.headers, debug=DEBUG)
        self.assertEqual(HTTPStatus.OK, response.status)

    def test_delete_not_found(self):
        id = ObjectId()
        request, response = self.app.test_client.delete('/v1/news/{}'.format(str(id)), headers=self.headers, debug=DEBUG)
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status)

    def test_update_success(self):
        title = self.faker.sentence()
        data = {'title': title, 'content': ''.join(self.faker.paragraphs())}
        request, response = self.app.test_client.post('/v1/news/', headers=self.headers, data=json.dumps(data), debug=DEBUG)
        self.assertEqual(HTTPStatus.CREATED, response.status)

        body = json.loads(response.body)
        data = body.get('data')
        id = data.get('id')

        title2 = title + ' updated'
        data2 = {'title': title2, 'content': ''.join(self.faker.paragraphs())}
        request2, response2 = self.app.test_client.put('/v1/news/{}'.format(id), headers=self.headers, data=json.dumps(data2), debug=DEBUG)
        self.assertEqual(HTTPStatus.OK, response2.status)

        body2 = json.loads(response2.body)
        data2 = body2.get('data')
        attrs = data2.get('attributes')
        title_updated = attrs.get('title')
        self.assertEqual(title2, title_updated)
