# подключение к dldb 

<!-- 
login = sergei
password  = S714801t
host = 51.250.54.232
name_db = dldb 
-->

# пример подключения через sqlalchemy

<!-- 
from sqlalchemy import create_engine
engine = create_engine('postgresql://sergei:S714801t@51.250.54.232:5432/dldb')
датасет.to_sql('название таблицы', engine, schema = 'sergei', if_exists='append', index = False) 
-->


#
# подключение к AX-SQL для получения остатков происходит по учётной записи пользователя Windows
# доступ по запросу предоставляет Сибилев Ярослав Алексеевич <Sibilev.Yaroslav@zolotoy.ru> 


# пример подключения через pymssql

<!-- conn = pymssql.connect(server='AX-SQL', database='Staging') -->
