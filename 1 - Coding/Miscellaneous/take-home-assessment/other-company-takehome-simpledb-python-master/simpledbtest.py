import unittest
import simpledb


class SimpleDBTest(unittest.TestCase):
    def test_unset(self):
        db = simpledb.SimpleDB()

        db.set("a", 10)
        self.assertValue(db, "a", 10)

        db.unset("a")
        self.assertRaises(KeyError, db.get, "a")

    def testRollback(self):
        db = simpledb.SimpleDB()

        db.begin()
        db.set("a", 10)
        self.assertValue(db, "a", 10)

        db.begin()
        db.set("a", 20)
        self.assertValue(db, "a", 20)

        db.rollback()
        self.assertValue(db, "a", 10)

        db.rollback()
        self.assertRaises(KeyError, db.get, "a")

    def testNestedCommit(self):
        db = simpledb.SimpleDB()

        db.begin()
        db.set("a", 30)

        db.begin()
        db.set("a", 40)

        db.commit()
        self.assertValue(db, "a", 40)

        self.assertRaises(Exception, db.rollback)

        self.assertRaises(Exception, db.commit)

    def testTransactionInterleavedKeys(self):
        db = simpledb.SimpleDB()

        db.set("a", 10)
        db.set("b", 10)
        self.assertValue(db, "a", 10)
        self.assertValue(db, "b", 10)

        db.begin()
        db.set("a", 20)
        self.assertValue(db, "a", 20)
        self.assertValue(db, "b", 10)

        db.begin()
        db.set("b", 30)
        self.assertValue(db, "a", 20)
        self.assertValue(db, "b", 30)

        db.rollback()
        self.assertValue(db, "a", 20)
        self.assertValue(db, "b", 10)

        db.rollback()
        self.assertValue(db, "a", 10)
        self.assertValue(db, "b", 10)

    def testTransactionRollbackUnset(self):
        db = simpledb.SimpleDB()

        db.set("a", 10)
        self.assertValue(db, "a", 10)

        db.begin()
        self.assertValue(db, "a", 10)
        db.set("a", 20)
        self.assertValue(db, "a", 20)

        db.begin()
        db.unset("a")
        self.assertRaises(KeyError, db.get, "a")

        db.rollback()
        self.assertValue(db, "a", 20)

        db.commit()
        self.assertValue(db, "a", 20)

    def testTransactionCommitUnset(self):
        db = simpledb.SimpleDB()

        db.set("a", 10)
        self.assertValue(db, "a", 10)

        db.begin()
        self.assertValue(db, "a", 10)
        db.unset("a")
        self.assertRaises(KeyError, db.get, "a")

        db.rollback()
        self.assertValue(db, "a", 10)

        db.begin()
        db.unset("a")
        self.assertRaises(KeyError, db.get, "a")

        db.commit()
        self.assertRaises(KeyError, db.get, "a")

        db.begin()
        self.assertRaises(KeyError, db.get, "a")
        db.set("a", 20)
        self.assertValue(db, "a", 20)

        db.commit()
        self.assertValue(db, "a", 20)

    def assertValue(self, db, key, value):
        actualValue = db.get(key)
        self.assertEqual(value, actualValue)


if __name__ == "__main__":
    unittest.main()
