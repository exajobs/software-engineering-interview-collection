class SimpleDB:
    def set(self, key, value):
        """set sets the value associated with the key"""
        pass

    def get(self, key):
        """
        get returns the value associated with the key
        get should raise a KeyError if the key doesn't exist
        """
        pass

    def unset(self, key):
        """unset should delete the key from the db"""
        pass

    def begin(self):
        """begin starts a new transaction"""
        pass

    def commit(self):
        """
        commit commits all transactions
        it should raise an Exception if there is no ongoing transaction
        """
        pass

    def rollback(self):
        """
        rollback undoes the most recent transaction
        it should raise an Exception if there is no ongoing transation
        """
        pass
