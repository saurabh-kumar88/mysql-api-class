# Basic class to wrap mysql commands

main class is MySql
method : __init__()
description : constructor for holding mysql db server credidentials

method : create_connection()
description : create mysql connection

method : execute_query()
description : execute not read-only queries e.g count rows, 'show databaeses', 'select * from table'

method: insert_record()
description : insert new record in table (modifies state)

method: update_record()
description: update record

method: delete_record()
description : deletes record
