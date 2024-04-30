import  os
DB_DETAILS={

    'dev':{
        'SOURCE_DB':{
            'DB_TYPE':'mysql',
            'DB_HOST':'139.99.209.131',
            'DB_NAME':'retail_db',
            'SOURCE_DB_USER':os.environ.get('SOURCE_DB_USER'),
            'SOURCE_DB_PASS':os.environ.get('SOURCE_DB_PASS'),
            'Buffer':os.environ.get('PYTHONUNBUFFERED')
        },
        'TARGET_DB':{

            'DB_TYPE':'postgres',
            'DB_HOST':'139.99.209.131',
            'DB_NAME':'retail_db',
            'TARGET_DB_USER':os.environ.get('TARGET_DB_USER'),
            'TARGET_DB_PASS':os.environ.get('TARGET_DB_PASS')
        }
    }
}
