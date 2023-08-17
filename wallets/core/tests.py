from django.test import TestCase
from rest_framework.test import APIClient


class FullyTestCase(TestCase):
    def test_change_balance(self):
        """Animals that can speak are correctly identified"""
        client = APIClient()
        resp = client.get('/api/v1/wallets/', format='json')
        data = resp.json()
        assert len(data.get('results', [])) == 0

        label = '1'
        resp = client.post('/api/v1/wallets/', {'label': label}, format='json')
        assert resp.status_code == 201
        data = resp.json()
        assert data.get('label') == label
        assert data.get('balance') == '0.00'

        resp = client.get('/api/v1/wallets/', format='json')
        assert resp.status_code == 200
        data = resp.json()
        assert len(data.get('results', [])) == 1

        wallet_id = data.get('results')[0].get('id')

        resp = client.get(f'/api/v1/wallets/{wallet_id}/', format='json')
        assert resp.status_code == 200
        data = resp.json()
        assert data.get('balance') == '0.00'

        txid = '1'
        amount = '10.00'
        resp = client.post('/api/v1/transactions/', {'txid': txid, 'amount': amount, 'wallet': wallet_id},
                           format='json')
        assert resp.status_code == 201

        resp = client.get(f'/api/v1/wallets/{wallet_id}/', format='json')
        assert resp.status_code == 200
        data = resp.json()
        assert data.get('balance') == amount

    def test_unique_txid(self):
        """Animals that can speak are correctly identified"""
        client = APIClient()
        label = '2'
        resp = client.post('/api/v1/wallets/', {'label': label}, format='json')
        assert resp.status_code == 201
        data = resp.json()

        txid = '2'
        amount = '10.00'
        resp = client.post('/api/v1/transactions/', {'txid': txid, 'amount': amount, 'wallet': data.get('id')},
                           format='json')
        assert resp.status_code == 201

        resp = client.post('/api/v1/transactions/', {'txid': txid, 'amount': amount, 'wallet': data.get('wallet')},
                           format='json')
        assert resp.status_code == 400

    def test_filtering_wallets(self):
        """Animals that can speak are correctly identified"""
        client = APIClient()
        label_1 = '5'
        label_2 = '6'
        labels = ('1', '2', '3', '4', label_1, label_1, label_1, label_2)
        for label in labels:
            resp = client.post('/api/v1/wallets/', {'label': label}, format='json')
            assert resp.status_code == 201

        resp = client.get('/api/v1/wallets/', format='json')
        assert resp.status_code == 200
        data = resp.json()
        assert len(data.get('results', [])) == len(labels)

        for label in (label_1, label_2):
            resp = client.get(f'/api/v1/wallets/?label={label}', format='json')
            assert resp.status_code == 200
            data = resp.json()
            assert len(data.get('results', [])) == len(list(filter(lambda x: x == label, labels)))
            assert data['results'][0].get('label') == label
