# FILE_NAME = 'Crime_Data_from_2020_to_Present.csv'
FILE_NAME = 'copy_criems.csv'
SQLITE_DB_PATH = 'crimes.db'
TABLE_NAME = 'crimes_data'

CREATE_TABLE_FORMAT = f'''
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    DR_NO VARCHAR(255),
    Date_Rptd VARCHAR(255),
    DATE_OCC VARCHAR(255),
    TIME_OCC INTEGER,
    AREA INTEGER,
    AREA_NAME VARCHAR(255),
    Rpt_Dist_No VARCHAR(255),
    Part_1_2 INTEGER,
    Crm_Cd INTEGER,
    Crm_Cd_Desc VARCHAR(255),
    Mocodes VARCHAR(255),
    Vict_Age INTEGER,
    Vict_Sex VARCHAR(255),
    Vict_Descent VARCHAR(255),
    Premis_Cd INTEGER,
    Premis_Desc VARCHAR(255),
    Weapon_Used_Cd INTEGER,
    Weapon_Desc VARCHAR(255),
    Status VARCHAR(255),
    Status_Desc VARCHAR(255),
    Crm_Cd_1 INTEGER,
    Crm_Cd_2 INTEGER,
    Crm_Cd_3 INTEGER,
    Crm_Cd_4 INTEGER,
    LOCATION VARCHAR(255),
    Cross_Street VARCHAR(255),
    LAT REAL,
    LON REAL
);
'''

COLUMNS_NAMES = [
    "DR_NO", "Date_Rptd", "DATE_OCC", "TIME_OCC", "AREA", "AREA_NAME", "Rpt_Dist_No",
    "Part_1_2", "Crm_Cd", "Crm_Cd_Desc", "Mocodes", "Vict_Age", "Vict_Sex",
    "Vict_Descent", "Premis_Cd", "Premis_Desc", "Weapon_Used_Cd", "Weapon_Desc",
    "Status", "Status_Desc", "Crm_Cd_1", "Crm_Cd_2", "Crm_Cd_3", "Crm_Cd_4",
    "LOCATION", "Cross_Street", "LAT", "LON"
]

columns_str = ", ".join(COLUMNS_NAMES)
placeholders = ", ".join(["%s"] * len(COLUMNS_NAMES))

insert_rows_format = f'INSERT INTO {TABLE_NAME} ({columns_str}) VALUES ({placeholders})'

min_seconds = 1
max_seconds = 3
