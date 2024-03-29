# WillowDb
## Simple json document nosql database with indexes

WillowDb is a simple json document nosql database all in a python module

# Features

- Secondary indexes for use with faster querys
- Built for speed with Query,insert,update and delete commands
- Scan command will be the most recourse intensive
- Scan command with filter statement that has the same format as python if statement
- Update Command to update a record
- Delete Command to update a record

# Installation

WillowDb requires [Python](https://python.org/) 3+ to run.

```sh
pip install willowDb
```

# Usage

#### Initialization 
```sh
import WillowDb
willowDb = WillowDb(folderPath="path/to/your/db/folder" errorConfig='raise')
```
##### Initialization Options:
- folderPath(optional): if provided it will look for an create tables in the folder provided otherwise it will create the tables
 inside the WillowDb module folder.
- errorConfig(optional)
    -  raise:  On errors will raise an error
    -  log: On errors will log an error
    -  both: On errors will log and raise an error
    -  None: On errors will do nothing

#### Create Table
```sh
willowDb.createTable(name="demoTable", primaryKey="id")
```
##### Create Table Options:
- name(REQUIRED): Name of the the table to create
- primaryKey(REQUIRED): Primary key for the default index of the table (the field to used to query, update, delete)

#### Table Initialization
```sh
demoTable = willowDb.table(name="demoTable", createPrimaryKey=True)
```

##### Table Initialization Options:
- name(REQUIRED): Name of the the table to use
- createPrimaryKey(Optional): Boolean, if True and the primary key is not in the insert data then it will create uuid for the
primary key.  For example bec6b12a-7302-462a-b526-bef9a07bc2a4.  If False it will not create a primary key.

#### Insert
```sh
demoTable.insert(data = {"id": "1234", "demoData1": "demo1", "demoData2": "demo2"})
```

##### Insert Options:
- data(REQUIRED): Dictionary, data to be inserted into table.  If createPrimaryKey was True on Table Initialization then the data 
must include the primary key.

#### Query
```sh
results = demoTable.query(primaryKey="1234", indexName="indexName")
```

##### Query Options:
- primaryKey(REQUIRED): The primary key of the record to fetch.
- indexName(Optional): If using an index, provide index here.  Defaults to the "default" index. 

#### Update
```sh
demoTable.update(primaryKey="1234", record={"demoData2": "demo2Updated"})
```

##### Update Options:
- primaryKey(REQUIRED): The primary key of the record to update.
- record(REQUIRED): Dictionary, the data to update in the record, if key already exists in the record the value will be updated.
If the key does not exist in the record the key and value will be added.  If the primary key is in the record it will be ignored.

#### Delete
```sh
demoTable.delete(primaryKey="1234")
```

##### Delete Options:
- primaryKey(REQUIRED): The primary key of the record to delete.

#### Scan
```sh
results = demoTable.scan(filter="demoData1 == 'demo1'")
```

##### Scan Options:
- filter(Optional): String, a python if statement in a string format to filter the data by, if not provided will grab the entire table

#### Create Index
```sh
demoTable.createIndex(indexName='demoData1Index', primaryKey='demoData1')
```

##### Create Index Options:
- indexName(REQUIRED): Name of the the index to create
- primaryKey(REQUIRED): Primary key for the index (the field to used to query)

#### Delete Index
```sh
devicesTable.deleteIndex(indexName="typeIndex")
```

##### Delete Index Options:
- indexName(REQUIRED): Name of the the index to delete

#### Delete Table
```sh
willowDb.deleteTable(name=tableName)
```

##### Delete Table Options:
- tableName(REQUIRED): Name of the the table to delete.
## License

MIT License

Copyright (c) 2024 monkeytravel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

