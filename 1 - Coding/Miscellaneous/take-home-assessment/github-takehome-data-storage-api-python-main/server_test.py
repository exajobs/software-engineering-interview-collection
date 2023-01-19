import unittest
import json
import webtest
import server


class DataStorageServerTest(unittest.TestCase):

    def setUp(self):
        app = server.DataStorageServer()
        self.testapp = webtest.TestApp(app)

    def test_put(self):
        resp1 = self.testapp.put("/data/my-repo", "something")
        res1 = json.loads(resp1.body)

        self.assertEqual(201, resp1.status_code)
        self.assertEqual(9, res1["size"])
        self.assertEqual(type(res1["oid"]), str)
        self.assertTrue(len(res1["oid"]) > 0)

        resp2 = self.testapp.put("/data/my-repo", "other")
        res2 = json.loads(resp2.body)

        self.assertEqual(201, resp2.status_code)
        self.assertEqual(5, res2["size"])
        self.assertEqual(type(res2["oid"]), str)
        self.assertTrue(len(res2["oid"]) > 0)

        self.assertNotEqual(res1["oid"], res2["oid"])

    def test_get(self):
        resp = self.testapp.put("/data/my-repo", "something")
        res1 = json.loads(resp.body)

        resp = self.testapp.put("/data/my-repo", "other")
        res2 = json.loads(resp.body)

        self.assertNotEqual(res1["oid"], res2["oid"])

        resp = self.testapp.get(f"/data/my-repo/{res1['oid']}")
        self.assertEqual(200, resp.status_code)
        self.assertEqual(b"something", resp.body)

        resp = self.testapp.get(f"/data/my-repo/{res2['oid']}")
        self.assertEqual(200, resp.status_code)
        self.assertEqual(b"other", resp.body)

    def test_get_not_found(self):
        resp = self.testapp.get("/data/my-repo/missing", expect_errors=True)
        self.assertEqual(404, resp.status_code)

    def test_delete(self):
        resp = self.testapp.put("/data/my-repo", "something")
        res = json.loads(resp.body)

        dup_resp = self.testapp.put("/data/other-repo", "something")
        dup_res = json.loads(dup_resp.body)

        resp = self.testapp.delete(f"/data/my-repo/{res['oid']}")
        self.assertEqual(200, resp.status_code)

        resp = self.testapp.get(f"/data/my-repo/{res['oid']}", expect_errors=True)
        self.assertEqual(404, resp.status_code)

        resp = self.testapp.get(f"/data/other-repo/{dup_res['oid']}", expect_errors=True)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(b"something", resp.body)


    def test_delete_nonexistent_object(self):
        resp = self.testapp.delete("/data/my-repo/missing", expect_errors=True)
        self.assertEqual(404, resp.status_code)


if __name__ == '__main__':
    unittest.main()
