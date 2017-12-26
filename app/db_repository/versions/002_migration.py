from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
admin = Table('admin', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=64)),
    Column('email', String(length=120)),
    Column('password', String(length=120)),
)

county = Table('county', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('headline', String(length=1000)),
    Column('content', String(length=10000)),
)

location = Table('location', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('address', String(length=120)),
    Column('county', Integer),
)

success_story = Table('success_story', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=64)),
    Column('last_name', String(length=64)),
    Column('video_link', String(length=120)),
    Column('image', String(length=120)),
    Column('story', String(length=1000)),
    Column('county', Integer),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=64)),
    Column('email', String(length=120)),
    Column('password', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['admin'].create()
    post_meta.tables['county'].create()
    post_meta.tables['location'].create()
    post_meta.tables['success_story'].create()
    pre_meta.tables['user'].columns['nickname'].drop()
    post_meta.tables['user'].columns['password'].create()
    post_meta.tables['user'].columns['username'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['admin'].drop()
    post_meta.tables['county'].drop()
    post_meta.tables['location'].drop()
    post_meta.tables['success_story'].drop()
    pre_meta.tables['user'].columns['nickname'].create()
    post_meta.tables['user'].columns['password'].drop()
    post_meta.tables['user'].columns['username'].drop()
