"""create post table

Revision ID: 4ff71afbdbd
Revises: None
Create Date: 2014-04-28 08:35:33.887074

"""

# revision identifiers, used by Alembic.
revision = '4ff71afbdbd'
down_revision = None

from alembic import op
from sqlalchemy import Column, String, Integer, DateTime


def upgrade():
    op.create_table('post',
                    Column('id', Integer, primary_key=True),
                    Column('body', String(1024)),
                    Column('title', String(48), nullable=False),
                    Column('page', String(24)),
                    Column('timestamp', DateTime)
                    )


def downgrade():
    op.drop_table('post')
