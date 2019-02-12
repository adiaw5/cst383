#!/usr/bin/env python3
#encoding: windows-1252
class IndexEntryU:  # unique index entry
    # IndexEntry contains a value (an integer, double or string value) and a rowid 
    def __init__(self, value, rowid):
        self.value = value
        self.rowid = rowid
        
class IndexEntryNU:  # non-unique index entry
    # IndexEntry contains a value (an integer, double or string value) and a rowid 
    def __init__(self, value):
        self.value = value
        self.rowids = []
        
class Index:
    # An index consists of a list of IndexEntry objects that are in order by their value
    # To define an index specify the database object, the column name and whether the index is UNIQUE
    # after defining an index, you must call the create method to build the index entries
    def __init__(self, db, colname, colindex):
        self.db = db
        self.entries = []            # list of IndexEntry instances    
        self.colindex = colindex     # index into column list in schema
        self.colname = colname       # column name
 

    def print(self):
        # for debug - print content of index
        print("Index", self.db.schema.cols[self.colindex].colname, "Non-Unique:")
        print("number of entries", len(self.entries))
        for entry in self.entries:
            print(entry.value, entry.rowids)
        print("Index end.")

    def create(self):
        for rowid in range(4096):
            row = self.db.getRow(rowid)
            if row != False:
                value = row.values[self.colindex]
                self.insert(rowid, value)

    def delete(self, rowid, value):
        for entry in self.entries:
            if entry.rowid == rowid and entry.value == value:
               del entry.value 
 
    def insert(self, rowid, value):
        for entry in self.entries:
            if entry.rowid == rowid:
                entry.value = value
        for i in self.entries:
            print(i)
                
    
    def search(self, value):
        # return index value of first IndexEntry 
        #         where IndexEntry.value >= value
        # return -1 if value is higher than all entries in index

        low = 0 
        high = len(self.entries)-1
        while low <= high:
            mid = (low + high) // 2
            if value == self.entries[mid].value:
                return 1
            elif value < self.entries[mid].value:
                high = mid - 1
            else:
                low = mid + 1      
        
        return -1
            
class UniqueIndex(Index):
    # this class is code unique to index that does not allow duplicate value entries
        def __init__(self, db, colname, colindex):
            super().__init__(db, colname, colindex)
        
        def print(self):
            # for debug - print content of index s
            print("Index", self.db.schema.cols[self.colindex].colname, "Unique:")
            print("number of entries", len(self.entries))
            for entry in self.entries:
                print(entry.value, entry.rowid)
            print("Index end.")
        
        def insert(self, rowid, value):
            for entry in self.entries:
                if self.emtries[i].rowid == rowid:
                    self.entries[i].value = value            
 
    
    
        def delete(self, rowid, value):
            for i in range(len(index.entries)-1):
                if self.entries[i].rowid == rowid and self.entries[i].value == value:
                   del self.entries[i].value 
        
