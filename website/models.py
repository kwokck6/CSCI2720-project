from bson import ObjectId
from typing import Optional, List
from flask_login import UserMixin


# always ignore warning 'shadows built-in name id', else app will throw error
class User(UserMixin):
    def __init__(self, id, user_name, password, event_id=None):
        self.id: ObjectId = id
        self.user_name: str = user_name
        self.password: str = password
        self.event_id: Optional[List[ObjectId]] = [] if event_id is None else event_id


user_schema = {'$jsonSchema':
                   {'bsonType': 'object',
                    'required': ['user_name', 'password'],
                    'properties':
                        {'user_name': {'bsonType': 'string'},
                         'password': {'bsonType': 'string'},
                         'event_id': {'bsonType': 'array',
                                      'items': {'bsonType': 'objectId'}}
                         }
                    }
               }

# FIXME: Does not work in create_database()
event_schema = {'$jsonSchema':
                   {'bsonType': 'object',
                    'required': ['EN_PGM_NAME', 'EN_VENUE', 'EN_ACT_TYPE_NAME'],
                    'properties':
                        {
                         'EN_PGM_NAME': {'bsonType': 'string'},
                         'EN_VENUE': {'bsonType': 'string'},
                         'EN_ACT_TYPE_NAME': {'bsonType': 'string'}
                         }
                    }
               }
